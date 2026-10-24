# Dialog e modali — Bootstrap Italia 2.x

**Stato:** documentato, non verificato in runtime. **Fonte ufficiale:** https://italia.github.io/bootstrap-italia/docs/componenti/modale/

**Esempio di partenza (didattico):** `examples/components/modal-confirm.html`. Non trattarlo come copia dell'implementazione ufficiale completa.

## Quando usare

Per un dialogo contestuale circoscritto; evitare modali per flussi lunghi o pagine che richiedono URL e salvataggio persistente.

## Vincoli e controlli

- Usare attributi aria-labelledby o aria-label, e preferire etichetta visibile.
- Usare il componente JavaScript ufficiale con data-bs-toggle e data-bs-target oppure API programmata, mai inizializzazioni doppie.
- Verificare focus iniziale, trap, Esc, uscita e ripristino focus sull’elemento attivatore.
- Per azioni distruttive la conferma esplicita non deve compromettere la possibilità di annullare.

## Classi rilevate nella documentazione

`.modal`, `.modal-dialog`, `.modal-content`, `.modal-header`, `.modal-body`, `.modal-footer`

Queste classi non rappresentano necessariamente il markup completo del componente.

## Compatibilità e breaking change

La documentazione Bootstrap Italia descrive role=dialog su .modal e role=document su .modal-dialog; seguire documentazione della versione.

## Prove di accettazione

- Test Tab/Shift+Tab e focus visibile; niente interazioni solo mouse.
- Etichette e annunci percepibili con tecnologia assistiva; niente testo fittizio in produzione.
- Prova mobile, zoom/reflow e navigazione alla tastiera.
- Documentare dipendenze JS e variazioni dalla documentazione del kit.
