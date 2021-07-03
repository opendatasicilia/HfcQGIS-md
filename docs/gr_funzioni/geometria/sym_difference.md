# sym_difference

Restituisce una geometria che rappresenta la porzione di due geometrie che non si interseca.

## Sintassi

sym_difference(_geometry1, geometry2_)

## Argomenti

* _geometry1_ una geometria
* _geometry2_ una geometria

## Esempi

* `geom_to_wkt( sym_difference( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'LINESTRING(3 3, 8 8)' ) ) ) → LINESTRING(5 5, 8 8)`

![](../../img/geometria/sym_difference/sym_difference1.png)

![](../../img/geometria/sym_difference/sym_difference3.png)

Espressione:

```
-- differenza simmetrica tra le due linee
sym_difference( 
make_line(  -- linea a
	start_point(geometry(get_feature_by_id('linea_a',0))), 
	start_point($geometry),
	end_point(geometry(get_feature_by_id('linea_a',0)))),
make_line(  -- linea b
	start_point($geometry), 
	end_point(geometry(get_feature_by_id('linea_a',0))),
	end_point($geometry))
				)
-- NB: -- l' ordine delle geometrie è indifferente
```

## prova tu

[Dati e progetto qgz](https://github.com/gbvitrano/HfcQGIS/raw/master/prova_tu/DIFFERENCE.zip)

## nota bene

--

## osservazioni

--

![](../../img/geometria/sym_difference/sym_difference2.png)
