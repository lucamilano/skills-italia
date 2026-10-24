# Regole trasversali UI/UX

## Layout e identità

- Identifica target: intranet del personale, servizio al cittadino o sito istituzionale. I pattern possono variare.
- Mantieni chiara gerarchia di titolo, breadcrumb quando utile, navigazione principale coerente e contenuto principale riconoscibile.
- Usa tipografia, spaziature, componenti e palette del kit/versione effettivamente installati. Non inventare token o classi.
- Non associare automaticamente una singola palette a tutta la PA: identità, varianti e loghi richiedono conferma.
- Considera contenuti lunghi, etichette italiane, errori su più righe, zoom 200–400% e schermi stretti.

## Interazione

- Stati: iniziale, loading, dati vuoti, errore, successo, disabilitato, timeout se applicabile.
- Per operazioni distruttive, esplicita conseguenze e offri conferma proporzionata.
- Per tabella: intestazioni comprensibili, filtri etichettati, ordinamento con stato dichiarato, paginazione accessibile, indicazione del numero risultati, mobile senza nascondere informazioni essenziali.
- Form: esplicita obbligatorietà, formato, vincoli, istruzioni e riepilogo errori; conserva dati validi dopo errore.
- Non fare affidamento su hover o colore come unico mezzo di comunicazione.

## Content design

- Italiano chiaro e orientato all'azione.
- Titoli coerenti con attività e terminologia effettiva dell'ente.
- Evita il testo segnaposto come unica istruzione nel campo.
- Evita messaggi fittizi tipo "Operazione completata" senza esito reale.

## Documentazione decisioni

Per ogni scelta significativa annota: componente, fonte/versione, motivazione, test da eseguire, eventuale alternativa.
