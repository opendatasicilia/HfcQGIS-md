# regexp_match

Restituisce la prima posizione di corrispondenza che soddisfa un'espressione regolare all'interno di una stringa, o 0 se la sottostringa non viene trovata.

## Sintassi

* regexp_match(*<span style="color:red;">input_string</span>, <span style="color:red;">regex</span>*)

## Argomenti

* *<span style="color:red;">input_string</span>* la stringa da confrontare con l'espressione regolare
* *<span style="color:red;">regex</span>* L'espressione regolare da confrontare. I caratteri backslash devono essere doppiamente escaped (es "\\s" per selezionare un carattere spazio bianco).

## Esempi
```
regexp_match('QGIS ROCKS','\\sROCKS') → 5
```

## Osservazioni

--

In questo esempio la prima lettere di *Fiandaca* si trova alla posizione 10

```
regexp_match('Salvatore Fiandaca','\\sFiandaca') → 10
```

![](/img/condizioni/regexp_match1.png)
