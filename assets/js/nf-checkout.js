/* ==========================================================================
   N-FORCE PERFORMANCE — nf-checkout.js
   Bestelpagina: overzicht van de winkelwagen + het KOPPELPUNT voor de
   betaalprovider. Er wordt hier niets afgerekend; zie README, sectie
   "Betaalprovider koppelen".
   ========================================================================== */
(function () {
  'use strict';
  var root = document.getElementById('co-app');
  if (!root) return;

  var t = NF.t, esc = NF.esc, pick = NF.pick;

  NF.ready.then(function (catalog) {
    render(catalog);
    root.addEventListener('click', function (e) {
      var id = e.target.getAttribute('data-remove');
      if (id) { NF.cart.remove(id); render(catalog); }
    });
  });

  function render(catalog) {
    var ids = NF.cart.read();
    if (!ids.length) {
      root.innerHTML = '<p class="notice">' + t('cartEmpty') + ' <a href="/' + NF.lang + '/' + t('slugHandbooks') + '/">' + t('toHandbooks') + '</a></p>';
      return;
    }
    var lines = ids.map(function (id) {
      var it = catalog.byId[id];
      if (!it) return '';
      return '<tr><td><strong>' + esc(pick(it.title)) + '</strong><br><span class="faint">' +
        it.version.toUpperCase() + ' \u00b7 ' + it.pages + ' ' + t('pages') + ' \u00b7 ' +
        it.languages.map(function (l) { return l.toUpperCase(); }).join('/') + '</span></td>' +
        '<td class="num">' + NF.euro(it.price) + '</td>' +
        '<td><button class="cartline__del" data-remove="' + esc(id) + '">' + t('remove') + '</button></td></tr>';
    }).join('');

    root.innerHTML =
      '<div class="split">' +
        '<div>' +
          '<h2>' + t('orderSummary') + '</h2>' +
          '<div class="table-wrap"><table><tbody>' + lines +
          '<tr><td><strong>' + t('total') + '</strong></td><td class="num"><strong>' + NF.euro(NF.cart.total()) + '</strong></td><td></td></tr>' +
          '</tbody></table></div>' +
          '<p class="faint mt-4">' + t('vatNote') + '</p>' +
        '</div>' +
        '<div class="card">' + payBlock() + '</div>' +
      '</div>';
  }

  /* ----------------------------------------------------------------------
     KOPPELPUNT BETAALPROVIDER
     ----------------------------------------------------------------------
     Zolang er geen provider gekoppeld is, gaat de bestelling via e-mail.
     Vervang de knop hieronder door:
       Stripe Payment Link  : <a class="btn btn--primary" href="LINK">…</a>
       Stripe Checkout      : POST naar je serverless functie met NF.cart.read()
       Mollie / Plug&Pay    : één betaal-URL per handboek uit handbooks.json
     -------------------------------------------------------------------- */
  function payBlock() {
    var ids = NF.cart.read().join(', ');
    var subject = encodeURIComponent('Interesse handboeken — N-Force Performance');
    var body = encodeURIComponent(
      'Ik heb interesse in de volgende handboeken (nog geen bestelling):\n\n' + ids +
      '\n\nNaam:\nE-mail:\nSport:\n'
    );
    var texts = {
      nl: { h: 'Binnenkort beschikbaar', p: 'De webshop gaat binnenkort live. Laat via de knop hieronder je interesse en gegevens achter — je betaalt nu nog niets, en je hoort als eerste zodra bestellen kan.', b: 'Interesse melden' },
      en: { h: 'Coming soon', p: 'The shop is launching soon. Use the button below to let us know you\'re interested — you don\'t pay anything now, and you\'ll be the first to hear once ordering opens.', b: 'Register interest' },
      de: { h: 'Demnächst verfügbar', p: 'Der Shop startet in Kürze. Nutze den Button unten, um dein Interesse zu hinterlassen — du zahlst jetzt noch nichts und hörst als Erste(r) von uns, sobald die Bestellung möglich ist.', b: 'Interesse anmelden' }
    };
    var x = texts[NF.lang] || texts.nl;
    return '<h3>' + x.h + '</h3><p>' + x.p + '</p>' +
      '<a class="btn btn--primary btn--block" href="mailto:nick@nforce-performance.nl?subject=' + subject + '&body=' + body + '">' + x.b + '</a>' +
      '<a class="btn btn--quiet btn--sm" href="/' + NF.lang + '/' + t('slugHandbooks') + '/">' + t('continueShopping') + '</a>';
  }
})();
