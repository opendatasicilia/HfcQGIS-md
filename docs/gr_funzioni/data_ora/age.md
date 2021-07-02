# age

Restituisce la differenza fra due date o datetimes.
La differenza è restituita come _Interval_ e deve essere usata con una della seguenti funzioni per estrarre informazioni utili:

* year
* month
* week
* day
* hour
* minute
* second

## Sintassi

* age(_<span style="color:red;">datetime1</span>, <span style="color:red;">datetime2</span>_)

## Argomenti

* _<span style="color:red;">datetime1</span>_ una stringa, in formato data o data/ora rappresentante la meno recente
* _<span style="color:red;">datetime2</span>_ una stringa, in formato data o data/ora rappresentante la data più recente

## Esempi

* `age('2012-05-12','2012-05-02') → intervallo (usa day per estrarre il numero di giorni)`
* `day(age('2012-05-12','2012-05-02')) → 10`

![](/img/data_e_ora/age1.png)
