# regexp_matches

Restituisce un array di tutte le stringhe catturate dai gruppo, nell'ordine che i gruppi stessi compaiono con l'espressione regolare fornita con una stringa.

## Sintassi

* regexp_matches(_<span style="color:red;">string</span>, <span style="color:red;">regex</span>, <span style="color:red;">empty_value</span>_)

## Argomenti

* _<span style="color:red;">string</span>_ la stringa con cui catturare i gruppi da un'espressione regolare
* _<span style="color:red;">regex</span>_ l'espressione regolare usata per catturare gruppi
* _<span style="color:red;">empty_value</span>_ la stringa opzionale da usare come sostituzione per le corrispondenze (lunghezza nulla) mancanti

## Esempi

* `regexp_matches('QGIS=>rocks','(.*)=>(.*)') → array: 'QGIS', 'rocks'`
* `regexp_matches('key=>','(.*)=>(.*)','empty value') → array: 'key', 'empty value'`
* `regexp_matches('key=>','(.*)=>','empty value') →'array: 'key'`
* `regexp_matches('key=>7','(.*)=>(.*)','empty value') → array: 'key', '7'`

![](/img/arrays/regexp_matches/regexp_matches1.png)

## nota bene

--

## osservazioni

--
