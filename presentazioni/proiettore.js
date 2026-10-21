/* ===== MODALITÀ PROIETTORE =====
   Disegno di un proiettore in alto a destra (o tasto C) per passare dalla versione normale
   a quella ad alto contrasto pensata per il proiettore (proiettore.css).
   La scelta resta salvata nel browser e vale per tutte le presentazioni;
   la vista relatore (tasto S) si allinea da sola. I PDF usano sempre la
   versione normale. */
(function () {
    var CHIAVE = 'slide-proiettore';
    var stampa = /print-pdf/.test(window.location.search);

    function leggi() {
        try { return localStorage.getItem(CHIAVE) === '1'; } catch (e) { return false; }
    }

    function salva(acceso) {
        try { localStorage.setItem(CHIAVE, acceso ? '1' : '0'); } catch (e) { /* niente */ }
    }

    // proiettore a pellicola in stile cartoon, visto di lato: da spento è
    // grigio e dorme (occhi chiusi, "z"), da acceso si colora, apre gli occhi,
    // sorride, l'obiettivo si illumina, esce il fascio di luce e le bobine
    // girano (stili in proiettore.css)
    function bobina(cx) {
        return '<g class="bobina-gruppo">' +
            '<circle class="bobina tratto" cx="' + cx + '" cy="14" r="10.5"/>' +
            '<circle class="foro" cx="' + cx + '" cy="8.6" r="2.6"/>' +
            '<circle class="foro" cx="' + (cx - 4.7) + '" cy="16.7" r="2.6"/>' +
            '<circle class="foro" cx="' + (cx + 4.7) + '" cy="16.7" r="2.6"/>' +
            '<circle class="perno tratto-sottile" cx="' + cx + '" cy="14" r="1.6"/>' +
            '</g>';
    }

    var DISEGNO =
        '<svg viewBox="0 0 100 52" aria-hidden="true" focusable="false">' +
        '<defs><linearGradient id="proiettore-luce" x1="1" y1="0" x2="0" y2="0">' +
        '<stop offset="0" stop-color="#fde047" stop-opacity="0.95"/>' +
        '<stop offset="1" stop-color="#fef9c3" stop-opacity="0"/>' +
        '</linearGradient></defs>' +
        '<g class="fascio">' +
        '<polygon points="24,28 24,40 0,52 0,16" fill="url(#proiettore-luce)"/>' +
        '<path class="scintilla" d="M8,22 l1.2,2.8 2.8,1.2 -2.8,1.2 -1.2,2.8 -1.2,-2.8 -2.8,-1.2 2.8,-1.2z"/>' +
        '<path class="scintilla" d="M13,41 l0.8,1.9 1.9,0.8 -1.9,0.8 -0.8,1.9 -0.8,-1.9 -1.9,-0.8 1.9,-0.8z"/>' +
        '</g>' +
        '<g class="macchina">' +
        '<path class="pellicola" d="M52,4 Q63,-1 74,4"/>' +
        bobina(52) + bobina(74) +
        '<rect class="piede tratto" x="42" y="42" width="8" height="7" rx="3"/>' +
        '<rect class="piede tratto" x="72" y="42" width="8" height="7" rx="3"/>' +
        '<rect class="corpo tratto" x="35" y="22" width="52" height="23" rx="8"/>' +
        '<rect class="riflesso" x="40" y="25.5" width="16" height="3" rx="1.5"/>' +
        '<rect class="canna tratto" x="23" y="27" width="14" height="14" rx="4"/>' +
        '<ellipse class="vetro tratto-sottile" cx="23" cy="34" rx="3.5" ry="6.5"/>' +
        '<g class="dorme">' +
        '<path class="occhio-chiuso" d="M53,33 q2.8,2.6 5.6,0 M65,33 q2.8,2.6 5.6,0"/>' +
        '<path class="bocca" d="M59.5,39 h4"/>' +
        '<text class="zeta" x="90" y="16">z</text><text class="zeta piccola" x="95" y="9">z</text>' +
        '</g>' +
        '<g class="sveglio">' +
        '<circle class="guancia" cx="51" cy="38" r="2.4"/><circle class="guancia" cx="72.5" cy="38" r="2.4"/>' +
        '<circle class="occhio" cx="55.8" cy="33" r="2.8"/><circle class="occhio" cx="67.8" cy="33" r="2.8"/>' +
        '<circle class="luccichio" cx="56.8" cy="32" r="1"/><circle class="luccichio" cx="68.8" cy="32" r="1"/>' +
        '<path class="bocca" d="M58,38.5 q3.8,3.6 7.6,0"/>' +
        '</g>' +
        '</g>' +
        '</svg>';

    var pulsante = document.createElement('button');
    pulsante.type = 'button';
    pulsante.className = 'pulsante-proiettore';
    pulsante.innerHTML = DISEGNO;

    function applica(acceso) {
        document.documentElement.classList.toggle('proiettore', acceso);
        pulsante.setAttribute('aria-label', acceso ? 'Proiettore acceso' : 'Proiettore spento');
        pulsante.setAttribute('aria-pressed', acceso ? 'true' : 'false');
        pulsante.title = (acceso ? 'Torna alla versione normale' : 'Versione ad alto contrasto per il proiettore') + ' (tasto C)';
    }

    function cambia() {
        var acceso = !document.documentElement.classList.contains('proiettore');
        salva(acceso);
        applica(acceso);
    }

    if (stampa) return;

    applica(leggi());
    pulsante.addEventListener('click', function () {
        cambia();
        pulsante.blur();
    });
    document.body.appendChild(pulsante);

    // un'altra finestra (es. la vista relatore) ha cambiato modalità
    window.addEventListener('storage', function (e) {
        if (e.key === CHIAVE) applica(e.newValue === '1');
    });

    if (window.Reveal) {
        var tasto = function () {
            Reveal.addKeyBinding({ keyCode: 67, key: 'C', description: 'Modalità proiettore' }, cambia);
        };
        if (Reveal.isReady && Reveal.isReady()) tasto();
        else Reveal.on('ready', tasto);
    }
})();
