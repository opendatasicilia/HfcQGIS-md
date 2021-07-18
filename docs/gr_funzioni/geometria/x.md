# x

Restituisce la minima coordinata x di una geometria punto, o la coordinata x del centroide di una geometria non puntuale.

## Sintassi

- x( _<span style="color:red;">geometry</span>_)

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria

## Esempi

* `x( geom_from_wkt( 'POINT(2 5)' ) ) → 2`
* `x( $geometry ) → coordinata x del centroide dell'elemento corrente`

![](../../img/geometria/x/x1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/x/x2.png)