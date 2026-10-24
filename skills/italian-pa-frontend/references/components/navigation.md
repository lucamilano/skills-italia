# Navigazione e breadcrumb — Bootstrap Italia 2.x

**Stato:** documentato, non verificato in runtime. **Fonte ufficiale:** https://italia.github.io/bootstrap-italia/docs/menu-di-navigazione/breadcrumbs/

**Esempio di partenza (didattico):** `examples/components/breadcrumb.html`. Non trattarlo come copia dell'implementazione ufficiale completa.

## Quando usare

Per aiutare le persone a orientarsi tra sezioni e capire dove si trovano; breadcrumbs per gerarchia e sidebar per navigazione di area.

## Vincoli e controlli

- Navigazione primaria e breadcrumb sono due pattern distinti; non sostituire l’uno con l’altro.
- Breadcrumb con nav etichettato, lista ordinata e aria-current=page sulla voce attiva.
- Per sidebar/megamenu usare codice ufficiale della versione e testare aria-expanded/focus.

## Classi rilevate nella documentazione

`.breadcrumb-container`, `.breadcrumb`, `.breadcrumb-item`

Queste classi non rappresentano necessariamente il markup completo del componente.

## Compatibilità e breaking change

2.8.0: varie modifiche a markup dropdown e megamenu; 2.15.0: comportamento mobile dialog.

## Prove di accettazione

- Test Tab/Shift+Tab e focus visibile; niente interazioni solo mouse.
- Etichette e annunci percepibili con tecnologia assistiva; niente testo fittizio in produzione.
- Prova mobile, zoom/reflow e navigazione alla tastiera.
- Documentare dipendenze JS e variazioni dalla documentazione del kit.
