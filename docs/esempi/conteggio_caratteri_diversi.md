## Conteggio caratteri diversi

**Problema**: come posso classificare in automatico i codici (tipo 133114 ecc.) per identificare il numero dei cambiamenti, cioè il numero di caratteri diversi? Per esempio, nella stringa 133114 ci sono "1" tre volte, "3" due volte, "4" una volta, dunque ci sono tre caratteri diversi. Nella stringa 222222 c'è un solo carattere ("2") ecc. [Quesito preso dalla ML QGIS-user-it](http://osgeo-org.1560.x6.nabble.com/calcolatore-di-campi-conteggio-simboli-numeri-lettere-diversi-td5444878.html)


Tabella di esempio:

ID|field|output
--|-----|:----:
1|133114 |3
2|222222 |1
3|ABBACD |4

Una soluzione passa per l'uso degli **array**:

```
array_length(
array_distinct(  
string_to_array(
regexp_replace(regexp_replace( 133114,'(.)','\\1,'),',$','')))) → 3
```

nel caso in esame utilizzando il campo `field`

```
array_length(
array_distinct(  
string_to_array(
regexp_replace(regexp_replace( "field",'(.)','\\1,'),',$',''))))
```

oppure per evitare il doppio `regex_replace` (Grazie **_Andrea Giudiceandrea_**)

```
array_length(
array_distinct(  
string_to_array(
substr(regexp_replace( "field",'(.)',',\\1'),2))))
```

[![screen](../img/esempi/conteggio_caratteri_diversi/img_01.png)](../img/esempi/conteggio_caratteri_diversi/img_01.png)

oppure possiamo evitare anche la funzione `substr`

```
array_length(
array_distinct(  
string_to_array(
regexp_replace( "field",'(.)\\B','\\1,'))))
```

---

Funzioni e variabili utilizzate:

* [array_length](../gr_funzioni/array/array_unico.md#array_length)
* [array_distinct](../gr_funzioni/array/array_unico.md#array_distinct)
* [string_to_array](../gr_funzioni/array/stringhe_di_testo_unico.md#string_to_array)
* [substr](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#substr)
* [regexp_replace](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#regexp_replace)

