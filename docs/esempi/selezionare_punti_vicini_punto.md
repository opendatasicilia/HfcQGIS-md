---
tags:
  - selezionare
  - vicinanza
  - punto
  - overlay
---

# Selezionare 'n' punti più vicini ad un punto selezionato

Supponiamo di avere un layer di punti e di voler selezionare i primi 10 punti più vicini ad un punto selezionato arbitrariamente. Questo esempio prende spunto da questa domanda posta su [StackExchange](https://gis.stackexchange.com/questions/410940/how-to-select-the-number-nearest-points-in-qgis).

Usando solo le espressioni di QGIS e `Select by Expression` ![](../img/icon/mIconExpressionSelect.png), l'espressione da usare è:


```
/*Select the first 'n' points closest to the selected point*/
-- fid selection
with_variable ('selected_fid',
	array_find(
	array_agg(geom_to_wkt($geometry,6)),
	array_agg(geom_to_wkt($geometry,6), filter:=is_selected())[0]),
-- selection circle	
with_variable ('circle', 
	make_circle (
	$geometry,
	aggregate(
	layer:=@layer_name,
	aggregate:='array_agg',
	expression:=
	array_max(array_foreach (
	overlay_nearest (@layer_name, $geometry,limit:=10),
	distance($geometry,@element))))[@selected_fid]),
-- verify
	intersects (@circle,array_agg($geometry)[@selected_fid]))
)
```

NB: il valore del parametro `limit:=` in questo caso specifico, dipende dal provider utilizzato:

1. per `shapefile` ($id inizia da 0) utilizzare `limit:=valore +1`
2. per `geopackage` ($id inizia da 1) utilizzare `limit:=valore`

![](https://i.stack.imgur.com/sNnlw.gif)

---

Funzioni e variabili utilizzate:

* [@with_variable](../gr_funzioni/variabili/with_variable.md)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [array_agg](../gr_funzioni/array/array_unico.md#array_agg)
* [array_foreach](../gr_funzioni/array/array_unico.md#array_foreach)
* [aggregate](../gr_funzioni/aggrega/aggrega_unico.md#aggregate)
* [geom_to_wkt](../gr_funzioni/geometria/geometria_unico.md#geom_to_wkt)
* [make_circle](../gr_funzioni/geometria/geometria_unico.md#make_circle)
* [distance](../gr_funzioni/geometria/geometria_unico.md#distance)
* [overlay_nearest](../gr_funzioni/geometria/geometria_unico.md#overlay_nearest)
* [intersects](../gr_funzioni/geometria/geometria_unico.md#intersects)
* [is_selected](../gr_funzioni/record_e_attributi/record_e_attributi_unico.md#is_selected)
* [$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)
