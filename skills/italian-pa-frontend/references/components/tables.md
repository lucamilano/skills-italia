# Tabelle dati — Bootstrap Italia 2.x

**Stato:** documentato, non verificato in runtime. **Fonte ufficiale:** https://italia.github.io/bootstrap-italia/docs/organizzare-i-contenuti/tabelle/

**Esempio di partenza (didattico):** `examples/components/table.html`. Non trattarlo come copia dell'implementazione ufficiale completa.

## Quando usare

Per dataset strutturati e confrontabili con molte righe; per dati non tabellari valutare liste o card.

## Vincoli e controlli

- Usare caption o titolo contestuale e intestazioni th scope=col.
- Per scorrimento orizzontale, valutare div .table-responsive e un nome/descrizione del contesto; controllare a zoom 400%.
- Distinguere ordinamento, filtro e paginazione; non implementare interazione fasulla.
- Le azioni di riga devono avere nomi accessibili distintivi.

## Classi rilevate nella documentazione

`.table`, `.table-responsive`

Queste classi non rappresentano necessariamente il markup completo del componente.

## Compatibilità e breaking change

Tabelle responsive con overflow possono tagliare dropdown/popover: testare o spostare overlay fuori dallo scroll container.

## Prove di accettazione

- Test Tab/Shift+Tab e focus visibile; niente interazioni solo mouse.
- Etichette e annunci percepibili con tecnologia assistiva; niente testo fittizio in produzione.
- Prova mobile, zoom/reflow e navigazione alla tastiera.
- Documentare dipendenze JS e variazioni dalla documentazione del kit.

**Attenzione:** `.table-responsive` utilizza overflow e può ritagliare menu e popup contenuti nella tabella.
