# is_empty_or_null

Restituisce vero se una geometria è vuota (senza coordinate), falso se la geometria non è vuota e NULL se non c'è geometria. Vedi anche `is_empty_or_null_or_null`.

## Sintassi

is_empty_or_null(<span style="color:red;">_geometry_</span>)

## Argomenti

* <span style="color:red;">_geometry_</span> una geometria

## Esempi

* `is_empty_or_null(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2)')) → falso`
* `is_empty_or_null(geom_from_wkt('LINESTRING EMPTY')) → vero`
* `is_empty_or_null(geom_from_wkt('POINT(7 4)')) → falso`
* `is_empty_or_null(geom_from_wkt('POINT EMPTY')) → vero`

![](/img/geometria/is_empty_or_null/is_empty_or_null1.png)

## nota bene

--

## osservazioni

![screen](/img/novita_312/Image02.png)
