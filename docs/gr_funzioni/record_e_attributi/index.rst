Record ed attributi
===================================

===================

Questo gruppo contiene funzioni e/o espressioni che agiscono sui record
o attributi. Es.: $id; get_feature().

+-----------------------------------+-----------------------------------+
| Funzione                          | Descrizione                       |
+===================================+===================================+
| `$currentfeature`_                | Restituisce l'elemento corrente   |
|                                   | corrente da valutare. Questo può  |
|                                   | essere usato con la funzione      |
|                                   | 'attribute' per valutare i valori |
|                                   | dell'attributo dall'elemento      |
|                                   | corrente                          |
+-----------------------------------+-----------------------------------+
| `$id`_                            | Restituisce l'id geometria della  |
|                                   | riga corrente                     |
+-----------------------------------+-----------------------------------+
| `attribute`_                      | Restituisce il valore di un       |
|                                   | attributo specificato da una      |
|                                   | geometria                         |
+-----------------------------------+-----------------------------------+
| `get_feature`_                    | Restituisce la prima geometria di |
|                                   | un vettore che corrisponde a un   |
|                                   | determinato valore di attributo   |
+-----------------------------------+-----------------------------------+
| `get_feature_by_id`_              | Restituisce l'id dell'elemento    |
|                                   | della riga corrente               |
+-----------------------------------+-----------------------------------+
| `is_selected`_                    | Indica se una geometria è         |
|                                   | selezionata. Se chiamata senza    |
|                                   | parametri, controlla la geometria |
|                                   | corrente                          |
+-----------------------------------+-----------------------------------+
| `num_selected`_                   | Restituisce il numero di          |
|                                   | geometrie selezionate in un       |
|                                   | vettore dato. Per impostazione    |
|                                   | predefinita funziona sul vettore  |
|                                   | sul quale l'espressione è         |
|                                   | valutata                          |
+-----------------------------------+-----------------------------------+
| `represent_value`_                | Restituisce il valore di          |
|                                   | rappresentazione configurato per  |
|                                   | un valore di campo. Dipende dal   |
|                                   | tipo di widget configurato.       |
|                                   | Spesso, questo è utile per i      |
|                                   | widget di 'Value Map'             |
+-----------------------------------+-----------------------------------+
| `uuid`_                           | Genera un Identificatore          |
|                                   | Universale Unico (UUID) per ogni  |
|                                   | riga usando il metodo Qt          |
|                                   | QUuid::createUuid. Ciascun UUID è |
|                                   | lungo 38                          |
+-----------------------------------+-----------------------------------+

|image0|

.. _$currentfeature: $currentfeature.html
.. _$id: $id.html
.. _attribute: attribute.html
.. _get_feature: get_feature.html
.. _get_feature_by_id: get_feature_by_id.html
.. _is_selected: is_selected.html
.. _num_selected: num_selected.html
.. _represent_value: represent_value.html
.. _uuid: uuid.html

.. |image0| image:: /img/record_e_attributi/gruppo_record_e_attributi1.png

**Elenco funzioni Record ed attributi**
   
.. toctree::
   :maxdepth: 3
   
   $currentfeature
   $id
   attribute
   get_feature
   get_feature_by_id
   is_selected
   num_selected
   represent_value
   uuid
   
