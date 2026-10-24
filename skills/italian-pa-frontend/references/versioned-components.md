# Matrice versionata dei componenti — v0.7.0

## Principio

Il **contratto funzionale** di un componente è indipendente dal framework; le **classi, il markup e il JavaScript** vanno invece verificati nella libreria e nella versione realmente installate. Le regole in `catalog/version-rules.json` sono documentate per **Bootstrap Italia 2.x** e non sono trasferibili automaticamente ad Angular, React, Dev Kit Italia o Bootstrap Italia 3.

## Procedura obbligatoria

1. Determina la libreria UI reale e la versione esatta nel lockfile, manifest o bundle; non dedurla dal solo framework applicativo.
2. Se la libreria **non** è Bootstrap Italia 2.x, usa i contratti agnostici e la documentazione ufficiale del componente della libreria scelta; non eseguire il lookup v2 come se fosse applicabile.
3. Per Bootstrap Italia 2.x esegui `python scripts/version_lookup.py --version 2.15.0 --component header`; applica soltanto regole introdotte **non dopo** la versione installata. Leggi anche la pagina ufficiale: la matrice non è esaustiva.
4. Tratta gli aggiornamenti come potenziali breaking changes: non mescolare esempi recenti con un progetto su versioni vecchie.
5. Documenta `versione verificata`, `regole applicabili`, `fonte`, `controlli effettuati` e `non verificato` nel report.

## Regole di evidenza

- `official-documentation` = ricavato da documentazione pubblica ufficiale, **non** testato in runtime.
- `runtime_verified: false` = non abbiamo provato quel comportamento in un browser con la libreria caricata.
- Il catalogo è **parziale**. Assenza di regole non implica compatibilità né assenza di cambiamenti.
- Non applicare automaticamente modifiche soltanto sulla base della matrice; confronta il codice reale e pianifica test su tastiera, focus, viewport e screen reader.

Fonti principali: https://italia.github.io/bootstrap-italia/docs/breaking-change/ ; https://designers.italia.it/design-system/componenti/
