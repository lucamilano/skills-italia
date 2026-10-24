# Adattatore React / Next.js

1. Controlla React, Next.js, lockfile, routing (App/Pages), CSS strategy e componenti esistenti.
2. Design React Kit è destinato a Bootstrap Italia 2.x; verifica la versione installata e le peer dependencies prima di aggiungerlo.
3. Il kit React non include automaticamente CSS e font Bootstrap Italia: verificare import secondo documentazione e bundler.
4. Non inventare props e nomi export di `design-react-kit`; confrontare API della versione installata.
5. Mantieni semantica HTML, form controllati quando utile, focus dopo cambi pagina/modal, loading/empty/error.
6. In Next.js, non spostare tutto lato client: delimita correttamente i componenti interattivi e rispetta rendering server/client e hydration.
7. Non includere dati sensibili nei componenti client o nei log. Validazione lato server sempre necessaria.
8. Se il kit non espone un pattern, usa HTML nativo e CSS coerente, spiegando l'eccezione.

`examples/react-search-form.tsx` mostra soltanto un pattern semantico indipendente dal kit; non è presentato come Design React Kit ufficiale.

## Catalogo v0.2

Usare `references/components/README.md` per selezionare il pattern, ma NON convertire automaticamente classi CSS HTML in props di Design React Kit: verificare export e proprietà documentate nel pacchetto installato. Per modal/stepper verificare ownership del DOM, lifecycle e hydration; non inizializzare contemporaneamente JS Bootstrap Italia e componenti React che gestiscono lo stesso nodo.
