---
tags:
  - vicinanza
  - linee
  - overlay
---

# Calcolo distanza minima tra due vettori

Dati due layer (es_uno puntuale e l'altro lineare), calcolare la lunghezza del segmento di minima distanza tra gli elementi dei due layer usando il calcolatore di campi:

Carico i due layer: `alberi` e `fiumi`

[![](../img/esempi/linea_min_distanza2/img_01.png)](../img/esempi/linea_min_distanza2/img_01.png)

Traccio la linea di minima distanza solo per visualizzarla a schermo tramite il generatore di geometrie, usando l'espressione:

[![](../img/esempi/linea_min_distanza2/img_02.png)](../img/esempi/linea_min_distanza2/img_02.png)

```
shortest_line(
	$geometry,
 	overlay_nearest( 
 	layer:='fiumi',
 	expression:=$geometry)[0]
	     )
```

per calcolare la lunghezza e aggiungerla come campo nella tabella attributi del layer `alberi`:

1. aprire tabella attributi;
2. aprire field calc;
3. aggiungere un nuovo campo numerico;
4. popolarlo con l'espressione:

```
length(
shortest_line(
	$geometry,
 	overlay_nearest( 
 	layer:='fiumi',
 	expression:=$geometry)[0]
	     )
       )
```

Osservazione: la funzione `overlay_nearest` è presente in QGIS a partire dalla 3.16 Hannover

---

Funzioni e variabili utilizzate:

* [aggregate](../gr_funzioni/aggrega/aggrega_unico.md#aggregate)
* [shortest_line](../gr_funzioni/geometria/geometria_unico.md#shortest_line)
* [overlay_nearest](../gr_funzioni/geometria/geometria_unico.md#overlay_nearest)
* [\$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)