# minimal_circle

Restituisce la circonferenza circoscritta minima di una geometria. Rappresenta il cerchio minimo che circoscrive tutte le geometrie presenti in un dataset.

## Sintassi

- minimal_circle(_<span style="color:red;">geometry</span>_[, _<span style="color:red;">segments=36</span>_])

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">segments</span>_ argomento opzionale per la segmentazione del poligono. Valore predefinito pari a 36

## Esempi

* `geom_to_wkt( minimal_circle( geom_from_wkt( 'LINESTRING(0 5, 0 -5, 2 1)' ), 4 ) ) → Polygon ((0 5, 5 -0, -0 -5, -5 0, 0 5))`
* `geom_to_wkt( minimal_circle( geom_from_wkt( 'MULTIPOINT(1 2, 3 4, 3 2)' ), 4 ) ) → Polygon ((3 4, 3 2, 1 2, 1 4, 3 4))`

![](../../img/geometria/minimal_circle/minimal_circle1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/minimal_circle/minimal_circle2.png)