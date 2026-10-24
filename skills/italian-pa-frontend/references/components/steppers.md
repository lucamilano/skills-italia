# Wizard e steppers — Bootstrap Italia 2.x

**Stato:** documentato, non verificato in runtime. **Fonte ufficiale:** https://italia.github.io/bootstrap-italia/docs/componenti/steppers/

**Esempio di partenza (didattico):** `examples/components/wizard.html`. Non trattarlo come copia dell'implementazione ufficiale completa.

## Quando usare

Per procedure multi-step con progressione reale e validazioni; non usarli per simulare navigazione di normali pagine.

## Vincoli e controlli

- Intestazione .steppers e lista degli step; active/confirmed non devono essere unico segnale di stato.
- Nei flussi SPA/AJAX usare aria-live=polite sul contenitore contenuti e gestire focus dopo lo step.
- I pulsanti Avanti/Indietro sono azioni: non usare link se non si naviga a una risorsa.
- Salva bozza, validazione per step e recupero dati dipendono da backend reale, non sono forniti dal CSS.

## Classi rilevate nella documentazione

`.steppers`, `.steppers-nav`, `.steppers-content`, `.steppers-btn-prev`, `.steppers-btn-next`

Queste classi non rappresentano necessariamente il markup completo del componente.

## Compatibilità e breaking change

2.3.0: .steppers-index fuori dalla lista; 2.13.0: SVG decorative con aria-hidden=true.

## Prove di accettazione

- Test Tab/Shift+Tab e focus visibile; niente interazioni solo mouse.
- Etichette e annunci percepibili con tecnologia assistiva; niente testo fittizio in produzione.
- Prova mobile, zoom/reflow e navigazione alla tastiera.
- Documentare dipendenze JS e variazioni dalla documentazione del kit.
