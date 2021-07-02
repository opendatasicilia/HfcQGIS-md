# array_to_string

Concatena gli elementi di un array in una stringa separata da un delimitatore usando una stringa opzionale per valori mancanti.

## Sintassi

* array_to_string(_<span style="color:red;">array</span>, <span style="color:red;">delimiter</span>, <span style="color:red;">empty_value</span>_)

## Argomenti

* _<span style="color:red;">array</span>_ l'array in ingresso
* _<span style="color:red;">delimiter</span>_ il delimitatore stringa usato per separare gli elementi array concatenati
* _<span style="color:red;">empty_value</span>_ la stringa opzionale da usare come sostituzione per le corrispondenze (lunghezza nulla) mancanti

## Esempi

* `array_to_string(array('1','2','3'),',') → 1,2,3'`
* `array_to_string(array('1','','3'),',','0') → 1,0,3'`

![](/img/arrays/array_to_string/array_to_string1.png)

## nota bene

--

## osservazioni

--
