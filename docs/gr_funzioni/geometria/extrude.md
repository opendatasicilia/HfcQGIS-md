# extrude

Restituisce una versione estrusa della geometria (Multi-)Curve o (Multi-)Linestring in ingresso, con un'estensione specificata da x e y.

## Sintassi

- extrude(_<span style="color:red;">geometry</span>_,_<span style="color:red;">x</span>_, _<span style="color:red;">y</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria poligono
* _<span style="color:red;">x</span>_ estensione x, valore numerico
* _<span style="color:red;">y</span>_ estensione y, valore numerico


## Esempi

* `extrude(geom_from_wkt('LineString(1 2, 3 2, 4 3)'), 1, 2) → Polygon ((1 2, 3 2, 4 3, 5 5, 4 4, 2 4, 1 2))`
* `extrude(geom_from_wkt('MultiLineString((1 2, 3 2), (4 3, 8 3)'), 1, 2) → MultiPolygon (((1 2, 3 2, 4 4, 2 4, 1 2)),((4 3, 8 3, 9 5, 5 5, 4 3)))`

![](../../img/geometria/extrude/extrude1.png)

## nota bene

--

## osservazioni

Nell'esempio ho utilizzato la funzione [boundary()](boundary.md) perché la geometria di ingresso deve essere lineare.

![](../../img/geometria/extrude/extrude1.png)