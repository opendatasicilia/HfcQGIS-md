# closest_point

Restituisce il punto sulla geometria1 che è più vicino alla geometria2.

## Sintassi

closest_point(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

## Argomenti

* _<span style="color:red;">geometry1</span>_ geometria _sulla_ quale cercare il punto più vicino
* _<span style="color:red;">geometry</span>_ geometria _dalla_ quale cercare il punto più vicino

## Esempi

* `geom_to_wkt(closest_point(geom_from_wkt('LINESTRING (20 80, 98 190, 110 180, 50 75 )'),geom_from_wkt('POINT(100 100)'))) → Point(73.0769 115.384)`

![](../../img/geometria/closest_point/closest_point1.png)

![](../../img/geometria/closest_point/closest_point2.png)

## nota bene

--

## osservazioni

Utilizzando il _geometry generator_ per i temi (il layer strade è una unica feature):

* `closest_point( geometry(get_feature('strade', 'reg',19)),$geometry)`

![](../../img/geometria/closest_point/closest_point3.png)

Gif animata: _geometry 1_ è la rete stradale; _geometry 2_ sono i punti; in rosso i closestpoint

![](../../img/geometria/closest_point/closestpoint.png)
