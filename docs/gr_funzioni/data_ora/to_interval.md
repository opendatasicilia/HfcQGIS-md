# to_interval

Converte una stringa in un tipo intervallo. Può essere usata per estrarre giorni, ore, mese, etc. da una data.

## Sintassi

* to_interval(_<span style="color:red;">string</span>_)

## Argomenti

* _<span style="color:red;">string</span>_ una stringa rappresentante un intervallo. I formati ammessi includono {n} giorni {n} ore {n} mesi.

## Esempi
```
to_datetime('2018-05-05 12:00:00') - to_interval('1 day 2 hours') → 2018-05-04T10:00:00
```

![](/img/data_e_ora/to_interval1.png)
