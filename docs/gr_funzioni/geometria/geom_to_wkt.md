# geom_to_wkt

Restituisce la rappresentazione Well-Known Text (WKT) della geometria senza metadati del SR

## Sintassi

- geom_to_wkt(_<span style="color:red;">geometry</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria

## Esempi

```
* geom_to_wkt( make_point(6, 50) ) → 'POINT(6 50)'
* geom_to_wkt(centroid(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))'))) → 'POINT(0 0.66666667)'
* geom_to_wkt(centroid(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))')), 2) → 'POINT(0 0.67)'
```

![](../../img/geometria/geom_to_wkt/geom_to_wkt1.png)

## nota bene

--

## osservazioni

--