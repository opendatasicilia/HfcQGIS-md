---
tags:
  - prossimità
  - condizioni
  - array
  - relazioni
---

# Geometria più vicina e filtro condizionato

Tre layer: 
1. Layer di punti che rappresenta delle utenze (**layer1**).
2. Layer di punti derivante da un rilevamento topografico (**layer2**).
3. Layer di poligoni rappresentante degli edifici (**layer3**).

Popolare un nuovo campo del `layer1` con il valore dell'attributo presente nel `layer2` relativo alla geometria più vicina a condizione che i punti ricadono nello steso poligono, `layer3`.

Esempio:

soluzione di Andrea Giudiceandrea
```
attribute( 
array_filter( 
overlay_nearest( 'layer2', $currentfeature, limit:=-1 ), 
attribute( @element, 'IDp' ) = "IDp" )[0], 'IDl2' )
```

Soluzione pigreco

```
relation_aggregate( 
	relation:='rel',
	aggregate:='array_agg',
	expression:="IDl2")
	[
		with_variable('fufu',
		array_foreach(
			relation_aggregate( 
				relation:='rel',
				aggregate:='array_agg',
				expression:=$geometry),
		distance($geometry,@element)),
		array_find(@fufu,array_min(@fufu)))
	]
```

Soluzione pigreco in SQL

```sql
SELECT l1."IDAG" AS la1 , id, shortestline(l1."geom", l2."geom") as geom
FROM "layer1" l1 , "layer2" l2 
WHERE l1."IDAG"=l2."IDAG"
group by l1."IDAG"
having min(st_distance(l1."geom", l2."geom"))
```

### prova tu

[dati e progetto QGIS 3.12](https://mega.nz/file/lUgwhIIA#gEwH2RpsdkNFGWM6qvqDFnXcMS6IIlfqhnkJnH3m164)

---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/variabili/with_variable.md)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [array_filter](../gr_funzioni/array/array_unico.md#array_filter)
* [array_agg](../gr_funzioni/aggrega/aggrega_unico.md#array_agg)
* [line_locate_point](../gr_funzioni/geometria/geometria_unico.md#line_locate_point)
* [line_interpolate_point](../gr_funzioni/geometria/geometria_unico.md#line_interpolate_point)
* [intersection](../gr_funzioni/geometria/geometria_unico.md#intersection)
* [length](../gr_funzioni/geometria/geometria_unico.md#length)
* [$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)