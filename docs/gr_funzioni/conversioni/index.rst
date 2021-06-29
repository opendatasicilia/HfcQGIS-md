Conversioni
===================================

Questo gruppo contiene funzioni per convertire i dati da un tipo ad
un altro, es. da stringa a intero, da intero a stringa.

+---------------------------------+------------------------------------+
| Funzione                        | Descrizione                        |
+=================================+====================================+
| `hash`_                         | Crea un hash da una stringa con un |
|                                 | determinato metodo                 |
+---------------------------------+------------------------------------+
| `md5`_                          | Crea un hash md5 da una stringa    |
|                                 |                                    |
+---------------------------------+------------------------------------+
| `sha256`_                       | Crea un hash sha256 da una stringa |
|                                 |                                    |
+---------------------------------+------------------------------------+
| `to_date`_                      | Converte una stringa in un oggetto |
|                                 | data                               |
+---------------------------------+------------------------------------+
| `to_datetime`_                  | Converte una stringa in un oggetto |
|                                 | datetime                           |
+---------------------------------+------------------------------------+
| `to_dm`_                        | Converte una coordinata in gradi,  |
|                                 | minuti                             |
+---------------------------------+------------------------------------+
| `to_dms`_                       | Converte una coordinata in gradi,  |
|                                 | minuti e secondi                   |
+---------------------------------+------------------------------------+
| `to_int`_                       | Converte una stringa in un numero  |
|                                 | intero. Non viene restituito nulla |
|                                 | se un valore non può essere        |
|                                 | convertito ad intero (es. ‘123asd’ |
|                                 | non è valido)                      |
+---------------------------------+------------------------------------+
| `to_interval`_                  | Converte una stringa in un tipo    |
|                                 | intervallo. Può essere usata per   |
|                                 | estrarre giorni, ore, mese, etc.   |
|                                 | da una data.                       |
+---------------------------------+------------------------------------+
| `to_real`_                      | Converte una stringa in un numero  |
|                                 | reale. Non viene restituito nulla  |
|                                 | se un valore non può essere        |
|                                 | convertito a reale (es.            |
|                                 | ‘123.56asd’ non è valido). I       |
|                                 | numeri sono arrotondati dopo aver  |
|                                 | salvato le modifiche se la         |
|                                 | precisione è minore del risultato  |
|                                 | della conversione                  |
+---------------------------------+------------------------------------+
| `to_string`_                    | Converte un numero in stringa      |
+---------------------------------+------------------------------------+
| `to_time`_                      | Converti una stringa in un oggetto |
|                                 | time                               |
+---------------------------------+------------------------------------+

|image0|

.. _to_date: to_date.html
.. _to_datetime: to_datetime.html
.. _to_dm: to_dm.html
.. _to_dms: to_dms.html
.. _to_int: to_int.html
.. _to_interval: to_interval.html
.. _to_real: to_real.html
.. _to_string: to_string.html
.. _to_time: to_time.html
.. _hash: hash.html
.. _md5: md5.html
.. _sha256: sha256.html

.. |image0| image:: /img/conversioni/gruppo_conversioni1.png

**Elenco funzioni Conversioni**

.. toctree::
   :maxdepth: 3
   
   to_date
   to_datetime
   to_dm
   to_dms
   to_int
   to_interval
   to_real
   to_string
   to_time
   hash
   md5
   sha256
   

