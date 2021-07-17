Aggregates
===========

Contiene funzioni che aggregano valori nei livelli e campi. A partire da
**QGIS 2.16** il motore di espressioni supporta l'uso di `parametri con
nome`_.

+---------------------------------+------------------------------------+
| Funzione                        | Descrizione                        |
+=================================+====================================+
| `aggregate`_                    | Restituisce un valore aggregato    |
|                                 | calcolato usando elementi da un    |
|                                 | altro vettore                      |
+---------------------------------+------------------------------------+
| `array_agg`_                    | Restituisce un array di valori     |
|                                 | aggregati da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `collect`_                      | Restituisce la geometria a parti   |
|                                 | multiple di geometrie aggregate da |
|                                 | una espressione                    |
+---------------------------------+------------------------------------+
| `concatenate`_                  | Restituisce tutte le stringhe      |
|                                 | aggregate tratte da un campo o da  |
|                                 | una espressione unite con un       |
|                                 | delimitatore                       |
+---------------------------------+------------------------------------+
| `count`_                        | Restituisce il conteggio degli     |
|                                 | elementi corrispondenti            |
+---------------------------------+------------------------------------+
| `count_distinct`_               | Restituisce il conteggio dei       |
|                                 | valori differenti                  |
+---------------------------------+------------------------------------+
| `count_missing`_                | Restituisce il conteggio dei       |
|                                 | valori mancanti (nulli)            |
+---------------------------------+------------------------------------+
| `iqr`_                          | Restituisce lo scarto              |
|                                 | interquartile calcolato da un      |
|                                 | campo o espressione                |
+---------------------------------+------------------------------------+
| `majority`_                     | Restituisce la maggioranza         |
|                                 | aggregata di valori (valore più    |
|                                 | comunemente presente) da un campo  |
|                                 | o espressione                      |
+---------------------------------+------------------------------------+
| `max_length`_                   | Restituisce la lunghezza massima   |
|                                 | delle stringhe di un campo o       |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `maximum`_                      | Restituisce il valore massimo      |
|                                 | aggregato da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `mean`_                         | Restituisce il valore medio        |
|                                 | aggregato da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `median`_                       | Restituisce il valore mediano      |
|                                 | aggregato da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `min_length`_                   | Restituisce la lunghezza minima    |
|                                 | delle stringhe di un campo o       |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `minimum`_                      | Restituisce il valore minimo       |
|                                 | aggregato da un campo o            |
|                                 | espressione.                       |
+---------------------------------+------------------------------------+
| `minority`_                     | Restituisce la minoranza aggregata |
|                                 | di valori (valore meno comunemente |
|                                 | presente) da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `q1`_                           | Restituisce il primo quartile      |
|                                 | calcolato da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `q3`_                           | Restituisce il terzo quartile      |
|                                 | calcolato da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+
| `range`_                        | Restituisce l'intervallo aggregato |
|                                 | di valori (massimo - minimo) da un |
|                                 | campo o espressione                |
+---------------------------------+------------------------------------+
| `relation_aggregate`_           | Restituisce un valore aggregato    |
|                                 | calcolato usando tutte le          |
|                                 | geometrie figlie corrispondenti da |
|                                 | un altro vettore                   |
+---------------------------------+------------------------------------+
| `stdev`_                        | Restituisce il valore di           |
|                                 | deviazione standard aggregato da   |
|                                 | un campo o espressione             |
+---------------------------------+------------------------------------+
| `sum`_                          | Restituisce il valore sommato      |
|                                 | aggregato da un campo o            |
|                                 | espressione                        |
+---------------------------------+------------------------------------+

|image0|

**Nota bene**

Grazie ai `parametri denominati`_ non è più indispensabile seguire, nella sintassi, l’ordine degli argomenti, ecco un esempio:

| La sintassi prevede due possibilità:
|
| 1. quella classica, senza l’uso dei paramentri denominati (l’ordine è fondamentale);
|     1. count_distinct(\ *expression, group_by, filter*)
|   
| 2. con i parametri denominati (l’ordine non è più fondamentale):      
|     1. count_distinct(\ *filter:=,expression:=,group_by:=*)
|
.. _parametri con nome: http://changelog.qgis.org/en/qgis/version/2.16.0/#named-parameters-expressions
.. _aggregate: aggregate.html
.. _array_agg: array_agg.html
.. _collect: collect.html
.. _concatenate: concatenate.html
.. _count: count.html
.. _count_distinct: count_distinct.html
.. _count_missing: count_missing.html
.. _iqr: iqr.html
.. _majority: majority.html
.. _max_length: max_length.html
.. _maximum: maximum.html
.. _mean: mean.html
.. _median: median.html
.. _min_length: min_length.html
.. _minimum: minimum.html
.. _minority: minority.html
.. _q1: q1.html
.. _q3: q3.html
.. _range: range.html
.. _relation_aggregate: relation_aggregate.html
.. _stdev: stdev.html
.. _sum: sum.html
.. _parametri denominati: http://changelog.qgis.org/en/qgis/version/2.16.0/#named-parameters-expressions

.. |image0| image:: /img/aggregates/gruppo_aggregates1.png


**Elenco funzioni Aggregates**
   
.. toctree::
   :maxdepth: 3

   aggregate
   array_agg
   collect
   concatenate
   count
   count_distinct
   count_missing
   iqr
   majority
   max_length
   maximum
   mean
   median
   min_length
   minimum
   minority
   q1
   q3
   range
   relation_aggregate
   stdev
   sum
