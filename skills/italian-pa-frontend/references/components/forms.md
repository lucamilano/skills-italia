# Form, input e select — Bootstrap Italia 2.x

**Stato:** documentato, non verificato in runtime. **Fonte ufficiale:** https://italia.github.io/bootstrap-italia/docs/form/input/

**Esempio di partenza (didattico):** `examples/components/form-search.html`. Non trattarlo come copia dell'implementazione ufficiale completa.

## Quando usare

Per raccolta di dati, ricerca e invio di richieste; definire obbligatorietà, formati, errori e protezioni dati con il backend.

## Vincoli e controlli

- Ogni controllo ha label associata, istruzioni collegate, errori espressi nel testo.
- Form-control sugli input pertinenti, secondo documentazione >=2.11.0.
- Quando l’input con label flottante ha placeholder o valore, verificare stato active della label.
- Validazione lato server e protezioni CSRF invariate.

## Classi rilevate nella documentazione

`.form-group`, `.form-control`, `.form-text`, `.select-wrapper`

Queste classi non rappresentano necessariamente il markup completo del componente.

## Compatibilità e breaking change

2.2.0: label active con placeholder/valore; 2.11.0: form-control sugli input pertinenti.

## Prove di accettazione

- Test Tab/Shift+Tab e focus visibile; niente interazioni solo mouse.
- Etichette e annunci percepibili con tecnologia assistiva; niente testo fittizio in produzione.
- Prova mobile, zoom/reflow e navigazione alla tastiera.
- Documentare dipendenze JS e variazioni dalla documentazione del kit.

**Attenzione:** `label.active` per input con placeholder/valore e `.form-control` sugli input pertinenti sono regole dipendenti dalla versione. Verificare il comportamento del label floating in browser.
