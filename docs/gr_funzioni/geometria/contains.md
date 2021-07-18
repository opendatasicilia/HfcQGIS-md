# contains

Verifica se una geometria ne contiene un'altra. Restituisce vero se e solo se nessun punto di geometry2 giace all'esterno di geometry1 e almeno un punto dell'interno di geometry2 si trova all'interno di geometry1.

## Sintassi

- contains(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

## Argomenti

* _<span style="color:red;">geometry1</span>_  una geometria
* _<span style="color:red;">geometry2</span>_  una geometria

## Esempi


* `contains( geom_from_wkt( 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))' ), geom_from_wkt( 'POINT(0.5 0.5 )' ) ) → vero`
* `contains( geom_from_wkt( 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → falso`


![](../../img/geometria/contains/contains1.png)

## nota bene

--

## osservazioni

Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (ctrl+F3):

espressione usata:

`contains(geometry(get_feature( 'province_rt_rt','pk_uid','46')),$geometry)`

dove:

* _geometry a_ è `geometry(get_feature( 'province_rt_rt','pk_uid','46'))`
* _geometry b_ è `$geometry`


![](../../img/geometria/contains/contains2.png)

seleziono tutti i comuni `contains` (contenuti) nella provincia con `pk_uid`46 (Lucca)

**PS:** potrei anche negare (`NOT`) l'espressione per selezionare il complementare (tutti i comuni tranne quelli contenuti nella provincia di Lucca).

`NOT contains(geometry(get_feature( 'province_rt_rt','pk_uid','46')),$geometry)`
