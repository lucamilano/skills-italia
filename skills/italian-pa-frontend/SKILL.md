---
name: italian-pa-frontend
description: "Progetta, genera, verifica e migliora frontend dei siti e servizi digitali della Pubblica Amministrazione italiana seguendo Designers Italia, Bootstrap Italia e accessibilità. Usa per dashboard, form, wizard, tabelle e portali PA con qualunque stack web scelto dall’utente o già presente nel progetto; attiva anche per audit e refactoring UX/UI di applicativi PA esistenti."
license: MIT
metadata:
  version: "1.0.0"
---

# Italian PA Frontend — v1.0.0

Skill per **generazione**, **audit** e **refactoring** di interfacce della Pubblica Amministrazione italiana.

## Ambito e maturità v1.0.0

Release consolidata delle funzionalità 0.1–0.9. Il catalogo Bootstrap Italia è parziale; i controlli statici non sono audit normativi, i test browser sono opzionali e richiedono un’applicazione locale avviata. La compatibilità funzionale in Claude Code e Codex non è stata verificata mediante sessioni interattive reali. Consulta `RELEASE_NOTES.md` per l’evidenza dei test.

## Attivazione

Usa questa skill quando l'utente richiede frontend, UX/UI o revisione di servizi pubblici italiani (es. portali del personale, bandi, candidature, dashboard, moduli amministrativi), anche senza nominare AGID. Non attivarla automaticamente per siti commerciali privati o per richieste esclusivamente backend.

## Percorsi del pacchetto e indipendenza

Gli helper richiedono Python 3.10+. I test Node e gli strumenti browser opzionali usano Node.js 22.12+; i test browser richiedono inoltre le dipendenze bloccate e Chromium. Il formato e i percorsi documentati riguardano client locali Agent Skills.

I percorsi `references/`, `catalog/`, `templates/`, `examples/`, `scripts/` e `browser-tests/` in questa skill sono relativi alla cartella che contiene questo `SKILL.md`, anche quando la skill è installata dentro `.agents/skills/` o `.claude/skills/`. Ricava tale cartella dalla skill caricata e usa percorsi assoluti per eseguire i suoi script dal progetto applicativo. Passa esplicitamente il percorso del progetto da analizzare; non confondere gli script dell'applicazione con quelli della skill. Per il modulo browser usa la sua directory come working directory.

Italian PA Frontend è il primo modulo della suite indipendente Skills Italia. Non è affiliato ufficialmente ad AGID, Designers Italia o al Governo italiano. Le altre skill della roadmap non sono dipendenze disponibili.

## Procedura obbligatoria

