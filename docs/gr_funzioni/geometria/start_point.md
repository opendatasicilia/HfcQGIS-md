# start_point

Restituisce il primo nodo di una geometria.

## Sintassi

- start_point( _<span style="color:red;">geometry</span>_)

## Argomenti

*  _<span style="color:red;">geometry</span>_ oggetto geometria

## Esempi

* `geom_to_wkt(start_point(geom_from_wkt('LINESTRING(4 0, 4 2, 0 2)'))) → 'Point (4 0)'`

![](../../img/geometria/start_point/start_point1.png)

## nota bene

--

## osservazioni _<span style="color:red;">geometry</span>_

--
Start_point di geometria poligonale:

![](../../img/geometria/start_point/start_point2.png)

Start_point di geometria lineare:

![](../../img/geometria/end_point/end_point3.png)