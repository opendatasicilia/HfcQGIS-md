# array_filter

Restituisce un array con solo gli elementi per i quali l'espressione restituisce true (vero).

## Sintassi

array_filter(_<span style="color:red;">array</span>,<span style="color:red;">expression</span>_)

## Argomenti

* _<span style="color:red;">array</span>_ un array
* _<span style="color:red;">expression</span>_ un'espressione da valutare su ogni oggetto. La variabile `@ element` sarà sostituita dal valore corrente.

## Esempi

* `array_filter(array(1,2,3),@element < 3) → [ 1, 2 ]`

![](/img/arrays/array_filter/array_filter1.png)

## nota bene

--

## osservazioni

--
