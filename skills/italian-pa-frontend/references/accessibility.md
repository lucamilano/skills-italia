# Accessibilità: checklist di lavoro (non certificazione)

I controlli automatici intercettano soltanto una parte dei problemi. Verificare i criteri WCAG applicabili e gli obblighi normativi italiani in vigore.

## HTML e navigazione

- `html[lang]` corretto, un titolo pagina descrittivo, landmark `main`, heading ordinati per struttura.
- Controlli nativi `button`, `a`, `input`, `select` preferiti a div interattivi.
- Ogni input ha nome accessibile, label, istruzioni e indicazione dei campi obbligatori (senza affidarsi solo ad asterischi).
- Collegare errore e istruzioni mediante `aria-describedby` ove necessario; `aria-invalid` sul controllo in errore.
- Tab order logico, focus visibile, tastiera completa (Tab, Invio, Spazio, Esc dove pertinente).
- Aggiornamenti asincroni importanti annunciati in modo misurato (`role=status`, live region); non usare sempre `role=alert`.
- Dialog: gestione focus, chiusura, label e ripristino focus; utilizzare componenti testati.
- Icone decorative nascoste alle tecnologie assistive; icone informative con nome accessibile.

## Visivo e responsive

- Contrasti secondo criteri WCAG applicabili; stato non espresso soltanto dal colore.
- Test 320 CSS px e reflow/zoom, 200% testo, spaziatura testo e orientamento.
- Target cliccabili sufficientemente accessibili, etichette non troncate, nessuno scorrimento a due assi salvo contenuti che lo richiedono.
- Preferenze di movimento ridotto per transizioni non essenziali.

## Form, wizard, messaggi

- Error summary con link ai campi quando appropriato.
- Indica step attuale e progressione anche testualmente, non solo attraverso forme o colori.
- Persistenza dati e possibilità di tornare indietro senza perdere valori.
- Validazione client complementare a quella server (mai sostitutiva).

## Piano minimo di prova

1. Test automatico con strumenti come axe-core/Lighthouse se disponibili.
2. Percorso completo da tastiera.
3. Zoom, reflow e display mobile.
4. Lettore di schermo su almeno i flussi critici (es. NVDA/VoiceOver), se disponibile.
5. Verifica manuale di chiarezza, focus, ordine di lettura, error recovery.

**Esito corretto**: "Superati i controlli automatizzati eseguiti; restano prove manuali e verifica normativa" — non "Conforme WCAG/AGID".
