# line_interpolate_angle

Restituisce l'angolo parallelo alla geometria ad una distanza specifica lungo una geometria di tipo linestring. Gli angoli sono in gradi in senso orario dal nord.

## Sintassi

- line_interpolate_angle(_<span style="color:red;">geometry</span>_, _<span style="color:red;">distance</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">distance</span>_ distanza lungo la linea a cui interpolare l'angolo

## Esempi

* `line_interpolate_angle(geometry:=geom_from_wkt('LineString(0 0, 10 0)'),distance:=5) → 90.0`

![](../../img/geometria/line_interpolate_angle/line_interpolate_angle1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/line_interpolate_angle/line_interpolate_angle2.png)