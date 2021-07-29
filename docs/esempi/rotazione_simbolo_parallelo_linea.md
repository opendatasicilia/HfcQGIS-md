# Rotazione simbolo parallelamente alla linea più vicina

L'espressione di sotto calcola l'angolo della linea più vicina e lo utilizza per far ruotare parallelamente un simbolo.

```
with_variable ('geom',
overlay_nearest('strade_palermo',$geometry)[0],
line_interpolate_angle( @geom,
line_locate_point(@geom,closest_point(@geom,$geometry))))
```

[![](../img/esempi/rotazione_simbolo/rotazione_simbolo.gif)](../img/esempi/rotazione_simbolo/rotazione_simbolo.gif)

---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/variabili/with_variable.md)
* [overlay_nearest](../gr_funzioni/geometria/geomatria_unico.md#overlay_nearest)
* [line_interpolate_angle](../gr_funzioni/geometria/geomatria_unico.md#line_interpolate_angle)
* [closest_point](../gr_funzioni/geometria/geomatria_unico.md#closest_point)
* [\$geometry](../gr_funzioni/geometria/geomatria_unico.md#geometry)
