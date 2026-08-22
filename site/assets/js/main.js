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
    var endpoint = form.getAttribute('data-endpoint') || '';
    var endpointReady = endpoint.indexOf('JOUW-FORMULIER-ID') === -1 && /^https:\/\//.test(endpoint);
    var submitBtn = form.querySelector('button[type="submit"]');
    var busy = false;

    function setStatus(state, key, fallback) {
      status.dataset.state = state;
      status.textContent = t(key, fallback);
    }

    function validate() {
      var values = {
        naam: form.naam.value.trim(),
        email: form.email.value.trim(),
        soort: form.soort.value,
        bericht: form.bericht.value.trim()
      };
      var missing = [];
      [['naam', values.naam], ['email', values.email], ['bericht', values.bericht]].forEach(function (pair) {
        var field = form[pair[0]];
        var ok = pair[1] !== '';
        if (pair[0] === 'email') ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(pair[1]);
        field.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok) missing.push(pair[0]);
      });
      return { values: values, missing: missing };
    }

    /* Terugval: openen van het e-mailprogramma met het bericht al ingevuld.
       Wordt gebruikt zolang er geen formulier-ID is ingevuld, en als het
       versturen mislukt (bijvoorbeeld zonder internet). */
    function openMailClient(v) {
      var subject = t('form.subject', 'Aanvraag via website — ') + v.soort;
      var body = [
        t('form.body_name', 'Naam') + ': ' + v.naam,
        t('form.body_email', 'E-mail') + ': ' + v.email,
        t('form.body_topic', 'Onderwerp') + ': ' + v.soort,
        '',
        v.bericht
      ].join('\n');
      var href = 'mailto:nick@nforce-performance.nl?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      setStatus('info', 'form.status_info', 'Je e-mailprogramma wordt geopend met dit bericht. Het is nog niet verzonden — je verstuurt het zelf. Opent er niets? Mail dan naar nick@nforce-performance.nl.');
      var win = window.open(href, '_self');
      if (win === null) {
        setStatus('error', 'form.status_nomail', 'Er is geen e-mailprogramma gekoppeld in deze browser. Mail het bericht zelf naar nick@nforce-performance.nl.');
      }
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (busy) return;

      var check = validate();
      if (check.missing.length) {
        setStatus('error', 'form.error', 'Vul je naam, een geldig e-mailadres en een bericht in.');
        form[check.missing[0]].focus();
        return;
      }

      // Spamval: door een mens nooit ingevuld. Doen alsof het gelukt is.
      if (form.website && form.website.value !== '') {
        setStatus('success', 'form.status_sent', 'Bedankt, je bericht is verstuurd. Ik reageer meestal binnen één werkdag.');
        form.reset();
        return;
      }

      if (!endpointReady || typeof window.fetch !== 'function') {
        openMailClient(check.values);
        return;
      }

      busy = true;
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.dataset.label = submitBtn.textContent;
        submitBtn.textContent = t('form.sending', 'Versturen…');
      }
      setStatus('info', 'form.sending', 'Versturen…');

      var payload = new FormData();
      payload.append('naam', check.values.naam);
      payload.append('email', check.values.email);
      payload.append('onderwerp', check.values.soort);
      payload.append('bericht', check.values.bericht);
      payload.append('_subject', t('form.subject', 'Aanvraag via website — ') + check.values.soort);
      payload.append('_replyto', check.values.email);

      fetch(endpoint, {
        method: 'POST',
        body: payload,
        headers: { 'Accept': 'application/json' }
      })
        .then(function (res) {
          if (!res.ok) throw new Error('HTTP ' + res.status);
          setStatus('success', 'form.status_sent', 'Bedankt, je bericht is verstuurd. Ik reageer meestal binnen één werkdag.');
          form.reset();
          ['naam', 'email', 'bericht'].forEach(function (n) { form[n].setAttribute('aria-invalid', 'false'); });
        })
        .catch(function () {
          setStatus('error', 'form.status_failed', 'Versturen lukte niet. Ik open je e-mailprogramma zodat je het bericht alsnog kunt sturen.');
          window.setTimeout(function () { openMailClient(check.values); }, 1200);
        })
        .then(function () {
          busy = false;
          if (submitBtn) {
            submitBtn.disabled = false;
            if (submitBtn.dataset.label) submitBtn.textContent = submitBtn.dataset.label;
          }
        });
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


