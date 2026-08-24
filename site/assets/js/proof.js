/* =============================================================================
   N-Force Performance | Bewijsonderdelen op de resultatenpagina
   -----------------------------------------------------------------------------
   Bouwt drie dingen op uit assets/data/proof.json:

     1. het teamprofiel (mediaan bij nulmeting en hertest, met referentieband)
     2. de benchmarktool (bezoeker vult zijn eigen waarde in)
     3. de tabelweergave onder de grafiek, voor schermlezers en voor wie
        liever getallen leest dan balken

   WAAROM DIT EEN APART BESTAND IS
   Deze code hoort bij een pagina. main.js hoort bij de hele site. Door ze
   gescheiden te houden laden de andere vijf pagina's dit niet mee.

   WAAROM DE TEKST HIER NIET IN STAAT
   Alles wat een bezoeker leest komt uit assets/i18n/*.json onder "proof".
   Deze code haalt die tekst op via window.NForce.t() en bouwt opnieuw op
   zodra iemand van taal wisselt. Zet hier dus nooit losse zinnen in.

   DE VOORBEELDMODUS
   Zolang proof.json op "status": "voorbeeld" staat, zet deze code boven elk
   datablok een zichtbare waarschuwing en geeft de benchmarktool geen oordeel.
   Dat is met opzet. Een verzonnen referentiewaarde laat iemand denken dat
   zijn sprong tekortschiet terwijl dat niet zo is, en dat is erger dan een
   pagina waar nog niets staat.
   ========================================================================== */

