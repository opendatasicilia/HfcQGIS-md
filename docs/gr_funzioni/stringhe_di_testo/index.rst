Stringhe di testo
===================================

Questo gruppo contiene le funzioni che operano sulle stringhe es.*sostituzione*, *conversione in maiuscolo*.

+-----------------------------+----------------------------------------+
| Funzione                    | Descrizione                            |
+=============================+========================================+
| `char`_                     | Restituisce il carattere associato ad  |
|                             | un codice unicode                      |
+-----------------------------+----------------------------------------+
| `concat`_                   | Concatena svariate stringhe in una     |
|                             | sola. Valori NULL sono convertiti in   |
|                             | stringhe vuote. Altri valori (come i   |
|                             | numeri) sono convertiti in stringa     |
+-----------------------------+----------------------------------------+
| `format`_                   | Formatta una stringa usando gli        |
|                             | argomenti forniti                      |
+-----------------------------+----------------------------------------+
| `format_date`_              | Formatta un tipo di data o stringa in  |
|                             | un formato stringa personalizzato. Usa |
|                             | stringhe nel formato data/ora Qt       |
+-----------------------------+----------------------------------------+
| `format_number`_            | Restituisce un numero formattato con   |
|                             | il separatore locale per le migliaia.  |
|                             | Inoltre tronca il numero al numero di  |
|                             | posti forniti                          |
+-----------------------------+----------------------------------------+
| `left(string, n)`_          | Restituisce una sottostringa che       |
|                             | contiene gli n caratteri più a         |
|                             | sinistra della stringa                 |
+-----------------------------+----------------------------------------+
| `length`_                   | Restituisce il numero di caratteri in  |
|                             | una stringa o la lunghezza di una      |
|                             | geometria di tipo linestring           |
+-----------------------------+----------------------------------------+
| `lower`_                    | Converte una stringa in lettere        |
|                             | minuscole                              |
+-----------------------------+----------------------------------------+
| `lpad`_                     | Restituisce una stringa riempita a     |
|                             | sinistra fino alla larghezza           |
|                             | specificata, utilizzando un carattere  |
|                             | di riempimento.                        |
+-----------------------------+----------------------------------------+
| `regexp_match`_             | Restituisce la prima posizione di      |
|                             | corrispondenza che soddisfa            |
|                             | un'espressione regolare all'interno di |
|                             | una stringa, o 0 se la sottostringa    |
|                             | non viene trovata                      |
+-----------------------------+----------------------------------------+
| `regexp_replace`_           | Restituisce una stringa con la parte   |
|                             | che soddisfa l'espressione regolare    |
|                             | sostituita                             |
+-----------------------------+----------------------------------------+
| `regexp_substr`_            | Restituisce la porzione di una stringa |
|                             | che soddisfa l'espressione regolare    |
|                             | passata                                |
+-----------------------------+----------------------------------------+
| `replace`_                  | Restituisce una stringa con la stringa |
|                             | o array di stringa passate sostituite  |
|                             | da una stringa o un array di stringhe  |
+-----------------------------+----------------------------------------+
| `right(string, n)`_         | Restituisce una sottostringa che       |
|                             | contiene gli n caratteri più a destra  |
|                             | della stringa                          |
+-----------------------------+----------------------------------------+
| `rpad`_                     | Restituisce una stringa riempita a     |
|                             | destra della larghezza specificata,    |
|                             | utilizzando un carattere di            |
|                             | riempimento.                           |
+-----------------------------+----------------------------------------+
| `strpos`_                   | Restituisce la prima posizione di      |
|                             | corrispondenza di una sottostringa     |
|                             | dentro in un'altra stringa o 0 se la   |
|                             | sottostringa non viene trovata         |
+-----------------------------+----------------------------------------+
| `substr`_                   | Restituisce una parte di una stringa   |
+-----------------------------+----------------------------------------+
| `title`_                    | Converte tutte le parole in "title     |
|                             | case" (tutte le parole in minuscolo    |
|                             | con la prima lettera maiuscola)        |
+-----------------------------+----------------------------------------+
| `to_string`_                | Converte un numero in stringa          |
+-----------------------------+----------------------------------------+
| `trim`_                     | Rimuove tutti gli spazi vuoti (spazi,  |
|                             | tabulazioni, etc.) all'inizio e alla   |
|                             | fine di una stringa                    |
+-----------------------------+----------------------------------------+
| `upper`_                    | Converte una stringa in lettere        |
|                             | maiuscole                              |
+-----------------------------+----------------------------------------+
| `wordwrap`_                 | Restituisce una stringa posta a capo   |
|                             | ad un massimo/minimo numero di         |
|                             | caratteri                              |
+-----------------------------+----------------------------------------+

|image0|

.. _char: char.html
.. _concat: concat.html
.. _format: format.html
.. _format_date: format_date.html
.. _format_number: format_number.html
.. _left(string, n): left.html
.. _length: length.html
.. _lower: lower.html
.. _lpad: lpad.html
.. _regexp_match: regexp_match.html
.. _regexp_replace: regexp_replace.html
.. _regexp_substr: regexp_substr.html
.. _replace: replace.html
.. _right(string, n): right.html
.. _rpad: rpad.html
.. _strpos: strpos.html
.. _substr: substr.html
.. _title: title.html
.. _to_string: to_string.html
.. _trim: trim.html
.. _upper: upper.html
.. _wordwrap: wordwrap.html

.. |image0| image:: /img/stringhe_di_testo/gruppo_stringhe_di_testo1.png


**Elenco funzioni Stringhe di testo**
   
.. toctree::
   :maxdepth: 3
   
   char
   concat
   format
   format_date
   format_number
   left
   length
   lower
   lpad
   regexp_match
   regexp_replace
   regexp_substr
   replace
   right
   rpad
   strpos
   substr
   title
   to_string
   trim
   upper
   wordwrap
   
