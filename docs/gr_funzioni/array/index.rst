Array (NOVITÀ QGIS 3.4)
======

solo DB (es:SpatiaLite, PostGIS)

Questo gruppo contiene funzioni espressione per la creazione e la
manipolazione di array (noti anche come strutture dati ad elenco).
L'ordine dei valori all'interno dell'array è importante, al contrario
della struttura dati 'a mappa' (`gruppo Maps`_), in cui l'ordine delle
coppie chiave-valore è irrilevante e i valori vengono identificati dalle
loro chiavi.

+------------------------+--------------------------+-----------------+
| Funzione               | Descrizione              |Info             |
+========================+==========================+=================+
| `array_filter`_        | Restituisce un array con | >=QGIS 3.4      |
|                        | solo gli elementi per i  |                 |
|                        | quali l'espressione      |                 |
|                        | restituisce true (vero)  |                 |
+------------------------+--------------------------+-----------------+
| `array_foreach`_       | Restituisce un matrice   | >=QGIS 3.4      |
|                        | con l'espressione data   |                 |
|                        | valutata su ciscun campo |                 |
+------------------------+--------------------------+-----------------+

|image0|


.. _gruppo Maps: ../maps
.. _array_filter: array_filter.html
.. _array_foreach: array_foreach.html

.. |image0| image:: /img/array/neo_gruppo.png


**Elenco funzioni Array**

.. toctree::
   :maxdepth: 3
   
   array_filter
   array_foreach
   
