# Fonti ufficiali, precedenza e versionamento

Verifica prima di usare API o riportare obblighi normativi. Questi link sono punti di accesso, **non copie sincronizzate**.

| Tema | Fonte primaria | Regola |
|---|---|---|
| Design system .italia | https://designers.italia.it/design-system/ | Fondamenti, componenti, pattern |
| Strumenti per sviluppatori | https://designers.italia.it/design-system/come-iniziare/per-sviluppatori/ | Riferimento versione corrente |
| Bootstrap Italia | https://italia.github.io/bootstrap-italia/ | Usare esempi della release installata |
| Sorgente Bootstrap Italia | https://github.com/italia/bootstrap-italia | Changelog/tag prima degli upgrade |
| Dev Kit Italia | https://github.com/italia/dev-kit-italia | Verificare maturità, versione e API prima dell'adozione |
| Design React Kit | https://github.com/italia/design-react-kit | Verificare compatibilità React, Bootstrap Italia, CSS e font |
| Accessibilità | https://designers.italia.it/design-system/fondamenti/accessibilita/ | Analizzare ciascun componente nel contesto |
| AgID | https://www.agid.gov.it/ | Requisiti e linee guida: verificare testi vigenti |
| Dichiarazioni accessibilità | https://www.agid.gov.it/it/design-servizi/accessibilita | Verificare il percorso e gli obblighi correnti |
| WCAG | https://www.w3.org/TR/WCAG22/ | Usare criteri applicabili, non assimilare WCAG a verifica normativa nazionale |
| ARIA APG | https://www.w3.org/WAI/ARIA/apg/ | Pattern accessibili con priorità HTML nativo |

## Snapshot iniziale (22 ottobre 2026)

- Designers Italia presenta Bootstrap Italia **2** come versione corrente.
- Il repository mostra la linea 2.x stabile e la linea 3.x beta; non selezionare 3.x soltanto perché l'etichetta GitHub dice `Latest`.
- Dev Kit Italia è riportato come beta.
- Design React Kit dichiara compatibilità con Bootstrap Italia 2.x e l'obbligo di installare CSS e font separatamente.

Queste informazioni richiedono **nuova verifica** in caso di aggiornamento o nuovo progetto.

Nella preparazione di Skills Italia del 24 ottobre 2026 sono stati ricontrollati i punti di accesso ufficiali, senza ricertificare come correnti le versioni dello snapshot storico. Le pagine AgID hanno reindirizzato a una pagina di manutenzione: i contenuti normativi non sono stati verificati. Un HTTP 200 o un reindirizzamento riuscito non dimostrano la disponibilità della pubblicazione pertinente.

## Gerarchia di affidabilità

1. Codice e lockfile reali del progetto (per identificare la versione usata).
2. Documentazione e changelog ufficiali associati alla **stessa versione**.
3. Documentazione ufficiale generale e risorse di Designers Italia.
4. Esempi terzi soltanto se verificati.
5. Suggerimenti generati dall'agente (da convalidare).

Se fonte e progetto divergono, **non aggiornare automaticamente** la dipendenza: documenta il disallineamento.

## Catalogo aggiunto nella 0.2.0

- Indice strutturato: `catalog/components.json`.
- Schede e fonti per componente: `references/components/README.md`.
- Documentazione consultata il 22 ottobre 2026. La home Bootstrap Italia indicava la versione corrente **2.18.3**; la versione integrata nel progetto può differire.
- In particolare: header e megamenu hanno breaking change dalla **2.15.0** (navigazione mobile con pattern dialog/focus); i form hanno variazioni note nelle linee **2.2.0** e **2.11.0**.
- La data di consultazione non è una data di release del pacchetto. Non usare informazioni di questa sezione per determinare automaticamente una dipendenza da aggiornare.
