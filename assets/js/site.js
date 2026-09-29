/* ==========================================================================
   NForce — site.js
   Navigatie, taalmenu, contactformulier (e-mailfallback) en de vaste CTA-balk op mobiel.
   ========================================================================== */
(function () {
  'use strict';

  /* mobiele navigatie */
  var toggle = document.querySelector('.nav-toggle');
  var mnav = document.getElementById('mobile-nav');
  if (toggle && mnav) {
    toggle.addEventListener('click', function () {
      var open = mnav.getAttribute('data-open') === 'true';
      mnav.setAttribute('data-open', String(!open));
      toggle.setAttribute('aria-expanded', String(!open));
    });
  }

  /* taalmenu */
  document.querySelectorAll('.langswitch').forEach(function (sw) {
    var btn = sw.querySelector('.langswitch__btn');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = sw.getAttribute('data-open') === 'true';
      sw.setAttribute('data-open', String(!open));
      btn.setAttribute('aria-expanded', String(!open));
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.langswitch[data-open="true"]').forEach(function (sw) {
      sw.setAttribute('data-open', 'false');
      var b = sw.querySelector('.langswitch__btn');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  });

  /* reveal */
  var targets = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && targets.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* contactformulier zonder formulierdienst: open het e-mailprogramma met de
     aanvraag ingevuld. Zodra FORM_ENDPOINT in tools/pages.py is gezet, heeft het
     formulier geen data-mailto meer en wordt het normaal verstuurd. */
  document.querySelectorAll('form[data-mailto]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var lines = [];
      form.querySelectorAll('input, textarea, select').forEach(function (el) {
        if (el.name) lines.push((el.getAttribute('data-label') || el.name) + ': ' + el.value);
      });
      var subject = form.getAttribute('data-subject') || 'Aanvraag via de website';
      location.href = 'mailto:' + form.getAttribute('data-mailto') +
        '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
    });
  });

  /* koud licht dat de cursor volgt (alleen muis): kaarten, pakketten, links */
  if (window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var spotSel = '.card, .plan, .next a, .hb-card, .ctaband';
    var markSpots = function (root) {
      (root || document).querySelectorAll(spotSel).forEach(function (el) { el.classList.add('fx-spot'); });
    };
    markSpots();
    /* handboekkaarten worden later door JavaScript opgebouwd */
    if ('MutationObserver' in window) {
      new MutationObserver(function () { markSpots(); }).observe(document.body, { childList: true, subtree: true });
    }
    document.addEventListener('pointermove', function (e) {
      var el = e.target.closest && e.target.closest('.fx-spot');
      if (!el) return;
      var r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      el.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }, { passive: true });
  }

  /* vaste CTA-balk op mobiel: verschijnt zodra de hero uit beeld is */
  var bar = document.querySelector('.mobilebar');
  var hero = document.querySelector('.hero, .page-hero');
  if (bar && hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      bar.setAttribute('data-show', entries[0].isIntersecting ? 'false' : 'true');
    }, { threshold: 0 }).observe(hero);
  } else if (bar) {
    bar.setAttribute('data-show', 'true');
  }
})();
