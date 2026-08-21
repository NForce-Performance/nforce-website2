/* N-Force Performance | Kracht & Conditie — interactie (dark-only, geen thema-wissel) */

/* =============================================================================
   MEERTALIGHEID (i18n) — hoe voeg je een taal toe?
   -----------------------------------------------------------------------------
   1. Kopieer assets/i18n/nl.json naar assets/i18n/<taalcode>.json
      (taalcode = ISO 639-1, bijv. "fr", "sv", "da").
   2. Vertaal in dat bestand alleen de waarden; laat de sleutels ongewijzigd.
      - HTML-tags in waarden (<strong>, <a>, <br>, <span class="placeholder">)
        blijven staan; ze worden bewust als HTML ingevoegd.
      - Vaktermen "Strength & Conditioning" en "return to play" blijven Engels.
      - [aanvullen]-markeringen blijven staan tot de gegevens bekend zijn.
   3. Zet de taalcode in de array LANGS hieronder. Dat is de ENIGE plek in de
      JavaScript die je hoeft aan te passen: de taalkiezer, de detectie en het
      opslaan van de keuze werken daarna automatisch.
   4. Voeg in nl.json/en.json/de.json (en de nieuwe taal) onder "lang.names" de
      naam van de nieuwe taal toe, en in het nieuwe bestand "lang.code" (de
      korte code die in de knop staat, bijv. "FR").
   5. Voeg in index.html en privacy.html een <link rel="alternate" hreflang="..">
      toe voor de nieuwe taal.

   Werking: HTML is Nederlands (NL is de basis), dus zonder JavaScript blijft de
   site volledig leesbaar. Bij het laden bepaalt de code de taal in deze volgorde:
   ?lang=xx in de URL > eerder gekozen taal in een cookie > navigator.language
   > NL. De keuze wordt een jaar bewaard in een first-party cookie (in een
   try/catch, zodat een geblokkeerde cookie niets kapotmaakt) en
   document.documentElement.lang wordt bijgewerkt.
   ========================================================================== */
var LANGS = ['nl', 'en', 'de'];

