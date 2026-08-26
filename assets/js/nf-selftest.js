/* ==========================================================================
   N-FORCE PERFORMANCE — nf-selftest.js
   Zelftest: testdata invullen → vergelijking met referentiewaarden per sport
   → hard rule-based handboekadvies.

   Referentiewaarden: /assets/data/benchmarks.json
   Aanbevelingsregels: /assets/data/rules.json
   Beide zijn data, geen code. Nieuwe regel of nieuwe test = JSON aanvullen.
   ========================================================================== */
(function () {
  'use strict';
  var root = document.getElementById('st-app');
  if (!root) return;

  var t = NF.t, esc = NF.esc, pick = NF.pick;
  var BM, RULES, CAT;

  var PROFILE = {
    sport: [
      { v: 'icehockey', k: 'sportIcehockey' },
      { v: 'football', k: 'sportFootball' },
      { v: 'handball', k: 'sportHandball' },
      { v: 'other', k: 'sportOther' }
    ],
    gender: [{ v: 'm', k: 'stMale' }, { v: 'f', k: 'stFemale' }],
    level: [
      { v: 'recreational', k: 'levelRecreational' },
      { v: 'competitive', k: 'levelCompetitive' },
      { v: 'semi-pro', k: 'levelSemiPro' },
      { v: 'pro', k: 'levelPro' }
    ],
    phase: [
      { v: 'off-season', k: 'phaseOffseason' },
      { v: 'pre-season', k: 'phasePreseason' },
      { v: 'season', k: 'phaseSeason' },
      { v: 'return-to-play', k: 'phaseRtp' }
    ],
    yesno: [{ v: 'no', k: 'stNo' }, { v: 'yes', k: 'stYes' }]
  };

  Promise.all([NF.ready, NF.data.benchmarks(), NF.data.rules()]).then(function (res) {
    CAT = res[0]; BM = res[1]; RULES = res[2];
    build();
  }).catch(function (err) {
    root.innerHTML = '<p class="notice">' + esc(err.message) + '</p>';
  });

  /* --- formulier ---------------------------------------------------------- */
  function sel(name, list, def) {
    return '<select id="st-' + name + '" name="' + name + '">' + list.map(function (o) {
      return '<option value="' + o.v + '"' + (o.v === def ? ' selected' : '') + '>' + t(o.k) + '</option>';
    }).join('') + '</select>';
  }

  function build() {
    var testFields = Object.keys(BM.tests).map(function (id) {
      var test = BM.tests[id];
      var unit = test.unit;
      if (NF.lang === 'en' && test.unitEn) unit = test.unitEn;
      if (NF.lang === 'de' && test.unitDe) unit = test.unitDe;
      return '<div class="field">' +
        '<label for="st-' + id + '">' + esc(pick(test.label)) + ' <span class="faint num">(' + esc(unit) + ')</span></label>' +
        '<input type="number" step="0.01" inputmode="decimal" id="st-' + id + '" name="' + id + '" placeholder="—">' +
        '<small>' + esc(pick(test.help)) + '</small>' +
      '</div>';
    }).join('');

    var provisional = Object.keys(BM.tests).some(function (k) { return BM.tests[k].provisional; });

    root.innerHTML =
      '<div class="selftest">' +
        '<form id="st-form" novalidate>' +
          '<div class="steps" id="st-steps"><span data-active="true">' + t('stAbout') + '</span><span>' + t('stTests') + '</span><span>' + t('stResult') + '</span></div>' +
          '<fieldset><legend>' + t('stAbout').replace(/^\d+ · /, '') + '</legend>' +
            '<div class="testgrid">' +
              '<div class="field"><label for="st-sport">' + t('stSport') + '</label>' + sel('sport', PROFILE.sport, 'icehockey') + '</div>' +
              '<div class="field"><label for="st-gender">' + t('stGender') + '</label>' + sel('gender', PROFILE.gender, 'm') + '</div>' +
              '<div class="field"><label for="st-level">' + t('stLevel') + '</label>' + sel('level', PROFILE.level, 'competitive') + '</div>' +
              '<div class="field"><label for="st-phase">' + t('stPhase') + '</label>' + sel('phase', PROFILE.phase, 'pre-season') + '</div>' +
              '<div class="field"><label for="st-injury">' + t('stInjury') + '</label>' + sel('injury', PROFILE.yesno, 'no') + '</div>' +
              '<div class="field"><label for="st-asymmetry">' + t('stAsymmetry') + '</label>' + sel('asymmetry', PROFILE.yesno, 'no') + '</div>' +
            '</div>' +
          '</fieldset>' +
          '<fieldset><legend>' + t('stTests').replace(/^\d+ · /, '') + '</legend>' +
            '<p class="faint" style="margin-bottom:1rem">' + t('stOptional') + '</p>' +
            '<div class="testgrid">' + testFields + '</div>' +
          '</fieldset>' +
          (provisional ? '<p class="notice"><strong>' + t('stProvisional') + '.</strong> ' + esc(pick(BM.provisionalNotice)) + '</p>' : '') +
          '<div class="actions"><button class="btn btn--primary btn--lg" type="submit">' + t('stAnalyse') + '</button>' +
          '<button class="btn btn--ghost" type="reset">' + t('stReset') + '</button></div>' +
          '<p class="faint mt-4" id="st-error" role="alert"></p>' +
        '</form>' +
        '<div class="result" id="st-result" aria-live="polite"></div>' +
      '</div>';

    document.getElementById('st-form').addEventListener('submit', function (e) {
      e.preventDefault();
      analyse();
    });
    document.getElementById('st-form').addEventListener('reset', function () {
      var r = document.getElementById('st-result');
      r.setAttribute('data-visible', 'false');
      r.innerHTML = '';
      document.getElementById('st-error').textContent = '';
    });
  }

  /* --- meten ------------------------------------------------------------- */
  function bandFor(test, sport, gender) {
    var b = test.bands[sport] || test.bands.all || test.bands['default'];
    if (!b) b = test.bands['default'];
    return (b && (b[gender] || b.m)) || null;
  }

  function statusOf(test, value, band) {
    var low = band[0], high = band[1];
    if (test.higherIsBetter) {
      if (value < low) return 'below';
      if (value > high) return 'above';
      return 'inside';
    }
    if (value > high) return 'below';   // hogere tijd = slechter
    if (value < low) return 'above';
    return 'inside';
  }

  function readForm() {
    var f = document.getElementById('st-form');
    var g = function (n) { return f.elements[n] ? f.elements[n].value : ''; };
    var ctx = {
      sport: g('sport'), gender: g('gender'), level: g('level'),
      phase: g('phase'), injury: g('injury'), asymmetry: g('asymmetry'),
      measures: [], domains: {}, weakDomains: 0, strongDomains: 0
    };
    Object.keys(BM.tests).forEach(function (id) {
      var raw = g(id);
      if (raw === '' || isNaN(parseFloat(raw))) return;
      var test = BM.tests[id];
      var band = bandFor(test, ctx.sport, ctx.gender);
      if (!band) return;
      var value = parseFloat(raw);
      var status = statusOf(test, value, band);
      ctx.measures.push({ id: id, test: test, value: value, band: band, status: status });
      /* strengste uitkomst per domein telt */
      var cur = ctx.domains[test.domain];
      if (!cur || cur === 'inside' && status !== 'inside' || cur === 'above' && status === 'below') {
        ctx.domains[test.domain] = status;
      }
    });
    Object.keys(ctx.domains).forEach(function (d) {
      if (ctx.domains[d] === 'below') ctx.weakDomains++;
      if (ctx.domains[d] === 'above') ctx.strongDomains++;
    });
    return ctx;
  }

  /* --- regels ------------------------------------------------------------ */
  function clauseMatches(c, ctx) {
    if (c.field !== undefined) return (c.in || []).indexOf(ctx[c.field]) !== -1;
    if (c.domain !== undefined) {
      var s = ctx.domains[c.domain];
      if (!s) return false;                       // niet gemeten = geen match
      if (c.is !== undefined) return s === c.is;
      if (c.isNot !== undefined) return s !== c.isNot;
      return true;
    }
    if (c.weakDomains !== undefined) return ctx.weakDomains === c.weakDomains;
    return false;
  }

  function proUpgrade(id, ctx) {
    var item = CAT.byId[id];
    if (!item || !item.proVariant || !CAT.byId[item.proVariant]) return id;
    var cfg = RULES.proUpgrade || {};
    var bySport = (cfg.sports || []).indexOf(ctx.sport) !== -1 && (cfg.levels || []).indexOf(ctx.level) !== -1;
    var byWeak = cfg.alsoWhenWeakDomains !== undefined && ctx.weakDomains >= cfg.alsoWhenWeakDomains;
    return (bySport || byWeak) ? item.proVariant : id;
  }

  function recommend(ctx) {
    var scores = {}, reasons = {}, forced = null;
    RULES.rules.forEach(function (rule) {
      var hit = (rule.when || []).every(function (c) { return clauseMatches(c, ctx); });
      if (!hit) return;
      var id = proUpgrade(rule.handbook, ctx);
      if (!CAT.byId[id]) return;
      scores[id] = (scores[id] || 0) + rule.weight;
      (reasons[id] = reasons[id] || []).push(pick(rule.reason));
      if (rule.blocksPrimaryOthers) forced = id;
    });

    var ranked = Object.keys(scores).sort(function (a, b) { return scores[b] - scores[a]; });
    if (!ranked.length) return { primary: null, secondary: [], scores: scores, reasons: reasons };

    var primary = forced || ranked[0];
    var seenFam = {};
    seenFam[CAT.byId[primary].family] = true;
    var secondary = ranked.filter(function (id) {
      if (id === primary) return false;
      var fam = CAT.byId[id].family;
      if (seenFam[fam]) return false;
      seenFam[fam] = true;
      return true;
    }).slice(0, 2);

    return { primary: primary, secondary: secondary, scores: scores, reasons: reasons };
  }

  /* --- weergave ---------------------------------------------------------- */
  function scaleHTML(m) {
    var ax = m.test.axis, lo = ax[0], hi = ax[1], span = hi - lo;
    var pct = function (v) { return Math.max(0, Math.min(100, ((v - lo) / span) * 100)); };
    var bandLeft = pct(m.band[0]), bandRight = pct(m.band[1]);
    var unit = m.test.unit;
    if (NF.lang === 'en' && m.test.unitEn) unit = m.test.unitEn;
    if (NF.lang === 'de' && m.test.unitDe) unit = m.test.unitDe;
    var statusLabel = { below: t('stBelow'), inside: t('stInside'), above: t('stAbove') }[m.status];
    return '<div class="scale">' +
      '<div class="scale__head"><span class="scale__label">' + esc(pick(m.test.label)) + '</span>' +
      '<span class="scale__status" data-s="' + m.status + '">' + statusLabel + '</span></div>' +
      '<div class="scale__bar">' +
        '<div class="scale__band" style="left:' + bandLeft.toFixed(1) + '%;width:' + Math.max(1, bandRight - bandLeft).toFixed(1) + '%"></div>' +
        '<div class="scale__marker" style="left:calc(' + pct(m.value).toFixed(1) + '% - 1.5px)"></div>' +
      '</div>' +
      '<div class="scale__axis"><span>' + lo + '</span><span>' + t('stRefRange') + ' ' + m.band[0] + '–' + m.band[1] + ' ' + esc(unit) + '</span><span>' + hi + '</span></div>' +
      '<p class="scale__verdict"><span class="scale__value num">' + m.value + ' ' + esc(unit) + '</span> — ' +
        esc(pick(m.test.verdict[m.status])) +
        ' <span class="faint num">(' + t('stErrorNote') + ' \u00b1' + m.test.error + ')</span></p>' +
    '</div>';
  }

  function recHTML(id, rec, ctx, primary) {
    var item = CAT.byId[id];
    var why = (rec.reasons[id] || []).slice(0, 2).map(function (r) {
      return '<p class="rec__why">' + esc(r) + '</p>';
    }).join('');
    var badges = (pick(item.badges) || []).map(function (b) {
      return '<span class="badge' + (b.toLowerCase() === 'pro' ? ' badge--pro' : '') + '">' + esc(b) + '</span>';
    }).join('');
    return '<article class="rec' + (primary ? ' rec--primary' : '') + '">' +
      '<div class="rec__top">' +
        '<span class="badge badge--solid">' + (primary ? t('stPrimary') : t('stUpsellFlag')) + '</span>' +
        '<span class="badge badge--blue num">' + t('stMatch') + ' ' + rec.scores[id] + '</span>' +
        badges +
      '</div>' +
      '<div class="rec__layout">' +
        '<div>' + NF.coverHTML(item, true) + '</div>' +
        '<div>' +
          '<h3>' + esc(pick(item.title)) + '</h3>' +
          '<p class="faint">' + esc(pick(item.tagline)) + '</p>' +
          '<h4 class="mt-4" style="font-family:var(--font-mono);font-size:.6875rem;letter-spacing:.14em;text-transform:uppercase;color:var(--blue)">' + t('stWhy') + '</h4>' +
          why +
          '<div class="rec__actions mt-4">' +
            '<button class="btn btn--primary" data-add="' + esc(item.id) + '">' + t('addToCart') + ' \u00b7 ' + NF.euro(item.price) + '</button>' +
            '<button class="btn btn--ghost" data-teaser="' + esc(item.id) + '">' + t('preview') + '</button>' +
          '</div>' +
        '</div>' +
      '</div>' +
    '</article>';
  }

  function analyse() {
    var ctx = readForm();
    var err = document.getElementById('st-error');
    if (!ctx.measures.length) {
      err.textContent = t('stNeedOne');
      return;
    }
    err.textContent = '';
    var rec = recommend(ctx);
    var host = document.getElementById('st-result');

    var scales = ctx.measures.map(scaleHTML).join('');
    var recCards = '';
    if (rec.primary) {
      recCards = recHTML(rec.primary, rec, ctx, true) +
        rec.secondary.map(function (id) { return recHTML(id, rec, ctx, false); }).join('');
    }
    var ids = [rec.primary].concat(rec.secondary).filter(Boolean);
    var bundle = ids.length > 1
      ? '<button class="btn btn--ghost" id="st-bundle">' + t('stBundle') + '</button>' : '';

    var stepsEl = document.getElementById('st-steps');
    if (stepsEl) {
      var sp = stepsEl.children;
      for (var si = 0; si < sp.length; si++) sp[si].removeAttribute('data-active');
      if (sp[2]) sp[2].setAttribute('data-active', 'true');
    }

    host.innerHTML =
      '<div class="verdict">' +
        '<p class="eyebrow">' + t('stProfile') + '</p>' +
        '<h3>' + (ctx.weakDomains ? headline(ctx) : t('stNoWeakness')) + '</h3>' +
        '<div class="verdict__score">' +
          '<div><b class="num">' + ctx.measures.length + '</b><span>' + t('stTestsDone') + '</span></div>' +
          '<div><b class="num">' + ctx.weakDomains + '</b><span>' + t('stWeakCount') + '</span></div>' +
          '<div><b class="num">' + ctx.strongDomains + '</b><span>' + t('stStrongCount') + '</span></div>' +
        '</div>' +
      '</div>' +
      '<h3>' + t('stPerTest') + '</h3>' + scales +
      '<div class="reclist mt-6">' + recCards + '</div>' +
      '<p class="faint mt-4">' + t('stMotivation') + '</p>' +
      '<div class="actions">' + bundle +
        '<a class="btn btn--ghost" href="/' + NF.lang + '/' + t('slugHandbooks') + '/' +
          (ids.length ? '?rec=' + ids.join(',') : '') + '">' + t('stAllHandbooks') + '</a>' +
      '</div>';

    host.setAttribute('data-visible', 'true');
    if (ids.length > 1) {
      document.getElementById('st-bundle').addEventListener('click', function () {
        ids.forEach(function (id) { NF.cart.add(id); });
      });
    }
    try { NF.store.set('nforce.selftest.v1', JSON.stringify({ ctx: { sport: ctx.sport, phase: ctx.phase }, ids: ids })); } catch (e) {}
    host.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function headline(ctx) {
    var weak = Object.keys(ctx.domains).filter(function (d) { return ctx.domains[d] === 'below'; });
    var names = weak.map(function (d) { return pick(BM.domains[d]).toLowerCase(); }).join(', ');
    var map = {
      nl: 'Je grootste winst zit in ' + names + '.',
      en: 'Your biggest gain sits in ' + names + '.',
      de: 'Dein größter Gewinn liegt in ' + names + '.'
    };
    return esc(map[NF.lang] || map.nl);
  }
})();
