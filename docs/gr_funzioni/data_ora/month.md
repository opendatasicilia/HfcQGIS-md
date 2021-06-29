# month

Estrae la parte mese da una data, o il numero di mesi da un intervallo.

## Variabile data

Estrae la parte mese da una data o datetime.

## Sintassi

* month(_<span style="color:red;">date</span>_)

## Argomenti

* _<span style="color:red;">date</span>_ un valore data o data/ora

## Esempi
```
* month('2012-05-12') → 05
```

![](/img/data_e_ora/month1.png)

## Variabile intervallo

Calcola la lunghezza in mesi di un intervallo.

## Sintassi

* month(_<span style="color:red;">interval</span>_)

## Argomenti

* _<span style="color:red;">interval</span>_ valore intervallo da cui restituire il numero di mesi

## Esempi
```
month(to_interval('3 months')) → 3
month(age('2012-01-01','2010-01-01')) → 24.3333
```

![](/img/data_e_ora/month1.png)
