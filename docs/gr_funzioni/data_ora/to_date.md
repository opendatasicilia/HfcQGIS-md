# to_date

Converte una stringa in un oggetto data

## Sintassi

* to_date(_<span style="color:red;">string</span>_,[_<span style="color:red;">format</span>_][,_<span style="color:red;">language</span>_])

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">string</span>_ stringa rappresentante il valore data
* _<span style="color:red;">format</span>_ formato usato per convertire la stringa in una data
* _<span style="color:red;">language</span>_ lingua (minuscolo, due o tre lettere, codice lingua ISO 639) utilizzata per convertire la stringa in una data. Per impostazione predefinita, viene utilizzata la locale dell'utente di QGIS corrente.

## Esempi
```
- to_date('2012-05-04') → 2012-05-04
- to_date('June 29, 2019','MMMM d, yyyy') → 2019-06-29, se la locale corrente utilizza il nome 'June' per il sesto mese, altrimenti si verifica un errore
- to_date('29 juin, 2019','d MMMM, yyyy','fr') → 2019-06-29
```

![](../../img/data_e_ora/to_date1.png)
