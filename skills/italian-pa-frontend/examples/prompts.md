# Prompt per Generate, Audit e Refactor

[Documentazione della skill](../README.md) · [Istruzioni operative](../SKILL.md)

Le tre modalità si indicano nel testo della richiesta. Negli esempi si usa `$italian-pa-frontend` per Codex; in Claude Code puoi sostituirlo con `/italian-pa-frontend` all'inizio del prompt, oppure chiedere di usare la skill per nome. Personalizza perimetro, tecnologia e requisiti: gli esempi non sono applicazioni già implementate.

| Modalità | Sceglila per | Consegna attesa |
| --- | --- | --- |
| **Generate** | Creare un frontend da zero, aggiungere una nuova sezione o definire una specifica. | Struttura, implementazione e verifiche; soltanto specifiche se richiesto. |
| **Audit** | Analizzare senza applicare correzioni. | Report con evidenze, priorità, grado di certezza e verifiche mancanti. |
| **Refactor** | Correggere o migliorare il codice esistente. | Interventi incrementali, contratti conservati e verifiche di regressione. |

## Generate — Creare nuove interfacce

### 1. Portale comunale da zero

```text
Usa $italian-pa-frontend in modalità Generate per costruire da zero
il frontend di un portale comunale dedicato ai servizi al cittadino.

Prevedi homepage, catalogo con ricerca e filtri, dettaglio del servizio
e modulo di richiesta organizzato in più passaggi.
Prima chiarisci con me destinatari, requisiti e tecnologia da usare.
Poi proponi pagine, componenti, stati ed errori e procedi con il codice.

Segui il design system .italia verificando librerie e versioni pertinenti.
Cura tastiera, focus, testi degli errori e layout responsive.
Se il backend non è disponibile, realizza un prototipo con dati sintetici
chiaramente dimostrativi, senza simulare invii o ricevute reali.
Riporta file creati, decisioni, test eseguiti e integrazioni da realizzare.
```

### 2. Sezione gestione bandi nel repository esistente

```text
Usa $italian-pa-frontend in modalità Generate per creare una nuova
sezione di gestione bandi con filtri, tabella e dettaglio.

Rileva lo stack e le versioni installate e riusa layout e componenti
esistenti. Se il progetto usa Bootstrap Italia, consulta le fonti della
versione effettiva prima di generare markup o JavaScript.
Mappa gli endpoint disponibili e collega soltanto contratti verificati.

Gestisci loading, errore, risultati vuoti e paginazione; conserva
filtri e ordinamento in modo coerente con la sorgente dati reale.
Verifica accessibilità e responsive e documenta le parti non provate.
```

### 3. Specifica di un wizard senza generare codice

```text
Usa $italian-pa-frontend in modalità Generate per preparare soltanto
la specifica UX di un wizard di candidatura. Non generare codice
e non scegliere un framework.

Parti dai requisiti che ti fornisco e identifica step, campi, condizioni,
validazioni, navigazione avanti/indietro, focus, errori e riepilogo.
Separa i requisiti confermati dai punti da chiarire. Considera bozza,
upload e invio finale solo come capacità da confermare con il backend.
Consegna struttura delle schermate e criteri di accettazione verificabili.
```

## Audit — Analizzare senza modificare il codice

### 4. Valutazione iniziale del portale

```text
Usa $italian-pa-frontend in modalità Audit sul portale esistente.
Non modificare i file e non applicare correzioni.

Ricostruisci stack, versioni, layout e componenti principali. Analizza
navigazione, gerarchia delle pagine, stati UI, responsive e accessibilità,
confrontando le implementazioni con le fonti pertinenti del design system.

Consegna un report prioritizzato con file/riga, evidenze riproducibili,
impatto e proposta di intervento. Distingui problemi confermati,
potenziali e verifiche non eseguite. L'audit non è una certificazione.
```

### 5. Verifica mirata del form e del wizard

