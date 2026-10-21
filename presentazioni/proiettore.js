/* ===== MODALITÀ PROIETTORE =====
   Pulsante in alto a destra (o tasto C) per passare dalla versione normale
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

    var pulsante = document.createElement('button');
    pulsante.type = 'button';
    pulsante.className = 'pulsante-proiettore';

    function applica(acceso) {
        document.documentElement.classList.toggle('proiettore', acceso);
        pulsante.textContent = acceso ? 'Proiettore: acceso' : 'Proiettore: spento';
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
