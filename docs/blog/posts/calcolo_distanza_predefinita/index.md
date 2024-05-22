---
social_image: img/card_social/hfc_blog.png
draft: false
date: 2024-05-21
authors:
  - pigreco
categories:
  - espressioni
tags:
  - blog
  - distanza
  - form
  - valore_predefinito
---

# Distanza Predefinita su Form

## Introduzione

Come calcolare la distanza tra due stazioni successive e far popolare l'attributo tramite il _Valore predefinito_ in in Form.

!!! Abstract "Funzione"
    Come usare il Valore predefinito per popolare un attributo legato alle geometrie.

<!-- more -->

Basta usare l'espressione:

```py
with_variable ('agg',array_agg(@geometry, order_by:="fid"),
round(distance(@agg[-1], @geometry ),3))
```

dove:

- `with_variable ('agg',array_agg(@geometry, order_by:="fid")` calcolo un array di tutti i punti precedentementi tracciati;
- `@agg[-1]` è l'ultima geometria tracciata prima della corrente;
- `@geometry` è la geometria corrente;
- `round(distance(@agg[-1], @geometry ),3)` calcola la distanza tra l'ultimo punti tracciato e il corrente, arrotonda a tre cifre.
- `"fid"` è il campo univoco autoincrementale creato dal GeoPackage


[![](./demo.gif)](./demo.gif)

**NB1:** l'espressione funziona bene per unica sessione iniziale, dalla seconda in poi calcolerà le distanze rispetto l'ultimo punto tracciato nella sessione iniziale. (ci sto lavorando per ovviare al problema!)

**NB2:** L'espressione di sopra funziona bene se ad ogni punto inserito salviamo le modifiche.
