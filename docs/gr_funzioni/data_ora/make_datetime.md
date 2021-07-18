# make_datetime

Crea un valore datetime da anno, mese, giorno, ora, minuti e secondi numeri.

## Sintassi

* make_datetime(_<span style="color:red;">year</span>_,_<span style="color:red;">month</span>_,_<span style="color:red;">day</span>_,_<span style="color:red;">hour</span>_,_<span style="color:red;">minute</span>_,_<span style="color:red;">second</span>_)

## Argomenti

* <span style="color:red;">year</span> Numero dell'anno. Gli anni da 1 a 99 vengono interpretati così come sono. L'anno 0 non è valido.
* <span style="color:red;">month</span> Numero del mese, dove 1 = gennaio
* <span style="color:red;">day</span> Day Numero del giorno, che inizia con 1 per il primo giorno del mese;
* <span style="color:red;">hour</span> numero ore;
* <span style="color:red;">minute</span> minuti;
* <span style="color:red;">second</span> secondi (i valori frazionari includono millisecondi).


## Esempi

* `make_datetime(2020,5,4,13,45,30.5) → datetime value 2020-05-04 13:45:30.500`

![](../../img/data_e_ora/make_datetime1.png)

## Osservazioni

--
