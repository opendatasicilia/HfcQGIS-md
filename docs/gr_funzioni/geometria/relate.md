# relate

Testa la rappresentazione Dimensional Extended 9 Intersection [Model (DE-9IM)](https://en.wikipedia.org/wiki/DE-9IM) della relazione tra due geometrie.

## Variabile di relazione

Restituisce la rappresentazione Dimensional Extended 9 Intersection Model (DE-9IM) della relazione tra due geometrie.

## Sintassi

* relate(_<span style="color:red;">geometry</span>_, _<span style="color:red;">geometry</span>_, geometry_)
)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">geometry</span>_ una geometria

## Esempi

* `relate( geom_from_wkt( 'LINESTRING(40 40,120 120)' ), geom_from_wkt( 'LINESTRING(40 40,60 120)' ) ) → 'FF1F00102'`

![](../../img/geometria/relate/relate1.png)

## Variabile di corrispondenza del modello

Testa se la relazione DE-9IM tra due geometrie corrisponde a un pattern specificato: restituisc true Vero, false Falso.

## Sintassi

- relate( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">geometry</span>_,  _<span style="color:red;">pattern</span>_)

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">pattern</span>_ Tratteggio DE-9IM da far corrispondere

## Esempio

* `relate( geom_from_wkt( 'LINESTRING(40 40,120 120)' ), geom_from_wkt( 'LINESTRING(40 40,60 120)' ), '**1F001**' ) → Vero`

## nota bene

--

## osservazioni

--

![](../../img/geometria/relate/relate1.png)

## Link utili

* [Wikipedia](https://en.wikipedia.org/wiki/DE-9IM)
* [OpenGeo](https://connect.boundlessgeo.com/docs/suite/4.6/dataadmin/pgAdvanced/de9im.html)
