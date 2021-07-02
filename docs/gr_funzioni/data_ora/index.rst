Data e ora
==========

Questo gruppo contiene funzioni per gestire dati con *date* e *ore*.

+---------------------------------+------------------------------------+
| Funzione                        | Descrizione                        |
+=================================+====================================+
| `age`_                          | Restituisce la differenza fra due  |
|                                 | date o datetimes                   |
+---------------------------------+------------------------------------+
| `day`_                          | Estrae il giorno da una data, o il |
|                                 | numero dei giorni da un intervallo |
+---------------------------------+------------------------------------+
| `day_of_week`_                  | Restituisce il giorno della        |
|                                 | settimana per una data o un        |
|                                 | datetime                           |
+---------------------------------+------------------------------------+
| `epoch`_                        | Restituisce l'intervallo in        |
|                                 | millisecondi fra l'epoca unix e la |
|                                 | data inserita                      |
+---------------------------------+------------------------------------+
| `format_date`_                  | Formatta un tipo di data o stringa |
|                                 | in un formato stringa              |
|                                 | personalizzato                     |
+---------------------------------+------------------------------------+
| `hour`_                         | Estrae la parte ore da una         |
|                                 | data/ora o orario, o il numero     |
|                                 | delle ore da un intervallo         |
+---------------------------------+------------------------------------+
| `minute`_                       | Estrae la parte minuti da un       |
|                                 | data/ora o ora, o il numero dei    |
|                                 | minuti da un intervallo            |
+---------------------------------+------------------------------------+
| `month`_                        | Estrae la parte mese da una data,  |
|                                 | o il numero di mesi da un          |
|                                 | intervallo                         |
+---------------------------------+------------------------------------+
| `now`_                          | Restituisce la data e l'ora        |
|                                 | attuale                            |
+---------------------------------+------------------------------------+
| `second`_                       | Estrae la parte secondi da un      |
|                                 | datetime o time, o il numero dei   |
|                                 | secondi da un intervallo           |
+---------------------------------+------------------------------------+
| `to_date`_                      | Converte una stringa in un oggetto |
|                                 | data                               |
+---------------------------------+------------------------------------+
| `to_datetime`_                  | Converte una stringa in un oggetto |
|                                 | datetime                           |
+---------------------------------+------------------------------------+
| `to_interval`_                  | Converte una stringa in un tipo    |
|                                 | intervallo. Può essere usata per   |
|                                 | estrarre giorni, ore, mese, etc.   |
|                                 | da una data                        |
+---------------------------------+------------------------------------+
| `to_time`_                      | Converti una stringa in un oggetto |
|                                 | time                               |
+---------------------------------+------------------------------------+
| `week`_                         | Estrae il numero della settimana   |
|                                 | da una data, o il numero di        |
|                                 | settimane da un intervallo         |
+---------------------------------+------------------------------------+
| `year`_                         | Estrae la parte anno da una data,  |
|                                 | o il numero di anni da un          |
|                                 | intervallo                         |
+---------------------------------+------------------------------------+
| `datetime_from_epoch`_          | Restituisce un datetime il cui     |
|                                 | datae orasono il numero di         |
|                                 | millisecondi...                    |
+---------------------------------+------------------------------------+
    
**Osservazione**

La possibilità di memorizzare i valori di data, ora e datetime
direttamente sui campi può dipendere dal fornitore dell'origine dati (ad
esempio, *shapefile* accetta il formato **data**, ma non il formato
**datetime** o **time**). Di seguito sono riportati alcuni suggerimenti
per superare questa limitazione.

*data*, *data e ora* possono essere memorizzati in campi di testo dopo
aver usato la funzione *to_format ()*.

Gli intervalli possono essere memorizzati nei campi di tipo intero o
decimale dopo aver utilizzato una delle funzioni di estrazione della
data (ad es. *day()* per ottenere l'intervallo espresso in giorni)

|image0|

.. _age: age.html
.. _day: day.html
.. _day_of_week: day_of_week.html
.. _epoch: epoch.html
.. _format_date: format_date.html
.. _hour: hour.html
.. _minute: minute.html
.. _month: month.html
.. _now: now.html
.. _second: second.html
.. _to_date: to_date.html
.. _to_datetime: to_datetime.html
.. _to_interval: to_interval.html
.. _to_time: to_time.html
.. _week: week.html
.. _year: year.html
.. _datetime_from_epoch: datetime_from_epoch.html

.. |image0| image:: /img/data_e_ora/gruppo_data_e_ora1.png

**Elenco funzioni Data e ora**

.. toctree::
   :maxdepth: 3
   
   age
   day
   day_of_week
   epoch
   format_date
   hour
   minute
   month
   now
   second
   to_date
   to_datetime
   to_interval
   to_time
   week
   year
   datetime_from_epoch
   
   
   
   
   
   
   
   
   
   
   
