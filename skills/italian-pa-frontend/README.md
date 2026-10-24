# Italian PA Frontend 🇮🇹

> Agent Skill open source per generazione, audit e refactoring di frontend della Pubblica Amministrazione italiana, con riferimenti a Designers Italia, Bootstrap Italia e accessibilità.

**Versione:** 1.0.0 (consolidamento) · **Lingua:** italiano · **Licenza:** MIT · **Stato:** release iniziale, non certificata e non affiliata.

Primo modulo della suite **Skills Italia**. Questa cartella è anche un pacchetto autonomo: i comandi qui sotto si eseguono dalla sua root. I percorsi delle risorse sono relativi a questa cartella, non al repository applicativo. Versione della skill 1.0.0 e versione della suite 0.1.0 sono indipendenti; changelog, roadmap e note di release locali conservano la storia precedente.

## Cosa fa

- Svolge ricognizione dello stack e delle versioni.
- Pianifica e genera interfacce amministrative secondo componenti e pattern del design system effettivamente disponibile.
- Analizza frontend esistenti e assiste nel refactoring incrementale.
- Richiama checklist di accessibilità e uno scanner statico euristico per markup.
- **Agnostica rispetto allo stack:** usa quello dichiarato dall’utente o rilevato nel progetto; supporta anche tecnologie non presenti negli esempi. HTML, ASP.NET MVC/Razor Pages e React/Next.js hanno approfondimenti opzionali, non esclusivi.
- Include il **catalogo consultabile offline** di 6 componenti Bootstrap Italia 2.x: header, navigazione/breadcrumb, form, tabelle, modali, steppers.
- Collega ogni scheda a fonte ufficiale, classi documentate, breaking change, checklist ed esempio esplicitamente dimostrativo.

**Non** include runtime Bootstrap Italia né contenuti copiati dalle librerie ufficiali, non garantisce conformità normativa e include un modulo separato e opzionale di test browser, ma non esegue audit WCAG completi né li considera certificazioni.

## Installazione rapida

Copia **l'intera cartella `italian-pa-frontend`**, inclusi `references/`, `templates/`, `scripts/` ed `examples/`.

- **Codex, progetto locale**: `<progetto>/.agents/skills/italian-pa-frontend/`
- **Claude Code, progetto locale**: `<progetto>/.claude/skills/italian-pa-frontend/`
- **Codex, globale (utente)**: `~/.agents/skills/italian-pa-frontend/`
- **Claude Code, globale (utente)**: `~/.claude/skills/italian-pa-frontend/`

Il pacchetto contiene installatori locali per Python 3.10+, con wrapper PowerShell e Bash. Installazioni identiche sono un no-op; installazioni modificate richiedono `--force`/`-Force` dopo un backup. I file generati, le dipendenze installate e le configurazioni private vengono esclusi dalla copia. Avviali dal pacchetto estratto:

### Windows PowerShell

```powershell
.\scripts\install.ps1 -Agent both -Scope project -ProjectPath "C:\percorso\progetto"
```

### Linux/macOS (bash)

```bash
bash scripts/install.sh --agent both --scope project --project-path /percorso/progetto
```

Per installare globalmente: sostituisci `project` con `user`. Per reinstallare una nuova versione: usa `-Force` in PowerShell oppure `--force` in bash (verifica eventuali personalizzazioni prima di sovrascrivere).

## Scelta della tecnologia

La skill **non ha una lista chiusa di framework**. Per ogni richiesta:

1. Se indichi la tecnologia («usa Blazor», «usa Angular», «usa React»), la rispetta.
2. Se stai lavorando su un progetto esistente e non dici nulla, prova a riconoscere lo stack e lo mantiene.
3. Se vuoi generare codice in un progetto nuovo e non è possibile individuare una tecnologia, chiede quale preferisci.
4. Per specifiche UX o audit indipendenti dal framework, procede senza domande superflue.

Le regole di accessibilità e design system restano uguali. Per i dettagli: `references/technology-selection.md`.

