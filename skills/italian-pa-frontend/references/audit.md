# Protocollo audit frontend PA

**Ambito**: statico (codice), runtime (se ambiente disponibile), normativo (solo con fonte vigente e verifica umana).

## Workflow

1. Definisci perimetro e stack senza modificare files.
2. Estrai componenti, schermate, layout condivisi, pattern form e tabelle.
3. Evidenzia dipendenze design system con nome e versione **verificata**.
4. Scansiona i file per evidenze; esegui `python scripts/pa_audit.py <path>` solo come primo filtro. Produce segnalazioni euristiche con possibili falsi positivi.
5. Se possibile avvia app e verifica un percorso reale con tastiera, lettore di schermo, dimensioni, errori.
6. Crea report con: severità (blocker/alta/media/bassa), evidenza, riproduzione, fonte, fix suggerito, conferma manuale richiesta.
7. Distingui **Verificato**, **Potenziale** e **Non verificabile**. Non stimare punteggio WCAG o conformità legale.

## Priorità tipiche

1. Task non completabile (tastiera, errori, perdita dati, focus bloccato).
2. Controlli senza nome accessibile o messaggi non percepibili.
3. Reflow/contrasto/zoom e navigazione incoerente.
4. Scostamenti di stile puramente estetici.

## Output

Usa `templates/audit-report.md` e allega, dove possibile, file e riga. Un'assenza di warning dallo script **non significa** assenza di difetti.
