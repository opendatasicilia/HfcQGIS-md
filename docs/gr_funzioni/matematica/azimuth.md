# azimuth

Restituisce l'azimut dal nord quale angolo in radianti misurato in senso orario dalla verticale del punto_a al punto_b.

## Sintassi

azimuth(_<span style="color:red;">point_a</span>, <span style="color:red;">point_b</span>_)

## Argomenti

* _<span style="color:red;">point_a</span>_ geometria punto
* _<span style="color:red;">point_b</span>_ geometria punto

## Esempi

* `degrees( azimuth( make_point(25, 45), make_point(75, 100) ) ) → 42.273689`
* `degrees( azimuth( make_point(75, 100), make_point(25,45) ) ) → 222.273689`

![](/img/matematica/azimuth/azimuth1.png)

## nota bene

--

## osservazioni

--

vedasi nel gruppo funzioni Geometria [Azimuth](../../gr_funzioni/geometria/azimuth.html)
