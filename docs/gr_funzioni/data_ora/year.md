# year

Estrae la parte anno da una data, o il numero di anni da un intervallo.

## Variabile data

Estrae la parte anno da una data o datetime.

## Sintassi

* year(_<span style="color:red;">date</span>_)

## Argomenti

* _<span style="color:red;">date</span>_ un valore data o data/ora

## Esempi
```
week('2018-05-09') → 19
```

![](../../img/data_e_ora/year1.png)

## Variabile intervallo

Calcola la lunghezza in anni di un intervallo.

## Sintassi

* year(_<span style="color:red;">interval</span>_)

## Argomenti

* _<span style="color:red;">interval</span>_ valore intervallo da cui restituire il numero di anni

## Esempi
```
year(to_interval('3 years')) → 3
year(age('2012-01-01','2010-01-01')) → 1.9986
```

![](../../img/data_e_ora/year2.png)
