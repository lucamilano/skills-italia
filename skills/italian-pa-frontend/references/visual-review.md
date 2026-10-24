# Review della qualità visiva — protocollo

**Non** è certificazione e non si riduce a uno screenshot. Condurre review su browser reale se disponibile e documentare ciò che non è stato eseguito.

1. Confermare stack, versione design system, token attivi e route esaminata.
2. Controllare gerarchia titoli, misura testo, allineamenti, ritmo e leggibilità dei contenuti.
3. Verificare layout desktop/mobile, reflow/zoom, overlap, overflow, menu mobile e contenuti lunghi.
4. Verificare stati default/hover/focus/disabled/invalid/loading/success/empty e recupero da errore.
5. Controllare contrasto con valori misurati e contesto, non guardando soltanto lo screenshot.
6. Controllare navigazione keyboard e annunci dei feedback con strumenti appropriati; axe-core è solo controllo parziale.
7. Annotare: URL, viewport, stato, screenshot se disponibile, elemento, problema osservato, severità, evidenza, correzione suggerita, retest.
8. Distinguere: `VERIFICATO`, `DA VERIFICARE`, `NON APPLICABILE`. Non dare un punteggio numerico fittizio.

Usa `templates/visual-review-report.md` e `scripts/validate_ui_spec.py` per la sola completezza della specifica JSON, non per la conformità visiva.
