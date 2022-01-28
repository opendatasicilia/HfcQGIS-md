## Conta punti nel poligono e per data

Immaginiamo di avere dei poligoni in cui ricadono dei punti: contare i punti per ogni poligono e per ogni data. 

![](https://i.stack.imgur.com/v1n42.png)

creare un nuovo campo nel layer poligonale e popolarlo con la seguente espressione:

```py
array_to_string(
	with_variable('arraydate',
		aggregate(
		layer:='nomeLayerPunti', -- layer punti con attributo date
		aggregate:='array_agg', 
		expression:="date", -- campo data
		order_by:="date",
		filter:= intersects( $geometry, geometry(@parent))),
	array_foreach(
		array_distinct(@arraydate),@element||': '||array_count(@arraydate,@element))
))
```

### prova tu

idea presa da qui SE: <https://gis.stackexchange.com/questions/422320/counting-points-in-polygon-by-time-in-qgis>

---

Funzioni e variabili utilizzate:

* [@parent](../gr_funzioni/variabili/parent.md)
* [@with_variable](../gr_funzioni/variabili/with_variable.md)
* [aggregate](../gr_funzioni/aggrega/aggrega_unico.md#aggregate)
* [array_to_string](../gr_funzioni/array/array_unico.md#array_to_string)
* [array_count](../gr_funzioni/array/array_unico.md#array_count)
* [array_foreach](../gr_funzioni/array/array_unico.md#array_foreach)
* [array_distinct](../gr_funzioni/array/array_unico.md#array_distinct)
* [$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)
* [intersects](../gr_funzioni/geometria/geometria_unico.md#intersects)
