# angle_at_vertex

Restituisce l'angolo della bisettrice (angolo medio) della geometria per un vertice specifico di una geometria di tipo linestring. Gli angoli sono in gradi in senso orario dal nord.

## Sintassi

angle_at_vertex(_<span style="color:red;">geometry</span>, <span style="color:red;">vertex</span>_)

## Argomento

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">vertex</span>_ indice vertice, partendo da 0

## Esempi

* `angle_at_vertex(geometry:=geom_from_wkt('LineString(0 0, 10 0, 10 10)'),vertex:=1) → 45.0`

![](../../img/geometria/angle_at_vertex/angle_at_vertex1.png)

## nota bene

Il primo ed ultimo vertice di una lineastring aperta la funzione restituisce il valore dell'angolo e non la bisettrice.

## osservazioni
--

![](../../img/geometria/angle_at_vertex/angle_at_vertex2.png)
