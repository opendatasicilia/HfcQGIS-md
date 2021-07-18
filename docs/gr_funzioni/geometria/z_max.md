# z_max

Restituisce la coordinata z massima di una geometria.

## Sintassi

* z_max( _<span style="color:red;">geometry</span>_)

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria con z coordinata

## Esempi

```
* z_max( geom_from_wkt( 'POINT ( 0 0 1 )' ) ) → 1
* z_max( geom_from_wkt( 'MULTIPOINT ( 0 0 1 , 1 1 3 )' ) ) → 3
* z_max( make_line( make_point( 0,0,0 ), make_point( -1,-1,-2 ) ) ) → 0
* z_max( geom_from_wkt( 'LINESTRING( 0 0 0, 1 0 2, 1 1 -1 )' ) ) → 2
* z_max( geom_from_wkt( 'POINT ( 0 0 )' ) ) → NULL
```

![](../../img/geometria/z_max/z_max1.png)

## nota bene

--

## osservazioni

--
