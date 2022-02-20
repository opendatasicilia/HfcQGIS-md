---
tags:
  - prossimità
  - condizioni
  - array
  - overlay
  - linee
---

# Geometria più vicina con filtro condizionato

Due layer di punti: `layer1` con attributo `id1` e `layer2` con `id2`.<br>
A partire dal `layer1`, ottenere per ogni punto del `layer1` tutti i punti del `layer2` dove `id2` ha un valore diverso da `id1` (collegarli con un segmento).

Esempio:

[![](https://i.stack.imgur.com/NsXXB.png)](https://i.stack.imgur.com/NsXXB.png)

Come si evince dallo screenshot, i punti in rosso devono collegarsi con i punti blu che hanno `id` differente. Il punto 6 è rimasto isolato perché non ci sono punti vicini e con id diverso da 6.

Espressione utilizzata (**>=QGIS 3.16**):

```
collect_geometries(
		make_line(
		$geometry,
		geometry(get_feature('layer2','id2',
								attribute( 
								array_filter( 
								overlay_nearest('layer2',$currentfeature,limit:=-1), 
								attribute( @element, 'id2' ) != "id1" )[0], 'id2' ))))
					)
```

Altra espressione più performante su grandi dataset (**>=QGIS 3.22.1**)

```
make_line (
    eval( 'overlay_nearest( 
		\'layer2\', 
		$geometry, 
		filter:=id2<>'||"id1"||')')[0],
    $geometry
)
```

idea presa da qui:

- [stackexchange](https://gis.stackexchange.com/questions/391120/qgis-expression-with-overlay-fuction-filter-condition-based-on-comparison-of-at)


### prova tu
- [GitHub](https://github.com/qgis/QGIS/issues/43146#issuecomment-836472827)
- [dati](https://drive.switch.ch/index.php/s/af5cHue6P3NA9xM)

---

Funzioni e variabili utilizzate:

* [array_filter](../gr_funzioni/array/array_unico.md#array_filter)
* [overlay_nearest](../gr_funzioni/geometria/geometria_unico.md#overlay_nearest)
* [attribute](../gr_funzioni/record_e_attributi/record_e_attributi_unico/#attribute)
* [make_line](../gr_funzioni/geometria/geometria_unico.md#make_line)
* [collect_geometries](../gr_funzioni/geometria/geometria_unico.md#collect_geometries)
* [$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)
* [geometry](../gr_funzioni/geometria/geometria_unico.md#geometry_1)