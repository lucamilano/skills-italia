# Skills Italia

**Skill per agenti AI per sviluppare software e servizi digitali della Pubblica Amministrazione italiana**

*AI Agent Skills for Italian Public Administration Development*

[English](README.en.md) · [Installazione](installation.md) · [Roadmap](../ROADMAP.md) · [Contributi](../CONTRIBUTING.md) · [Licenza MIT](../LICENSE)

[![Verifiche della suite](https://github.com/lucamilano/skills-italia/actions/workflows/checks.yml/badge.svg)](https://github.com/lucamilano/skills-italia/actions/workflows/checks.yml)

[Repository GitHub](https://github.com/lucamilano/skills-italia) · [Segnala un problema](https://github.com/lucamilano/skills-italia/issues/new/choose) · [Discussioni](https://github.com/lucamilano/skills-italia/discussions)

Skills Italia è una suite open source indipendente di **skill per agenti AI** dedicata agli sviluppatori che realizzano e mantengono software e servizi digitali per la Pubblica Amministrazione italiana. Fornisce fonti ufficiali da verificare per versione, procedure di implementazione e strumenti di controllo nel processo di sviluppo dell'agente.

La suite parte dal frontend: siti pubblici accessibili, form amministrativi, dashboard e applicazioni esistenti. La visione comprende sicurezza, identità, interoperabilità e modernizzazione software PA. Oggi è disponibile soltanto la skill frontend.

La suite **0.1.0** distribuisce Italian PA Frontend **1.0.0**. I due versionamenti hanno cicli distinti: consulta il [changelog](../CHANGELOG.md).

## Perché Skills Italia?

I servizi pubblici richiedono interfacce usabili, integrazioni affidabili e decisioni fondate sul progetto reale. La generazione generica di codice può mescolare versioni del design system Italia, sostituire componenti funzionanti o inventare capacità backend. Skills Italia guida l'analisi del repository, il riuso delle soluzioni esistenti, la consultazione delle fonti pertinenti e la rendicontazione delle verifiche effettive.

Le competenze riutilizzabili sono pensate per gli agenti AI usati dagli sviluppatori. Supportano implementazione, analisi e manutenzione del software per la pubblica amministrazione, senza certificare conformità legale o sostituire valutazioni specialistiche.

## Skill disponibili — Available Skills

| Skill | Versione | Stato | Ambito |
| --- | --- | --- | --- |
| [Italian PA Frontend](../skills/italian-pa-frontend/SKILL.md) | 1.0.0 | **Disponibile — Available** | Generazione, audit e refactoring frontend con qualunque stack web scelto o rilevato. |

Italian PA Frontend comprende:

- Procedure basate sul design system .italia e Designers Italia; riferimenti ai componenti Bootstrap Italia e regole versionate, valutando Dev Kit Italia e Design React Kit quando pertinenti al progetto reale.
- Componenti accessibili, form e wizard amministrativi, dashboard e tabelle responsive.
- Rilevamento dello stack, inventario indicativo dei pattern riutilizzabili e audit statico di file simili a HTML.
- Validatori strutturali di specifiche JSON, template di consegna ed [esempi d'uso](../skills/italian-pa-frontend/examples/prompts.md).
- Modulo separato e opzionale Playwright e axe, screenshot e revisione iterativa con limite di iterazioni.

Catalogo e matrice versioni sono parziali. I validatori controllano le specifiche, non il comportamento di un'applicazione in esecuzione. Consulta la [documentazione del modulo](../skills/italian-pa-frontend/README.md) e i [limiti delle verifiche](verification.md).

## Skill pianificate — Planned Skills

Sono proposte per moduli futuri, **non skill installabili**. Non esistono implementazioni segnaposto.

| Modulo | Stato | Ambito previsto |
| --- | --- | --- |
| Italian PA Accessibility | **Pianificata — Planned** | WCAG 2.2 e requisiti applicabili, tastiera, focus, screen reader e audit con evidenze. |
| Italian PA Identity | **Pianificata — Planned** | Integrazione SPID CIE, OpenID Connect, SAML pertinente e sessioni sicure. |
| Italian PA Interoperability | **Pianificata — Planned** | REST, OpenAPI, interoperabilità PDND, e-service, contratti e osservabilità. |
| Italian PA Security | **Pianificata — Planned** | Secure coding, OWASP, segreti, autorizzazioni e threat modeling. |
| Italian PA Architecture | **Pianificata — Planned** | Analisi legacy, architetture modulari, modernizzazione graduale, migrazioni e ADR. |
| Italian PA Quality | **Da valutare — Under consideration** | Test unitari, integrazione, E2E, contratti, prestazioni e CI/CD. |
| Italian PA Documentation | **Da valutare — Under consideration** | Specifiche, manuali operativi, diagrammi e tracciabilità dei requisiti. |
| Italian PA Privacy | **Da valutare — Under consideration** | Privacy by design, minimizzazione, conservazione e supporto tecnico alle valutazioni privacy. |

La [roadmap pubblica](../ROADMAP.md) chiarisce confini, prerequisiti e criteri di disponibilità. Non assegna date arbitrarie. La community può proporre moduli tramite Issues o Discussions del repository.

## Compatibilità con gli agenti AI

| Agente | Installazione | Invocazione esplicita | Evidenza |
| --- | --- | --- | --- |
| OpenAI Codex | `.agents/skills/` nel progetto o nella home utente | `$italian-pa-frontend` | Formato e percorsi confrontati con la [documentazione ufficiale](https://developers.openai.com/codex/skills/). |
| Claude Code | `.claude/skills/` nel progetto o nella home utente | `/italian-pa-frontend` | Formato e percorsi confrontati con la [documentazione ufficiale](https://code.claude.com/docs/en/skills). |
| Altri agenti Agent Skills | Secondo la documentazione dell'agente | Specifica dell'agente | Non verificati: controllare discovery, accesso agli script e permessi. |

Installazione locale e compatibilità strutturale sono verificate separatamente dal comportamento degli agenti. Le sessioni interattive con entrambi gli agenti **non sono state collaudate**. La guida riguarda i client locali: ambienti cloud e gestiti possono applicare regole diverse. Il pacchetto segue il [formato Agent Skills](https://agentskills.io/specification).

## Installazione

Scarica o clona una copia revisionata del repository ed esegui dalla root con Python **3.10+**. Gli script Python non richiedono dipendenze esterne. Node.js **22.12+** serve solo per i controlli Node e gli strumenti browser opzionali. Gli installatori non scaricano né eseguono script remoti.

```console
git clone https://github.com/lucamilano/skills-italia.git
cd skills-italia
```

Una singola skill nel progetto di destinazione già esistente:

```console
python scripts/install.py --skill italian-pa-frontend --agent codex --scope project --project-path /percorso/progetto
```

Tutte le skill disponibili per entrambi gli agenti a livello utente (attualmente una sola):

```console
python scripts/install.py --all --agent both --scope user
```

Usa `--agent claude` per Claude Code, `--dry-run` per ispezionare le destinazioni e `--force` per sostituire un'installazione modificata dopo averne fatto un backup. Installazioni identiche non vengono riscritte. Sono presenti entry point PowerShell e Bash per Windows, Linux e macOS. [Guida completa a installazione, aggiornamento e rimozione](installation.md).

## Avvio rapido

1. Installa la skill nel progetto o nella home utente.
2. Avvia una nuova sessione locale dell'agente nel progetto e verifica che la skill sia elencata.
3. Invocala con un obiettivo circoscritto e controlla modifiche ed evidenze riportate.

Esempio Codex:

```text
Usa $italian-pa-frontend per analizzare questo progetto e migliorarne
l'interfaccia seguendo il design system della Pubblica Amministrazione italiana.

Rileva lo stack esistente, riusa i componenti disponibili e verifica
l'accessibilità, distinguendo i controlli eseguiti da quelli ancora da svolgere.
```

Esempio con Claude Code per la pubblica amministrazione:

```text
/italian-pa-frontend Analizza la dashboard amministrativa senza modificare file.
Verifica tastiera, filtri della tabella e stati di errore.
Riporta evidenze distinguendo criticità confermate e controlli non eseguiti.
```

## Esempi d'uso

```text
Usa $italian-pa-frontend per migliorare il form di candidatura esistente.
Rileva lo stack, riusa i componenti e conserva validazioni e autorizzazioni.
Non inventare API per bozze o allegati. Verifica focus, errori e responsive.
```

```text
Usa la skill italian-pa-frontend per migliorare i risultati di ricerca del servizio.
Mantieni lo stack Java/Thymeleaf e i contratti backend esistenti.
Verifica ordinamento, paginazione, stati vuoti e accesso alle azioni da mobile.
```

Per usare Bootstrap Italia con assistenza AI, chiedi prima di identificare la versione installata della libreria. La skill per Codex dedicata alla pubblica amministrazione è lo stesso modulo utilizzabile con Claude Code. L'uso di Designers Italia con agenti AI non implica approvazione ufficiale.

## Scelta delle tecnologie

La scelta esplicita dell'utente ha priorità. In assenza di indicazioni, l'agente analizza lo stack esistente e ne mantiene framework, versioni e convenzioni. È possibile indicare qualunque stack web plausibile; gli esempi React, Razor e HTML sono approfondimenti opzionali. Nei nuovi progetti si chiede una tecnologia solo se necessaria per procedere. Audit UX e specifiche possono essere svolti senza scegliere un framework.

## Architettura modulare

```text
skills-italia/
├── README.md, LICENSE, CONTRIBUTING.md, SECURITY.md
├── suite.json, CHANGELOG.md, ROADMAP.md, RELEASE_NOTES.md
├── docs/                 # panoramica bilingue, installazione, governance, release
├── skills/
│   └── italian-pa-frontend/
│       ├── SKILL.md, LICENSE, README.md, CHANGELOG.md, ROADMAP.md
│       ├── references/, catalog/, templates/, examples/
│       ├── scripts/, tests/
│       └── browser-tests/
├── scripts/              # installazione, validazione e pacchetti della suite
├── tests/                # regressioni della suite e dell'installazione
└── .github/              # CI, aggiornamenti dipendenze e template contributi
```

Ogni skill disponibile è autonoma, installabile e versionabile indipendentemente. Le regole generali della suite non sostituiscono quelle specialistiche dei moduli. [Architettura e versionamento](architecture.md).

## Accessibilità e sicurezza

I controlli automatici rilevano soltanto parte dei problemi. Servono verifiche di tastiera, focus, screen reader, zoom e qualità visiva, oltre alla valutazione dei requisiti applicabili. L'utilizzo di un kit, l'assenza di violazioni axe o un report generato non certificano conformità WCAG né accessibilità AGID.

Mantieni autorizzazioni, validazioni server, protezioni CSRF ed escaping esistenti. Non inserire segreti, dati personali o sessioni di produzione in esempi, screenshot e report. I test browser richiedono un target configurato e autorizzato, limitato a localhost per default. [Policy di sicurezza](../SECURITY.md).

## Roadmap

Skills Italia intende supportare il ciclo di vita del software oltre il frontend. Consulta i [moduli Available, Planned e Under consideration](../ROADMAP.md), inclusi i futuri ambiti identità, interoperabilità e modernizzazione. Una nuova skill diventa disponibile soltanto con procedure utili ed evidenze credibili.

## Fonti ufficiali

- [Designers Italia](https://designers.italia.it/) e [design system .italia](https://designers.italia.it/design-system/): documentazione ufficiale di design.
- [Bootstrap Italia](https://github.com/italia/bootstrap-italia), [Dev Kit Italia](https://github.com/italia/dev-kit-italia) e [Design React Kit](https://github.com/italia/design-react-kit): strumenti e librerie ufficiali da confrontare con le versioni installate.
- [AgID](https://www.agid.gov.it/): verificare requisiti giuridici e tecnici nelle pubblicazioni ufficiali pertinenti.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): raccomandazione tecnica W3C; l'applicabilità al singolo servizio richiede una valutazione separata.

Skills Italia offre procedure indipendenti e raccomandazioni tecniche, senza introdurre requisiti normativi. [Registro delle verifiche sulle fonti](sources.md).

## Come contribuire

Leggi [CONTRIBUTING.md](../CONTRIBUTING.md), la [guida alle nuove skill](contributing-skills.md) e il [Codice di condotta](../CODE_OF_CONDUCT.md). Sono benvenuti contributi in italiano o inglese con fonti ufficiali, prove riproducibili e limiti dichiarati.

Controlli locali di preparazione della release:

```console
python scripts/release_check.py
```

Il comando esegue controlli strutturali, documentali, Python, Node e installazione. I test E2E richiedono un'applicazione e restano separati. [Guida alle verifiche](verification.md).

## Licenza

[MIT](../LICENSE). Sono conservate le attribuzioni dei contributori di Italian PA Frontend. Documentazione e librerie esterne mantengono licenze e marchi propri.

## Disclaimer

Skills Italia è un progetto open source indipendente, non ufficialmente affiliato, approvato o sostenuto da AGID, Designers Italia o dal Governo italiano.

Skills Italia is an independent open-source project and is not officially affiliated with or endorsed by AGID, Designers Italia, or the Italian Government.

Le skill supportano il lavoro tecnico e non sostituiscono professionisti legali, di sicurezza, accessibilità o privacy. Non esiste una certificazione automatica di conformità.
