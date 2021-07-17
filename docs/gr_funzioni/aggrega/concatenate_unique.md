# concatenate_unique

Restituisce tutte le stringhe aggregate univoche tratte da un campo o da una espressione unite con un delimitatore.

## Sintassi

concatenate_unique(_<span style="color:red;">expression</span>_, _<span style="color:red;">group_by</span>_, _<span style="color:red;">filter, concatenator</span>_)

## Argomenti

* _<span style="color:red;">expression</span>_ sotto espressione o campo da aggregare
* _<span style="color:red;">group_by</span>_ espressione opzionale da usarsi per raggruppare i calcoli aggregati
* _<span style="color:red;">filter</span>_ espressione opzionale da usare per filtrare gli elementi usati per calcolare il valore aggregato
* _<span style="color:red;">concatenator</span>_ stringa opzionale da usarsi per unire i valori

## Esempi

* `concatenate_unique( expression:="DEN_PCM",group_by:="COD_REG",concatenator:=',') → lista separata da virgola di "DEN_PCM", raggruppata dal campo "COD_REG"`

![](../../img/aggregates/concatenate_unique/concatenate_unique1.png)

## nota bene

--

## osservazioni

--