/* ================================================================
   MICRO-ANIMATIES
   Alles hieronder controleert eerst of de bezoeker "verminderde
   beweging" aan heeft staan. Zo ja, dan gebeurt er niets en blijft
   de site volledig bruikbaar zonder animatie.
   ================================================================ */
(function () {
  'use strict';

  var motionQuery = window.matchMedia
    ? window.matchMedia('(prefers-reduced-motion: reduce)')
    : { matches: false, addEventListener: function () {} };

  function motionOk() { return !motionQuery.matches; }

  /* ---------- 2. Leesvoortgang bovenaan ---------- */
  var bar = null;
  function initProgress() {
    if (!motionOk() || bar) return;
    bar = document.createElement('div');
    bar.className = 'progress-bar';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
  }

  /* ---------- 3. Header verdicht + 10. WhatsApp verschijnt ---------- */
  var header = document.getElementById('siteHeader');
  var wa = document.querySelector('.wa-float');
  var ticking = false;

  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      var y = window.pageYOffset || document.documentElement.scrollTop;

      if (header) header.classList.toggle('is-scrolled', y > 40);
      if (wa) wa.classList.toggle('is-in', y > 500 || !motionOk());

      if (bar) {
        var doc = document.documentElement;
        var max = (doc.scrollHeight - window.innerHeight) || 1;
        bar.style.transform = 'scaleX(' + Math.min(y / max, 1).toFixed(4) + ')';
      }
      ticking = false;
    });
  }

  /* ---------- 4. Getrapte reveal ---------- */
  function stagger() {
    if (!motionOk()) return;
    document.querySelectorAll('.plans, .partners, .results, .reviews, .steps, .split, .footer-inner').forEach(function (group) {
      var items = group.querySelectorAll(':scope > .reveal');
      items.forEach(function (el, i) {
        el.style.setProperty('--reveal-delay', Math.min(i * 70, 350) + 'ms');
      });
    });
  }

  /* ---------- 9. Cijfers tellen op zodra ze in beeld komen ---------- */
  function parseNumber(text) {
    var m = String(text).match(/^([^\d-]*)(-?[\d.,]+)(.*)$/);
    if (!m) return null;
    var raw = m[2];
    // Nederlandse notatie: komma is decimaalteken
    var decimals = raw.indexOf(',') > -1 ? raw.length - raw.indexOf(',') - 1 : 0;
    var value = parseFloat(raw.replace(/\./g, '').replace(',', '.'));
    if (isNaN(value)) return null;
    return { prefix: m[1], value: value, suffix: m[3], decimals: decimals };
  }

  function formatNumber(value, decimals) {
    return decimals > 0 ? value.toFixed(decimals).replace('.', ',') : String(Math.round(value));
  }

  function countUp(el) {
    if (el.dataset.counted === '1') return;
    var parsed = parseNumber(el.textContent.trim());
    if (!parsed) return;
    el.dataset.counted = '1';
    if (!motionOk()) return;

    var startValue = parsed.value * 0.82;
    var duration = 850;
    var t0 = null;

    function step(now) {
      if (t0 === null) t0 = now;
      var p = Math.min((now - t0) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var current = startValue + (parsed.value - startValue) * eased;
      el.textContent = parsed.prefix + formatNumber(current, parsed.decimals) + parsed.suffix;
      if (p < 1) window.requestAnimationFrame(step);
      else el.textContent = parsed.prefix + formatNumber(parsed.value, parsed.decimals) + parsed.suffix;
    }
    window.requestAnimationFrame(step);
  }

  function initCounters() {
    // Alleen meetresultaten tellen op. Prijzen bewust niet: tijdens de
    // animatie zou er kort een lager bedrag staan dan wat het werkelijk kost,
    // en een prijs hoort nooit iets anders te tonen dan de echte prijs.
    var targets = document.querySelectorAll('.result__to');
    if (!targets.length || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        countUp(entry.target);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.6 });
    targets.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Starten ---------- */
  function start() {
    stagger();
    initProgress();
    initCounters();
    onScroll();
  }

  start();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });

  // Verandert de bezoeker zijn voorkeur tijdens het bezoek, dan volgen we die.
  if (motionQuery.addEventListener) {
    motionQuery.addEventListener('change', function () {
      if (!motionOk() && bar) { bar.remove(); bar = null; }
      if (motionOk()) initProgress();
      if (wa) wa.classList.toggle('is-in', !motionOk());
      onScroll();
    });
  }
})();


