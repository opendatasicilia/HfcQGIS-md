# count_distinct

Restituisce il conteggio dei valori differenti.

## Sintassi

count_distinct(_<span style="color:red;">expression</span>, <span style="color:red;">group_by</span>, <span style="color:red;">filter</span>_)

## Argomenti

* _<span style="color:red;">expression</span>_ sotto espressione o campo da aggregare
* _<span style="color:red;">group_by</span>_ espressione opzionale da usarsi per raggruppare i calcoli aggregati
* _<span style="color:red;">filter</span>_ espressione opzionale da usare per filtrare gli elementi usati per calcolare il valore aggregato

## Esempi

* `count_distinct(expression:= "DEN_PCM" ,group_by:= "COD_REG" ,filter:= "COD_REG"<5) → conta i valori differenti delle "DEN_PCM", raggruppate per il campo "COD_REG" con filtro le prime 4 Regioni`

![](../../img/aggregates/count_distinct/count_distinct1.png)

## nota bene

La sintassi prevede due possibilità:
1. quella classica, senza l'uso dei paramentri denominati (l'ordine è fondamentale);
    1. majority(_<span style="color:red;">expression</span>, <span style="color:red;">group_by</span>, <span style="color:red;">filter</span>_)
2. con i parametri denominati (l'ordine non è più fondamentale): 
    1. majority(_<span style="color:red;">filter:=</span> ,<span style="color:red;">expression:=</span> ,<span style="color:red;">group_by:=</span>_ )

## osservazioni

--

![](../../img/aggregates/count_distinct/count_distinct2.png)
