# hamming_distance

Restituisce la distanza di Hamming tra due stringhe. Questa equivale al numero di caratteri nelle corrispondenti posizioni delle stringhe in ingresso dove i caratteri sono diversi. Le stringhe in ingresso devono avere la stessa lunghezza, e il confronto è sensibile alle lettere maiuscole.

## Sintassi

* hamming_distance(*<span style="color:red;">string1</span>, <span style="color:red;">string2</span>*)

## Argomenti

* _<span style="color:red;">string1</span>_ una stringa
* _<span style="color:red;">string2</span>_ una stringa

## Esempi
```
* hamming_distance('abc','xec') → 2
* hamming_distance('abc','ABc') → 2
* hamming_distance(upper('abc'),upper('ABC')) → 0
```

![](../../img/corrispondenza_fuzzy/hamming_distance1.png)
