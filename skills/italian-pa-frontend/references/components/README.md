# Catalogo componenti — Bootstrap Italia 2.x

Questa directory è una **guida operativa per agenti**: serve a individuare i vincoli di un componente, non sostituisce il sito ufficiale e non certifica la conformità. La **fonte primaria è la documentazione collegata a ogni scheda**; verificare sempre la versione installata del progetto.

| Componente | Scheda | Esempio | Fonte primaria |
|---|---|---|---|
| Header istituzionale | [header](header.md) | [header.md](../../examples/components/header.md) | [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/menu-di-navigazione/header/) |
| Navigazione e breadcrumb | [navigation](navigation.md) | [breadcrumb.html](../../examples/components/breadcrumb.html) | [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/menu-di-navigazione/breadcrumbs/) |
| Form, input e select | [forms](forms.md) | [form-search.html](../../examples/components/form-search.html) | [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/form/input/) |
| Tabelle dati | [tables](tables.md) | [table.html](../../examples/components/table.html) | [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/organizzare-i-contenuti/tabelle/) |
| Dialog e modali | [modals](modals.md) | [modal-confirm.html](../../examples/components/modal-confirm.html) | [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/componenti/modale/) |
| Wizard e steppers | [steppers](steppers.md) | [wizard.html](../../examples/components/wizard.html) | [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/componenti/steppers/) |

## Livello di verifica

- `documented-not-runtime-verified`: classi, pattern e breaking change riscontrati nella documentazione online; **non** garantisce test su browser/stack reali.
- Gli esempi sono **didattici**: non costituiscono kit grafico completo o componenti già compilati. Tutti assumono gli asset CSS/JS/font Bootstrap Italia 2.x installati nel progetto, quando richiesti.
- Non usare le regole v2.x su bootstrap-italia 1.x o 3.x; per componenti interattivi (header mobile, modali e wizard) verificare la release *esatta*.

## Workflow per agente

1. Leggere `catalog/components.json` o eseguire `python scripts/component_lookup.py list`.
2. Scegliere il componente e consultare **solo** la scheda pertinente con le relative fonti.
3. Leggere l'adattatore stack in `references/`.
4. Identificare gli stati e il contratto funzionale del componente prima di generare codice.
5. Verificare il componente nel browser sul progetto reale e descrivere quanto non è stato verificato.
