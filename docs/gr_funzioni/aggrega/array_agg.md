# array_agg

Restituisce un array di valori aggregati da un campo o espressione.

## Sintassi

array_agg(_<span style="color:red;">expression</span>[,<span style="color:red;">group_by</span>][,<span style="color:red;">filter</span>][,<span style="color:red;">order_by</span>_])

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">expression</span>_ sotto espressione o campo da aggregare
* _<span style="color:red;">group_by</span>_ espressione opzionale da usarsi per raggruppare i calcoli aggregati
* _<span style="color:red;">filter</span>_ espressione opzionale da usare per filtrare gli elementi usati per calcolare il valore aggregato
* _<span style="color:red;">order_by</span>_ espressione opzionale da usare per ordinare gli elementi usati per calcolare il valore aggregato. Da predefinito, gli elementi verranno restituiti in un ordine non specificato.

## Esempi

* `array_agg( "DEN_PCM" ,group_by:= "COD_REG" ) → lista di valori del "DEN_PCM", ragguppata per il campo "COD_REG"`

![](../../img/aggregates/array_agg/array_agg1.png)

## nota bene

Per prendere un valore specifico dell'array: 
- `array_agg("z")[0]` → 148,03 è il primo valore dell'array, indice 0;
- `array_agg("z")[1]` → 164,21 è il secondo valore dell'array, indice 1;
- ecc...

## osservazioni

--
