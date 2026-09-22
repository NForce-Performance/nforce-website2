/* ==========================================================================
   N-FORCE PERFORMANCE — nf-core.js
   Gedeelde laag: taal, datalading, UI-teksten, prijsopmaak, covers,
   handboekkaarten, teaser-modal en de winkelwagen.
   Deze module wordt door elke pagina geladen. Paginaspecifieke logica staat in
   nf-handbooks.js en nf-selftest.js.
   ========================================================================== */
window.NF = (function () {
  'use strict';

  var LANGS = ['nl', 'en', 'de'];
  var lang = (function () {
    var m = location.pathname.match(/^\/(nl|en|de)(\/|$)/);
    return m ? m[1] : 'nl';
  })();

  /* --- opslag: localStorage kan geblokkeerd zijn (preview-iframe) --------- */
  var mem = {};
  var store = {
    get: function (k) {
      try { return window.localStorage.getItem(k); } catch (e) { return mem[k] || null; }
    },
    set: function (k, v) {
      try { window.localStorage.setItem(k, v); } catch (e) { mem[k] = v; }
    }
  };

  /* --- taal & teksten ---------------------------------------------------- */
  var UI = {};
  function t(key) {
    var row = UI[key];
    if (!row) return key;
    return row[lang] || row.nl || key;
  }
  function pick(field) {
    if (field === null || field === undefined) return '';
    if (typeof field === 'string') return field;
    return field[lang] || field.nl || '';
  }

  /* --- data -------------------------------------------------------------- */
  var cache = {};
  function json(path) {
    if (!cache[path]) {
      cache[path] = fetch(path, { cache: 'no-cache' }).then(function (r) {
        if (!r.ok) throw new Error('Kan ' + path + ' niet laden (' + r.status + ')');
        return r.json();
      });
    }
    return cache[path];
  }
  var data = {
    ui: function () { return json('/assets/data/i18n.json'); },
    handbooks: function () { return json('/assets/data/handbooks.json'); },
    benchmarks: function () { return json('/assets/data/benchmarks.json'); },
    rules: function () { return json('/assets/data/rules.json'); }
  };

  /* --- helpers ----------------------------------------------------------- */
  function euro(n) {
    return '\u20ac' + Number(n).toFixed(0);
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }
  function el(html) {
    var d = document.createElement('div');
    d.innerHTML = html.trim();
    return d.firstElementChild;
  }
  function qs(name) {
    return new URLSearchParams(location.search).get(name);
  }

  /* --- handboekregister -------------------------------------------------- */
  var catalog = null; // { items, byId, families }
  function loadCatalog() {
    return data.handbooks().then(function (raw) {
      if (!catalog) {
        var byId = {};
        raw.items.forEach(function (i) { byId[i.id] = i; });
        catalog = { items: raw.items, byId: byId, families: raw.families };
      }
      return catalog;
    });
  }
  function famLabel(item) {
    if (!catalog || !catalog.families[item.family]) return '';
    return pick(catalog.families[item.family].label);
  }

  /* --- cover (uit data opgebouwd, geen losse afbeelding nodig) ------------ */
  function coverHTML(item, small) {
    if (item.cover) {
      return '<img class="cover' + (small ? ' cover--sm' : '') + '" src="' + esc(item.cover) +
        '" alt="' + esc(pick(item.title)) + '" width="640" height="400" loading="lazy">';
    }
    var title = pick(item.title).split('—')[0].trim();
    return '<div class="cover' + (item.version === 'pro' ? ' cover--pro' : '') + (small ? ' cover--sm' : '') + '" role="img" aria-label="' + esc(pick(item.title)) + '">' +
      '<span class="cover__ver">' + esc(item.version) + '</span>' +
      '<span class="cover__fam">' + esc(famLabel(item)) + '</span>' +
      '<span class="cover__title">' + esc(title) + '</span>' +
      '</div>';
  }

  /* --- handboekkaart ----------------------------------------------------- */
  function cardHTML(item, opts) {
    opts = opts || {};
    var badges = (pick(item.badges) || []).slice(0, 3).map(function (b) {
      return '<span class="badge' + (b.toLowerCase() === 'pro' ? ' badge--pro' : '') + '">' + esc(b) + '</span>';
    }).join('');
    var price = '<b class="num">' + euro(item.price) + '</b>' +
      (item.compareAt ? ' <s class="num">' + euro(item.compareAt) + '</s>' : '');
    return '<article class="hb-card' + (opts.recommended ? ' hb-card--rec' : '') + '" data-id="' + esc(item.id) + '">' +
      (opts.flag ? '<p class="hb-card__flag">' + esc(opts.flag) + '</p>' : '') +
      coverHTML(item) +
      '<div class="hb-card__body">' +
        '<div class="badgerow">' + badges + '</div>' +
        '<h3>' + esc(pick(item.title)) + '</h3>' +
        '<p class="hb-card__tagline">' + esc(pick(item.tagline)) + '</p>' +
        '<p class="hb-card__meta num">' + item.pages + ' ' + t('pages') + ' \u00b7 ' + item.weeks + ' ' + t('weeks') + '</p>' +
        '<div class="hb-card__foot">' +
          '<p class="hb-card__price">' + price + '</p>' +
          '<div class="hb-card__actions">' +
            '<button class="btn btn--ghost btn--sm" data-teaser="' + esc(item.id) + '">' + t('preview') + '</button>' +
            '<button class="btn btn--primary btn--sm" data-add="' + esc(item.id) + '">' + t('addToCart') + '</button>' +
          '</div>' +
        '</div>' +
      '</div>' +
    '</article>';
  }

  /* --- teaser-modal ------------------------------------------------------ */
  function teaserHTML(item) {
    function block(label, body) {
      return '<div class="teaser__block"><h4>' + esc(label) + '</h4>' + body + '</div>';
    }
    var learn = '<ul class="ticks">' + (pick(item.learn) || []).map(function (l) {
      return '<li>' + esc(l) + '</li>';
    }).join('') + '</ul>';

    var toc = pick(item.contents) || [];
    var tocHTML = '<ol class="teaser__toc">' + toc.map(function (c, i) {
      return '<li' + (i > 1 ? ' data-locked="true"' : '') + '>' + esc(c) + '</li>';
    }).join('') + '</ol>';

    var variant = '';
    var other = item.proVariant || item.coreVariant;
    if (other && catalog.byId[other]) {
      var o = catalog.byId[other];
      variant = '<p class="faint">' + t(item.proVariant ? 'alsoPro' : 'alsoCore') + ' ' +
        '<button class="btn btn--quiet btn--sm" data-teaser="' + esc(o.id) + '">' + esc(pick(o.title)) + ' \u2014 ' + euro(o.price) + '</button></p>';
    }

    var sample = item.sample
      ? '<a class="btn btn--ghost btn--sm" href="' + esc(item.sample) + '" target="_blank" rel="noopener">' + t('samplePdf') + '</a>'
      : '';

    return '<div class="teaser">' +
      '<div>' + coverHTML(item) +
        '<div class="badgerow mt-4">' + (pick(item.badges) || []).map(function (b) {
          return '<span class="badge' + (b.toLowerCase() === 'pro' ? ' badge--pro' : '') + '">' + esc(b) + '</span>';
        }).join('') + '</div>' +
        '<p class="hb-card__meta num mt-4">' + item.pages + ' ' + t('pages') + ' \u00b7 ' + item.weeks + ' ' + t('weeks') +
        ' \u00b7 ' + item.languages.map(function (l) { return l.toUpperCase(); }).join(' / ') + '</p>' +
      '</div>' +
      '<div>' +
        '<p class="eyebrow">' + esc(famLabel(item)) + ' \u00b7 ' + esc(item.version) + '</p>' +
        '<h2>' + esc(pick(item.title)) + '</h2>' +
        '<p class="lede">' + esc(pick(item.tagline)) + '</p>' +
        '<p class="teaser__quote">' + esc(pick(item.teaserQuote)) + '</p>' +
        block(t('whatIsIt'), '<p>' + esc(pick(item.summary)) + '</p>') +
        block(t('forWhom'), '<p>' + esc(pick(item.audience)) + '</p>') +
        block(t('whatYouLearn'), learn) +
        block(t('contents'), tocHTML + '<p class="faint mt-4">' + t('lockedNote') + '</p>') +
        variant +
        '<div class="teaser__buy">' +
          '<p class="teaser__price"><b class="num">' + euro(item.price) + '</b>' +
            (item.compareAt ? ' <s class="num faint">' + euro(item.compareAt) + '</s>' : '') + '</p>' +
          '<button class="btn btn--primary" data-add="' + esc(item.id) + '">' + t('addToCart') + '</button>' +
          sample +
        '</div>' +
        '<p class="faint mt-4">' + t('vatNote') + '</p>' +
      '</div>' +
    '</div>';
  }

  var modal;
  function openTeaser(id) {
    var item = catalog.byId[id];
    if (!item) return;
    if (!modal) {
      modal = el('<div class="modal" role="dialog" aria-modal="true" aria-label="' + t('preview') + '">' +
        '<div class="modal__scrim" data-close></div>' +
        '<div class="modal__panel"><button class="modal__close" data-close aria-label="' + t('close') + '">\u00d7</button>' +
        '<div class="modal__content"></div></div></div>');
      document.body.appendChild(modal);
      modal.addEventListener('click', function (e) {
        if (e.target.hasAttribute('data-close')) closeTeaser();
      });
    }
    modal.querySelector('.modal__content').innerHTML = teaserHTML(item);
    modal.setAttribute('data-open', 'true');
    document.documentElement.style.overflow = 'hidden';
    modal.querySelector('.modal__close').focus();
  }
  function closeTeaser() {
    if (modal) modal.setAttribute('data-open', 'false');
    document.documentElement.style.overflow = '';
  }

  /* --- winkelwagen -------------------------------------------------------
     Frontend-only. De echte betaling koppel je in checkout() — zie README,
     sectie "Betaalprovider koppelen".
     -------------------------------------------------------------------- */
  var KEY = 'nforce.cart.v1';
  var cart = {
    read: function () {
      try { return JSON.parse(store.get(KEY) || '[]'); } catch (e) { return []; }
    },
    write: function (arr) {
      store.set(KEY, JSON.stringify(arr));
      render();
    },
    add: function (id) {
      var arr = cart.read();
      if (arr.indexOf(id) === -1) arr.push(id); // digitale producten: max 1 per stuk
      cart.write(arr);
      openDrawer();
    },
    remove: function (id) {
      cart.write(cart.read().filter(function (x) { return x !== id; }));
    },
    clear: function () { cart.write([]); },
    total: function () {
      return cart.read().reduce(function (sum, id) {
        var it = catalog && catalog.byId[id];
        return sum + (it ? it.price : 0);
      }, 0);
    },
    count: function () { return cart.read().length; }
  };

  var drawer;
  function buildDrawer() {
    drawer = el('<div class="drawer" role="dialog" aria-modal="true" aria-label="' + t('cart') + '">' +
      '<div class="drawer__scrim" data-close></div>' +
      '<div class="drawer__panel">' +
        '<div class="drawer__head"><h3>' + t('cart') + '</h3>' +
        '<button class="modal__close" data-close aria-label="' + t('close') + '">\u00d7</button></div>' +
        '<div class="drawer__body"></div>' +
        '<div class="drawer__foot"></div>' +
      '</div></div>');
    document.body.appendChild(drawer);
    drawer.addEventListener('click', function (e) {
      if (e.target.hasAttribute('data-close')) closeDrawer();
      var del = e.target.getAttribute('data-remove');
      if (del) cart.remove(del);
      if (e.target.hasAttribute('data-checkout')) checkout();
    });
  }
  function openDrawer() {
    if (!drawer) buildDrawer();
    render();
    drawer.setAttribute('data-open', 'true');
  }
  function closeDrawer() { if (drawer) drawer.setAttribute('data-open', 'false'); }

  function render() {
    var n = cart.count();
    document.querySelectorAll('[data-cart-count]').forEach(function (node) {
      node.textContent = n;
      var btn = node.closest('.cartbtn');
      if (btn) btn.setAttribute('data-empty', n === 0 ? 'true' : 'false');
    });
    if (!drawer || !catalog) return;

    var body = drawer.querySelector('.drawer__body');
    var foot = drawer.querySelector('.drawer__foot');
    var ids = cart.read();
    if (!ids.length) {
      body.innerHTML = '<p class="cart-empty">' + t('cartEmpty') + '</p>';
      foot.innerHTML = '<a class="btn btn--ghost btn--block" href="/' + lang + '/' + t('slugHandbooks') + '/">' + t('toHandbooks') + '</a>';
      return;
    }
    body.innerHTML = ids.map(function (id) {
      var it = catalog.byId[id];
      if (!it) return '';
      return '<div class="cartline">' + coverHTML(it, true) +
        '<div><b>' + esc(pick(it.title)) + '</b><small>' + esc(it.version.toUpperCase()) + ' \u00b7 ' + it.pages + ' ' + t('pages') + '</small>' +
        '<button class="cartline__del" data-remove="' + esc(id) + '">' + t('remove') + '</button></div>' +
        '<span class="cartline__price">' + euro(it.price) + '</span></div>';
    }).join('');
    foot.innerHTML =
      '<div class="carttotal"><span>' + t('total') + '</span><b>' + euro(cart.total()) + '</b></div>' +
      '<p class="faint">' + t('vatNote') + '</p>' +
      '<button class="btn btn--primary btn--block" data-checkout>' + t('checkout') + '</button>' +
      '<a class="btn btn--quiet btn--sm" href="/' + lang + '/' + t('slugHandbooks') + '/">' + t('continueShopping') + '</a>';
  }

  /* ----------------------------------------------------------------------
     CHECKOUT — HIER KOPPEL JE DE BETAALPROVIDER
     ----------------------------------------------------------------------
     Nu: de wagen wordt opgeslagen en de bezoeker gaat naar de
     bestelpagina met een samenvatting en een mailto/formulier-fallback.

     Stripe (aanbevolen, werkt zonder eigen server):
       1. Maak per handboek een Payment Link in Stripe.
       2. Zet die URL in handbooks.json als veld "paymentLink".
       3. Vervang de regel onder KOPPELPUNT door:
            location.href = catalog.byId[ids[0]].paymentLink;
          of, voor meerdere producten, een Stripe Checkout Session via een
          kleine serverless functie (Netlify Functions / Vercel).
     Mollie of Plug&Pay: zelfde principe, één betaal-URL per product.
     -------------------------------------------------------------------- */
  function checkout() {
    var ids = cart.read();
    if (!ids.length) return;
    /* KOPPELPUNT betaalprovider */
    location.href = '/' + lang + '/' + t('slugCheckout') + '/';
  }

  /* --- init -------------------------------------------------------------- */
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  var readyPromise = Promise.all([data.ui(), loadCatalog()]).then(function (res) {
    UI = res[0];
    return res[1];
  });

  ready(function () {
    document.addEventListener('click', function (e) {
      var add = e.target.getAttribute && e.target.getAttribute('data-add');
      if (add) { readyPromise.then(function () { cart.add(add); }); return; }
      var teaser = e.target.getAttribute && e.target.getAttribute('data-teaser');
      if (teaser) { readyPromise.then(function () { openTeaser(teaser); }); return; }
      if (e.target.closest && e.target.closest('[data-open-cart]')) {
        e.preventDefault();
        readyPromise.then(openDrawer);
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeTeaser(); closeDrawer(); }
    });
    readyPromise.then(render);
  });

  return {
    lang: lang, langs: LANGS, t: t, pick: pick, euro: euro, esc: esc, el: el, qs: qs,
    data: data, cart: cart, catalog: function () { return catalog; },
    coverHTML: coverHTML, cardHTML: cardHTML, openTeaser: openTeaser,
    openCart: openDrawer, ready: readyPromise, store: store, onReady: ready
  };
})();