1. **Selezione tecnologia senza vincoli**: segui `references/technology-selection.md`; quando esiste un repository puoi raccogliere indizi con `python scripts/detect_stack.py <repository> --json` (rilevazione non vincolante). Usa prima lo stack esplicitamente richiesto dall’utente; in assenza di una scelta, rileva framework/versioni dal repository. Se non c’è un repository o lo stack è realmente ambiguo e la scelta impedisce di procedere, poni **una domanda breve** sulla tecnologia preferita; non presentare una lista chiusa e non scegliere React, Razor o altri framework per abitudine. Se la richiesta riguarda solo specifiche/audit, non serve scegliere uno stack. Conserva framework, versioni, asset CSS/JS, convenzioni e vincoli individuati. Non introdurre nuove dipendenze senza consenso o ragione tecnica.
2. **Versione del design system**: individua la versione effettivamente installata e consultane la documentazione. Per nuovi progetti verifica lo stato corrente delle librerie ufficiali e la compatibilità con lo stack scelto; lo snapshot storico in `references/official-sources.md` non stabilisce quale versione sia attualmente stabile. Il catalogo locale riguarda Bootstrap Italia **2.x**: per altre versioni o Dev Kit Italia consulta le fonti pertinenti senza trasferire automaticamente quelle regole. Non mescolare esempi/API di versioni differenti. Se non puoi consultare le fonti, dichiara l'incertezza.
3. **Consulta soltanto i riferimenti pertinenti** (progressive disclosure): `references/official-sources.md`, `references/design-rules.md`, `references/accessibility.md`. Per componenti della PA consulta `references/component-workflow.md` e `catalog/components.json` oppure `python scripts/component_lookup.py list` / `python scripts/component_lookup.py show <id>`; **leggi la scheda** dei soli componenti usati in `references/components/` e poi verifica la fonte ufficiale linkata. I documenti `references/razor-mvc.md`, `references/react-next.md`, `references/html-bootstrap.md` sono **approfondimenti opzionali**, non un elenco di stack supportati o obbligatori. Per qualunque altro stack ricava la sintassi dai file esistenti e dalla documentazione aggiornata delle librerie installate, senza inventare API. Per audit leggi `references/audit.md`; per wizard `references/patterns.md`. Le schede del catalogo sono validate documentalmente, non testate in runtime.
4. **Compatibilità versionata prima di generare markup**: consulta `references/versioned-components.md`. Se il progetto usa Bootstrap Italia 2.x verifica la versione esatta e consulta `python scripts/version_lookup.py --version <versione> --component <id>`; verifica sempre la documentazione corrente relativa a quella release. Per framework e librerie differenti NON trapiantare classi o API Bootstrap Italia: parti dai contratti funzionali e dalla documentazione del loro stack. La matrice è parziale e non runtime-verificata.
5. **Contratti d’accettazione**: leggi `references/acceptance-contracts.md` per ogni componente richiesto e usa `templates/technology-decision.md` per documentare come è stato determinato lo stack. I contratti sono indipendenti dal framework e vanno verificati nell’implementazione reale.
6. **Progetta gerarchia e layout**: leggi `references/visual-foundations.md` e scegli un pattern da `references/page-composition.md`, descrivi ordine dei contenuti, azioni principali e stati. Compila `templates/ui-quality-spec.example.json` come modello per una specifica personalizzata quando utile; `python scripts/validate_ui_spec.py <file.json>` verifica solo i campi, non la qualità della UI. Evita valori CSS arbitrari se il progetto possiede token.
7. **Form e wizard amministrativi**: se la richiesta include raccolta dati o procedure multistep, consulta `references/administrative-forms.md` e `references/administrative-wizards.md`. Prima di implementare, definisci step, stati, validazioni e capacità backend confermate. Usa `templates/administrative-flow.example.json` come esempio e `python scripts/validate_administrative_flow.py <specifica.json>` per la struttura; i warning indicano endpoint da verificare, non errori di sintassi. Non attivare bozza, upload o invio finale senza integrazioni effettive.
8. **Liste, tabelle, dashboard e riuso**: per viste dati consulta `references/administrative-data-views.md` e `references/pattern-reuse.md`; prima di creare nuovi componenti usa `python scripts/discover_ui_patterns.py <repository> --json` come inventario **indicativo**, poi verifica i file reali. Definisci ricerca, filtri, ordinamento, paginazione, export, stati, permessi e API effettivamente disponibili; `python scripts/validate_data_view.py <spec.json>` valida solo la struttura della specifica. Non considerare la visibilità dei pulsanti un controllo di autorizzazione.
9. **Piano breve**: elenca pagine/componenti coinvolti, dati e stati necessari, rischi di regressione e verifiche. Non inventare API del backend, classi CSS o comportamenti non documentati.
10. **Implementa** applicando il catalogo selezionato (`header`, `navigation`, `forms`, `tables`, `modals`, `steppers`) e usando semantic HTML, componenti ufficiali disponibili e pattern del design system. Privilegia riuso, manutenibilità, responsive e testabilità. Non aggiungere librerie senza ragione. Proteggi rendering di testo utente; non inserire dati reali o segreti in demo e log.
11. **Verifica**: esegui comandi già disponibili nel progetto (build, lint, test). Quando la UI è eseguibile su un ambiente di sviluppo autorizzato e Node/browser sono disponibili, consulta `references/browser-verification.md` e proponi/esegui il modulo opzionale `browser-tests/` per controlli Playwright + axe sul DOM renderizzato; configura URL, pagine e selettori in base al progetto, non usare quelli dimostrativi senza adattarli. Non avviare test che potrebbero modificare dati reali o inviare moduli in produzione. Valida navigazione da tastiera, focus, errori, zoom, responsive, contrasti e lettore di schermo tramite review manuale dove possibile. In alternativa usa `python scripts/pa_audit.py <percorso>` per un controllo **euristico non esaustivo** di HTML/CSHTML/JSX/TSX. Non presentare mai quel controllo come certificazione.
12. **Review visiva**: consulta `references/visual-review.md`; verifica gerarchia, densità, layout responsive, stati, feedback, focus e contrasti con browser quando disponibile; registra evidenze in `templates/visual-review-report.md` e indica chiaramente test non eseguiti.
13. **Revisione iterativa quando autorizzata**: consulta `references/iterative-review.md`; usa `npm run review -- --config config/local.json --iteration 1` nel modulo `browser-tests/`, ispeziona realmente screenshot desktop/mobile e risultati axe, correggi solo se richiesto, riesegui fino a 3 iterazioni per default. Non simulare analisi visuali né eseguire fix autonomi in modalità audit.
14. **Consegna** con file modificati, decisioni, fonti/versioni, controlli eseguiti e limitazioni. Distingui test eseguiti, non eseguiti, falliti e verifiche manuali; allega report browser se prodotti. Per audit separa osservazioni confermate, possibili criticità e informazioni non verificabili.

