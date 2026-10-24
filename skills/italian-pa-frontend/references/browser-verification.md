# Verifica browser con Playwright e axe — v0.4

Il modulo [`browser-tests/`](../browser-tests/README.md) effettua verifiche delle pagine **renderizzate**, a prescindere da Razor, React, Blazor, Vue, Angular o altri stack. Non è parte dell'applicazione.

## Procedura

1. Verifica il consenso a eseguire test su ambiente di sviluppo/staging, mai su produzione per default.
2. Rileva URL locale, pagine e componenti in uso. Evita input e credenziali reali.
3. Usa `browser-tests/config/example.json` come schema e crea una configurazione dedicata con selettori basati sul DOM effettivo. Togli i componenti non implementati.
4. Installa le dipendenze nel solo modulo browser-tests (`npm install`, `npx playwright install chromium`).
5. Avvia l'app in modo ordinario nel suo stack, poi esegui la suite.
6. Analizza report HTML/JSON, dai priorità a problemi riproducibili, modifica il codice e ripeti.
7. Aggiungi una revisione manuale: focus, tastiera, lettore schermo, zoom/reflow, contrasto, messaggi e flussi multi-step.

## Classificazione evidenza

- **PASSATO**: test realmente eseguito e riuscito su URL/data/viewport indicati.
- **FALLITO**: allega identificatore, pagina, componente, traccia/errore.
- **NON ESEGUITO**: tool mancante, pagina non disponibile, componente non configurato.
- **MANUALE DA VERIFICARE**: aspetti non coperti dai controlli automatizzati.

Non assimilare "0 violazioni axe" a conformità WCAG, AGID o normativa. Le regole axe sono selezionate tramite tag WCAG 2.0/2.1/2.2 A/AA; i tag non implicano copertura esaustiva. I test di form e wizard possono richiedere fixture e dati specifici, non usare dati veri.

Fonti: https://playwright.dev/docs/accessibility-testing ; https://playwright.dev/docs/intro ; https://playwright.dev/docs/browsers
