# Selezione della tecnologia — framework agnostic

Questo documento definisce **come scegliere** lo stack per un singolo task. Non fornisce una whitelist di framework. Le regole di componenti, UX e accessibilità rimangono comuni.

## Ordine di priorità

1. **Richiesta esplicita** dell’utente: stack e versione dichiarati, inclusi eventuali vincoli (nessuna nuova dipendenza, JavaScript vanilla, ecc.).
2. **Progetto esistente**: se non viene scelto uno stack, identifica la tecnologia già in uso e preservala. Cerca indizi come `package.json`, `.csproj`, `pom.xml`, `build.gradle`, `composer.json`, framework config, dipendenze e codice UI effettivo; non dedurre lo stack solo dal nome della cartella.
3. **Progetto nuovo senza indicazioni**: domanda in modo conciso «Quale tecnologia vuoi usare per il frontend?» prima di generare file specifici, solo quando questa scelta è indispensabile. Accetta **qualunque** risposta tecnica plausibile, non soltanto quelle documentate negli esempi.
4. **Task indipendente dal framework** (analisi UX, wireframe testuale, specifiche, checklist): procedi senza chiedere uno stack.

## Non imporre un framework

- Non creare un progetto React o Razor per default. Non migrare il repository senza richiesta.
- Gli approfondimenti `razor-mvc.md`, `react-next.md`, `html-bootstrap.md` sono optional e si consultano solo se pertinenti. La loro presenza non implica un supporto esclusivo.
- Se lo stack scelto non dispone di una libreria PA ufficiale, applica i pattern tramite HTML semantico/CSS/JS o integrazioni compatibili, previa verifica documentale; non inventare pacchetti ufficiali.
- Per componenti interattivi conserva il comportamento previsto (focus, tastiera, stati, errori) indipendentemente dalla tecnologia.
- Registra le versioni **effettivamente installate** e non mescolare documentazione tra versioni.

## Sequenza di lavoro

1. Registra: origine della scelta (`user`/`repository`/`question`/`not-needed`), linguaggio, framework, versione, styling, librerie UI, build/test tools, vincoli.
2. Se possibile mappa componenti del catalogo PA alle primitive già disponibili.
3. Consulta documentazione ufficiale per il design system **e**, se necessario, per il framework scelto.
4. Genera codice idiomatico nel progetto, senza trascinare snippet in sintassi di un altro framework.
5. Verifica build, interazioni, accessibilità e limiti.

## Esempi

- «Crea un form PA in Angular»: Angular, non React; verifica librerie presenti e API prima dell'uso.
- «Aggiungi il filtro all'elenco esistente»: rileva lo stack e mantienilo.
- «Progetta una pagina di candidatura»: se vuole specifiche UX, procedi; se vuole codice e non c'è progetto, chiedi lo stack.
- «Usa Bootstrap Italia con Blazor»: conserva Blazor, verifica modalità di integrazione JS/CSS e ciclo di vita del componente; non promettere API non verificate.

## Supporto al rilevamento

Esegui `python scripts/detect_stack.py . --json` per raccogliere indizi senza alterare il progetto. Il risultato non sostituisce la lettura del codice né la richiesta esplicita dell’utente: con più framework presenti identifica l’app corretta anziché scegliere arbitrariamente. Usa `templates/technology-decision.md` per registrare la decisione.
