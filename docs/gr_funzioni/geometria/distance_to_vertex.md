# distance_to_vertex

Restituisce la distanza lungo una geometria ad un vertice specificato.

## Sintassi

- distance_to_vertex(_<span style="color:red;">geometry</span>_, _<span style="color:red;">vertex</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">vertex</span>_ indice vertice, partendo da 0; se il valore è negativo, l'indice del vertice selezionato sarà il suo conteggio totale meno il valore assoluto


## Esempi

* `distance_to_vertex(geometry:=geom_from_wkt('LineString(0 0, 10 0, 10 10)'),vertex:=1) → 10.0`

![](../../img/geometria/distance_to_vertex/distance_to_vertex1.png)

## nota bene

--

## osservazioni

--

esempio di sopra:

![](../../img/geometria/distance_to_vertex/distance_to_vertex3.png)