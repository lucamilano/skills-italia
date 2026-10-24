# Form amministrativi — contratti funzionali v0.8.0

Questo documento definisce **comportamenti indipendenti dallo stack**: non attribuisce capacità di salvataggio o protocollazione a componenti UI. Verificare requisiti di processo, versioni librerie e normative applicabili per ogni ente/servizio.

## Prima di generare
1. Identifica scopo, pubblico, campi obbligatori, condizioni e modalità di validazione; evita di richiedere dati già posseduti se non strettamente necessario.
2. Distingui i dati presenti e i requisiti confermati da quelli non specificati; non inventare requisiti giuridici, dichiarazioni sostitutive, scadenze o condizioni di ammissibilità.
3. Descrivi fonti dati, identificatori, destinazione dei documenti, limiti file, consenso e implicazioni di privacy **solo se noti**.
4. Pianifica stati `editing`, `validating`, `invalid`, `submitting`, `submitted`, `error`; se è prevista bozza, aggiungi `saving`, `saved`, `save-error`, `conflict` e `expired` quando pertinenti.
5. Per campi condizionali chiarisci condizioni di visibilità, obbligatorietà e cancellazione dei valori nascosti.

## Validazione
- Ogni input ha label visibile o equivalente accessibile, identificatore stabile e suggerimenti contestuali associati.
- Validazione client per feedback immediato; **backend come autorità** per accettazione e autorizzazione. Regole condivise senza assumere che siano automaticamente sincronizzate.
- Errori al submit: riepilogo con link ai campi e messaggi puntuali utili; focus portato al riepilogo o al primo errore in modo coerente. Non fare affidamento soltanto su bordo rosso o placeholder.
- `aria-invalid` soltanto quando il campo è in errore; collegare messaggi tramite `aria-describedby` e mantenere focus percepibile. Evitare annunci `aria-live` eccessivi.
- Distinguere errori di formato, obbligatorietà, conflitto, rete, permesso e indisponibilità backend; non mostrare successi presunti.
- Evitare `disabled` per nascondere informazioni cruciali o impedire copia; preservare i dati dopo rifiuto server.

## Bozze (solo se richieste)
- Definire chi crea la bozza, identificatore, storage, autenticazione, permessi, scadenza, concorrenza, versionamento e risposta ai conflitti.
- Indicatore esplicito `Salvataggio...`, `Bozza salvata alle ...`, `Impossibile salvare`, `Modifiche non salvate`; nessuna conferma prima della risposta backend.
- Autosave **non è automatico**; richiede consenso architetturale, gestione debounce, errori di rete e dati sensibili. Non persistere dati personali in localStorage per default.
- Su refresh o navigazione, recuperare la bozza **solo** con endpoint verificato; non fabbricare API.

## Allegati (solo se richiesti)
- Input file accessibile anche senza drag-and-drop; indicare formati, dimensioni, massimo file e scopo se documentati.
- Validazioni client su tipo/size solo come UX; convalida server obbligatoria, inclusi MIME/contenuto, permessi, limiti, gestione sicura e scansioni dove previste dal sistema.
- Stati per file: selected, uploading, uploaded, rejected, failed, removed; progressi solo con telemetria reale.
- Non trattare una selezione locale come upload completato; non memorizzare URL permanenti immaginari; gestire retry e rimozione mediante backend verificato.
- Non inserire documenti o dati di utenti reali in screenshot, log o fixture.

## Riepilogo e invio
- Riprodurre i valori effettivamente raccolti, distinguendo allegati caricati da file solo selezionati; possibilità di correggere la sezione.
- L'azione finale mostra una descrizione chiara dell'effetto. Separare revisione, conferma finale e ricevuta quando previsto dai requisiti.
- Prevenire doppi click nel client; **idempotenza e stato definitivo** vanno garantiti dal backend, non dal bottone disabilitato.
- Mostrare numero pratica/protocollo solo se restituito realmente dal backend. Se manca, non inventarlo.
- Errori di rete dopo il submit possono avere esito incerto: offrire verifica stato, non dire automaticamente che l'invio è fallito.

## Fonti documentali
- Form: https://designers.italia.it/design-system/componenti/form/
- Form Bootstrap Italia: https://italia.github.io/bootstrap-italia/docs/form/introduzione/
- Upload: https://italia.github.io/bootstrap-italia/docs/form/upload/
- Esempio form: https://italia.github.io/bootstrap-italia/docs/esempi/form/
