# Pattern di composizione pagine — indipendenti dallo stack

Leggi `references/visual-foundations.md` prima di creare una schermata. I pattern sono **contratti UX**, non template specifici di un framework.

## Dashboard amministrativa
- Titolo della pagina e periodo/dati di riferimento, descrizione contestuale.
- Riepiloghi comparabili con etichette, unità, valori e spiegazione della provenienza; non usare solo icone o colori.
- Priorità alle attività operabili; una card deve linkare o attivare solo se l'azione è reale.
- Dati scarsi: descrizione e azione praticabile; dati in caricamento: annuncio dello stato senza flicker.
- Testare numeri grandi, etichette lunghe, filtri attivi e permessi differenziati.

## Elenco / ricerca / tabella
- Intestazione, numero risultati, controlli filtro con label, reset filtri; distinguere nessun dato da nessun risultato.
- Tabella semantica quando ci sono relazioni per righe/colonne; intestazioni accessibili, azioni contestualizzate.
- Ordinamento e paginazione devono conservare stato, mostrare stato attivo e comunicare risultati.
- Su mobile scegliere una soluzione basata sulla natura dei dati: scrolling controllato o rappresentazione alternativa verificata; non convertire automaticamente ogni tabella in card.

## Form / procedura
- Raggruppare campi in sezioni significative con hint e obbligatorietà esplicita.
- Errori vicini ai campi, riepilogo errori se opportuno, preservazione input; validazione client mai sostitutiva di server.
- Azione primaria univoca per schermata; annulla/esci con conseguenze chiare.

## Wizard
- Passi con titoli chiari, progressione significativa, passaggio da tastiera.
- Separare navigazione UI da persistenza di bozza, back-end e upload.
- Dopo errore indicare il problema senza perdere dati e mantenere il focus prevedibile.

## Dettaglio pratica / documento
- Identificativo, stato con testo, data/ora contestualizzate, cronologia se disponibile, azioni autorizzate.
- Evitare di mascherare dati sensibili in aria-label o log; mostrare solo dati autorizzati.

## Evidenze da produrre
- Specifica di contenuto e stato; diagramma della gerarchia semplice; 2 viewport rappresentativi; checklist manuale; problemi e limitazioni.
