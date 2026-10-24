# Pattern funzionali per portali PA

## Dashboard

- Definisci persona/ruolo, azioni principali, KPI realmente disponibili, date di aggiornamento.
- Non inventare numeri; usa dataset demo esplicitamente indicati come fittizi.
- Stati senza permesso, senza dati, caricamento ed errore.

## Tabelle amministrative

- Colonne necessarie e significato, filtri combinati, reset, ordinamento, paginazione, export solo se autorizzato.
- Gli elementi delle righe devono essere leggibili da lettori di schermo; su mobile prediligi reflow o scorrimento etichettato quando appropriato.
- Esprimi stato con testo e non con colore isolato.

## Wizard candidature e bandi

- Mappa passi, vincoli, salvataggio bozza, ripresa e scadenze fornite da fonte reale.
- Per ogni step: titoli, progressione comprensibile, validazione lato server, error summary, navigazione avanti/indietro, persistenza.
- Nel riepilogo: mostra i dati in sezioni leggibili, fornisci modifica puntuale; "Invia" deve essere distinto da "Salva bozza".
- Alla conferma mostra protocollo/identificativo soltanto se ricevuto da backend reale.
- Upload: verifica estensioni, dimensioni, sicurezza server-side e feedback accessibile.

## Moduli e dichiarazioni

- Separare autorizzazioni/consensi da dichiarazioni amministrative, seguendo il testo fornito dall'ente.
- Non generare affermazioni legali, privacy policy o autocertificazioni inventate.
