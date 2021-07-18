# point_n

Restituisce un nodo specifico da una geometria.

## Sintassi

- point_n(_<span style="color:red;">geometry</span>_, _<span style="color:red;">index</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ oggetto geometria
* _<span style="color:red;">index</span>_ indice del nodo da restituire, dove 1 è il primo nodo; se il valore è negativo, l'indice del vertice selezionato sarà il suo conteggio totale meno il valore assoluto

## Esempi

* `geom_to_wkt(point_n(geom_from_wkt('POLYGON((0 0, 4 0, 4 2, 0 2, 0 0))'),2)) → 'Point (4 0)'`


![](../../img/geometria/point_n/point_n1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/point_n/point_n2.png)

---

## Esempi correlati

[esempio nro 4](/esempi/add_col_z.md) - Come aggiungere la quota Z alla tabella attributi
