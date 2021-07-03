# regexp_replace

Restituisce una stringa con la parte che soddisfa l'espressione regolare sostituita.

## Sintassi

regexp_replace(_<span style="color:red;">input_string</span>, <span style="color:red;">regex</span>, <span style="color:red;">replacement</span>_)

## Argomenti

* _<span style="color:red;">input_string</span>_ la stringa in cui sostituire
* _<span style="color:red;">regex</span>_ L'espressione regolare per sostituire. I caratteri backslash devono essere double escaped (es "\\s" per selezionare un carattere spazio bianco).
* _<span style="color:red;">replacement</span>_ La stringa che sostituirà qualsiasi occorrenza corrispondente dell'espressione regolare passata. I gruppi catturati possono essere inseriti nella stringa di sostituzione usando `\\1`, `\\2`, etc.


## Esempi

![](../../img/stringhe_di_testo/regexp_replace/regexp_replace1.png)

## Esempio 2

Tabella:

id|particella
--|----------
1 |00AXJ
2 |000BBG
3 |0JJU

Aggiornare il campo `particella` togliendo gli zeri iniziali:

espressione da usare:

- `regexp_replace(  "particella" ,'^0+','')`

risultato:

id|particella
--|----------
1 |AXJ
2 |BBG
3 |JJU

ecco un tool dove provare le regexp: <https://regex101.com/r/SSDBmj/1>

## Esempio 3

id | valore
---|------
1  | data20200224
2  | data20200225
3  | data20200226

eliminare data e inserire un simbolo tra anno, mese e giorno

espressione da usare:

- `regexp_replace("valore" ,'(data)(....)(..)(..)','\\2-\\3-\\4')`

risultato:

id | valore
---|------
1  | 2020-02-24
2  | 2020-02-25
3  | 2020-02-26

## Esempio 4

Tabella:

id|particella
--|----------
1 |00AXJ.su
2 |000BBG.cot
3 |0JJU.1234

Aggiornare il campo `particella` togliendo tutto quello dopo il punto (.):

espressione da usare:

- ` regexp_replace( 'xxxxx.yyy','\\.(.+)$','')`

risultato:

id|particella
--|----------
1 |00AXJ
2 |000BBG
3 |0JJU

## nota bene

--

## osservazioni

--
