# z_min

Restituisce la coordinata z minima di una geometria.

## Sintassi

* z_min( _<span style="color:red;">geometry</span>_)

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria con z coordinata

## Esempi

```
* z_min( geom_from_wkt( 'POINT ( 0 0 1 )' ) ) → 1
* z_min( geom_from_wkt( 'MULTIPOINT ( 0 0 1 , 1 1 3 )' ) ) → 1
* z_min( make_line( make_point( 0,0,0 ), make_point( -1,-1,-2 ) ) ) → -2
* z_min( geom_from_wkt( 'LINESTRING( 0 0 0, 1 0 2, 1 1 -1 )' ) ) → -1
* z_min( geom_from_wkt( 'POINT ( 0 0 )' ) ) → NULL
```

![](../../img/geometria/z_min/z_min1.png)

## nota bene

--

## osservazioni

--