(function () {
  'use strict';

  var host = document.querySelector('[data-proof]');
  if (!host) return;

  var DATA = null;
  var reduced = window.matchMedia
    ? window.matchMedia('(prefers-reduced-motion: reduce)')
    : { matches: false };

  /* ---------- Kleine helpers ---------- */

  function t(key, fallback) {
    if (window.NForce && typeof window.NForce.t === 'function') {
      return window.NForce.t(key, fallback);
    }
    return fallback;
  }

  function lang() {
    return (window.NForce && window.NForce.lang) || document.documentElement.lang || 'nl';
  }

  function fill(key, fallback, vars) {
    var s = t(key, fallback);
    Object.keys(vars || {}).forEach(function (k) {
      s = s.split('{' + k + '}').join(vars[k]);
    });
    return s;
  }

  function num(value, decimals) {
    if (value === null || value === undefined || isNaN(value)) return '';
    try {
      return value.toLocaleString(lang(), {
        minimumFractionDigits: decimals, maximumFractionDigits: decimals
      });
    } catch (err) {
      return String(value);
    }
  }

  /* Hoeveel decimalen hoort er bij deze eenheid? Een sprinttijd van 1,8
     seconde is iets anders dan 1,79; een sprong van 44 centimeter meten we
     niet in honderdsten. */
  function decimalsFor(test) {
    return test.eenheid === 's' ? 2 : 1;
  }

  /* Positie op de as, als percentage. Altijd binnen 0 en 100 houden,
     anders schuift een uitschieter buiten het spoor.

     BELANGRIJK: bij een sprinttijd is een LAGERE waarde beter. Zou de as
     dan gewoon van laag naar hoog lopen, dan schuift de hertest-stip naar
     LINKS bij vooruitgang, terwijl hij bij de sprong naar rechts schuift.
     Twee rijen die hetzelfde bedoelen maar de andere kant op wijzen: dat
     leest iedereen verkeerd. Daarom draaien we de as om bij die tests, en
     zetten we de schaalgetallen in dezelfde omgekeerde volgorde eronder.
     Rechts is dan altijd beter, in elke rij. */
  function pos(test, value) {
    var lo = test.schaal[0], hi = test.schaal[1];
    if (hi === lo) return 0;
    var p = ((value - lo) / (hi - lo)) * 100;
    if (test.hogerBeter === false) p = 100 - p;
    return Math.max(0, Math.min(100, p));
  }

  /* Asuiteinden in de volgorde waarin ze getekend worden. */
  function schaalUiteinden(test) {
    return test.hogerBeter === false
      ? [test.schaal[1], test.schaal[0]]
      : [test.schaal[0], test.schaal[1]];
  }

  function heeftReferentie(test) {
    return Array.isArray(test.referentie) && test.referentie.length === 2 &&
      test.referentie[0] !== null && test.referentie[1] !== null;
  }

  function isVoorbeeld() {
    return !DATA || DATA.status !== 'definitief';
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  }

  /* ---------- Waarschuwingsstrook bij voorbeelddata ---------- */

  function waarschuwing() {
    var box = el('p', 'proof-warn');
    box.setAttribute('role', 'note');
    box.appendChild(el('strong', null, t('proof.warn_t', 'Voorbeelddata')));
    box.appendChild(document.createTextNode(' ' + t('proof.warn_x',
      'De cijfers hieronder zijn nog niet ingevuld met echte metingen.')));
    return box;
  }

  /* ---------- 1. Teamprofiel ---------- */

  function renderProfiel(mount) {
    mount.innerHTML = '';
    if (!DATA || !DATA.tests || !DATA.tests.length) return;

    if (isVoorbeeld()) mount.appendChild(waarschuwing());

    /* Legenda. Twee markeringen betekent twee series, dus een legenda is
       verplicht: niemand mag identiteit uit kleur alleen hoeven afleiden. */
    var legend = el('p', 'proof-legend');
    var l1 = el('span', 'proof-legend__item');
    l1.appendChild(el('span', 'proof-legend__dot proof-legend__dot--t1'));
    l1.appendChild(el('span', null, t('proof.legend_t1', 'Nulmeting')));
    var l2 = el('span', 'proof-legend__item');
    l2.appendChild(el('span', 'proof-legend__dot proof-legend__dot--t2'));
    l2.appendChild(el('span', null, t('proof.legend_t2', 'Hertest')));
    legend.appendChild(l1);
    legend.appendChild(l2);
    mount.appendChild(legend);

    var list = el('ul', 'pf');
    list.setAttribute('role', 'list');

    DATA.tests.forEach(function (test) {
      var d = decimalsFor(test);
      var heeftT2 = test.t2 !== null && test.t2 !== undefined;
      var row = el('li', 'pf__row');

      /* Kop: naam links, waarden rechts. De waarden staan hier en niet bij
         de stippen, want bij een kleine verandering zouden twee labels bij
         de stippen over elkaar heen vallen. */
      var head = el('div', 'pf__head');
      head.appendChild(el('span', 'pf__name',
        t('proof.tests.' + test.id + '.name', test.id)));

      var vals = el('span', 'pf__vals');
      vals.appendChild(el('span', 'pf__v1', num(test.t1, d)));
      if (heeftT2) {
        vals.appendChild(el('span', 'pf__sep'));
        vals.appendChild(el('span', 'pf__v2', num(test.t2, d) + ' ' + test.eenheid));
      } else {
        vals.appendChild(el('span', 'pf__unit', ' ' + test.eenheid));
      }
      head.appendChild(vals);
      row.appendChild(head);

      /* Spoor */
      var track = el('div', 'pf__track');
      var x1 = pos(test, test.t1);
      var x2 = heeftT2 ? pos(test, test.t2) : x1;

      if (heeftReferentie(test)) {
        var band = el('div', 'pf__band');
        var b1 = pos(test, test.referentie[0]);
        var b2 = pos(test, test.referentie[1]);
        band.style.left = Math.min(b1, b2) + '%';
        band.style.width = Math.abs(b2 - b1) + '%';
        track.appendChild(band);
      }

      /* Verbindingsstuk tussen de twee stippen. Groeit bij het in beeld
         komen van de nulmeting naar de hertest. */
      if (heeftT2 && x2 !== x1) {
        var link = el('div', 'pf__link');
        link.style.left = Math.min(x1, x2) + '%';
        link.style.setProperty('--w', Math.abs(x2 - x1) + '%');
        track.appendChild(link);
      }

      var dot1 = el('div', 'pf__dot pf__dot--t1');
      dot1.style.left = x1 + '%';
      track.appendChild(dot1);

      if (heeftT2) {
        var dot2 = el('div', 'pf__dot pf__dot--t2');
        dot2.style.setProperty('--from', x1 + '%');
        dot2.style.setProperty('--to', x2 + '%');
        track.appendChild(dot2);
      }
      row.appendChild(track);

      /* Asuiteinden, zodat de stippen een schaal hebben om tegen te lezen */
      var scale = el('div', 'pf__scale');
      var uit = schaalUiteinden(test);
      scale.appendChild(el('span', null, num(uit[0], d) + ' ' + test.eenheid));
      scale.appendChild(el('span', null, num(uit[1], d) + ' ' + test.eenheid));
      row.appendChild(scale);

      /* Toelichting: wat de test meet, plus de referentie of het ontbreken
         daarvan. Dat laatste is geen tekortkoming om weg te moffelen. */
      var what = el('p', 'pf__what',
        t('proof.tests.' + test.id + '.what', ''));
      row.appendChild(what);

      var ref = el('p', 'pf__ref');
      if (heeftReferentie(test)) {
        ref.textContent = fill('proof.ref_x',
          'Referentiebereik {lo} tot {hi} {eenheid}.', {
            lo: num(test.referentie[0], d),
            hi: num(test.referentie[1], d),
            eenheid: test.eenheid
          }) + (test.bron ? ' ' + test.bron : '');
      } else {
        ref.className = 'pf__ref pf__ref--none';
        ref.textContent = t('proof.no_ref',
          'Voor deze test heb ik geen referentiegroep die aansluit bij dit niveau en deze sport. De waarde staat er als startpunt voor de hertest, niet als oordeel.');
      }
      row.appendChild(ref);

      list.appendChild(row);
    });

    mount.appendChild(list);

    /* Onderschrift. Verplicht bij elke grafiek: wie, hoeveel, wanneer, en
       wat er bewust niet in staat. */
    var m = DATA.meting || {};
    var cap = el('p', 'proof-caption', fill('proof.caption',
      'Mediaan van {n} spelers, {niveau}, {t1} en {t2}. De band is het referentiebereik voor dit niveau, geen streefwaarde. Individuele waarden zijn niet weergegeven.', {
        n: m.n === null || m.n === undefined ? '?' : m.n,
        niveau: t(m.niveau_key || 'proof.level.semipro', 'semi-pro niveau'),
        /* De periodes staan in de vertaalbestanden, niet in proof.json:
           "najaar 2025" moet in het Duits ook Duits zijn. */
        t1: t(m.t1_key || 'proof.period_t1', m.t1_label || '?'),
        t2: t(m.t2_key || 'proof.period_t2', m.t2_label || '?')
      }));
    mount.appendChild(cap);

    /* Let op: een gemeten verandering over een seizoen is geen bewijs van
       oorzaak. Dat hoort er zichtbaar bij te staan. */
    mount.appendChild(el('p', 'proof-caption proof-caption--warn',
      t('proof.cause', 'Dit is wat er gemeten is, niet een bewijs van oorzaak: een selectie traint, speelt en ontwikkelt ook zonder begeleiding. Er is geen controlegroep.')));

    mount.appendChild(tabel());
    activeer(mount);
  }

  /* ---------- Tabelweergave ---------- */

  function tabel() {
    var box = el('details', 'proof-table');
    box.appendChild(el('summary', null, t('proof.table_open', 'Bekijk dit als tabel')));

    var tbl = el('table');
    var thead = el('thead');
    var hr = el('tr');
    [t('proof.th_test', 'Test'),
     t('proof.legend_t1', 'Nulmeting'),
     t('proof.legend_t2', 'Hertest'),
     t('proof.th_ref', 'Referentiebereik')].forEach(function (h) {
      var th = el('th', null, h);
      th.setAttribute('scope', 'col');
      hr.appendChild(th);
    });
    thead.appendChild(hr);
    tbl.appendChild(thead);

    var tbody = el('tbody');
    DATA.tests.forEach(function (test) {
      var d = decimalsFor(test);
      var tr = el('tr');
      var th = el('th', null, t('proof.tests.' + test.id + '.name', test.id));
      th.setAttribute('scope', 'row');
      tr.appendChild(th);
      tr.appendChild(el('td', null, num(test.t1, d) + ' ' + test.eenheid));
      tr.appendChild(el('td', null,
        (test.t2 === null || test.t2 === undefined)
          ? t('proof.pending', 'nog niet gemeten')
          : num(test.t2, d) + ' ' + test.eenheid));
      tr.appendChild(el('td', null, heeftReferentie(test)
        ? num(test.referentie[0], d) + ' tot ' + num(test.referentie[1], d) + ' ' + test.eenheid
        : t('proof.no_ref_short', 'geen passende referentie')));
      tbody.appendChild(tr);
    });
    tbl.appendChild(tbody);
    box.appendChild(tbl);
    return box;
  }

  /* ---------- Animatie bij in beeld komen ---------- */

  function activeer(mount) {
    var rows = mount.querySelectorAll('.pf__row');
    if (reduced.matches || !('IntersectionObserver' in window)) {
      rows.forEach(function (r) { r.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var i = Array.prototype.indexOf.call(rows, entry.target);
        entry.target.style.transitionDelay = (i * 70) + 'ms';
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.35 });
    rows.forEach(function (r) { io.observe(r); });
  }

  /* ---------- 2. Benchmarktool ---------- */

  function renderTool(mount) {
    mount.innerHTML = '';
    if (!DATA || !DATA.tests || !DATA.tests.length) return;

    if (isVoorbeeld()) mount.appendChild(waarschuwing());

    var controls = el('div', 'bench__controls');

    var f1 = el('div', 'field');
    var lblTest = el('label', null, t('proof.tool_test', 'Welke test?'));
    lblTest.setAttribute('for', 'benchTest');
    var sel = el('select');
    sel.id = 'benchTest';
    DATA.tests.forEach(function (test, i) {
      var opt = el('option', null, t('proof.tests.' + test.id + '.name', test.id));
      opt.value = String(i);
      sel.appendChild(opt);
    });
    f1.appendChild(lblTest);
    f1.appendChild(sel);

    var f2 = el('div', 'field');
    var lblVal = el('label', null, t('proof.tool_value', 'Jouw waarde'));
    lblVal.setAttribute('for', 'benchValue');
    var wrap = el('div', 'bench__input');
    var input = el('input');
    input.id = 'benchValue';
    input.type = 'number';
    input.step = 'any';
    input.setAttribute('inputmode', 'decimal');
    input.setAttribute('autocomplete', 'off');
    var unit = el('span', 'bench__unit');
    wrap.appendChild(input);
    wrap.appendChild(unit);
    f2.appendChild(lblVal);
    f2.appendChild(wrap);

    controls.appendChild(f1);
    controls.appendChild(f2);
    mount.appendChild(controls);

    var track = el('div', 'pf__track bench__track');
    var band = el('div', 'pf__band');
    var mark = el('div', 'bench__mark');
    mark.hidden = true;
    track.appendChild(band);
    track.appendChild(mark);
    mount.appendChild(track);

    var scale = el('div', 'pf__scale');
    var s1 = el('span'), s2 = el('span');
    scale.appendChild(s1);
    scale.appendChild(s2);
    mount.appendChild(scale);

    var verdict = el('p', 'bench__verdict');
    verdict.setAttribute('role', 'status');
    verdict.setAttribute('aria-live', 'polite');
    mount.appendChild(verdict);

    var caveat = el('p', 'bench__caveat', t('proof.tool_caveat',
      'Dit is een indicatie, geen oordeel. Een testwaarde krijgt pas betekenis naast de rest van je profiel, je sport, je positie en de fase van je seizoen.'));
    mount.appendChild(caveat);

    function huidige() { return DATA.tests[parseInt(sel.value, 10) || 0]; }

    function tekenLeeg() {
      var test = huidige();
      var d = decimalsFor(test);
      unit.textContent = test.eenheid;
      input.setAttribute('placeholder', num((test.schaal[0] + test.schaal[1]) / 2, d));
      var uit = schaalUiteinden(test);
      s1.textContent = num(uit[0], d) + ' ' + test.eenheid;
      s2.textContent = num(uit[1], d) + ' ' + test.eenheid;

      if (heeftReferentie(test)) {
        var b1 = pos(test, test.referentie[0]);
        var b2 = pos(test, test.referentie[1]);
        band.hidden = false;
        band.style.left = Math.min(b1, b2) + '%';
        band.style.width = Math.abs(b2 - b1) + '%';
      } else {
        band.hidden = true;
      }
      mark.hidden = true;
      verdict.textContent = '';
    }

    function beoordeel() {
      var test = huidige();
      var raw = parseFloat(String(input.value).replace(',', '.'));
      if (isNaN(raw)) { mark.hidden = true; verdict.textContent = ''; return; }

      var d = decimalsFor(test);
      mark.hidden = false;
      mark.style.left = pos(test, raw) + '%';

      if (isVoorbeeld()) {
        verdict.className = 'bench__verdict bench__verdict--none';
        verdict.textContent = t('proof.tool_novalues',
          'Zodra de referentiewaarden zijn ingevuld staat hier wat jouw waarde betekent. Tot die tijd geef ik liever geen oordeel dan een oordeel op verzonnen cijfers.');
        return;
      }
      if (!heeftReferentie(test)) {
        verdict.className = 'bench__verdict bench__verdict--none';
        verdict.textContent = t('proof.no_ref',
          'Voor deze test heb ik geen referentiegroep die aansluit bij dit niveau en deze sport.');
        return;
      }

      var lo = test.referentie[0], hi = test.referentie[1];
      var binnen = raw >= lo && raw <= hi;
      var boven = test.hogerBeter ? raw > hi : raw < lo;
      var key = binnen ? 'proof.verdict_in' : (boven ? 'proof.verdict_over' : 'proof.verdict_under');
      var vast = {
        'proof.verdict_in': 'Je zit binnen het referentiebereik voor dit niveau.',
        'proof.verdict_over': 'Je zit boven het referentiebereik voor dit niveau.',
        'proof.verdict_under': 'Je zit onder het referentiebereik voor dit niveau.'
      };
      verdict.className = 'bench__verdict' + (binnen ? ' bench__verdict--in' : '');
      verdict.textContent = fill(key, vast[key], {
        waarde: num(raw, d),
        eenheid: test.eenheid,
        lo: num(lo, d),
        hi: num(hi, d)
      });
    }

    sel.addEventListener('change', function () { tekenLeeg(); beoordeel(); });
    input.addEventListener('input', beoordeel);
    tekenLeeg();
  }

  /* ---------- Opbouwen en opnieuw opbouwen bij taalwissel ---------- */

  function render() {
    var profiel = host.querySelector('[data-proof-chart]');
    var tool = host.querySelector('[data-proof-tool]');
    if (profiel) renderProfiel(profiel);
    if (tool) renderTool(tool);
  }

  fetch('assets/data/proof.json', { cache: 'no-cache' })
    .then(function (res) {
      if (!res.ok) throw new Error('proof.json: ' + res.status);
      return res.json();
    })
    .then(function (data) {
      DATA = data;
      render();
    })
    .catch(function (err) {
      /* Data niet te laden? Dan blijft de pagina gewoon werken en staat er
         niets misleidends. Alleen een regel in de console voor jou. */
      if (window.console) console.warn(err && err.message ? err.message : err);
    });

  window.addEventListener('nforce:lang', function () { if (DATA) render(); });
  if (reduced.addEventListener) reduced.addEventListener('change', render);
})();