```text
Usa $italian-pa-frontend in modalità Audit sul flusso di candidatura,
senza cambiare codice.

Verifica label e istruzioni, errori associati ai campi, riepilogo errori,
focus, tastiera, passaggi avanti/indietro e conservazione dei dati.
Esamina come la UI rappresenta bozza, allegati e invio finale: separa
i comportamenti provati dalle integrazioni backend non verificabili.

Riporta difetti con evidenze, scenari di riproduzione e priorità.
Indica quali prove browser, mobile e screen reader restano da svolgere.
```

### 6. Header e menu rispetto alla versione installata

```text
Usa $italian-pa-frontend in modalità Audit sull'header e sul menu mobile.
Non modificare i file.

Identifica la libreria UI e la versione reale dal progetto. Se usa
Bootstrap Italia 2.x, consulta la matrice locale e le fonti ufficiali
della release; per altre librerie usa la loro documentazione pertinente.
Controlla apertura e chiusura, nomi accessibili, focus e ritorno al trigger.

Produci un report con prove, incompatibilità documentate e test mancanti.
Non considerare l'assenza di regole nel catalogo una garanzia di correttezza.
```

## Refactor — Migliorare mantenendo il servizio

### 7. Form di candidatura con backend esistente

```text
Usa $italian-pa-frontend in modalità Refactor solo sul form di candidatura.
Prima ricostruisci il comportamento attuale, i componenti riutilizzabili
e i contratti backend; mantieni tecnologia e versioni del progetto.

Migliora label, istruzioni, messaggi server, riepilogo errori e gestione
del focus. Conserva endpoint, validazioni server-side, autorizzazioni,
protezioni CSRF e logica business. Non aggiungere nuove funzioni backend.

Procedi per piccoli interventi, verifica regressioni e flussi di errore
e documenta modifiche, fonti, test svolti e limiti residui.
```

### 8. Dashboard e tabelle su mobile

```text
Usa $italian-pa-frontend in modalità Refactor sulla dashboard delle pratiche.
Mantieni lo stack attuale e riusa filtri, tabella, paginazione e token
già presenti. Prima mappa API, campi e regole di autorizzazione reali.

Migliora layout, densità, stati vuoti ed errori e accesso alle azioni
nei viewport mobili. Mantieni dati, colonne, filtri e ordinamenti coerenti
tra pagine. Conserva i controlli server e non introdurre export fittizi.
Verifica tastiera, focus e menu dentro contenitori con overflow.
Consegna report e verifiche di regressione, indicando quelle non eseguite.
```

### 9. Revisione iterativa con browser e screenshot

```text
Usa $italian-pa-frontend in modalità Refactor per migliorare la pagina
di dettaglio del servizio nell'ambiente locale di sviluppo autorizzato.
Usa esclusivamente dati sintetici e limita le modifiche a questa pagina.

Verifica stack e componenti, poi configura le verifiche browser per URL
e selettori effettivi. Acquisisci screenshot desktop/mobile e risultati axe.
Apri realmente gli screenshot, identifica problemi riproducibili e applica
correzioni incrementali mantenendo comportamento e contratti del servizio.

Riesegui le verifiche per un massimo di tre iterazioni e documenta
il confronto. Se mancano browser, applicazione o capacità di ispezione,
indica i controlli non eseguiti; non simulare evidenze o dichiarare conformità.
```

## Come adattare il prompt

Specifica obiettivo, pagine coinvolte, tecnologia se già scelta, vincoli e servizi confermati. In Generate puoi scegliere uno stack esplicito o far rilevare quello esistente; una specifica UX può procedere senza framework. In Audit chiarisci il perimetro della sola analisi. In Refactor indica il comportamento da conservare e le verifiche attese.

Per esempi più specialistici consulta anche [i contratti di componenti](prompts-v02.md), [la scelta dello stack](prompts-v03.md), [le verifiche browser](prompts-v04.md), [form e wizard](prompts-v08.md) e [dashboard e dati](prompts-v09.md).
