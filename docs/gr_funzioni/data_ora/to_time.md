# to_time

Converti una stringa in un oggetto time.

## Sintassi

* to_time(_<span style="color:red;">string</span>_,[_<span style="color:red;">format</span>_][,_<span style="color:red;">language</span>_])

## Argomenti

* _<span style="color:red;">string</span>_ stringa rappresentante il valore ora
* _<span style="color:red;">format</span>_ formato usato per convertire la stringa in orario
* _<span style="color:red;">language</span>_ lingua (minuscolo, due o tre lettere, codice lingua ISO 639) utilizzata per convertire la stringa in un orario.
* 
## Esempi

```
- to_time('12:30:01') → 12:30:01
- to_time('12:34','HH:mm') → 12:34:00
- to_time('12:34','HH:mm','fr') → 12:34:00
```

![](../../img/data_e_ora/to_time1.png)
