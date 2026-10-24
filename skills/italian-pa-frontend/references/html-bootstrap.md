# Adattatore HTML / Bootstrap Italia

- Verifica quale release di Bootstrap Italia è già inclusa e da quali percorsi vengono serviti CSS, JS, SVG e font.
- Usa classi e attributi previsti dalla documentazione di **quella release**. Evita di copiare markup Bootstrap generico senza verifica.
- Non riprodurre header/footer ufficiali incompleti come se fossero normativamente sufficienti.
- Preferisci controlli HTML nativi e progressive enhancement; evita JavaScript quando HTML risolve il caso.
- Script di libreria: verifica inizializzazione, ordine, duplicati e fallback; non importare contemporaneamente bundle incompatibili.
- Per ambienti pubblici esamina CSP, asset locali, privacy/cookie e performance con i referenti del progetto.

Per sketch non verificati usa il minimo HTML semantico; marca la successiva integrazione con il kit come TODO.

## Catalogo v0.2

Per un componente presente nel catalogo, leggere prima `references/components/README.md` e la scheda corrispondente. I frammenti `examples/components/` richiedono CSS e, dove indicato, JS/font/sprite Bootstrap Italia presenti; non copiarli come pagine complete.
