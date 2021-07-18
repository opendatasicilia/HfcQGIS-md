# overlay_touches

Restituisce se l'elemento corrente tocca spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target toccati dall'elemento corrente.

Leggi ulteriori informazioni sul predicato GEOS "Touches", come descritto nella funzione PostGIS [ST_TOUCHES](https://postgis.net/docs/ST_Touches.html).

## Sintassi

- overlay_touches(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_]_)

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

## Esempi

```
* overlay_touches('regions') → true se l'elemento corrente tocca spazialmente una regione
* overlay_touches('regions', filter:= population > 10000) → vero se l'elemento corrente tocca spazialmente una regione con una popolazione maggiore di 10000
* overlay_touches('regions', name) → un array di nomi, per le regioni tocacte dall'elemento corrente
* string_to_array(overlay_touches('regions', name)) → una stringa come lista di nomi separati da virgole, per le regioni toccate dall'elemento corrente
* overlay_touches('regions', name)[0] → una stringa con il nome della regione toccata dall'elemento corrente
* array_sort(overlay_touches(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni toccate dall'elemento attuale e con una popolazione superiore a 10000
* overlay_touches(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni toccate dall'elemento corrente
```


![](../../img/geometria/refFunction/overlay_touches.png)

## nota bene

--

## osservazioni

--
