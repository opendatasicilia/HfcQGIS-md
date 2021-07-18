# make_circle

Crea un poligono circolare.

## Sintassi

- make_circle(_<span style="color:red;">center</span>_, _<span style="color:red;">radius</span>_[, _<span style="color:red;">segments=36</span>_])

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">center</span>_ centro del cerchio
* _<span style="color:red;">radius</span>_ raggio del cerchio
* _<span style="color:red;">segments</span>_ argomento opzionale per la segmentazione del poligono. Valore predefinito pari a 36

## Esempi

* `geom_to_wkt(make_circle(make_point(10,10), 5, 4)) → 'Polygon ((10 15, 15 10, 10 5, 5 10, 10 15))'`
* `geom_to_wkt(make_circle(make_point(10,10,5), 5, 4)) → 'PolygonZ ((10 15 5, 15 10 5, 10 5 5, 5 10 5, 10 15 5))''`
* `geom_to_wkt(make_circle(make_point(10,10,5,30), 5, 4)) → 'PolygonZM ((10 15 5 30, 15 10 5 30, 10 5 5 30, 5 10 5 30, 10 15 5 30))'`

![](../../img/geometria/make_circle/make_circle1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/make_circle/make_circle2.png)