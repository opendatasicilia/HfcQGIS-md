---
tags:
  - punti
  - linee
  - nearest
  - distance
---

# ragnetto

Dato un layer di punti, l'espressione permette di simulare un ragnetto che si sposta nella mappa a partire dal centro della stessa mappa. (per far seguire il mouse usare la variabile `@layer_cursor_point` al posto di `@map_extent_center`)

L'espressione va utilizzata in un layer di stile come `generatore di geometrie`.

```
with_variable(
  'center',
  transform(@map_extent_center, @map_crs, @layer_crs),
  if(
    array_contains(
      array_slice(
        array_agg(
          @id,
          order_by := distance(@geometry, @center)
        ), 0, 7
      ),
      @id
    ),
    make_line(@geometry, @center),
    NULL
  )
)
```

[![](../img/esempi/ragnetto/ragnetto.mp4)](../img/esempi/ragnetto/ragnetto.mp4)

- riferimento: <https://discourse.osgeo.org/t/funziona-male-lespressione-overlay-nearest-edit-no/146923>
- ringraziamenti: [Andrea Giudiceandrea](https://github.com/agiudiceandrea)

---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/generale/generale_unico#with_variable)
* [@map_extent_center](../gr_funzioni/variabili/parent.md)
* [@map_crs](../gr_funzioni/variabili/parent.md)
* [@layer_crs](../gr_funzioni/variabili/parent.md)
* [distance](../gr_funzioni/geometria/geometria_unico#distance)
* [make_line](../gr_funzioni/geometria/geometria_unico#make_line)
* [transform](../gr_funzioni/geometria/geometria_unico#transform)
* [array_contains](../gr_funzioni/array/array_unico#array_contains)
* [array_slice](../gr_funzioni/array/array_unico#array_slice)
* [array_agg](../ggr_funzioni/array/array_unico#array_agg)
