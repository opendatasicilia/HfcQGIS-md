# Layer più vicino

Dati enne layer vettoriali (es:punto, linea e poligono) e un vettore punto di confronto. Come stabilire a quale layer è più vicino un punto tracciato a caso?

![](https://user-images.githubusercontent.com/7631137/111915642-92965880-8a77-11eb-94ac-6e87f061e91a.gif)

Espressione usata nel generatore di geometria del layer punti di confronto:

```
shortest_line(
overlay_nearest(layer:=
with_variable('in_layer',array('punti','line','poligono'), -- three layers
with_variable('in_dist',
        array_foreach(@in_layer,distance(overlay_nearest(@element,$geometry)[0], $geometry)),
array_get(@in_layer, array_find(@in_dist, array_min(@in_dist)))))
,expression:= $geometry )[0],
$geometry)
```

link: <https://gist.github.com/pigreco/f1705597c3515c21d81c64df1b46db09#gistcomment-3673986>

---

Funzioni e variabili utilizzate:

* [@with_variable](../gr_funzioni/variabili/with_variable.md)
* [array_get](../gr_funzioni/array/array_unico.md#array_get)
* [array_foreach](../gr_funzioni/array/array_unico.md#array_foreach)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [array_min](../gr_funzioni/arrayarray_unico.md#array_min)
* [overlay_nearest](../gr_funzioni/geometria/geometria_unico.md#overlay_nearest)
* [distance](../gr_funzioni/geometria/geometria_unico.md#distance)
* [array](../gr_funzioni/array/array_unico.md#start_point)
* [shortest_line](../gr_funzioni/geometria/geometria_unico.md#shortest_line)
* [$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)
