# combine

Restituisce la combinazione di due geometrie.

## Sintassi

combine(_<span style="color:red;">geometry1</span>, <span style="color:red;">geometry2</span>_)

## Argomenti

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria


## Esempi


* `geom_to_wkt( combine( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 2 1)' ) ) ) → MULTILINESTRING((4 4, 2 1), (3 3, 4 4), (4 4, 5 5))`
* `geom_to_wkt( combine( geom_from_wkt( 'LINESTRING(3 3, 4 4)' ), geom_from_wkt( 'LINESTRING(3 3, 6 6, 2 1)' ) ) ) → LINESTRING(3 3, 4 4, 6 6, 2 1)`

![](/img/geometria/combine/combine1.png)

## nota bene

--

## osservazioni

--
