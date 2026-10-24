# Fondamenti visivi — v0.5.0

Queste sono **regole di composizione e verifica**, non una nuova libreria CSS e non valori da imporre al progetto. Prima di implementare rileva tema, versione e token realmente disponibili nel progetto e consulta le fonti ufficiali. Non inventare nomi di variabili, classi o colori.

## Tipografia e gerarchia

- Una pagina deve avere un titolo principale significativo (`h1`) e sezioni con gerarchia semantica coerente. Non scegliere i tag in base alla dimensione desiderata.
- Preferire gli stili tipografici del design system effettivamente installato; il riferimento ufficiale usa Titillium Web e descrive anche Lora e Roboto Mono.
- Per la lettura, privilegiare righe di testo non eccessivamente lunghe (Designers Italia consiglia max ~75 caratteri/riga). Non comprimere il testo solo per farlo entrare in una card.
- Usare testo ordinario, non segnaposto generici o abbreviazioni non spiegate; ogni blocco deve avere un ruolo informativo chiaro.

## Spaziatura e densità

- Utilizzare la scala/tokens di spacing esistente. La baseline tipografica del design system è 4px: **non** significa forzare tutte le dimensioni a multipli fissi senza verificare il sistema effettivo.
- Definire ritmo tra sezioni, gruppi, label/campo/help/error, pulsanti e azioni. Evitare margini ad hoc per ogni singola pagina.
- Presentare solo informazioni e azioni necessarie, non riempire la pagina con card decorative.

## Griglia e adattabilità

- Impaginare mobile-first. Per Bootstrap Italia 2.x il riferimento è una griglia di 12 colonne con breakpoint documentati; per altri stack usare la griglia nativa/equivalente già adottata.
- Verificare a 320 CSS px, 375 CSS px, 768 CSS px, 1280 CSS px, ingrandimento 200% e reflow equivalente a 400% ove applicabile. Questi viewport sono **scenari di test proposti**, non breakpoint normativi universali.
- Le tabelle di dati possono richiedere scorrimento orizzontale; evitare troncamenti irreversibili, mantenere intestazioni/contesto e verificare focus/tastiera.
- Ordine visuale, ordine DOM e sequenza focus devono restare coerenti.

## Colore, contrasto e stati

- Usare i token esistenti per neutral, primary e semantic status; non inventare una palette «ministeriale».
- Non codificare stato, priorità o errori solo attraverso il colore: usare etichetta, testo e, se opportuno, icona con nome accessibile.
- Controllare contrasto per coppie effettive di foreground/background: WCAG AA generalmente 4.5:1 per testo normale, 3:1 per testo grande e per componenti/elementi grafici pertinenti; consultare criteri applicabili ed eccezioni.
- Focus chiaramente percepibile; verificare anche hover, active, selected, disabled, pending, invalid, success e read-only quando presenti.

## Composizione pagina

1. Identificare il compito primario e la navigazione contestuale.
2. Stabilire una gerarchia: titolo, descrizione breve, azione principale, contenuto, azioni secondarie.
3. Raggruppare dati e controlli per significato, non per comodità CSS.
4. Rendere espliciti loading, empty, error, success, permission-denied e timeout/offline quando pertinenti.
5. Validare a desktop e mobile con contenuti realistici (etichette lunghe, numeri, errori, 0 o molti risultati).
6. Preferire componenti ufficiali disponibili per la versione verificata; gli esempi non sono prove di conformità.

## Fonti (verificate 2026-10-22)

- https://designers.italia.it/design-system/fondamenti/tipografia/
- https://designers.italia.it/design-system/fondamenti/colori/
- https://designers.italia.it/design-system/fondamenti/
- https://italia.github.io/bootstrap-italia/docs/organizzare-gli-spazi/griglie/
- https://italia.github.io/bootstrap-italia/docs/organizzare-i-contenuti/tipografia/