/* ================================================================
   CTA-MICROINTERACTIE EN OPENEN VAN HET FORMULIER
   1. Knop indrukken (~170ms) + korte bevestigingsring na de klik.
   2. Klik op "Plan een kennismaking" scrolt naar het contactblok,
      laat het formulier met fade en slide binnenkomen en zet de
      cursor in het eerste veld.
   Alles wordt overgeslagen bij "verminderde beweging".
   ================================================================ */
(function () {
  'use strict';

  var mq = window.matchMedia
    ? window.matchMedia('(prefers-reduced-motion: reduce)')
    : { matches: false };
  function motionOk() { return !mq.matches; }

  var PRESS_MS = 170;

  /* ---------- 1. Indrukken en bevestigen ---------- */
  var buttons = document.querySelectorAll('.btn--accent, .btn--ghost');

  buttons.forEach(function (btn) {
    function press() {
      if (!motionOk()) return;
      btn.classList.add('is-pressed');
      window.setTimeout(function () { btn.classList.remove('is-pressed'); }, PRESS_MS);
    }

    function confirm() {
      if (!motionOk()) return;
      btn.classList.remove('is-confirmed');
      // Forceer herstart van de animatie
      void btn.offsetWidth;
      btn.classList.add('is-confirmed');
      window.setTimeout(function () { btn.classList.remove('is-confirmed'); }, 500);
    }

    btn.addEventListener('pointerdown', press);
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') press();
    });
    btn.addEventListener('click', function () {
      window.setTimeout(confirm, PRESS_MS - 40);
    });
  });

  /* ---------- 2. Formulier openen met fade en slide ---------- */
  var form = document.getElementById('contactForm');
  var contact = document.getElementById('contact');

  function openForm() {
    if (!form) return;

    function animateAndFocus() {
      if (motionOk()) {
        form.classList.remove('is-opening');
        void form.offsetWidth;
        form.classList.add('is-opening');
        window.setTimeout(function () { form.classList.remove('is-opening'); }, 1000);
      }
      // Focus na de animatie, zodat de pagina niet terugspringt.
      window.setTimeout(function () {
        var first = form.querySelector('input, textarea, select');
        if (first) first.focus({ preventScroll: true });
      }, motionOk() ? 420 : 0);
    }

    if (!contact) { animateAndFocus(); return; }

    contact.scrollIntoView({
      behavior: motionOk() ? 'smooth' : 'auto',
      block: 'start'
    });

    // Wacht tot het scrollen klaar is voordat het formulier binnenkomt.
    var settled = 0;
    var last = -1;
    var timer = window.setInterval(function () {
      var y = Math.round(window.pageYOffset);
      if (y === last) settled++; else settled = 0;
      last = y;
      if (settled >= 3 || !motionOk()) {
        window.clearInterval(timer);
        animateAndFocus();
      }
    }, 60);
    // Veiligheidsklep: nooit langer dan 1,2 seconde wachten.
    window.setTimeout(function () { window.clearInterval(timer); }, 1200);
  }

  document.querySelectorAll('a[href="#contact"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      if (history.replaceState) history.replaceState(null, '', '#contact');
      openForm();
    });
  });
})();
