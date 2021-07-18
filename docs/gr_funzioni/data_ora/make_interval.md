# make_interval

Crea un valore di intervallo dai valori di anno, mese, settimane, giorni, ore, minuti e secondi.

## Sintassi

* make_interval(_<span style="color:red;">_years=0</span>_][,_<span style="color:red;">months=0</span>_][,_<span style="color:red;">weeks=0</span>_][,_<span style="color:red;">days=0</span>_][,_<span style="color:red;">hours=0</span>_][,_<span style="color:red;">minutes=0</span>_][,_<span style="color:red;">seconds=0</span>])

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">year</span>_ Numero di anni (presuppone una durata di 365,25 giorni).
* _<span style="color:red;">month</span>_ Numero di mesi (presuppone una durata del mese di 30 giorni)
* _<span style="color:red;">weeks</span>_ numero settimane;
* _<span style="color:red;">day</span>_ Numero di giorno;
* _<span style="color:red;">hour</span>_ numero ore;
* _<span style="color:red;">minute</span>_ minuti;
* _<span style="color:red;">second</span>_ secondi.


## Esempi

* `make_interval(2020,5,4,13,45,30.5) → datetime value 2020-05-04 13:45:30.500`

![](../../img/data_e_ora/make_interval1.png)

## Osservazioni

--