## Primo utilizzo

Per Codex:

```text
Usa $italian-pa-frontend per analizzare il progetto e creare una tabella
candidature filtrabile. Conserva le API esistenti, controlla la versione
Bootstrap Italia e restituisci i controlli di accessibilità eseguiti.
```

Per Claude Code locale: usa `/italian-pa-frontend` seguito dalla richiesta, oppure chiedi di usare la skill per nome. Formato e percorsi sono documentati; le sessioni interattive dei due agenti non sono state collaudate.

Altri esempi: `examples/prompts.md`.

## Catalogo componenti (v0.2.0)

```bash
python scripts/component_lookup.py list
python scripts/component_lookup.py show header
python scripts/component_lookup.py show forms
```

Il catalogo strutturato è `catalog/components.json`, con schede in `references/components/` ed esempi in `examples/components/`. È basato sulla documentazione Bootstrap Italia **2.x** consultata il 22 ottobre 2026; i singoli esempi **non** sono stati testati dentro un'app con il kit installato. La documentazione e i changelog della versione effettiva del progetto sono sempre prioritari.

### Nota sulle interfacce interattive

Gli snippet di dialog e wizard richiedono il bundle e/o gli handler del progetto: non sono demo autonome. Per l'header mobile (>=2.15.0) la skill richiede di partire dall'implementazione ufficiale. Non crea una navigazione accessibile con un solo toggle CSS. Il codice può essere prodotto dall'agente nel progetto reale dopo la ricognizione degli asset.

## Controlli inclusi

```bash
python scripts/validate_skill.py
python scripts/component_lookup.py list
python -m unittest discover -s tests -v
python scripts/pa_audit.py path/to/frontend --format text
python scripts/pa_audit.py path/to/frontend --format json
```

Lo scanner non installa dipendenze e controlla alcuni segnali su file `.html`, `.htm`, `.cshtml`, `.jsx`, `.tsx` (limiti documentati in `references/audit.md`). Esito pulito ≠ pagina accessibile.

## Struttura

```text
italian-pa-frontend/
├── SKILL.md
├── README.md
├── catalog/           # Catalogo JSON machine-readable
├── references/        # Regole, schede componenti, stack, audit
├── templates/         # Specifiche UI e report
├── examples/          # Prompt e frammenti didattici per componenti
├── scripts/           # Installatori, audit e validazione
└── tests/             # Test automatici dello scanner
```

## Migrazione dalle versioni precedenti

Reinstalla con `--force` (bash) / `-Force` (PowerShell) **solo dopo avere salvato eventuali modifiche locali**. La skill continua a chiamarsi `italian-pa-frontend`; i percorsi di installazione non cambiano.

## Fonti e responsabilità

Fonti ufficiali consultabili in `references/official-sources.md`. Le informazioni di versione sono uno snapshot: verificare sempre release e requisiti applicabili. Questo progetto è indipendente e non è uno strumento di certificazione accessibilità.

## Contributi

Apri una issue con scenario riproducibile, framework/versione, link documentazione e comportamento atteso. Aggiungere nuove regole richiede fonte/versione e, quando possibile, una fixture di regressione.

Consulta `ROADMAP.md` e `CHANGELOG.md`.


## Novità 0.3.0: tecnologia scelta dall’utente

La skill non impone un framework. Priorità: richiesta esplicita, stack del repository, domanda solo se la tecnologia è necessaria e non ricavabile. Per una prima ricognizione non distruttiva: `python scripts/detect_stack.py /percorso/progetto --json`. La skill segue i contratti indipendenti dallo stack in `references/acceptance-contracts.md`. La selezione può essere documentata con `templates/technology-decision.md`. Non significa che tutte le combinazioni tecnologiche siano già testate.

## Browser testing opzionale (v0.4.0)

Il modulo `browser-tests/` contiene Playwright, axe-core, configurazioni per pagine/contratti, report e test di validazione. Lo stack applicativo resta invariato.

