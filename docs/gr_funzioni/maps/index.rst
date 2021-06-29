Maps
===================================
solo DB (es:PostGIS)

Questo gruppo contiene funzioni espressione per la creazione e la
manipolazione di strutture di dati 'a mappa' (noti anche come oggetti
dizionario, coppie chiave-valore o array associative). Si possono
assegnare valori a determinate chiavi. L'ordine delle coppie chiave
valore nell'oggetto mappa non è rilevante come per gli Arrays (`gruppo
Arrays`_).

+--------------------------+----------------------------+-------------+
| Funzione                 | Descrizione                | Plugin      |
+==========================+============================+=============+
|`from_json`_              |Carica una stringa          |>= QGIS 3.6  |
|                          |formattata JSON             |             |
+--------------------------+----------------------------+-------------+
| `hstore_to_map`_         | Coverte hstore in map      |>= QGIS 3.4  |
+--------------------------+----------------------------+-------------+
| `json_to_map`_           | Converte string json in    |>= QGIS 3.4  |
|                          | map                        |             |
+--------------------------+----------------------------+-------------+
| `map`_                   | Restituisce una mappa con  |             |
|                          | tutte le chiavi ed i       |             |
|                          | valori passati come coppie |             |
|                          | di parametri               |             |
+--------------------------+----------------------------+-------------+
| `map_akeys`_             | Restituisce tutte le       |             |
|                          | chiavi di una mappa come   |             |
|                          | un array                   |             |
+--------------------------+----------------------------+-------------+
| `map_avals`_             | Restituisce tutti valori   |             |
|                          | di una mappa come un array |             |
+--------------------------+----------------------------+-------------+
| `map_concat`_            | Restituisce una mappa con  |             |
|                          | tutte le entità della      |             |
|                          | mappe fornite              |             |
+--------------------------+----------------------------+-------------+
| `map_delete`_            | Restituisce una mappa con  |             |
|                          | il valore della            |             |
|                          | corrispondente chiave      |             |
|                          | passata rimosso            |             |
+--------------------------+----------------------------+-------------+
| `map_exist`_             | Restituisce vero se la     |             |
|                          | chiave passata esiste in   |             |
|                          | mappa                      |             |
+--------------------------+----------------------------+-------------+
| `map_get`_               | Restituisce il valore di   |             |
|                          | una mappa, passando la sua |             |
|                          | chiave                     |             |
+--------------------------+----------------------------+-------------+
| `map_insert`_            | Restituisce una mappa con  |             |
|                          | una chiave/valore aggiunto |             |
+--------------------------+----------------------------+-------------+
| `map_to_hstore`_         | Unisci gli elementi della  |             |
|                          | mappa in una stringa       |             |
|                          | formattata in hstore       |>= QGIS 3.4  |
+--------------------------+----------------------------+-------------+
| `map_to_json`_           | Unisci gli elementi della  |             |
|                          | mappa in una stringa       |             |
|                          | formattata con json        |>= QGIS 3.4  |
+--------------------------+----------------------------+-------------+
| `to_json`_               | Creare una stringa in      | >= QGIS 3.6 |
|                          | formato JSON da una mappa, |             |
|                          | array o altro valore       |             |
+--------------------------+----------------------------+-------------+

|image0|

.. _gruppo Arrays: ../arrays
.. _from_json: from_json.html
.. _hstore_to_map: hstore_to_map.html
.. _json_to_map: json_to_map.html
.. _map: map.html
.. _map_akeys: map_akeys.html
.. _map_avals: map_avals.html
.. _map_concat: map_concat.html
.. _map_delete: map_delete.html
.. _map_exist: map_exist.html
.. _map_get: map_get.html
.. _map_insert: map_insert.html
.. _map_to_hstore: map_to_hstore.html
.. _map_to_json: map_to_json.html
.. _to_json: to_json.html

.. |image0| image:: /img/maps/gruppo_maps1.png

**Elenco funzioni Maps**
   
.. toctree::
   :maxdepth: 3
   
   from_json
   hstore_to_map
   json_to_map
   map
   map_akeys
   map_avals
   map_concat
   map_delete
   map_exist
   map_get
   map_insert 
   map_to_hstore
   map_to_json
   to_json
   
