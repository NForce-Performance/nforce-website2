/* Uitgelichte handboeken op de homepage: drie kaarten uit handbooks.json.
   Welke drie? De items met "featured": true, anders de eerste drie. */
(function () {
  'use strict';
  var host = document.getElementById('hb-featured');
  if (!host) return;
  NF.ready.then(function (catalog) {
    var picks = catalog.items.filter(function (i) { return i.featured; });
    if (picks.length < 3) {
      catalog.items.forEach(function (i) {
        if (picks.length < 3 && picks.indexOf(i) === -1) picks.push(i);
      });
    }
    host.innerHTML = picks.slice(0, 3).map(function (i) { return NF.cardHTML(i); }).join('');
  });
})();
