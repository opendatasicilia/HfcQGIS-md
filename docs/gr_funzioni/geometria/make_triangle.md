# make_triangle

Crea un poligono triangolare

## Sintassi

- make_triangle(_<span style="color:red;">point1</span>_,_<span style="color:red;">point2</span>_,_<span style="color:red;">point3</span>_)

## Argomenti

- _<span style="color:red;">point1</span>_ Primo punto del triangolo
- _<span style="color:red;">point2</span>_ Secondo punto del triangolo
- _<span style="color:red;">point3</span>_ Secondo punto del triangolo
- 
## Esempi

* `geom_to_wkt(make_triangle(make_point(0,0), make_point(5,5), make_point(0,10))) → 'Triangle ((0 0, 5 5, 0 10, 0 0))'`
* `geom_to_wkt(boundary(make_triangle(make_point(0,0), make_point(5,5), make_point(0,10)))) → 'LineString (0 0, 5 5, 0 10, 0 0)'`

![](../../img/geometria/make_triangle/make_triangle1.png)

## nota bene

--

## osservazioni

--