## 1.0.0 — Consolidamento (2026-10-22)

- Consolidate istruzioni e documentazione, senza introdurre framework obbligatori.
- Aggiunto controllo di release ripetibile e matrice esplicita dei test ancora da eseguire.
- Allineato numero di versione e limiti del pacchetto, predisposta verifica in CI.

## 0.9.0 — Dashboard e dati amministrativi (2026-10-22)

- Regole agnostiche su ricerca, filtri, sort, paginazione, export e policy di autorizzazione.
- Scanner a basso impatto di nomi file per suggerire componenti riutilizzabili (non audit).
- Specifica JSON con validatore strutturale, warning sulle integrazioni non verificate e test.
- Nessuna modifica automatica al backend o dipendenza frontend imposta.

## 0.8.0 — Form e wizard amministrativi (2026-10-22)

- Contratti indipendenti dal framework per validazione, riepilogo, errori e navigazione di step.
- Bozze e upload opzionali con separazione esplicita tra UI e integrazioni backend.
- Catalogo JSON dei flussi, esempio di specifica, validatore CLI senza dipendenze e test.
- Nessun endpoint fittizio, nessuna dichiarazione di conformità automatica.

## 0.7.0 — Matrice componenti versionata (2026-10-22)

- Aggiunte 11 regole documentate con fonte verificabile e versione di introduzione per Bootstrap Italia 2.x.
- CLI di lookup senza dipendenze, con output testuale/JSON e filtri per componente/versione.
- Workflow skill aggiornato per evitare l’uso improprio di markup e API tra versioni.
- Test di soglie semver, fonte e copertura regole.
- Matrice parziale e non validata in un browser reale; nessuna certificazione di accessibilità.

## 0.5.0 — Composizione visiva agnostica (2026-10-22)

- Aggiunte regole su gerarchia, tipografia, ritmo, layout responsive e stati UI.
- Aggiunti pattern per dashboard, elenco, form, wizard e dettaglio pratica.
- Aggiunti protocollo/report di review visiva e validator JSON di sola completezza con test.
- Confermata scelta tecnologica a richiesta o dal repository; nessun framework imposto.
- Nessuna validazione browser reale o certificazione di conformità rivendicata.

## 0.3.0
- Architettura technology-first con rilevamento indicativo dello stack e priorità alla scelta dell’utente.
- Contratti di accettazione per form, tabelle, header, navigazione, modali e wizard.
- Template decisione tecnologica, nuovi prompt e test per stack multipli.
- Nessuna specializzazione vincolante; le guide di framework restano opzionali.

# Changelog

## [0.4.0] — 2026-10-22

- Modulo browser-tests/ indipendente dal framework con Playwright e axe-core.
- Configurazione locale di pagine e contratti UI; report HTML e JSON.
- Policy locale di default per evitare test involontari su siti remoti.
- Procedura di verifica manuale e distinzione tra test eseguiti e non eseguiti.
- E2E su portali reali non ancora eseguiti.


## [0.2.1] — 2026-10-22

- Resa esplicita la neutralità tecnologica della skill.
- Tecnologia selezionata dall'utente, altrimenti rilevata dal progetto; domanda solo quando indispensabile.
- Rimosso l'obbligo di scegliere tra adattatori predefiniti.
- Aggiunto `references/technology-selection.md` e aggiornati README, workflow e template UI.
- Catalogo Bootstrap Italia e controlli indipendenti dal framework invariati.

## [0.2.0] — 2026-10-22

- Aggiunto catalogo componenti JSON di 6 famiglie, con percorsi e fonti ufficiali.
- Aggiunte schede per header, navigazione, form, tabelle, modali e steppers.
- Aggiunti snippet didattici e prompt mirati, con limiti di interattività espliciti.
- Aggiunto comando `scripts/component_lookup.py list|show` e test strutturali.
- SKILL.md aggiornata per consultazione dei componenti e incompatibilità >=2.15.0 dell'header mobile.
- Nessun claim di conformità normativa né runtime verificato dei componenti.

## [0.1.0] - 2026-10-22

- Prima release: skill, riferimenti ufficiali e adattatori stack.
- Workflow generate / audit / refactor.
- Scanner statico euristico, test e installatori.
- Template e prompt dimostrativi.

## 0.6.0 — iterative browser review
- Nuovo workflow a iterazioni limitate, indipendente dal framework.
- Screenshot full-page desktop e mobile con allegati Playwright e diagnostica overflow.
- Runner `npm run review` con report Markdown/JSON e gestione del codice di uscita.
- Manual review, sicurezza e stop condition documentati.
