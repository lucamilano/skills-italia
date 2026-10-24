# Browser checks (facoltativi, framework-agnostici)

Test HTTP renderizzati nel browser, indipendenti dal framework server/client. **Non installare Playwright dentro l'applicazione della PA**: esegui questo modulo separatamente.

## Preparazione

1. Avvia il sito **di sviluppo** in locale con dati fittizi.
2. Da `browser-tests/`: `npm ci` (usa il lockfile e richiede accesso al registro npm o una cache popolata).
3. `npx playwright install chromium` (scarica i browser richiesti).
4. Copia `config/example.json` in `config/local.json` e configura l'URL e i percorsi reali. La configurazione di esempio **non** è pronta per qualunque sito.
5. Esegui `PA_TEST_CONFIG=config/local.json npm test` su Linux/macOS; su PowerShell usa `$env:PA_TEST_CONFIG='config/local.json'; npm test`.
6. Apri `npm run test:report`; report JSON in `reports/results.json` e allegati axe disponibili nel report HTML.

**Sicurezza:** il target è limitato a localhost per impostazione predefinita. Per un ambiente remoto di test esplicitamente autorizzato, imposta `PA_ALLOW_REMOTE=1`. Non utilizzare produzione o dati reali senza autorizzazione. Non inserire credenziali in configurazione o URL. Per app con autenticazione, crea fixture di sessione sicure fuori dal repository pubblico.

## Contratti configurabili

Le sezioni `components.menu`, `.modal`, `.form`, `.table`, `.wizard` sono **opzionali**. Elimina quelle non presenti nel progetto. I selettori d'esempio sono fittizi: sostituiscili con quelli reali. Se un test manca dal catalogo, non dichiararlo superato: è **non eseguito**.

- Pages: risposta HTTP, JS error, axe sul DOM renderizzato; due viewport (desktop/mobile).
- Menu: apertura, pannello visibile, accessibilità durante apertura, chiusura e ritorno focus.
- Modal: nome accessibile, apertura/chiusura, ritorno focus, scan con dialogo aperto.
- Form: tentativo submit vuoto e indicazione d'errore accessibile (configurare solo form con validazione applicativa; l'HTML nativo può bloccare il submit).
- Table: intestazioni visibili, scansione, righe vuote ammesse.
- Wizard: cambio step ed eventuale ritorno allo step iniziale (configurare dati di test validi per proseguire).

## Limiti

Axe individua solo una parte dei problemi. Serve review manuale con tastiera, screen reader, zoom, contrasto di stati, testi e flussi. I test qui proposti **non certificano WCAG né requisiti AGID**. Alcuni contratti richiedono test personalizzati specifici del progetto. Non disabilitare regole axe per far passare i test senza motivazione documentata.

Fonti: https://playwright.dev/docs/accessibility-testing e https://playwright.dev/docs/browsers

## v0.6.0: iterazione con screenshot e report

`npm run review -- --config config/local.json --iteration 1` lancia i test configurati in Chromium desktop/mobile, cattura screenshot full-page come allegati in `reports/html` e produce `reports/review-1.md` e `reports/review-1.json`. Apri gli allegati con `npm run test:report`; lo script non giudica automaticamente il design e non corregge codice. Il limite procedurale raccomandato è tre iterazioni, con ispezione visuale e modifiche autorizzate tra le esecuzioni.
