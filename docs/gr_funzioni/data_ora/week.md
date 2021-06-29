# week

Estrae il numero della settimana da una data, o il numero di settimane da un intervallo.

## Variabile data

Estrae il numero della settimana da una data o un datetime.

## Sintassi

* week(_<span style="color:red;">date</span>_)

## Argomenti

* _<span style="color:red;">date</span>_ un valore data o data/ora

## Esempi
```
week('2018-05-09') → 19
```

![](/img/data_e_ora/week1.png)

## Variabile intervallo

Calcola la lunghezza in settimane di un intervallo.

## Sintassi

* week(_<span style="color:red;">interval</span>_)

## Argomenti

* _<span style="color:red;">interval</span>_ valore intervallo da cui restituire il numero di mesi

## Esempi
```
week(tointerval('3 weeks')) → 3
week(age('2012-01-01','2010-01-01')) → 104.285
```

![](/img/data_e_ora/week2.png)
