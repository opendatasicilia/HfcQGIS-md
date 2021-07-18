# line_interpolate_point

Restituisce il punto interpolato ad una specifica distanza lungo una geometria di tipo linestring.

## Sintassi

- line_interpolate_point(_<span style="color:red;">geometry</span>_, _<span style="color:red;">distance</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">distance</span>_ distanza lungo la linea

## Esempi

* `geom_to_wkt(line_interpolate_point(geometry:=geom_from_wkt('LineString(0 0, 10 0)'),distance:=5)) → 'Point (4 0)'`

![](../../img/geometria/line_interpolate_point/line_interpolate_point1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/line_interpolate_point/line_interpolate_point2.png)