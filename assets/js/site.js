/* ==========================================================================
   N-FORCE PERFORMANCE — site.js
   Navigatie, taalmenu, reveal-animatie en de vaste CTA-balk op mobiel.
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
