Arrays
======

solo DB (es:SpatiaLite, PostGIS)

Questo gruppo contiene funzioni espressione per la creazione e la
manipolazione di array (noti anche come strutture dati ad elenco).
L'ordine dei valori all'interno dell'array è importante, al contrario
della struttura dati 'a mappa' (`gruppo Maps`_), in cui l'ordine delle
coppie chiave-valore è irrilevante e i valori vengono identificati dalle
loro chiavi.

+------------------------+--------------------------+-----------------+
| Funzione               | Descrizione              | Plugin          |
+========================+==========================+=================+
| `array`_               | Restituisce un array     |                 |
|                        | contenente tutti i       |                 |
|                        | valori passati come      |                 |
|                        | parametro                |                 |
+------------------------+--------------------------+-----------------+
| `array_append`_        | Restituisce un array con |                 |
|                        | il valore passato        |                 |
|                        | aggiunto alla fine       |                 |
+------------------------+--------------------------+-----------------+
| `array_avg`_           | Calcola il valore medio  | ArrayPlus       |
|                        | di un array              |                 |
+------------------------+--------------------------+-----------------+
| `array_cat`_           | Restituisce un array     |                 |
|                        | contenente tutti gli     |                 |
|                        | arrays passati           |                 |
|                        | concatenati              |                 |
+------------------------+--------------------------+-----------------+
| `array_contains`_      | Restituisce true se un   |                 |
|                        | array contiene il valore |                 |
|                        | specificato              |                 |
+------------------------+--------------------------+-----------------+
| `array_count`_         | Conta un dato valore in  | ArrayPlus       |
|                        | un array                 |                 |
+------------------------+--------------------------+-----------------+
| `array_distinct`_      | Restituisce un array     |                 |
|                        | contenente valori        |                 |
|                        | distinti dell'array dato |                 |
+------------------------+--------------------------+-----------------+
| `array_find`_          | Restituisce l'indice di  |                 |
|                        | un valore all'interno di |                 |
|                        | un array                 |                 |
+------------------------+--------------------------+-----------------+
| `array_first`_         | Restituisce il primo     |                 |
|                        | valore di un array       |                 |
+------------------------+--------------------------+-----------------+
| `array_filter`_        | Restituisce un array con | >=QGIS 3.4      |
|                        | solo gli elementi per i  |                 |
|                        | quali l'espressione      |                 |
|                        | restituisce true (vero)  |                 |
+------------------------+--------------------------+-----------------+
| `array_foreach`_       | Restituisce un matrice   | >=QGIS 3.4      |
|                        | con l'espressione data   |                 |
|                        | valutata su ciscun campo |                 |
+------------------------+--------------------------+-----------------+
| `array_get`_           | Restituisce il valore    |                 |
|                        | ennesimo di un array     |                 |
+------------------------+--------------------------+-----------------+
| `array_insert`_        | Restituisce un array con |                 |
|                        | il valore passato        |                 |
|                        | aggiunto nella posizione |                 |
|                        | indicata                 |                 |
+------------------------+--------------------------+-----------------+
| `array_lambda`_        | Applica una funzione     | ArrayPlus       |
|                        | personalizzata a ciascun |                 |
|                        | elemento (x)             |                 |
+------------------------+--------------------------+-----------------+
| `array_intersect`_     | Restituisce vero se      |                 |
|                        | almeno un elemento       |                 |
|                        | dell'array1 esiste in    |                 |
|                        | array2                   |                 |
+------------------------+--------------------------+-----------------+
| `array_last`_          | Restituisce l'ultimo     |                 |
|                        | valore di un array       |                 |
+------------------------+--------------------------+-----------------+
| `array_length`_        | Restituisce il numero di |                 |
|                        | elementi di un array     |                 |
+------------------------+--------------------------+-----------------+
| `array_majority`_      | Restituisce il valore    | ArrayPlus       |
|                        | più comune. Restituisce  |                 |
|                        | un valore arbitrario se  |                 |
|                        | ex-equo                  |                 |
+------------------------+--------------------------+-----------------+
| `array_minority`_      | Restituisce il valore    | ArrayPlus       |
|                        | più comune. Restituisce  |                 |
|                        | un valore arbitrario se  |                 |
|                        | ex-equo                  |                 |
+------------------------+--------------------------+-----------------+
| `array_max`_           | Restituisce il valore    | ArrayPlus       |
|                        | massimo di un array      |                 |
+------------------------+--------------------------+-----------------+
| `array_min`_           | Restituisce il valore    | ArrayPlus       |
|                        | minimo di un array       |                 |
+------------------------+--------------------------+-----------------+
| `array_prepend`_       | Restituisce un array con |                 |
|                        | il valore dato aggiunto  |                 |
|                        | all'inizio               |                 |
+------------------------+--------------------------+-----------------+
| `array_prioritize`_    | Ordina un array rispetto | ArrayPlus       |
|                        | ad un altro QGIS >= 3.2  |                 |
+------------------------+--------------------------+-----------------+
| `array_remove_all`_    | Restituisce un array con |                 |
|                        | tutti gli elementi del   |                 |
|                        | valore passato rimossi   |                 |
+------------------------+--------------------------+-----------------+
| `array_remove_at`_     | Restituisce un array con |                 |
|                        | l'indice passato rimosso |                 |
+------------------------+--------------------------+-----------------+
| `array_replace`_       | Ordina i valori in       | ArrayPlus       |
|                        | ordine crescente (usa    |                 |
|                        | *array_reverse* per      |                 |
|                        | desc)                    |                 |
+------------------------+--------------------------+-----------------+
| `array_reverse`_       | Restituisce l'array dato |                 |
|                        | con valori dell'array in |                 |
|                        | ordine inverso           |                 |
+------------------------+--------------------------+-----------------+
| `array_slice`_         | Restituisce una porzione |                 |
|                        | dell'array               |                 |
+------------------------+--------------------------+-----------------+
| `array_sort`_          | Ordina i valori in       |    >= QGIS 3.4  |
|                        | ordine crescente (usa    |                 |
|                        | *array_reverse* per      |                 |
|                        | desc)                    |                 |
+------------------------+--------------------------+-----------------+
| `array_sum`_           | Calcola la somma dei     | ArrayPlus       |
|                        | valori                   |                 |
+------------------------+--------------------------+-----------------+
| `array_to_string`_     | Concatena gli elementi   |                 |
|                        | di un array in una       |                 |
|                        | stringa separata da un   |                 |
|                        | delimitatore usando una  |                 |
|                        | stringa opzionale per    |                 |
|                        | valori mancanti          |                 |
+------------------------+--------------------------+-----------------+
| `generate_series`_     | La funzione crea una     | >= QGIS 3.4     |
|                        | matrice contenete una    |                 |
|                        | sequenza di numeri       |                 |
+------------------------+--------------------------+-----------------+
| `regexp_matches`_      | Restituisce un array di  |                 |
|                        | tutte le stringhe        |                 |
|                        | catturate dai gruppo,    |                 |
|                        | nell'ordine che i gruppi |                 |
|                        | stessi compaiono con     |                 |
|                        | l'espressione regolare   |                 |
|                        | fornita con una stringa  |                 |
+------------------------+--------------------------+-----------------+
| `string_to_array`_     | Divide la stringa in un  |                 |
|                        | array usando il          |                 |
|                        | delimitatore fornito e   |                 |
|                        | la stringa opzionale per |                 |
|                        | valori mancanti          |                 |
+------------------------+--------------------------+-----------------+

