# Header: contratto semantico, non implementazione istituzionale

> Questo esempio **non è** un header Bootstrap Italia completo. Il menu mobile, l'header slim/center/nav e i relativi attributi ARIA sono troppo sensibili alla versione per inventare uno snippet semplificato.

```html
<a class="visually-hidden-focusable" href="#contenuto-principale">Vai al contenuto</a>
<header>
  <!-- TODO: integrare header ufficiale della release bootstrap-italia installata;
       usare dati REALI dell'ente e testare la navbar mobile dalla 2.15.0. -->
  <p>Nome del servizio (configurato dall'amministrazione)</p>
</header>
<main id="contenuto-principale" tabindex="-1">
  <h1>Titolo della pagina</h1>
</main>
```

La sola presenza di `header` non equivale all'adozione del componente ufficiale. Per sviluppare consultare https://italia.github.io/bootstrap-italia/docs/menu-di-navigazione/header/ e annotare la release esatta.
