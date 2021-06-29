# Inclination

Restituisce l'inclinazione misurata dallo zenit (0) al nadir (180) del punto_a al punto_b.

## Sintassi

inclination(_<span style="color:red;">point_a</span>, <span style="color:red;">point_b</span>_)

## Argomenti

* _<span style="color:red;">point_a</span>_ geometria punto
* _<span style="color:red;">point_b</span>_ geometria punto

## Esempi

* `inclination( make_point( 5, 10, 0 ), make_point( 5, 10, 5 ) ) → 0.0`
* `inclination( make_point( 5, 10, 0 ), make_point( 5, 10, 0 ) ) → 90.0`
* `inclination( make_point( 5, 10, 0 ), make_point( 50, 100, 0 ) ) → 90.0`
* `inclination( make_point( 5, 10, 0 ), make_point( 5, 10, -5 ) ) → 180.0`

![](/img/matematica/Inclination/Inclination1.png)

## nota bene

--

## osservazioni

--

vedasi nel gruppo funzioni Geometria [Inclination](../geometria/inclination.html)
