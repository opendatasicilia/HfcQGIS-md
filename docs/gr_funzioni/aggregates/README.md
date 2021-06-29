# Aggregates

Contiene funzioni che aggregano valori nei livelli e campi. A partire da **QGIS 2.16** il motore di espressioni supporta l'uso di [parametri con nome](http://changelog.qgis.org/en/qgis/version/2.16.0/#named-parameters-expressions).

| Funzione  | Descrizione|
|----------:|:-----------|
|[aggregate](aggregate.html)|Restituisce un valore aggregato calcolato usando elementi da un altro vettore|
|[array_agg](array_agg.html)|Restituisce un array di valori aggregati da un campo o espressione|
|[collect](collect.html)|Restituisce la geometria a parti multiple di geometrie aggregate da una espressione|
|[concatenate](concatenate.html)|	Restituisce tutte le stringhe aggregate tratte da un campo o da una espressione unite con un delimitatore|
|[count](count.html)|Restituisce il conteggio degli elementi corrispondenti|
|[count_distinct](count_distinct.html)|Restituisce il conteggio dei valori differenti|
|[count_missing](count_missing.html)|Restituisce il conteggio dei valori mancanti (nulli)|
|[iqr](iqr.html)|Restituisce lo scarto interquartile calcolato da un campo o espressione|
|[majority](majority.html)|Restituisce la maggioranza aggregata di valori (valore più comunemente presente) da un campo o espressione|
|[max_length](max_length.html)|Restituisce la lunghezza massima delle stringhe di un campo o espressione|
|[maximum](maximum.html)|Restituisce il valore massimo aggregato da un campo o espressione|
|[mean](mean.html)|Restituisce il valore medio aggregato da un campo o espressione|
|[median](median.html)|Restituisce il valore mediano aggregato da un campo o espressione|
|[min_length](min_length.html)|Restituisce la lunghezza minima delle stringhe di un campo o espressione|
|[minimum](minimum.html)|Restituisce il valore minimo aggregato da un campo o espressione.|
|[minority](minority.html)|Restituisce la minoranza aggregata di valori (valore meno comunemente presente) da un campo o espressione|
|[q1](q1.html)|Restituisce il primo quartile calcolato da un campo o espressione|
|[q3](q3.html)|Restituisce il terzo quartile calcolato da un campo o espressione|
|[range](range.html)|Restituisce l'intervallo aggregato di valori (massimo - minimo) da un campo o espressione|
|[relation_aggregate](relation_aggregate.html)|Restituisce un valore aggregato calcolato usando tutte le geometrie figlie corrispondenti da un altro vettore|
|[stdev](stdev.html)|Restituisce il valore di deviazione standard aggregato da un campo o espressione|
|[sum](sum.html)|Restituisce il valore sommato aggregato da un campo o espressione|

![](/img/aggregates/gruppo_aggregates1.png)

## Nota bene

Grazie ai [_parametri denominati_](http://changelog.qgis.org/en/qgis/version/2.16.0/#named-parameters-expressions) non è più indispensabile seguire, nella sintassi, l'ordine degli argomenti, ecco un esempio:

La sintassi prevede due possibilità:
1. quella classica, senza l'uso dei paramentri denominati (l'ordine è fondamentale);
    1. count_distinct(_expression, group_by, filter_)
2. con i parametri denominati (l'ordine non è più fondamentale): 
    1. count_distinct(filter:= ,_expression:= ,group_by:=_)
