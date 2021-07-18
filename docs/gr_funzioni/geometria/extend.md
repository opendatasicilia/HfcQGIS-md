# extend

Estende l'inizio e la fine di una geometria di tipo linestring di una quantità specificata. Le linee sono estese usando la direzione di immersione del primo e dell'ultimo segmento nella linea. Le distanze sono espresse nel SR di tale geometria.

## Sintassi

- extend(_<span style="color:red;">geometry</span>_, _<span style="color:red;">start_distance</span>_, _<span style="color:red;">end_distance</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria (multi)linestring
* _<span style="color:red;">start_distance</span>_ distanza alla quale estendere l'_inizio_ della linea
* _<span style="color:red;">end_distance</span>_ distanza alla quale estendere la _fine_ della linea.


## Esempi

```
* geom_to_wkt(extend(geom_from_wkt('LineString(0 0, 1 0, 1 1)'),1,2)) → 'LineString (-1 0, 1 0, 1 3)'
* geom_to_wkt(extend(geom_from_wkt('MultiLineString((0 0, 1 0, 1 1), (2 2, 0 2, 0 5))'),1,2)) → 'MultiLineString ((-1 0, 1 0, 1 3),(3 2, 0 2, 0 7))'
```

![](../../img/geometria/extend/extend1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/extend/extend1.png)