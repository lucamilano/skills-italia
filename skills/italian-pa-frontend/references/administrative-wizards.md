# Wizard amministrativi — specifica UI e transizioni v0.8.0

Stepper = indicatore e navigazione UI; non sostituisce macchina a stati del processo. Non imporre una tecnologia specifica: traduci i contratti in widget/componenti nativi dello stack scelto.

## Architettura per step
- Definire `step.id`, `title`, campi, criteri di ingresso/uscita, step opzionali e dipendenze, semantica di completamento.
- Avanti: validare lo step corrente, esporre errori, impedire avanzamento soltanto quando previsto dal processo; evitare perdita di input e focus.
- Indietro: conservare dati raccolti; non rimuovere allegati già caricati senza procedura deliberata.
- Navigazione diretta: consentire solo step accessibili in base a regole esplicite; spiegare blocchi.
- Mobile: posizione e numero dello step leggibili; pulsanti avanti/indietro/salva distinguibili. `aria-current="step"` può supportare la semantica quando appropriato, ma controllare pattern e markup della libreria in uso.
- SPA/AJAX: aggiornamenti comunicati alle tecnologie assistive senza duplicare annunci; gestire focus sul titolo del nuovo step. Con Bootstrap Italia verificare `.steppers-content` e `aria-live="polite"` nella documentazione della versione.

## Invarianti
- Un solo step corrente; ordine stabile; niente salti impliciti basati su timing o rete.
- Nessun avanzamento quando il backend ha rifiutato un dato che è necessario validare prima del passo successivo.
- Non confondere `step-complete` (UI) con domanda inviata/confermata (backend).
- Riepilogo mostra solo dati confermati/stato reale; stato allegati distinto.
- Ripresa dopo refresh e bozza sono opzionali e dipendono da servizi esistenti o concordati.

## Esiti test minimi
1. Compilazione corretta: avanzamento, ritorno, edit, riepilogo.
2. Errori multipli: riepilogo, messaggi associati, focus e recupero.
3. Solo tastiera e mobile; zoom al 200%; screen reader da verificare manualmente.
4. Reload, timeout, offline, conflitto e upload interrotto **solo se la feature li prevede**.
5. Invio doppio e risposta incerta: non duplicare l'operazione, non inventare ricevute.

## Fonte
https://italia.github.io/bootstrap-italia/docs/componenti/steppers/
