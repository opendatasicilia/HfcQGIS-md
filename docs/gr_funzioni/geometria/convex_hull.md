# convex_hull

Restituisce il poligono convesso di una geometria. Rappresenta la minima geometria convessa che racchiude tutte le geometria contenute nell'insieme.

## Sintassi

- convex_hull(_<span style="color:red;">geometry</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria

## Esempi

* `geom_to_wkt( convex_hull( geom_from_wkt( 'LINESTRING(3 3, 4 4, 4 10)' ) ) ) → POLYGON((3 3,4 10,4 4,3 3))`

![](../../img/geometria/convex_hull/convex_hull1.png)

## nota bene

--

## Osservazioni

La funzione restituisce sempre un poligono.

![](../../img/geometria/convex_hull/convex_hull2.png)
