/* N-Force Performance — site.js
   Bewust klein en zonder afhankelijkheden. Alles degradeert netjes zonder JS. */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. Mobiele navigatie ------------------------------------------- */
  var toggle = document.querySelector('.nav-toggle');
  var mnav = document.getElementById('mobile-nav');
  if (toggle && mnav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      mnav.setAttribute('data-open', String(!open));
    });
    mnav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        toggle.setAttribute('aria-expanded', 'false');
        mnav.setAttribute('data-open', 'false');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mnav.getAttribute('data-open') === 'true') {
        toggle.setAttribute('aria-expanded', 'false');
        mnav.setAttribute('data-open', 'false');
        toggle.focus();
      }
    });
  }

  /* ---- 2. Reveal: één subtiele beweging, alleen bij binnenkomst -------- */
  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length) {
    if (reduced || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---- 3. Vaste CTA-balk op mobiel, pas na de hero -------------------- */
  var bar = document.querySelector('.mobilebar');
  var anchor = document.querySelector('.hero, .page-hero');
  if (bar && anchor && 'IntersectionObserver' in window) {
    var barIo = new IntersectionObserver(function (entries) {
      bar.setAttribute('data-show', String(!entries[0].isIntersecting));
    }, { threshold: 0 });
    barIo.observe(anchor);
  }

  /* ---- 4. Ontbrekende beelden stil verbergen -------------------------- */
  document.querySelectorAll('.hero__media img, .page-hero__media img, .split__media img')
    .forEach(function (img) {
      img.addEventListener('error', function () { img.style.display = 'none'; });
    });

  /* ---- 5. Benchmarkcheck --------------------------------------------- */
  var bench = document.querySelector('[data-bench]');
  if (bench && window.NFORCE_BENCHMARKS) {
    var select = bench.querySelector('[data-bench-test]');
    var input = bench.querySelector('[data-bench-value]');
    var meter = bench.querySelector('[data-bench-meter]');
    var scale = bench.querySelector('[data-bench-scale]');
    var out = bench.querySelector('[data-bench-out]');
    var srcBox = bench.querySelector('[data-bench-source]');

    Object.keys(window.NFORCE_BENCHMARKS).forEach(function (key) {
      var o = document.createElement('option');
      o.value = key;
      o.textContent = window.NFORCE_BENCHMARKS[key].label;
      select.appendChild(o);
    });

    function render() {
      var t = window.NFORCE_BENCHMARKS[select.value];
      if (!t) return;
      var min = t.axis[0], max = t.axis[1];
      var span = max - min;
      meter.innerHTML = '';

      var band = document.createElement('div');
      band.className = 'meter__band';
      band.style.left = ((t.band[0] - min) / span * 100) + '%';
      band.style.width = ((t.band[1] - t.band[0]) / span * 100) + '%';
      meter.appendChild(band);

      scale.innerHTML = '<span>' + min + ' ' + t.unit + '</span>' +
        '<span>referentiebereik ' + t.band[0] + '–' + t.band[1] + ' ' + t.unit + '</span>' +
        '<span>' + max + ' ' + t.unit + '</span>';

      srcBox.textContent = t.source;

      var v = parseFloat(String(input.value).replace(',', '.'));
      if (isNaN(v)) { out.textContent = ''; return; }

      var clamped = Math.min(Math.max(v, min), max);
      var mark = document.createElement('div');
      mark.className = 'meter__mark';
      mark.style.left = ((clamped - min) / span * 100) + '%';
      mark.setAttribute('data-label', v + ' ' + t.unit);
      meter.appendChild(mark);

      var better = t.higherIsBetter;
      var msg;
      if (v < t.band[0]) {
        msg = better
          ? '<strong>Onder het referentiebereik.</strong> ' + t.below
          : '<strong>Boven het referentiebereik.</strong> ' + t.above;
      } else if (v > t.band[1]) {
        msg = better
          ? '<strong>Boven het referentiebereik.</strong> ' + t.above
          : '<strong>Onder het referentiebereik.</strong> ' + t.below;
      } else {
        msg = '<strong>Binnen het referentiebereik.</strong> ' + t.inside;
      }
      out.innerHTML = msg + ' Verschillen kleiner dan de meetfout (' + t.error + ') zijn ruis.';
    }

    select.addEventListener('change', render);
    input.addEventListener('input', render);
    render();
  }
})();