|image0|


.. _gruppo Maps: ../maps
.. _array: array.html
.. _array_append: array_append.html
.. _array_avg: array_avg.html
.. _array_cat: array_cat.html
.. _array_contains: array_contains.html
.. _array_count: array_count.html
.. _array_distinct: array_distinct.html
.. _array_find: array_find.html
.. _array_first: array_first.html
.. _array_filter: array_filter.html
.. _array_foreach: array_foreach.html
.. _array_get: array_get.html
.. _array_insert: array_insert.html
.. _array_lambda: array_lambda.html
.. _array_intersect: array_intersect.html
.. _array_last: array_last.html
.. _array_length: array_length.html
.. _array_majority: array_majority.html
.. _array_minority: array_minority.html
.. _array_max: array_max.html
.. _array_min: array_min.html
.. _array_prepend: array_prepend.html
.. _array_prioritize: array_prioritize.html
.. _array_remove_all: array_remove_all.html
.. _array_remove_at: array_remove_at.html
.. _array_replace: array_replace.html
.. _array_reverse: array_reverse.html
.. _array_slice: array_slice.html
.. _array_sort: array_sort.html
.. _array_sum: array_sum.html
.. _array_to_string: array_to_string.html
.. _generate_series: generate_series.html
.. _regexp_matches: regexp_matches.html
.. _string_to_array: string_to_array.html

.. |image0| image:: /img/arrays/gruppo_arrays1.png


**Elenco funzioni Arrays**

.. toctree::
   :maxdepth: 3
   
   array
   array_append
   array_avg
   array_cat
   array_contains
   array_count
   array_distinct
   array_find
   array_first
   array_filter
   array_foreach
   array_get
   array_insert
   array_intersect
   array_lambda
   array_last
   array_length
   array_majority
   array_max
   array_min
   array_minority
   array_prepend
   array_prioritize
   array_remove_all
   array_remove_at
   array_replace
   array_reverse
   array_slice
   array_sort
   array_sum
   array_to_string
   generate_series
   regexp_matches
   string_to_array
   array_first
