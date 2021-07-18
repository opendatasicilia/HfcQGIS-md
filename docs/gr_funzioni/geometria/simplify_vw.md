# simplify_vw

Semplifica una geometria rimuovendo nodi usando una soglia basata sull'area (cioè, l'algoritmo Visvalingam-Whyatt ). L'algoritmo rimuove i vertici che creano piccole aree nelle geometrie, ad esempio picchi stretti o segmenti quasi rettilinei.

## Sintassi

- simplify_vw(_<span style="color:red;">geometry</span>, <span style="color:red;">tolerance</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">tolerance</span>_ una misura dell'area massima creata da un nodo per il nodo da rimuovere

## Esempi

* `geom_from_wkt('LineString(0 0, 5 0, 5.01 10, 5.02 0, 10 0)'),tolerance:=5)) → 'LineString(0 0, 10 0)'`

![](../../img/geometria/simplify_vw/simplify_vw1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/simplify_vw/simplify_vw2.png)
