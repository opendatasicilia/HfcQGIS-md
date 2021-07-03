# wordwrap

Restituisce una stringa posta a capo ad un massimo/minimo numero di caratteri.

## Sintassi

wordwrap(_<span style="color:red;">string</span>, <span style="color:red;">wrap_length</span>, <span style="color:red;">delimiter_string</span>_)

## Argomenti

* _<span style="color:red;">string</span>_ la stringa da spezzare
* _<span style="color:red;">wrap_length</span>_ un intero. Se wrap_length è positivo il numero rappresenta il numero massimo ideale di caratteri a cui spezzare; se negativo, il numero rappresenta il numero minimo di caratteri a cui spezzare.
* _<span style="color:red;">delimiter_string</span>_ il delimitatore stringa per spezzare in una nuova linea (opzionale).

## Esempi
```
wordwrap('UNIVERSITY OF QGIS',13) → 'UNIVERSITY OF
QGIS'

wordwrap('UNIVERSITY OF QGIS',-3) → 'UNIVERSITY
OF QGIS'
```

![](../../img/stringhe_di_testo/wordwrap/wordwrap1.png)

## nota bene

--

## osservazioni

--
