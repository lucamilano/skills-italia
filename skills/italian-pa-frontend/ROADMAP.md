## v1.0.0 — Consolidamento (2026-10-22)

- [x] Validazione packaging, unit test Python e test unitari Node
- [x] Documentazione limiti e matrice della release
- [x] Workflow CI per verifiche riproducibili
- [ ] E2E in browser su un portale realmente avviato
- [ ] Test PowerShell su Windows e smoke test interattivo Claude Code / Codex
- [ ] Pubblicazione su GitHub (non effettuata)

# Roadmap — progressiva

## v0.1.0 (completato)

- [x] SKILL.md portabile Claude/Codex
- [x] Routing generate/audit/refactor
- [x] Riferimenti Designers Italia e accessibilità
- [x] Adattatori per HTML, MVC/Razor, React/Next.js
- [x] Scanner statico euristico e fixture di test
- [x] Script di installazione per Windows/Linux/macOS

## v0.2.0 — catalogo componenti (completato)

- [x] Matrice documentale iniziale Bootstrap Italia 2.x per sei famiglie (non testata in runtime)
- [x] Schede ufficialmente collegate, note sui breaking change ed esempi didattici
- [x] Ricerca componenti offline da CLI e test del catalogo
- [x] Istruzioni obbligatorie della skill aggiornate per il routing dei componenti

## v0.2.1 — neutralità tecnologica (completato)

- [x] Selezione esplicita dell’utente prima degli esempi predefiniti
- [x] Inferenza dello stack dal repository quando non specificato
- [x] Domanda mirata solo per generazione di codice realmente ambigua
- [x] Stack notes opzionali e catalogo comune indipendente dal framework

## v0.2.x — specifiche capillari (successive)

- [ ] Mappatura semantica per tutte le varianti con release minima e codice eseguibile verificato
- [ ] Audit reali con test di navigazione, focus e lettore di schermo
- [ ] Template completi e realmente interattivi: dashboard, tabella ricerca, wizard a più step
- [ ] Esempi di integrazione Blazor, Angular e Vue **opzionali**, senza rendere la skill dipendente da questi framework
- [ ] Checklist normativa italiana revisionata con fonti puntuali e aggiornate

## v0.3.x — automazione e collaborazione

- [x] Modulo opzionale test browser e axe-core configurabili (esecuzione E2E su app reale ancora da effettuare)
- [ ] Fixture React e ASP.NET compilabili in CI
- [ ] Storybook/design token quando maturi
- [ ] Workflow CI e release GitHub
- [ ] Documentazione bilingue, contributi e version pinning

## Decisioni da mantenere esplicite

- La skill non è ufficiale né certificante.
- La versione attiva del design system è una decisione di progetto verificabile, non hardcoded.
- Nuovi framework sono adattatori, non fork di tutte le regole.


### Dopo 0.3.0
- Verifiche browser reali dei contratti con Playwright/axe (quando disponibili), senza spacciare audit automatici per certificazioni.
- Matrice versionata di pattern e interazioni Bootstrap Italia con evidenza della fonte.
- Esempi end-to-end in stack scelti dall’utente, mai obbligatori.

## v0.4.0 — browser checks (modulo consegnato)
- [x] Runner Playwright separato dalla tecnologia applicativa.
- [x] Axe sul DOM e report HTML/JSON.
- [x] Scenari opzionali configurabili per menu, dialog, form, table, wizard.
- [x] Limitazione target localhost per default e test unitari configurazione.
- [ ] Esecuzione completa dei test browser contro applicazione reale autorizzata.
- [ ] Verifica manuale con lettore di schermo e diverse tecnologie assistive.

## v0.5.0 — qualità visiva e composizione (completato)
- [x] Fondamenti visivi tracciati alle fonti ufficiali, senza token hardcoded
- [x] Pattern di pagina indipendenti dallo stack
- [x] Protocollo di review visiva e report
- [x] Brief JSON verificabile nella struttura, con test
- [ ] Review browser su portale reale e validazione manuale del contrasto/focus
- [ ] Allineamento token con versioni specifiche del design system e report di regressione screenshot

## v0.6.0 — revisione iterativa (completato)
- [x] Evidenze screenshot desktop/mobile a ogni esecuzione del runner
- [x] Report Markdown e JSON, runner con esito test e iterazioni numerate
- [x] Procedura di revisione manuale / agente visuale, con limite iterazioni
- [ ] Test E2E effettivi contro portale autorizzato e controllo visivo su screenshot reali
- [ ] Mascheramento integrato per contenuti dinamici e confronto visuale baseline (eventuale versione successiva)

## v0.7.0 — matrice versioni (completato)
- [x] Regole con fonte, soglia di versione, verifica richiesta e stato evidenza
- [x] Comando CLI per identificare regole applicabili e test automatici
- [ ] Ampliare copertura a tutti i componenti .italia e versioni Bootstrap Italia 2.x
- [ ] Test browser delle regole su versioni reali
- [ ] Valutare regole per altre librerie soltanto dopo verifica documentale separata

## v0.8.0 — Form e wizard amministrativi (completato)
- [x] Contratti form e wizard stack-agnostic con fonti ufficiali
- [x] Stati di validazione, bozze, upload, riepilogo e invio distinto dal backend
- [x] Specifica JSON e validazione strutturale con avvisi per backend non identificati
- [ ] Test browser con API simulate e successivamente con portale autorizzato
- [ ] Approfondimenti futuri su localizzazione, validazione semantica e casi reali

## v0.9.0 — dashboard e dati (completato)
- [x] Contratti ricerca, filtri, sort, paginazione, export, autorizzazioni e responsive.
- [x] Inventario indicativo pattern di progetto e workflow di verifica manuale.
- [x] Schema esempio JSON, validatore strutturale e test automatici.
- [ ] Test integrati con backend autorizzato e permessi reali.
- [ ] Browser E2E su dashboard reali, compresi export e navigazione responsive.
