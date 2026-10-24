# Ricognizione e riuso dei pattern UI

1. Ispeziona componenti condivisi, CSS/token, layout, naming, routing, controlli tabellari, paginazione, error handling e test del repository.
2. `scripts/discover_ui_patterns.py` restituisce **indizi** basati su nomi file e token, non riconosce semanticamente componenti né la loro accessibilità.
3. Apri i file suggeriti e documenta: percorso, funzione reale, uso in produzione, dipendenze, limiti e test disponibili. Riutilizza solo pattern verificati e coerenti con versione design system, accessibilità e UX.
4. Se pattern esistente è difettoso, segnala il difetto e correggilo incrementalmente quando autorizzato. Non duplicare un problema solo per uniformità.
5. Non modificare componenti globali senza verificare l'impatto sulle altre pagine. Prima di creare nuovi widget, controlla quelli già disponibili.
6. Mantieni i nomi, i token e le convenzioni del progetto; non eseguire migrazioni né aggiungere librerie per default.
7. La scansione ignora cartelle comuni di build/cache e non carica segreti; non usare output come inventario esaustivo.
