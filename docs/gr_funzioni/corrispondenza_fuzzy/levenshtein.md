# levenshtein

Restituisce la distanza di Levenshtein tra due stringhe. Questa equivale al minimo numero di modifiche di caratterere (inserimenti, cancellazioni o sostituzione) richieste per cambiare una stringa in un'altra.
La distanza di Levenshtein è una misura della somiglianza tra due stringhe. Distanze più piccole corrispondono a stringhe più simili, e distanze più grandi corrispondono a stringhe più differenti. La distanza è sensibile alle lettere maiuscole.

## Sintassi

* levenshtein(*<span style="color:red;">string1</span>, <span style="color:red;">string2</span>*)

## Argomenti

* _<span style="color:red;">string1</span>_ una stringa
* _<span style="color:red;">string2</span>_ una stringa

## Esempi
```
* levenshtein('kittens','mitten') → 2
* levenshtein('Kitten','kitten') → 1
* levenshtein(upper('Kitten'),upper('kitten')) → 0
```

![](../../img/corrispondenza_fuzzy/levenshtein1.png)
