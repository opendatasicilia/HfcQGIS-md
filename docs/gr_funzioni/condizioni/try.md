# try

Prova un'espressione e restituisce il suo valore se priva di errori. Se l'espressione restituisce un errore, verrà restituito un valore alternativo se fornito altrimenti la funzione restituirà null.

## Sintassi

* try(_<span style="color:red;">expression</span>_[,_<span style="color:red;">alternative</span>_])

[ ] contrassegna componenti opzionali

## Argomenti

* _<span style="color:red;">expression</span>_ l'espressione che dovrebbe essere eseguita
* _<span style="color:red;">alternative</span>_ il risultato che verrà restituito se l'espressione restituisce un errore


## Esempi
```
* try( to_int( '1' ), 0 ) → 1
* try( to_int( 'a' ), 0 ) → 0
* try( to_date( 'invalid_date' ) ) → NULL
```

## Osservazioni

--

![](../../img/condizioni/try1.png)
