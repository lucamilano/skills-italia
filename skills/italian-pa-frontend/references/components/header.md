# Header istituzionale — Bootstrap Italia 2.x

**Stato:** documentato, non verificato in runtime. **Fonte ufficiale:** https://italia.github.io/bootstrap-italia/docs/menu-di-navigazione/header/

**Esempio di partenza (didattico):** `examples/components/header.md`. Non trattarlo come copia dell'implementazione ufficiale completa.

## Quando usare

Per l’identità del sito/servizio e la navigazione principale; prima di implementare conoscere nome ente, destinazioni reali, ricerca e autenticazione.

## Vincoli e controlli

- Controllare struttura slim/center/nav e identità reale dell’ente.
- Per mobile e forte ingrandimento sulla linea >=2.15.0 partire dall’esempio ufficiale con comportamento dialog/focus-trap; NON ricostruire il menu con un semplice toggle CSS.
- Fornire skip link, nome accessibile e gestione tastiera; testare zoom e screen reader.

## Classi rilevate nella documentazione

`.it-header-wrapper`, `.it-header-slim-wrapper`, `.it-header-center-wrapper`, `.it-header-navbar-wrapper`

Queste classi non rappresentano necessariamente il markup completo del componente.

## Compatibilità e breaking change

2.15.0: navbar mobile/zoom reimplementata come dialog con backdrop; verificare modifiche a CSS/JS personalizzati.

## Prove di accettazione

- Test Tab/Shift+Tab e focus visibile; niente interazioni solo mouse.
- Etichette e annunci percepibili con tecnologia assistiva; niente testo fittizio in produzione.
- Prova mobile, zoom/reflow e navigazione alla tastiera.
- Documentare dipendenze JS e variazioni dalla documentazione del kit.

**Attenzione:** non viene distribuito un header istituzionale completo come snippet. Il layout e la navigazione mobile devono essere importati/adattati dall’esempio ufficiale della release installata; l’esempio contiene solo il contratto semantico di base.
