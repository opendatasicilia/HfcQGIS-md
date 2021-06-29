Concetti fondamentali sulla `tabella attributi`_ di QGIS
========================================================

La tabella attributi |ico0| (**F6**) è una tabella che contiene i dati
alfanumerici (attributi) dello strato vettoriale e rappresenta una delle
differenze fondamentali tra un vettore CAD e uno GIS.

Negli shapefile la tabella attributi rappresenta il file .dbf che è uno
dei tre file fondamentali che caratterizzano lo shapefile (.shp, .shx,
.dbf) la mancanza di uno di questi rende inutilizzabile lo strato.

Una tabella è caratterizzata da righe (rosso) e colonne (verde), le
righe rappresentano i record (nello specifico una feature), le colonne
(o campi) rappresentano gli attributi:

.. figure:: /img/tabella_attributi/tab_attr1.png
   :alt: tab_attr1

   
Elementi della tabella
----------------------

La tabella attributi di QGIS è caratterizzata da vari elementi:

.. figure:: /img/tabella_attributi/tab_attr2.png
   :alt: tab_attr2

  
1. nell’intestazione della tabella è presente una stringa che da
   informazioni su:

   1. nome della tabella;
   2. totale degli elementi/record/feature;
   3. numero dei record *filtrati*;
   4. numero dei record *selezionati*.

.. figure:: /img/tabella_attributi/tab_attr3_NEW.png
   :alt: tab_attr3


.. _tabella attributi: https://docs.qgis.org/testing/en/docs/user_manual/working_with_vector/attribute_table.html

.. |ico0| image:: /img/tabella_attributi/icon/mActionOpenTable.png

2. barra degli strumenti;

.. raw:: html

    <embed>
        <p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionToggleEditing.png" title="matita per attivare modifica" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>matita per attivare modifica;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionMultiEdit.png" Title="modifica multipla;" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>modifica multipla;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionFileSave.png" Title="salva modifiche" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>salva modifiche;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionDraw.png" Title="aggiorna" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>aggiorna;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionNewTableRow.png" Title="aggiungi elemento (solo alfanumerico)" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>aggiungi elemento (solo alfanumerico)</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionDeleteSelected.png" Title="cancella elemento/i" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>cancella elemento/i;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionEditCut.png" Title="taglia" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>taglia;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionEditCopy.png" Title="copia elemento/i" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>copia elemento/i;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionEditPaste.png" Title="incolla elemento/i" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>incolla elemento/i;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mIconExpressionSelect.png" Title="seleziona elementi tramite espressione" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>seleziona elementi tramite espressione;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionSelectAll.png" Title="seleziona tutto" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>seleziona tutto;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionInvertSelection.png" Title="inverti selezione" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>inverti selezione;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionDeselectAll.png" Title="cancella selezione" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>cancella selezione;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionFilterMap.png" Title="seleziona/filtra" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>seleziona/filtra</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionSelectedToTop.png" Title="sposta la selezione in cima alla tabella" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>sposta la selezione in cima alla tabella;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionPanToSelected.png" Title=" sposta mappa alle righe selezionate" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>sposta mappa alle righe selezionate;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionZoomToSelected.png" Title="zooma mappa alle righe selezionate" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>zooma mappa alle righe selezionate;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionNewAttribute.png" Title="nuovo campo" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>nuovo campo;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionDeleteAttribute.png" Title="elimina campo esistente" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>elimina campo esistente;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionCalculateField.png" Title="apre il calcolatore di campi" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>apre il calcolatore di campi;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionConditionalFormatting.png" Title="formattazione condizionale" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>formattazione condizionale;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mDockify.png" Title="da finestra a dock e viceversa (>= QGIS 3.4)" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>da finestra a dock e viceversa (&gt;=<strong>QGIS 3.4</strong>);</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mAction.png" Title=" azioni" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/>azioni.</p>
    </embed>

.. figure:: /img/tabella_attributi/tab_attr4.png
   :alt: tab_attr4


3. menu filtro:

   1. mostra tutti gli elementi;
   2. mostra gli elementi selezionati;
   3. mostra gli elementi visibili nella mappa;
   4. mostra gli elemeneti modificati ed i nuovi;
   5. filtro campo (elenca tuti i campi presenti nella tabella);
   6. filtro avanzato (tramite espressione).