## Neutralità tecnologica

- Le regole del design system, la semantica, l’accessibilità e i requisiti funzionali sono **indipendenti dal framework**. Lo stack viene deciso al momento dell’invocazione.
- Non migrare framework né reimplementare la UI in un’altra tecnologia senza richiesta esplicita. Se l’utente specifica uno stack incompatibile con il progetto, evidenzia il conflitto e proponi il cambiamento minimo verificabile.
- Bootstrap Italia può essere integrato tramite modalità diverse secondo lo stack; Design React Kit è un’opzione **solo** se coerente con la scelta dell’utente e con le dipendenze/versioni verificate. Non imporlo su progetti React e non presentarlo come disponibile su altri framework.
- Esempi specifici di linguaggio sono illustrativi, non un obbligo di adozione.

## Regole non negoziabili

- La documentazione **ufficiale e specifica della versione** prevale su esempi memorizzati e su questa skill.
- Non affermare mai che un'interfaccia sia automaticamente "conforme AGID", "conforme WCAG" o legalmente certificata perché utilizza un kit o supera un test automatico.
- Non rimuovere validazioni server-side, protezioni CSRF, autorizzazioni o logica business durante il refactoring frontend.
- Label per i campi, testo degli errori utile, navigazione da tastiera, indicatori di focus visibili, ordine di tab coerente, messaggi di stato percepibili e alternative ai soli indizi cromatici.
- Preferisci il linguaggio chiaro in italiano, senza attribuire testi legali o informativi non forniti da una fonte.
- Non introdurre marchi, stemmi, nomi di amministrazioni o palette istituzionali inventate.
- Se manca una componente nel kit, costruisci con HTML semantico e spiega la scelta.
- In caso di dubbio normativo, indica l'esigenza di verifica con fonti aggiornate e referente competente.

## Contratto di generazione componenti (v0.2)

