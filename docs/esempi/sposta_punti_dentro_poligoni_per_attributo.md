---
tags:
  - punti
  - poligoni
  - calamita
  - linee
---

# Spostare i punti dentro i poligoni in base agli attributi

Un layer poligonale con tre particelle, attributo `Parcel_No` (1,2 e 3) e un layer puntuale con mille punti e attributo `Parcel_No` (1,2 e 3), quindi i punti hanno solo tre valori. Spostare i punti nel corrispondente poligono, utilizzando, appunto, l'attributo comune.

espressione utilizzata:

```
closest_point(
   geometry(get_feature('polygon','Parcel_No',
   attribute($currentfeature,'Parcel_No' ))),
   $geometry)
```
[![](https://i.stack.imgur.com/wRsSK.png)](https://i.stack.imgur.com/wRsSK.png)

l'espressione crea un altro punto più vicino al poligono, quindi li vedremo quasi tutti lungo il perimetro; se invece volessimo i punti dentro i relativi poligoni, per esempio lungo un cerchio, ecco altra espressione:

```
with_variable('geomPolygon', 
  geometry(
     get_feature('polygon',
                 'Parcel_No',
                  attribute( $currentfeature, 'Parcel_No' ))),
closest_point(buffer(centroid(
   @geomPolygon), bounds_height((@geomPolygon))/5),
   $geometry))
```

[![](https://i.stack.imgur.com/dQnQ7.png)](https://i.stack.imgur.com/dQnQ7.png)

l'espressione di sotto distribuisce casualmente i punti dentro ogni poligono, a partire dal centroide:

```
--> variabile
with_variable('geomPolygon', 
	geometry(
	get_feature('polygon',
			'Parcel_No',
			 attribute( $currentfeature, 'Parcel_No' ))),
--> variabile
project(
point:=
	closest_point(
	geometry1:=centroid(@geomPolygon), -- polygon
	geometry2:=$geometry), -- point
distance:=
	distance(
	closest_point(
	boundary(@geomPolygon),centroid(@geomPolygon)),
	centroid(@geomPolygon))*randf(0,1),
azimuth:=
	radians (rand(0,360))
	)
)
```

![](https://i.stack.imgur.com/lwruV.png)

- Maggiori dettagli nel [blog](https://pigrecoinfinito.com/2022/03/12/qgis-le-espressioni-come-una-calamita/) post su Pigrecoinfinito
- idea presa da [Stackexchange](https://gis.stackexchange.com/questions/425911/move-points-into-center-of-polygons-base-on-common-field-attributes-using-qgis)

Animazione:

[![](../img/esempi/calamita/calamita.gif)](../img/esempi/calamita/calamita.gif)

espressione utilizzata:

per tracciare le linee:

```
with_variable('geomPolygon', geometry(get_feature('polygon','Parcel_No',attribute( $currentfeature, 'Parcel_No' ))),
if(contains(@geomPolygon,@canvas_cursor_point)=1,
make_line(
$geometry,
closest_point(buffer(centroid(
@geomPolygon), bounds_height((@geomPolygon))/5),
$geometry))
,null))
```

per tracciare i punti:

```
with_variable('geomPolygon',
    geometry(get_feature('polygon','Parcel_No',attribute($currentfeature, 'Parcel_No'))),
      -- condizione
      if(contains(@geomPolygon,@canvas_cursor_point)=1,
        closest_point(buffer(centroid(
          @geomPolygon), bounds_height((@geomPolygon))/5),
          $geometry), null))
```

### prova tu

[dati e progetto QGIS 3.24](https://drive.google.com/file/d/1TG4i6qP9BcIkSZAr7lq8H7wKfhkta-8W/view?usp=sharing)

---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/variabili/with_variable.md)
* [get_feature](../gr_funzioni/record_e_attributi/record_e_attributi_unico.md/#get_feature)
* [closest_point](../gr_funzioni/geometria/geometria_unico.md#closest_point)
* [bounds_height](../gr_funzioni/geometria/geometria_unico.md#bounds_height)
* [centroid](../gr_funzioni/geometria/geometria_unico.md#centroid)
* [attribute](../gr_funzioni/record_e_attributi/record_e_attributi_unico,md/#attribute)
* [$currentfeature](../gr_funzioni/record_e_attributi/record_e_attributi_unico.md/#currentfeature)