```bash
cd browser-tests
npm install
npx playwright install chromium
# avvia prima la tua app su localhost
# adatta config/example.json a config/local.json
PA_TEST_CONFIG=config/local.json npm test
```

Per PowerShell: `$env:PA_TEST_CONFIG='config/local.json'; npm test`. Leggi `browser-tests/README.md` e `references/browser-verification.md` prima di eseguire test con interazioni. La suite non è stata ancora eseguita su una vera app della PA.

## Composizione delle pagine (v0.5.0)

Le regole in `references/visual-foundations.md` e `references/page-composition.md` descrivono gerarchia tipografica, spacing, griglie, stati e layout per dashboard, elenchi, form, wizard e dettagli pratica, senza prescrivere un framework. In `references/visual-review.md` trovi un protocollo di review manuale.

Per specificare una schermata copia `templates/ui-quality-spec.example.json`, compila il JSON e valida **solo la struttura** con:

```bash
python scripts/validate_ui_spec.py percorso/schermata.json
```

Il controllo non analizza CSS renderizzato, accessibilità o conformità normativa. Per i test browser consulta `browser-tests/README.md`.

## v0.6.0 — review iterativa

Nel modulo `browser-tests/`, dopo la configurazione e installazione Playwright, esegui `npm run review -- --config config/local.json --iteration 1`. Il runner salva screenshot full-page in allegati Playwright desktop/mobile, dati JSON e `reports/review-1.md`. L’agente o un umano deve **guardare** le immagini, proporre piccole correzioni autorizzate e rieseguire al massimo 3 iterazioni per default. Nessuna correzione automatica incontrollata né dichiarazione di conformità normativa. Leggi `references/iterative-review.md`.

## Novità v0.7.0 — regole per versioni

Le regole di modifica documentate da Bootstrap Italia 2.x sono registrate in `catalog/version-rules.json`. Consulta le sole regole applicabili alla versione reale:

```bash
python scripts/version_lookup.py --version 2.15.0 --component header
python scripts/version_lookup.py --version 2.11.0 --component forms --json
```

La matrice è **parziale** e non sostituisce il controllo della fonte ufficiale. Se il frontend usa un'altra libreria o framework, non applicare le classi Bootstrap Italia per analogia. Vedi `references/versioned-components.md`.

## Flussi amministrativi (v0.8.0)

Form e wizard descritti da contratti tecnologicamente neutrali: validazione, riepilogo, upload e bozze condizionali, gestione degli stati e invio. I servizi backend non sono generati per supposizione.

```bash
python scripts/validate_administrative_flow.py templates/administrative-flow.example.json
python scripts/validate_administrative_flow.py templates/administrative-flow.example.json --json
```

Vedi `references/administrative-forms.md`, `references/administrative-wizards.md`, `examples/prompts-v08.md`.

## Dashboard e viste dati (v0.9.0)

- Ricerca/filtri/sort/paginazione, stati UI, esportazione e autorizzazioni: `references/administrative-data-views.md`.
- Rilevamento indizi di componenti riutilizzabili: `python scripts/discover_ui_patterns.py <repository> --json`; **richiede ispezione manuale**.
- Esempio `templates/data-view.example.json`; validazione strutturale: `python scripts/validate_data_view.py templates/data-view.example.json --json`.
- **Non** crea backend inesistenti e **non** garantisce enforcement dei permessi né conformità WCAG.


## Verifica prima del rilascio (v1.0.0)

Da root esegui `python scripts/release_check.py`; controlla struttura skill, test Python, test unitari Node e controlli di consistenza. Richiede Python 3 e Node.js; **non** esegue Playwright sul browser.

Leggi `RELEASE_NOTES.md` per la matrice dei controlli eseguiti e dei limiti. Lo script di installazione non pubblica nulla né installa le dipendenze browser. Per provare Playwright è necessario preparare separatamente un'applicazione locale autorizzata.

Per aggiornare un'installazione già personalizzata, crea un backup prima di usare `-Force` o `--force`. Non eseguire i test browser su ambienti di produzione contenenti dati reali.