- **Header e menu mobile**: dalla versione 2.15.0 consultare l'implementazione ufficiale per il comportamento dialog/focus; mai clonare un vecchio hamburger CSS e dichiararlo accessibile.
- **Form**: label e istruzioni collegate; controllare classi Bootstrap Italia v2.x, comportamento label floating e validazione server-side.
- **Tabelle**: `<th scope>`, caption o nome tabella, righe con azioni distinguibili, overflow responsive verificato.
- **Modali**: titolo accessibile, gestione focus, chiusura, annullamento, JS non inizializzato due volte.
- **Wizard**: gli Steppers gestiscono presentazione e navigazione UI, **non** garantiscono bozza, persistenza, upload, validazione server o invio.
- Gli esempi `examples/components/` sono **didattici** e non completi; non consegnare pulsanti dimostrativi senza handler come funzionalità operativa.
- Per ogni componente riporta la documentazione ufficiale consultata, versione, controlli reali eseguiti e parti rimaste da provare.

## Modalità

- **Generate**: definisci architettura UI minima, stati (loading, vuoto, errore, successo), poi genera il codice e verifica.
- **Audit**: nessuna modifica di default; segnala criticità prioritarie con prova (file/riga), impatto, proposta e grado di certezza.
- **Refactor**: prima mappa comportamento e contratti; modifica in incrementi, mantieni le funzionalità, registra eventuali rischi.

## Output suggerito

Usa `templates/implementation-report.md` per la relazione di consegna; `templates/ui-spec.md` per specifiche di nuove schermate. Per ulteriori esempi: `examples/prompts.md` e `examples/prompts-v02.md` e `examples/prompts-v03.md`.

## Riferimenti

- Designers Italia: https://designers.italia.it/design-system/come-iniziare/per-sviluppatori/
- Bootstrap Italia: https://github.com/italia/bootstrap-italia
- Design React Kit: https://github.com/italia/design-react-kit
- Fondamento accessibilità: https://designers.italia.it/design-system/fondamenti/accessibilita/
- Skill standard: https://agentskills.io/specification

## Test browser opzionali (v0.4)

Il modulo `browser-tests/` utilizza Playwright + axe-core **fuori dallo stack applicativo**. Segui `references/browser-verification.md`: non forzare dipendenze frontend, non supporre che gli esempi di selettori siano validi, non dichiarare conformità dopo test automatizzati.

## Composizione visiva (v0.5)

La qualità visiva è una responsabilità trasversale e indipendente dal framework: riferimenti in `references/visual-foundations.md`, `references/page-composition.md`, `references/visual-review.md`. Non introdurre un nuovo sistema di token né imporre preferenze estetiche arbitrarie.

## Iterative visual review (v0.6)

Il runner acquisisce prove, **non interpreta automaticamente gli screenshot e non modifica il progetto**. Per giudizi visivi servono ispezione dell’agente con capacità visive o revisore umano. Limite di 3 iterazioni salvo indicazione diversa. Documentazione: `references/iterative-review.md`, template: `templates/iteration-review-report.md`.

## Catalogo di versioni (v0.7)

`catalog/version-rules.json` documenta breaking change selezionate per Bootstrap Italia 2.x con fonte e versione. `scripts/version_lookup.py` ne filtra l’applicabilità. Nessun risultato del lookup significa solo assenza di regole catalogate, non compatibilità garantita.

## Procedure amministrative (v0.8)

I contratti per form, validazione, allegati, bozze, riepilogo e invio sono in `references/administrative-forms.md` e `references/administrative-wizards.md`. Un flusso UI non dimostra la disponibilità di servizi backend. Il validatore della specifica controlla solo forma e segnalazioni di integrazioni non risolte.

## Dashboard e tabelle amministrative (v0.9)

I requisiti stack-agnostic e i test di accettazione sono in `references/administrative-data-views.md`. Usa l’inventario indicativo `scripts/discover_ui_patterns.py` per evitare duplicazioni, senza confondere l’indizio con la prova. La specifica di esempio è `templates/data-view.example.json` e si valida con `scripts/validate_data_view.py`. Ricorda: query, sort, paginazione, export e autorizzazioni richiedono comportamento backend verificato.
