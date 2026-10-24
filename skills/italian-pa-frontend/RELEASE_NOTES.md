# Release 1.0.0 — 22 ottobre 2026

## Scopo
Consolidamento del catalogo componenti, dei contratti di accettazione e dei workflow Generate, Audit e Refactor. Nessuna dipendenza obbligatoria sul framework applicativo.

## Garanzie e limitazioni
- Le linee guida citate sono riferimenti di progetto, non attestati di conformità AGID/WCAG.
- Catalogo e matrice versioni sono parziali: verificare sempre versione del progetto e fonte ufficiale.
- Validatori JSON verificano la forma delle specifiche, non le funzionalità del portale.
- Gli script di test browser non sono stati eseguiti su un portale PA reale; richiedono target locale e installazione di Playwright.
- Non è stata svolta una sessione interattiva effettiva con Claude Code o Codex: la compatibilità è fondata sul formato Agent Skills e sui percorsi di installazione documentati, non su un collaudo end-to-end dei due agenti.
- L'installatore PowerShell non è stato eseguito in ambiente Windows durante questo consolidamento.

## Test riproducibili
```bash
python scripts/release_check.py
```

## Test da effettuare prima di dichiarare conformità di un portale
1. Implementazione e build di un'app dimostrativa con lo stack scelto.
2. Navigazione e interazioni reali con Playwright, compresi stati di errore.
3. Verifiche manuali con tastiera, ingrandimento, lettore di schermo, contrasti e testi.
4. Revisione della documentazione normativa corrente e dei requisiti applicabili.

## Pubblicazione
Repository GitHub e tag non creati automaticamente. La release ZIP è una distribuzione locale pronta da caricare, non una pubblicazione remota.
