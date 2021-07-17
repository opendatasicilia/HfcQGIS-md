# nullif

Restituisce un valore nullo se _value1_ è uguale a _value2_; altrimenti restituisce _value1_. Questo può essere usato per sostituire in modo condizionale i valori con `NULL`.

## Sintassi

* nullif(_<span style="color:red;">value1</span>_,_<span style="color:red;">value2</span>_)

## Argomenti

* _<span style="color:red;">value1</span>_ Il valore che dovrebbe essere utilizzato o sostituito con `NULL`.
* _<span style="color:red;">value2</span>_ Il valore di controllo che attiverà la sostituzione `NULL`.

## Esempi
```
nullif('(none)', '(none)') → NULL
nullif('text', '(none)') → 'text'
nullif("name", '') → NULL, se "name" è una stringa vuota (o già NULL), "name" in qualsiasi altro caso.
```

## Osservazioni

--

![](../../img/condizioni/nullif1.jpg)
