# Contratti di accettazione (agnostici rispetto allo stack)

Questi contratti sono requisiti comportamentali e semantici, **non** API CSS/JS specifiche. Tradurli nel framework scelto solo dopo aver identificato librerie e versioni effettive. Il superamento delle checklist **non** prova conformità normativa.

## Form
- Ogni controllo ha un nome accessibile; label e istruzioni sono collegate programmaticamente.
- Campi obbligatori, formati ed errori sono comprensibili senza dipendere soltanto dal colore.
- Errori di validazione lato server restano attivi; al submit fallito focus/riepilogo errori sono gestiti in modo coerente.
- Stati: idle, invio, errore, successo; previeni doppi invii indesiderati; preserva input quando possibile.
- Test: solo tastiera, errori su campi multipli, zoom al 200%, viewport mobile.

## Tabelle
- Intestazioni e associazioni colonna/riga corrette; caption o nome accessibile quando opportuno.
- Filtri e paginazione hanno etichette, focus e stati caricamento/vuoto/errore; azioni riga hanno nomi non ambigui.
- Su mobile nessun dato essenziale viene perso; decidere e testare overflow, adattamento o vista alternativa.
- Test: tabella lunga, zero risultati, label azioni ripetute, ordinamento tastiera.

## Header e navigazione
- Nome dell'ente/servizio solo se fornito e verificato; landmarks e navigazione coerenti.
- Menu mobile: focus iniziale, trap quando previsto dal pattern ufficiale e ritorno focus alla chiusura; Escape secondo comportamento documentato.
- Stato attivo, breadcrumb e struttura headings non dipendono da soli stili visivi.
- Test: apri/chiudi solo tastiera, resize, focus dopo navigazione.

## Modali
- Usarle soltanto quando appropriate, con titolo e scopo chiari.
- Gestire apertura, focus, chiusura e ritorno focus; distinguere azioni distruttive.
- Non usare dialog per riprodurre informazioni che possono stare nella pagina.

## Wizard
- Indicatore di avanzamento semanticamente comprensibile, passaggio attuale identificabile.
- Dati conservati tra step secondo requisiti, con validazione client e server distinta.
- Bozza, upload, persistenza e invio finale sono funzionalità backend da specificare, mai inferite dallo stepper.
- Test: indietro/avanti, errori, reload, salvataggio se presente, invio duplicato.

## Report per ogni feature
Scrivi: tecnologia selezionata (origine e versione), design-system/versione, componenti, contratti soddisfatti, test eseguiti, test non eseguiti, rischi e fonti. Preferisci l'esito `non verificato` a un'affermazione di conformità.
