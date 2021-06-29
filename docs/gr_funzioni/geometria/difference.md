# difference

Restituisce una geometria che rappresenta la porzione della _geometry_a_ che non interseca la _geometry_b_.

## Sintassi

difference(_<span style="color:red;">geometry_a</span>, <span style="color:red;">geometry_b</span>_)

## Argomenti

* _<span style="color:red;">geometry_a</span>_ una geometria
* _<span style="color:red;">geometry_b</span>_ una geometria

## Esempi

* `geom_to_wkt( difference( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4)' ) ) ) → LINESTRING(4 4, 5 5)`

![](/img/geometria/difference/difference1.png)

![](/img/geometria/difference/difference31.png)

Espressione:

```
-- differenza linea a - linea b
difference( 
make_line(  -- linea a
	start_point(geometry(get_feature_by_id('linea_a',0))), 
	start_point($geometry),
	end_point(geometry(get_feature_by_id('linea_a',0)))),
make_line(  -- linea b
	start_point($geometry), 
	end_point(geometry(get_feature_by_id('linea_a',0))),
	end_point($geometry))
				)
-- NB: -- è importante ordine delle geometrie
-- a - b è diverso da b - a
```

![](/img/geometria/difference/difference32.png)

```
-- differenza linea b - linea a
difference( 
make_line( -- linea b
	start_point($geometry), 
	end_point(geometry(get_feature_by_id('linea_a',0))),
	end_point($geometry)),
make_line(  -- linea a
	start_point(geometry(get_feature_by_id('linea_a',0))), 
	start_point($geometry),
	end_point(geometry(get_feature_by_id('linea_a',0))))
				)
-- NB: -- è importante ordine delle geometrie
-- a - b è diverso da b - a
```

## prova tu

[Dati e progetto qgz](https://github.com/gbvitrano/HfcQGIS/raw/master/prova_tu/DIFFERENCE.zip)

## nota bene

--

## osservazioni

--

Esempio di sopra:

![](/img/geometria/difference/difference2.png)
