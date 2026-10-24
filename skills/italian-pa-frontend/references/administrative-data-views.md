# Dashboard e viste dati amministrative — v0.9.0

## Prima di generare codice
- Individua la tecnologia preferita dall'utente, altrimenti ricava stack e dipendenze dal repository; non imporre Bootstrap, React o una data grid.
- Esegui `python scripts/discover_ui_patterns.py <repository> --json` e verifica manualmente gli indizi rilevati: la scansione non dimostra che un pattern sia corretto o utilizzabile.
- Elenca endpoint, campi consentiti, semantica dei filtri, limitazioni sui dati e autorizzazioni server **confermati**. In mancanza, genera solo UI dimostrativa esplicitamente indicata, senza inventare integrazioni.
- Per Bootstrap Italia 2.x consulta la documentazione della versione realmente usata e le regole versionate della skill.

## Ricerca, filtri, ordinamento
- Fornisci etichette ai controlli, invio esplicito se appropriato, pulsante pulisci filtri e indicatore dei filtri attivi.
- Mantieni lo stato di ricerca/filtri/pagina nell'URL quando coerente con il progetto; evita di mettere dati sensibili in query string.
- Definisci matching, debounce, applicazione e reset secondo il backend effettivo. Non filtrare il solo sottoinsieme della pagina se l'utente si aspetta una ricerca sull'intera raccolta.
- L'ordinamento deve indicare campo/direzione, essere utilizzabile da tastiera, seguire una whitelist server-side e restare stabile con criteri secondari.

## Paginazione e selezione
- Concorda paginazione server/client e total count reale; non dichiarare totali ignoti. Mostra intervallo e dimensione pagina solo se disponibili.
- Mantieni filtri e sort tra le pagine. Valida parametri in ingresso anche sul server.
- Selezione multipla: chiarisci se interessa pagina corrente o tutte le corrispondenze. Azioni bulk confermate dal server; anteprima e conferma se distruttive.

## Tabelle e dashboard
- Tabelle dati: `<table>`, intestazioni con `scope`, `caption` descrittiva (anche visivamente nascosta se giustificato); non usare tabelle per layout.
- Responsive: valutare scroll orizzontale o vista alternativa che NON perda dati o azioni; verificare focus e dropdown dentro contenitori con overflow (Bootstrap Italia documenta possibili ritagli verticali).
- Dashboard: preferire metriche con etichetta, periodo, unità, fonte, aggiornamento e testo esplicativo; i grafici devono avere alternativa testuale/tabellare e non dipendere solo da colori.
- Stato caricamento, vuoto, nessun risultato filtrato, errore, accesso negato e parzialmente disponibile distinti; recupero/nuovo tentativo solo se operativo.

## Stati delle pratiche e autorizzazioni
- Stati e transizioni devono provenire da regole business confermate; non inventare «approvato», «protocollato», scadenze o operazioni possibili.
- Distinguere visibilità/abilitazione delle azioni lato UI dalle autorizzazioni **obbligatorie lato server**, incluse API/export/bulk.
- Non rivelare dati personali tramite demo, tooltip, telemetria o export. Minimizza dati, applica escaping, CSRF e ruoli già presenti.

## Esportazione
- Definisci ambito: pagina, selezionati o intero risultato filtrato; formato, campi ammessi, permessi e limiti di volume.
- L'export vero richiede un backend o una sorgente dati autorizzata; evitare simulazioni di successo.
- Proteggi contro CSV formula injection nei valori controllati dall'utente; evitare PII inutili; indicare quando è generato il file.

## Accettazione e prove
- Tutti i filtri e sort producono dati coerenti tra pagine; reset ripristina lo stato concordato.
- Interazioni accessibili con tastiera, focus, annunci di risultati aggiornati, loading ed errori.
- L'utente non vede né esporta dati per cui non dispone dell'autorizzazione reale (da verificare con test server/integrati).
- La UI non perde colonne o azioni nei viewport mobili; niente menu ritagliati nella tabella responsive.
- Esegui `python scripts/validate_data_view.py <spec.json> --json`; questo validatore controlla solo completezza dei requisiti.

## Fonti
- Bootstrap Italia — Tabelle: https://italia.github.io/bootstrap-italia/docs/organizzare-i-contenuti/tabelle/
- Designers Italia — Contenuti, tabelle e dati: https://designers.italia.it/design-system/fondamenti/contenuti/
- Designers Italia — Accessibilità: https://designers.italia.it/design-system/fondamenti/accessibilita/