.. figure:: /img/tabella_attributi/tab_attr5.png
   :alt: tab_attr5

  
4. modalità di visualizzazione della tabella:

.. raw:: html

    <embed>
        <p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionOpenTable.png" title="vista tabella" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/> vista tabella;</p><p><img   class="immagonobox" src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/tabella_attributi/icon/mActionFormView.png" Title="vista modulo" style="float: left; margin-right:8px; display: block; height:24px !important; width:24px !important;"/> vista modulo;</p>
		</embed>
 

.. figure:: /img/tabella_attributi/tab_attr6.png
   :alt: tab_attr6

nella vista modulo è presente un ulterione menu:

1. espressione, permette di creare un filtro tramite una espressione;
2. anteprima colonna;
3. ordina tramite anteprima espressione;
4. storico.

Barra del calcolatore di campi rapida (Quick Field Calculation bar)
-------------------------------------------------------------------

Questa barra è visibile solo se è attiva la modalità modifica |ico25| e
consente di applicare rapidamente calcoli a tutte o parte delle feature
del livello. Questa barra utilizza le stesse espressioni del calcolatore
di campi |ico26|

.. figure:: /img/field_calc_rapida1.png
   :alt: field_calc

Esempio di uso della barra (vedi screenshot sotto):

1. raccoglie tutti i campi della tabella;
2. apre la finestra di dialogo delle espressioni;
3. campo dove digitare numeri, stringhe e forimule/espressioni;
4. aggiorna tutti i record con il valore immesso nella 3;
5. aggiorna solo le righe selezionate con il valore immesso nella 3;

nel nostro caso (vedi screenshot sotto), se cliccassi su 4 (aggiorna
tutto) aggiornerei tutti i valori del campo “COD_REG” con il valore 19;
se cliccassi su 5 (Aggiorna selezione) aggiornerei solo le quattro righe
selezionate.

.. figure:: /img/tabella_attributi/tab_attr11.png
   :alt: tab_attr11


.. |ico25| image:: /img/tabella_attributi/icon/mActionToggleEditing.png
.. |ico26| image:: /img/tabella_attributi/icon/mActionCalculateField.png

Interagire con il corpo della tabella
-------------------------------------

È possibile interagire con il corpo della tabella usando il tasto destro
del mouse: sulla intestazione dei campi oppure sulle celle:

.. figure:: /img/tabella_attributi/tab_attr8.png
   :alt: tab_attr8

nel caso dell’\ *intestazione colonna* compare un tendina con la
possibilità di: nascondere la colonna; definire la larghezza della
colonna; autodimensiona la larghezza colonna; Organizza le colonne;
Ordina

.. figure:: /img/tabella_attributi/tab_attr9.png
   :alt: tab_attr9

.. figure:: /img/tabella_attributi/tab_attr10.png
   :alt: tab_attr10

nel caso delle *celle* (vedi screen sotto) compare un tendina con la possibilità di:selezionare tutte le righe (Ctrl+A); Copiare il contenuto della cella; Zoom alla geometria; Pan alla geometria; Flash geometria;
Apri modalità Modulo |ico27|

.. figure:: /img/tabella_attributi/tab_attr7.png
   :alt: tab_attr7

Novità introdotta nella QGIS 3.4:
---------------------------------

nuovo pulsante nella barra degli strumenti della tabella degli attributi
per passare dalla modalità docked alla modalità finestra

.. figure:: /img/tabella_attributi/dockify.gif
   :alt: tab_attr12

.. |ico27| image:: /img/tabella_attributi/icon/mActionFormView.png

Novità introdotta nella QGIS 3.8 Zanzibar:
---------------------------------

in modalità `modulo` introdotta la possibilità di sfogliare i record
con Zoom, centramento feature e lampeggio

.. figure:: /img/novita_38/sfoglia.gif
   :alt: tab_attr12
   
Novità introdotta nella QGIS 3.12 xxxxxx:
---------------------------------

possibilità di salvare le `espressioni utente`_
le espressioni sono memorizzate nel profilo utente

.. figure:: /img/novita_312/espressioni_utente.gif
   :alt: tab_attr12

.. _espressioni utente: https://pigrecoinfinito.com/2019/12/14/field-calc-di-qgis-save-expressions-crowdfunding/
