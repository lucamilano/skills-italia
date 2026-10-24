# Ciclo iterativo di revisione UI — v0.6.0

## Obiettivo
Eseguire verifiche browser e acquisire evidenze ripetibili, lasciando **all’agente che può vedere gli screenshot o a un revisore umano** l'interpretazione visuale. Uno script da solo non può decidere se una UI è esteticamente buona. Tecnologia applicativa sempre scelta dall'utente o dal repository.

## Procedura (max 3 iterazioni per default)

1. Leggi `references/technology-selection.md`, `references/visual-foundations.md`, `references/visual-review.md` e `references/browser-verification.md`. Identifica stack e comandi già presenti nel progetto, senza migrare framework.
2. Ottieni autorizzazione a eseguire il portale in locale, con dati fittizi; non avviare procedimenti di invio/salvataggio con dati reali. Usa un ambiente isolato e verifica i permessi. Le pagine che richiedono accesso devono usare sessioni di test gestite in modo sicuro (non inserire token nel repository o negli screenshot).
3. In `browser-tests/`, configura `config/local.json` (non tracciato) con baseURL e percorsi reali, poi `npm install`, `npx playwright install chromium` se necessari.
4. Esegui `npm run review -- --config config/local.json --iteration 1`; produce `reports/review-1.md`, `reports/review-1.json` e allegati screenshot nell'HTML report. Il codice di uscita rispecchia i test Playwright.
5. Leggi **screenshot reali** a desktop e mobile, report JSON e violazioni axe. Non dichiarare analizzati screenshot non aperti. Verifica contenuti, gerarchia, spazi, overflow, focus, stati, interazioni e compatibilità del design system nella versione installata.
6. Registra una lista ordinata di criticità (impatto, evidenza, file, correzione minima). Se l'utente ha chiesto solo audit, **non modificare** il codice. Se è stata chiesta generazione/refactoring, applica modifiche piccole dopo verifica del comportamento esistente.
7. Riesegui `npm run review -- --config config/local.json --iteration 2` e confronta report/screenshot. Ripeti al massimo 3 volte per default; se restano problemi, riporta blocchi e richiedi decisioni quando necessarie. Nessun ciclo infinito, nessun fix a caso per far passare axe.
8. Prima della consegna: build/lint/test disponibili; riepilogo per pagina e viewport; report con PASS/FAIL/NOT RUN e review manuali ancora da fare.

## Vincoli di sicurezza
- Nessuna modifica al codice in modalità audit e nessuna mutazione dei dati durante test in ambienti remoti/produzione.
- Le screenshot potrebbero contenere dati personali: usare fixture sintetiche, non pubblicare immagini/test con dati reali.
- Non disabilitare regole axe né aggiornare baseline per mascherare regressioni.
- Il runner non avvia da solo servizi, non altera file del sito e non corregge autonomamente il progetto. L’agente applica patch solo se richieste e consentite.
- Su app dinamiche, applicare fixture, mascheramento o stabilizzazione prima di confrontare screenshot. Screenshot ≠ pixel-diff: in 0.6.0 non è previsto un algoritmo di comparazione visiva automatica.

## Criteri di uscita
- Test configurati superati e screenshot ispezionati, oppure limite di iterazioni raggiunto con difetti documentati.
- Se manca il browser, il portale o la sessione, marca test NON ESEGUITO: non simulare risultati.
- Nessuna certificazione automatica WCAG/AGID.
