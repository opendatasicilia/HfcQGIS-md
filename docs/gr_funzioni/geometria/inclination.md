# inclination

Restituisce l'inclinazione misurata dallo zenit (0) al nadir (180) del _punto_a_ al _punto_b_.

## Sintassi

- inclination(_<span style="color:red;">point_a</span>_, _<span style="color:red;">point_b</span>_)

## Argomenti

* _<span style="color:red;">point_a</span>_ geometria punto
* _<span style="color:red;">point_b</span>_ geometria punto

## Esempi

* `inclination( make_point( 5, 10, 0 ), make_point( 5, 10, 5 ) ) → 0.0`
* `inclination( make_point( 5, 10, 0 ), make_point( 5, 10, 0 ) ) → 90.0`
* `inclination( make_point( 5, 10, 0 ), make_point( 50, 100, 0 ) ) → 90.0`
* `inclination( make_point( 5, 10, 0 ), make_point( 5, 10, -5 ) ) → 180.0`

![](../../img/geometria/inclination/inclination1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/inclination/inclination2.png)