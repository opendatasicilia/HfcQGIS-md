# with_variable

Questa funzione imposta una variabile per qualunque codice di espressione che sarà fornita come argomento terzo. Questo è utile solamente per espressioni complicate, in cui lo stesso valore calcolato deve essere usato in posti differenti.

## Sintassi

* with_variable(*<span style="color:red;">name</span>, <span style="color:red;">value</span>, <span style="color:red;">node</span>*)

## Argomento

* *<span style="color:red;">name</span>* il nome della variabile da impostare
* *<span style="color:red;">value</span>* il valore da impostare
* *<span style="color:red;">node</span>* l'espressione per la quale la variabile sarà disponibile



## Esempi
```
with_variable('my_sum', 1 + 2 + 3, @my_sum * 2 + @my_sum * 5) → 42
with_variable('duepigreco',2*3.1415, @duepigreco * 2 +@duepigreco*5 ) → 43.981
```

![](../../img/generale/with_variable1.png)
