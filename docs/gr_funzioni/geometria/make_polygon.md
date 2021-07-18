# make_polygon

Crea una geometria poligono da un'anello esterno e opzionalmente da geometrie ad anello interne.

## Sintassi

- make_polygon(_<span style="color:red;">outerRing</span>_[, _<span style="color:red;">innerRing1</span>_][, _<span style="color:red;">innerRing2</span>_] …_)

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">outerRing</span>_ geometria a linea chiusa per l'anello esterno del poligono
* _<span style="color:red;">innerRing</span>_ geometria a linea chiusa opzionale per anello interno

## Esempi
* `geom_to_wkt(make_polygon(geom_from_wkt('LINESTRING( 0 0, 0 1, 1 1, 1 0, 0 0 )'))) → 'Polygon ((0 0, 0 1, 1 1, 1 0, 0 0))'`
* `geom_to_wkt(make_polygon(geom_from_wkt('LINESTRING( 0 0, 0 1, 1 1, 1 0, 0 0 )'),geom_from_wkt('LINESTRING( 0.1 0.1, 0.1 0.2, 0.2 0.2, 0.2 0.1, 0.1 0.1 )'),geom_from_wkt('LINESTRING( 0.8 0.8, 0.8 0.9, 0.9 0.9, 0.9 0.8, 0.8 0.8 )'))) → 'Polygon ((0 0, 0 1, 1 1, 1 0, 0 0),(0.1 0.1, 0.1 0.2, 0.2 0.2, 0.2 0.1, 0.1 0.1),(0.8 0.8, 0.8 0.9, 0.9 0.9, 0.9 0.8, 0.8 0.8))'`

![](../../img/geometria/make_polygon/make_polygon1.png)

## nota bene

--

## osservazioni

--