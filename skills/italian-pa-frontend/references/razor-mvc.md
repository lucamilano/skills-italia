# Adattatore ASP.NET MVC / Razor Pages

1. Identifica target framework, pacchetti e struttura di `_Layout.cshtml`, bundling e layout condivisi.
2. Preferisci tag helper (`asp-for`, `asp-validation-for`, `asp-validation-summary`) ove già in uso; non rimuovere validazione server-side, antiforgery e autorizzazione.
3. Mantieni escaping predefinito di Razor: evitare `Html.Raw` per input non attendibile.
4. Non inventare nomi di proprietà ViewModel: ricava da modelli reali o marca TODO espliciti.
5. Se si usa Bootstrap Italia, verificare JS inizializzato e componenti disponibili nella versione effettiva; evitare collisioni con Bootstrap generico.
6. Per AJAX: gestire caricamento, errori, messaggio `status`, focus e valori precedenti. Non fare affidamento su soli handler client-side.
7. Creare partials/ViewComponents soltanto quando migliorano davvero il riuso e non confliggono con convenzioni locali.

## Checklist PR

- Build .NET passa? Test e antiforgery invariati?
- Etichette/errori sono associati ai controlli?
- Responsive e tastiera testati?
- Nuovi CSS/JS compatibili con asset presenti?

L'esempio `examples/razor-form.cshtml` è uno **scheletro didattico**: usa i campi del ViewModel reale e non pretende di essere un componente Bootstrap Italia pronto.

## Catalogo v0.2

Usare `references/components/README.md` per selezionare il pattern. Applicare le classi della versione Bootstrap Italia realmente presente nel `_Layout.cshtml`; gli esempi HTML sono frammenti concettuali e devono essere tradotti in Views/Tag Helpers senza interrompere model binding, anti-CSRF, route e validation summary.
