# simplify

Semplifica una geometria rimuovendo nodi usando una soglia basata sulla distanza (cioè, l'algoritmo Douglas Peucker). L'algoritmo mantiene grandi deviazioni nelle geometrie e riduce il numero di vertici in segmenti quasi rettilinei.

## Sintassi

- simplify(simplify_vw(_<span style="color:red;">geometry</span>, <span style="color:red;">tolerance</span>_)

## Argomenti

* _<span style="color:red;">geometry</span> una geometria
* _<span style="color:red;">tolerance</span> deviazione massima dai segmenti rettilinei per i punti da rimuovere

## Esempi

* `geom_to_wkt(simplify(geometry:=geom_from_wkt('LineString(0 0, 5 0.1, 10 0)'),tolerance:=5)) → 'LineString(0 0, 10 0)'`

![](../../img/geometria/simplify/simplify1.png)

## nota bene

--

## osservazioni

--