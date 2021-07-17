# relation_aggregate

Restituisce un valore aggregato calcolato usando tutte le geometrie figlie corrispondenti da un altro vettore.

## Sintassi

relation_aggregate(_<span style="color:red;">relation</span>, <span style="color:red;">aggregate</span>, <span style="color:red;">expression</span>, <span style="color:red;">concatenator</span>_)

## Argomenti

* <span style="color:red;">_relation_</span> una stringa, rappresentante un ID di relazione
* <span style="color:red;">_aggregate_</span> una stringa corrispondente all'aggregato da calcolare. Opzioni valide sono:

    * count
    * count_distinct
    * count_missing
    * min
    * max
    * sum
    * mean
    * median
    * stdev
    * stdevsample
    * range
    * minority
    * majority
    * q1: primo quartile
    * q3: terzo quartile
    * iqr: scarto interquartile
    * min_length: minima lunghezza stringa
    * max_length: massima lunghezza stringa
    * concatenate: unisci stringhe con un concatenatore
    
* <span style="color:red;">_expression_</span> sotto espressione o nome campo da aggregare
* <span style="color:red;">_concatenator_</span> stringa opzionale da usare per unire i valori per il raggruppamento 'concatenate'

## Esempi


* `relation_aggregate(relation:='rel_prov_com',aggregate:='concatenate',concatenator:=',',expression:="COMUNE" ) →  elenco separato da virgole del campo "COMUNE" per tutte le geometrie figlie corrispondenti usando la relation 'rel_prov_com'`
* `relation_aggregate(relation:='my_relation',aggregate:='mean',expression:="passengers") → valore medio di tutte le geometrie figlie corrispondenti usando la relazione 'my_relation'`
* `relation_aggregate('my_relation','sum', "passengers"/7) → somma del campo passengers diviso per 7 per tutte le geometrie figlie corrispondenti usando la relazione 'my_relation'`
* `relation_aggregate('my_relation','concatenate', "towns", concatenator:=',') → elenco separato da virgole del campo town per tutte le geometrie figlie corrispondenti usando la relation 'my_relation'`


![](../../img/aggregates/relation_aggregate/relation_aggregate1.png)

## nota bene

La sintassi prevede due possibilità:
1. quella classica, senza l'uso dei paramentri denominati (l'ordine è fondamentale);
    1. relation_aggregate(_<span style="color:red;">relation</span>, <span style="color:red;">aggregate</span>, <span style="color:red;">expression</span>, <span style="color:red;">concatenator</span>_)
2. con i parametri denominati (l'ordine non è più fondamentale): 
    1. relation_aggregate(_<span style="color:red;">relation:=</span>, <span style="color:red;">aggregate:=</span>, <span style="color:red;">expression:=<span style="color:red;">, <span style="color:red;">concatenator:=</span>_)

## osservazioni

--

![](../../img/aggregates/relation_aggregate/relation_aggregate2.png)
