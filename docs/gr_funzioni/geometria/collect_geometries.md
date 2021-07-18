# collect_geometries

Raccoglie un set di geometrie in un oggetto geometria multiparte.

## Variante geometry

## Sintassi

- collect_geometries(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>_...)

## Argomenti

* _<span style="color:red;">geometry</span>_ geometria sulla quale cercare il punto più vicino

## Esempi

* `geom_to_wkt(collect_geometries(make_point(1,2), make_point(3,4), make_point(5,6))) → 'MultiPoint ((1 2),(3 4),(5 6))'`

![](../../img/geometria/collect_geometries/collect_geometries2.png)

## Variante con array

## Sintassi

- collect_geometries(_<span style="color:red;">array</span>_)

## Argomenti

* _<span style="color:red;">array</span>_ array con oggetti geometrici


## Esempi

* `geom_to_wkt(collect_geometries(array(make_point(1,2), make_point(3,4), make_point(5,6)))) → 'MultiPoint ((1 2),(3 4),(5 6))'`

![](../../img/geometria/collect_geometries/collect_geometries1.png)

## nota bene

--

## osservazioni

![screen](https://user-images.githubusercontent.com/1829991/63907352-6ca4ff80-ca5e-11e9-9b18-82a1618e1eba.png)
