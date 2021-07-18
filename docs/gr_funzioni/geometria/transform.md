# transform

Restituisce la geometria trasformata da un SR sorgente ad un SR di destinazione.

## Sintassi

- transform( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">source_auth_id</span>_,  _<span style="color:red;">dest_auth_id</span>_)

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">source_auth_id</span>_ ID del SR sorgente
*  _<span style="color:red;">dest_auth_id</span>_ ID del SR destinazione

## Esempi

* `geom_to_wkt( transform( $geometry, 'EPSG:2154', 'EPSG:4326' ) ) → POINT(0 51)`

![](../../img/geometria/transform/transform1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/transform/transform2.png)