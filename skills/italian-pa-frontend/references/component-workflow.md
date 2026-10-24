# Generare componenti senza inventare API

## Routing

La skill deve leggere `references/components/README.md` e, per ogni richiesta, soltanto le schede dei componenti coinvolti; il catalogo JSON può essere cercato con `scripts/component_lookup.py` per ridurre il contesto. Le schede sono vincoli di progetto, non codice da copiare indiscriminatamente.

## Richieste tipiche

- **Layout PA:** `header`, `navigation`, eventuale sidebar, landmark `main`; no logo o nome ente inventato.
- **Elenco amministrativo:** `forms` per filtri + `tables` per risultati; attenzione a paginazione server-side e autorizzazioni.
- **Conferma azione:** `modals` quando breve, evitando overlay superflui.
- **Candidatura multi-step:** `steppers` + `forms`, contratto backend per bozza, validazione e invio finale.

## Checklist obbligatoria di esecuzione

1. Risolvi lo stack con `references/technology-selection.md`, poi identifica versione reale del kit e del framework. Se non nota, NON indicare markup come garantito per la versione.
2. Individua la *fonte ufficiale* corrispondente e le eventuali modifiche incompatibili. Non mescolare v1/v2/v3.
3. Per ogni componente definisci `required data`, `states`, `interactions`, `accessibility`, `errors`, `mobile`, `security`.
4. Applica controlli pertinenti allo stack scelto: per React verifica API/import/peer-deps e hydration delle librerie effettivamente usate; per Razor mantieni Tag Helpers/antiforgery e encoding; per altri stack verifica binding, lifecycle, protezioni CSRF e compatibilità delle librerie senza inventare API.
5. Scrivi un test di accettazione funzionale (non solo visivo) e una checklist per QA manuale.
6. Etichetta evidenze: verificato su codice, documentato sul sito, non verificato in runtime, richiede verifica normativa.

## Requisiti di completamento per tutti i componenti

- Nessun link `#` fittizio o pulsante privo di azione nel codice definitivo.
- Nomi/ruoli/stati accessibili e focus chiaramente visibile.
- Gestione degli stati caricamento, errore, vuoto, successo se pertinenti.
- Niente esiti “conforme ad AGID” senza valutazione specialistica.
