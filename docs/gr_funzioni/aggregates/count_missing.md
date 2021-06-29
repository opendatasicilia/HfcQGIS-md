# count_missing

Restituisce il conteggio dei valori mancanti (nulli).

## Sintassi

count_missing(_<span style="color:red;">expression</span>, <span style="color:red;">group_by</span>, <span style="color:red;">filter</span>_)

## Argomenti

* _<span style="color:red;">expression</span>_ sotto espressione o campo da aggregare
* _<span style="color:red;">group_by</span>_ espressione opzionale da usarsi per raggruppare i calcoli aggregati
* _<span style="color:red;">filter</span>_ espressione opzionale da usare per filtrare gli elementi usati per calcolare il valore aggregato

## Esempi

* ` count_missing( filter:= "COD_REG">=10,expression:= "DEN_PCM" , group_by:= "COD_REG") → conta i valori mancanti (nulli) delle "DEN_PCM", raggruppate per il campo "COD_REG" con filtro le ultime 10 Regioni`

![](/img/aggregates/count_missing/count_missing1.png)

## nota bene

La sintassi prevede due possibilità:
1. quella classica, senza l'uso dei paramentri denominati (l'ordine è fondamentale);
    1. count_missing(_<span style="color:red;">expression</span>, <span style="color:red;">group_by</span>, <span style="color:red;">filter</span>_)
2. con i parametri denominati (l'ordine non è più fondamentale): 
    1. count_missing(_<span style="color:red;">filter:=</span> ,<span style="color:red;">expression:=</span> ,<span style="color:red;">group_by:=</span>_ )

--

## osservazioni

--