(function () {
  'use strict';

  var DEFAULT_LANG = LANGS[0];
  var STORAGE_KEY = 'nforce-lang';
  var dict = {};
  var current = DEFAULT_LANG;

  /* ---------- Kleine helpers ---------- */
  var memory = {};
  function store(key, value) {
    memory[key] = value;
    try {
      document.cookie = encodeURIComponent(key) + '=' + encodeURIComponent(value) +
        ';path=/;max-age=31536000;samesite=lax';
    } catch (err) { /* cookie geblokkeerd, we houden het in het geheugen */ }
  }
  function read(key) {
    if (memory[key]) return memory[key];
    try {
      var match = document.cookie.match(
        new RegExp('(?:^|; )' + encodeURIComponent(key).replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '=([^;]*)')
      );
      return match ? decodeURIComponent(match[1]) : null;
    } catch (err) { return null; }
  }
  function normalise(code) {
    if (!code) return null;
    var base = String(code).toLowerCase().split('-')[0];
    return LANGS.indexOf(base) > -1 ? base : null;
  }
  function t(key, fallback) {
    var parts = key.split('.');
    var node = dict;
    for (var i = 0; i < parts.length; i++) {
      if (node == null || typeof node !== 'object') return fallback;
      node = node[parts[i]];
    }
    return typeof node === 'string' ? node : fallback;
  }

  /* ---------- Taal bepalen ---------- */
  function detect() {
    var params;
    try { params = new URLSearchParams(window.location.search); } catch (err) { params = null; }
    var fromUrl = params ? normalise(params.get('lang')) : null;
    if (fromUrl) return fromUrl;

    var stored = normalise(read(STORAGE_KEY));
    if (stored) return stored;

    var navLangs = navigator.languages && navigator.languages.length
      ? navigator.languages
      : [navigator.language || navigator.userLanguage];
    for (var i = 0; i < navLangs.length; i++) {
      var hit = normalise(navLangs[i]);
      if (hit) return hit;
    }
    return DEFAULT_LANG;
  }

  /* ---------- Vertalingen toepassen ---------- */
  function apply() {
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var value = t(el.getAttribute('data-i18n'), null);
      if (value !== null) el.textContent = value;
    });
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var value = t(el.getAttribute('data-i18n-html'), null);
      if (value !== null) el.innerHTML = value;
    });
    document.querySelectorAll('[data-i18n-attr]').forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(',').forEach(function (pair) {
        var bits = pair.split(':');
        if (bits.length < 2) return;
        var attr = bits[0].trim();
        var value = t(bits.slice(1).join(':').trim(), null);
        if (value !== null) el.setAttribute(attr, value);
      });
    });
    document.documentElement.setAttribute('lang', current);
    syncMenuLabel();
    updateSwitchers();
    updateInternalLinks();
  }

  /* ---------- Interne links de taalkeuze meegeven ---------- */
  function updateInternalLinks() {
    document.querySelectorAll('a[href]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href || !/\.html(\?|#|$)/.test(href) || /^https?:/i.test(href)) return;
      var base = href.split('#')[0].split('?')[0];
      var hash = href.indexOf('#') > -1 ? href.slice(href.indexOf('#')) : '';
      a.setAttribute('href', current === DEFAULT_LANG ? base + hash : base + '?lang=' + current + hash);
    });
  }

  /* ---------- Taal laden ---------- */
  function load(lang, remember) {
    return fetch('assets/i18n/' + lang + '.json', { cache: 'no-cache' })
      .then(function (res) {
        if (!res.ok) throw new Error('i18n ' + lang + ': ' + res.status);
        return res.json();
      })
      .then(function (data) {
        dict = data;
        current = lang;
        if (remember) store(STORAGE_KEY, lang);
        apply();
      })
      .catch(function (err) {
        if (window.console) console.warn(err && err.message ? err.message : err);
      });
  }


  /* ---------- Menu-links naar verborgen secties automatisch verbergen ----------
     Zo hoef je alleen het woord "hidden" bij een <section> weg te halen;
     de bijbehorende links in het menu en de footer verschijnen dan vanzelf. */
  function syncHiddenSectionLinks() {
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      if (!id) return;
      var target = document.getElementById(id);
      if (target && target.hasAttribute('hidden')) {
        link.hidden = true;
      } else if (link.hidden) {
        link.hidden = false;
      }
    });
  }
  syncHiddenSectionLinks();

  /* ---------- Taalkiezer (opgebouwd uit LANGS) ---------- */
  var switchers = [];

  function buildSwitchers() {
    document.querySelectorAll('[data-lang-switcher]').forEach(function (host, index) {
      host.hidden = false;
      host.innerHTML = '';

      var menuId = 'langMenu' + index;
      var toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'lang__toggle';
      toggle.setAttribute('aria-haspopup', 'true');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-controls', menuId);
      toggle.innerHTML = '<span class="lang__code"></span><svg class="lang__chevron" viewBox="0 0 12 8" width="10" height="7" aria-hidden="true" fill="none"><path d="M1 1.5 6 6.5l5-5" stroke="currentColor" stroke-width="1.6" stroke-linecap="square"/></svg>';

      var menu = document.createElement('div');
      menu.className = 'lang__menu';
      menu.id = menuId;
      menu.setAttribute('role', 'menu');
      menu.hidden = true;

      LANGS.forEach(function (code) {
        var item = document.createElement('button');
        item.type = 'button';
        item.className = 'lang__option';
        item.setAttribute('role', 'menuitem');
        item.setAttribute('lang', code);
        item.dataset.lang = code;
        function choose(e) {
          if (e) e.preventDefault();
          setOpen(false);
          if (code !== current) load(code, true);
        }
        item.addEventListener('click', choose);
        menu.appendChild(item);
      });

      function setOpen(open) {
        toggle.setAttribute('aria-expanded', String(open));
        menu.hidden = !open;
        host.classList.toggle('is-open', open);
      }

      toggle.addEventListener('click', function (e) {
        setOpen(toggle.getAttribute('aria-expanded') !== 'true');
        // Alleen bij toetsenbordbediening (detail === 0) de focus verplaatsen.
        // Op touchscreens zorgt focus() ervoor dat het menu direct weer sluit.
        if (!menu.hidden && e.detail === 0) {
          var first = menu.querySelector('.lang__option[aria-current="true"]') || menu.querySelector('.lang__option');
          if (first) first.focus();
        }
      });

      host.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
          e.stopPropagation();
          setOpen(false);
          toggle.focus();
        }
      });

      document.addEventListener('click', function (e) {
        if (!host.contains(e.target)) setOpen(false);
      });
      host.addEventListener('focusout', function (e) {
        // Op mobiel is relatedTarget vaak null bij een tik; dan niet sluiten,
        // anders verdwijnt het menu voordat de taalkeuze geregistreerd wordt.
        if (e.relatedTarget && !host.contains(e.relatedTarget)) setOpen(false);
      });

      host.appendChild(toggle);
      host.appendChild(menu);
      switchers.push({ host: host, toggle: toggle, menu: menu, setOpen: setOpen });
    });
  }

  function updateSwitchers() {
    switchers.forEach(function (s) {
      s.toggle.querySelector('.lang__code').textContent = t('lang.code', current.toUpperCase());
      s.toggle.setAttribute('aria-label', t('lang.label', 'Taal wijzigen') + ' — ' + t('lang.names.' + current, current));
      s.menu.setAttribute('aria-label', t('lang.menu_label', 'Kies een taal'));
      s.menu.querySelectorAll('.lang__option').forEach(function (item) {
        var code = item.dataset.lang;
        item.textContent = t('lang.names.' + code, code.toUpperCase());
        if (code === current) {
          item.setAttribute('aria-current', 'true');
        } else {
          item.removeAttribute('aria-current');
        }
      });
    });
  }

  /* ---------- Mobiel menu ---------- */
  var navToggle = document.querySelector('.nav-toggle');
  var mobileNav = document.getElementById('mobileNav');
  var setMenuOpen = null;
  if (navToggle && mobileNav) {
    setMenuOpen = function (open) {
      navToggle.setAttribute('aria-expanded', String(open));
      navToggle.setAttribute(
        'aria-label',
        open ? t('a11y.menu_close', 'Menu sluiten') : t('a11y.menu_open', 'Menu openen')
      );
      mobileNav.hidden = !open;
    };
    setMenuOpen(false);
    navToggle.addEventListener('click', function () {
      setMenuOpen(navToggle.getAttribute('aria-expanded') !== 'true');
    });
    mobileNav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setMenuOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navToggle.getAttribute('aria-expanded') === 'true') {
        setMenuOpen(false);
        navToggle.focus();
      }
    });
  }

  function syncMenuLabel() {
    if (!setMenuOpen || !navToggle) return;
    var open = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute(
      'aria-label',
      open ? t('a11y.menu_close', 'Menu sluiten') : t('a11y.menu_open', 'Menu openen')
    );
  }

  /* ---------- Scroll reveals ---------- */
  var reveals = document.querySelectorAll('.reveal');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!('IntersectionObserver' in window) || reduce) {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    reveals.forEach(function (el, i) {
      el.style.transitionDelay = Math.min(i % 4, 3) * 70 + 'ms';
      io.observe(el);
    });
  }

  /* ---------- Jaartal in footer ---------- */
  document.querySelectorAll('#jaar').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------- Contactformulier: opent de eigen e-mailclient (mailto) ---------- */
  var form = document.getElementById('contactForm');
  var status = document.getElementById('formStatus');
  if (form && status) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var naam = form.naam.value.trim();
      var email = form.email.value.trim();
      var soort = form.soort.value;
      var bericht = form.bericht.value.trim();

      var missing = [];
      [['naam', naam], ['email', email], ['bericht', bericht]].forEach(function (pair) {
        var field = form[pair[0]];
        var ok = pair[1] !== '';
        if (pair[0] === 'email') ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(pair[1]);
        field.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok) missing.push(pair[0]);
      });

      if (missing.length) {
        status.dataset.state = 'error';
        status.textContent = t('form.error', 'Vul je naam, een geldig e-mailadres en een bericht in.');
        form[missing[0]].focus();
        return;
      }

      var subject = t('form.subject', 'Aanvraag via website — ') + soort;
      var body = [
        t('form.body_name', 'Naam') + ': ' + naam,
        t('form.body_email', 'E-mail') + ': ' + email,
        t('form.body_topic', 'Onderwerp') + ': ' + soort,
        '',
        bericht
      ].join('\n');

      var href = 'mailto:nick@nforce-performance.nl?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);

      status.dataset.state = 'info';
      status.textContent = t('form.status_info', 'Je e-mailprogramma wordt geopend met dit bericht. Het is nog niet verzonden — je verstuurt het zelf. Opent er niets? Mail dan naar nick@nforce-performance.nl.');

      var win = window.open(href, '_self');
      if (win === null) {
        status.dataset.state = 'error';
        status.textContent = t('form.status_nomail', 'Er is geen e-mailprogramma gekoppeld in deze browser. Mail het bericht zelf naar nick@nforce-performance.nl.');
      }
    });
  }

  /* ---------- Start ---------- */
  buildSwitchers();
  var initial = detect();
  if (initial === DEFAULT_LANG) {
    // NL staat al in de HTML: alleen het woordenboek laden voor JS-teksten en de kiezer.
    load(DEFAULT_LANG, false);
  } else {
    load(initial, true);
  }
})();
