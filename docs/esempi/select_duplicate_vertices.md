---
tags:
  - selezionare
  - vertici
  - conta
  - array
---

# Selezionare vertici duplicati

Ogni volta che estraiamo i vertici in una geometria (lineare o poligonale) otteniamo quasi sempre dei vertici duplicati, in questo esempio vedremo come selezionarli usando le espressioni.

[![](../img/esempi/select_duplicate_vertices/img_01.png)](../img/esempi/select_duplicate_vertices/img_01.png)

Per selezionare i vertici duplicati vedremo due soluzioni diverse:

- prima soluzione usando una funzione di aggregazione `count`

```
count(
    expression:=geom_to_wkt( $geometry,2),
    group_by:=geom_to_wkt( $geometry,2)
      ) > 1
```

Ogni espressione viene valutata riga per riga nella tabella attributi, questa espressione sarà vera solo in quelle righe dove il conteggio delle geometrie sono maggiori di uno e quindi duplicate: prima riga, conteggio con aggregazione, eistono più geometrie uguali?? se si il count è >1 e seleziona la riga.

- seconda soluzione usando gli `array`

```
array_length(
        array_agg( 
            expression:=$geometry,
            group_by:=geom_to_wkt($geometry,2))
            ) > 1
```

Il concetto è simile a quello precedente, ma usando gli array: quindi quando un array contiene più di un elemento (geometria=vertice), la lunghezza dell'array sarà > 1 e quindi duplicato.

per entrambe stesso risultato:

[![](../img/esempi/select_duplicate_vertices/img_02.png)](../img/esempi/select_duplicate_vertices/img_02.png)

## Selezionare solo uno dei due punti doppi

espressione da utilizzare:

- seleziona primo punto

```
if($id = 
  array_first( -- primo punto
    array_agg(
    expression:= $id,
    filter:=
      array_length(
      array_agg( 
      expression:=$geometry,
      group_by:=geom_to_wkt($geometry)))>1,
    group_by:=geom_to_wkt($geometry)
    )
  )
, $id, '')
```

- selezionare ultimo punto

```
if($id = 
  array_last( -- ultimo punto
    array_agg(
    expression:= $id,
    filter:=
      array_length(
      array_agg( 
      expression:=$geometry,
      group_by:=geom_to_wkt($geometry)))>1,
    group_by:=geom_to_wkt($geometry)
    )
  )
, $id, '')
```

[![](../img/esempi/select_duplicate_vertices/img_03.png)](../img/esempi/select_duplicate_vertices/img_03.png)

- nel caso di molti punti sovrapposti si potrebbe utilizzare la notazione degli array, cioè le parentesi quadre:

```
if($id = 
    array_agg(
    expression:= $id,
    filter:=
      array_length(
      array_agg( 
      expression:=$geometry,
      group_by:=geom_to_wkt($geometry)))>1,
    group_by:=geom_to_wkt($geometry)
    )[0] -- primo vertice doppio; [-1] per ultimo; [x] per xesimo posto
, $id, '')
```

**NB1:** La selezione potrebbe non essere visibile a schermo a causa della sovrapposizione dei punti, per ovviare alternare le funzioni `array_first` con `array_last`. <br>
**NB2:** I calcoli da fare sono molti e per dataset pesanti potrebbe impiegarci molto tempo (dipende anche dalle risorse hardware)

In collaborazione con **Valerio Pinna** che ringrazio per la disponibilità.

## Prova tu

il geopackage è scaricabile [qui](https://github.com/pigreco/HfcQGIS/raw/master/esempi/vertici_duplicati.gpkg)

---

Funzioni e variabili utilizzate:

* [if](../gr_funzioni/condizioni/condizioni_unico.md#if)
* [\$id](../gr_funzioni/array/array_unico.md#id)
* [get_feature_by_id](../gr_funzioni/record_e_attributi/record_e_attributi_unico.md#get_feature_by_id)
* [array_agg](../gr_funzioni/array/array_unico.md#array_agg)
* [array_sort](../gr_funzioni/array/array_unico.md#array_sort)
* [string_to_array](../gr_funzioni/array/array_unico.md#string_to_array)
* [array_last](../gr_funzioni/array/array_unico.md#array_last)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [array_reverse](../gr_funzioni/array/array_unico.md#array_reverse)
* [geom_to_wkt](../gr_funzioni/geometria/geometria_unico.md#geom_to_wkt)
* [count](../gr_funzioni/aggrega/aggrega_unico.md#y_min)
* [array_length](../gr_funzioni/array/array_unico.md#array_length)
* [\$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)