# to_datetime

Converte una stringa in un oggetto datetime. È possibile fornire una stringa di formato opzionale per analizzare la stringa; vedi [QDate::fromString](https://doc.qt.io/qt-5/qdate.html#fromString-2), [QTime::fromString](https://doc.qt.io/qt-5/qtime.html#fromString-1) o la documentazione della funzione format_date per ulteriore documentazione sul formato. Per impostazione predefinita, viene utilizzata la locale dell'utente di QGIS corrente.

## Sintassi

* to_datetime(_<span style="color:red;">string</span>_,[_<span style="color:red;">format</span>_][,_<span style="color:red;">language</span>_])

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">string</span>_ stringa rappresentante il valore data
* _<span style="color:red;">format</span>_ formato usato per convertire la stringa in una data
* _<span style="color:red;">language</span>_ lingua (minuscolo, due o tre lettere, codice lingua ISO 639) utilizzata per convertire la stringa in una data. Per impostazione predefinita, viene utilizzata la locale dell'utente di QGIS corrente.

## Esempi

```
- to_datetime('2012-05-04 12:50:00') → 2012-05-04T12:50:00
- to_datetime('June 29, 2019 @ 12:34','MMMM d, yyyy @ HH:mm') → 2019-06-29T12:34, se la locale corrente utilizza il nome 'June' per il sesto mese, altrimenti si verifica un errore
- to_datetime('29 juin, 2019 @ 12:34','d MMMM, yyyy @ HH:mm','fr') → 2019-06-29T12:3
```

![](../../img/data_e_ora/to_datetime1.png)
