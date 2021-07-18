# make_square

Crea un quadrato da una diagonale.

## Sintassi

- make_square(_<span style="color:red;">point1</span>_,_<span style="color:red;">point2</span>_)

## Argomenti

- _<span style="color:red;">point1</span>_ Primo punto della diagonale
- _<span style="color:red;">point2</span>_ Secondo punto della diagonale

## Esempi

* `geom_to_wkt(make_square( make_point(0,0), make_point(5,5))) → 'Polygon ((0 0, -0 5, 5 5, 5 0, 0 0))'`
* `geom_to_wkt(make_square( make_point(5,0), make_point(5,5))) → 'Polygon ((5 0, 2.5 2.5, 5 5, 7.5 2.5, 5 0))'`

![](../../img/geometria/make_square/make_square1.png)

## nota bene

--

## osservazioni

--
