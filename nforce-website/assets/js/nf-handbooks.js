/* ==========================================================================
   N-FORCE PERFORMANCE — nf-handbooks.js
   Handboekenpagina: filters, badges, kaarten en (via ?rec=) de aanbevelingen
   uit de zelftest bovenaan.
   Alle content komt uit /assets/data/handbooks.json.
   ========================================================================== */
(function () {
  'use strict';
  var root = document.getElementById('hb-app');
  if (!root) return;

  var SPORTS = [
    { v: 'all', k: 'sportAll' },
    { v: 'icehockey', k: 'sportIcehockey' },
    { v: 'football', k: 'sportFootball' },
    { v: 'handball', k: 'sportHandball' }
  ];
  var PHASES = [
    { v: 'off-season', k: 'phaseOffseason' },
    { v: 'pre-season', k: 'phasePreseason' },
    { v: 'season', k: 'phaseSeason' },
    { v: 'power', k: 'phasePower' },
    { v: 'agility', k: 'phaseAgility' },
    { v: 'return-to-play', k: 'phaseRtp' }
  ];
  var CATS = [
    { v: 'strength', k: 'catStrength' },
    { v: 'speed', k: 'catSpeed' },
    { v: 'conditioning', k: 'catConditioning' },
    { v: 'sport-specific', k: 'catSportSpecific' },
    { v: 'rehab', k: 'catRehab' }
  ];
  var VERSIONS = [{ v: 'core', k: null, label: 'Core' }, { v: 'pro', k: null, label: 'Pro' }];

  var state = {
    sport: NF.qs('sport') || '',
    phase: NF.qs('phase') || '',
    category: NF.qs('category') || '',
    version: NF.qs('version') || ''
  };
  var recIds = (NF.qs('rec') || '').split(',').filter(Boolean);

  NF.ready.then(function (catalog) {
    root.innerHTML =
      '<div class="filters" id="hb-filters"></div>' +
      '<p class="filtercount" id="hb-count" aria-live="polite"></p>' +
      '<div id="hb-rec"></div>' +
      '<div class="hb-grid" id="hb-grid"></div>';

    renderFilters();
    renderRecommended(catalog);
    renderGrid(catalog);

    document.getElementById('hb-filters').addEventListener('change', function (e) {
      var f = e.target.getAttribute('data-filter');
      if (!f) return;
      state[f] = e.target.value;
      renderGrid(catalog);
    });
    document.getElementById('hb-filters').addEventListener('click', function (e) {
      if (!e.target.hasAttribute('data-reset')) return;
      state = { sport: '', phase: '', category: '', version: '' };
      renderFilters();
      renderGrid(catalog);
    });
  });

  function opts(list, selected) {
    return '<option value="">' + NF.t('filterAll') + '</option>' + list.map(function (o) {
      var label = o.k ? NF.t(o.k) : o.label;
      return '<option value="' + o.v + '"' + (selected === o.v ? ' selected' : '') + '>' + label + '</option>';
    }).join('');
  }

  function renderFilters() {
    document.getElementById('hb-filters').innerHTML =
      field('sport', NF.t('filterSport'), opts(SPORTS, state.sport)) +
      field('phase', NF.t('filterPhase'), opts(PHASES, state.phase)) +
      field('category', NF.t('filterCategory'), opts(CATS, state.category)) +
      field('version', NF.t('filterVersion'), opts(VERSIONS, state.version)) +
      '<div class="filters__reset"><button class="btn btn--ghost btn--sm" data-reset>' + NF.t('filterReset') + '</button></div>';
  }
  function field(name, label, inner) {
    return '<div class="field"><label for="f-' + name + '">' + label + '</label>' +
      '<select id="f-' + name + '" data-filter="' + name + '">' + inner + '</select></div>';
  }

  function match(item) {
    if (state.sport && item.sports.indexOf(state.sport) === -1) return false;
    if (state.phase && item.phase.indexOf(state.phase) === -1) return false;
    if (state.category && item.category !== state.category) return false;
    if (state.version && item.version !== state.version) return false;
    return true;
  }

  function renderRecommended(catalog) {
    var host = document.getElementById('hb-rec');
    if (!recIds.length) { host.innerHTML = ''; return; }
    var items = recIds.map(function (id) { return catalog.byId[id]; }).filter(Boolean);
    if (!items.length) { host.innerHTML = ''; return; }
    host.innerHTML =
      '<div class="notice mt-0" style="margin-bottom:1.5rem"><strong>' + NF.t('stRecommendedFlag') + '.</strong> ' +
      NF.t('stMotivation') + '</div>' +
      '<div class="hb-grid" style="margin-bottom:2.5rem">' + items.map(function (it, i) {
        return NF.cardHTML(it, { recommended: true, flag: i === 0 ? NF.t('stPrimary') : NF.t('stUpsellFlag') });
      }).join('') + '</div>' +
      '<div class="blueline" style="margin-bottom:2.5rem"></div>';
  }

  function renderGrid(catalog) {
    var items = catalog.items.filter(match);
    var grid = document.getElementById('hb-grid');
    document.getElementById('hb-count').textContent = items.length + ' ' + NF.t('resultsCount');
    if (!items.length) {
      grid.innerHTML = '<p class="notice">' + NF.t('noResults') + '</p>';
      return;
    }
    /* Pro boven Core binnen dezelfde familie, en aanbevolen items eerst. */
    items.sort(function (a, b) {
      var ra = recIds.indexOf(a.id), rb = recIds.indexOf(b.id);
      if (ra !== rb) return (ra === -1 ? 99 : ra) - (rb === -1 ? 99 : rb);
      if (a.family !== b.family) return a.family < b.family ? -1 : 1;
      return a.version === b.version ? 0 : (a.version === 'pro' ? -1 : 1);
    });
    grid.innerHTML = items.map(function (it) {
      return NF.cardHTML(it, { recommended: recIds.indexOf(it.id) !== -1 });
    }).join('');
  }
})();
