# Concetti fondamentali sulla tabella degli attributi di QGIS

!!! Abstract "Intro"
    **In questa sezioni sono raccolti i concetti fondamentali sulla tabella degli attributi. La conoscenza di questi concetti permette di velocizzare il lavoro e capire il comportamento della tabella.**

[QGIS-DOC](https://docs.qgis.org/3.16/it/docs/user_manual/working_with_vector/attribute_table.html)

La tabella degli attributi ![ico](../img/tabella_attributi/icon/mActionOpenTable.png) (**F6**) è una tabella che contiene i dati alfanumerici (attributi) dello strato vettoriale e rappresenta una delle differenze fondamentali tra un vettore CAD e uno GIS.

Negli shapefile la tabella degli attributi rappresenta il file `.dbf` che è uno dei tre file fondamentali che caratterizzano lo shapefile (.shp, .shx, .dbf) la mancanza di uno di questi rende inutilizzabile lo strato.

Una tabella è caratterizzata da righe (rosso) e colonne (verde), le righe rappresentano i record (nello specifico una feature), le colonne (o campi) rappresentano gli attributi:

[![tab_attr](../img/tabella_attributi/tab_attr1.png)](../img/tabella_attributi/tab_attr1.png)

**Osservazione**: la geometria è anch'essa un attributo (speciale) ma non viene visualizzato nella tabella degli attributi per scelta degli sviluppatori. Per richimare tale attributo basta utilizzare `$geometry`.

## Elementi della tabella

La tabella attributi di QGIS è caratterizzata da vari elementi:

[![tab_attr](../img/tabella_attributi/tab_attr2.png)](../img/tabella_attributi/tab_attr2.png)

1. nell'intestazione della tabella è presente una stringa che da informazioni su:
    1. nome della tabella;
    2. totale degli elementi/record/feature;
    3. numero dei record _filtrati_;
    4. numero dei record _selezionati_.
   

[![tab_attr](../img/tabella_attributi/tab_attr3.png)](../img/tabella_attributi/tab_attr3.png)

2. barra degli strumenti;
    * ![ico](../img/tabella_attributi/icon/mActionToggleEditing.png) matita per attivare modifica;
    * ![ico](../img/tabella_attributi/icon/mActionMultiEdit.png) modifica multipla;
    * ![ico](../img/tabella_attributi/icon/mActionFileSave.png) salva modifiche;
    * ![ico](../img/tabella_attributi/icon/mActionDraw.png) aggiorna;
    * ![ico](../img/tabella_attributi/icon/mActionNewTableRow.png) aggiungi elemento (solo alfanumerico):

    ![tab_attr](../img/tabella_attributi/tab_attr32.png)

    * ![ico](../img/tabella_attributi/icon/mActionDeleteSelected.png) cancella elemento/i;
    * ![ico](../img/tabella_attributi/icon/mActionEditCut.png ) taglia;
    * ![ico](../img/tabella_attributi/icon/mActionEditCopy.png) copia elemento/i;
    * ![ico](../img/tabella_attributi/icon/mActionEditPaste.png) incolla elemento/i;
    * ![ico](../img/tabella_attributi/icon/mIconExpressionSelect.png) seleziona elementi tramite espressione;
    * ![ico](../img/tabella_attributi/icon/mActionSelectAll.png) seleziona tutto;
    * ![ico](../img/tabella_attributi/icon/mActionInvertSelection.png) inverti selezione;
    * ![ico](../img/tabella_attributi/icon/mActionDeselectAll.png) cancella selezione;
    * ![ico](../img/tabella_attributi/icon/mActionFilterMap.png) seleziona/filtra;
    * ![ico](../img/tabella_attributi/icon/mActionSelectedToTop.png ) sposta la selezione in cima alla tabella;
    * ![ico](../img/tabella_attributi/icon/mActionPanToSelected.png) sposta mappa alle righe selezionate;
    * ![ico](../img/tabella_attributi/icon/mActionZoomToSelected.png) zooma mappa alle righe selezionate;
    * ![ico](../img/tabella_attributi/icon/mActionNewAttribute.png) nuovo campo;
    * ![ico](../img/tabella_attributi/icon/mActionDeleteAttribute.png) elimina campo esistente;
    * ![ico](../img/tabella_attributi/icon/mActionCalculateField.png) apre il calcolatore di campi;
    * ![ico](../img/tabella_attributi/icon/mActionConditionalFormatting.png) formattazione condizionale;
    * ![tab_attr](../img/tabella_attributi/icon/mDockify.png) da finestra a dock e viceversa (**>= QGIS 3.4**)
    * ![ico](../img/tabella_attributi/icon/mAction.png) azioni.

[![tab_attr](../img/tabella_attributi/tab_attr4.png)](../img/tabella_attributi/tab_attr4.png)

3. menu filtro:
    1. ![](../img/tabella_attributi/icon/mActionOpenTable.png) Mostra tutti gli Elementi;
    2. ![](../img/icon/mActionOpenTableSelected.png) Mostra gli Elementi Selezionati;
    3. ![](../img/icon/mActionOpenTableVisible.png) Mostra gli Elementi Visibili nella Mappa;
    4. ![](../img/icon/mActionOpenTableEdited.png) Mostra gli Elementi Modificati ed i Nuovi;
    5. Filtro Campo (elenca tutti i campi presenti nella tabella);
    6. ![](../img/icon/mActionFilterMap.png) Filtro Avanzato (tramite espressione);
    7. ![](../img/icon/mActionHandleStoreFilterExpressionChecked.png) Espressioni Filtro Salvate.

[![tab_attr](../img/tabella_attributi/tab_attr5.png)](../img/tabella_attributi/tab_attr5.png)

4. modalità di visualizzazione della tabella:
    * ![ico](../img/tabella_attributi/icon/mActionOpenTable.png)  vista tabella;
    * ![ico](../img/tabella_attributi/icon/mActionFormView.png) vista modulo:

[![tab_attr](../img/tabella_attributi/tab_attr6.png)](../img/tabella_attributi/tab_attr6.png)

nella **Vista Modulo** è presente un ulterione menu:

1. ![](../img/icon/mIconExpressionFilter.png) Espressione, permette di creare un filtro tramite una espressione;
2. anteprima colonna;
3. ![](../img/icon/sort.png) Ordina...;
4. storico.

## Calcolatore di campi rapido

Questa barra è visibile solo se è attiva la modalità modifica ![ico](../img/tabella_attributi/icon/mActionToggleEditing.png) e consente di applicare rapidamente calcoli a tutte o parte delle feature del livello. Questa barra utilizza le stesse espressioni del calcolatore di campi ![ico](../img/tabella_attributi/icon/mActionCalculateField.png)

[![field_calc](../img/field_calc_rapida1.png)](../img/field_calc_rapida1.png)

Esempio di uso della barra (vedi screenshot sotto):

1. raccoglie tutti i campi della tabella;
2. apre la finestra di dialogo delle espressioni;
3. campo dove digitare numeri, stringhe e forimule/espressioni;
4. aggiorna tutti i record con il valore immesso nella 3;
5. aggiorna solo le righe selezionate con il valore immesso nella 3;

nel nostro caso (vedi screenshot sotto), se cliccassi su 4 (aggiorna tutto) aggiornerei tutti i valori del campo "COD_REG" con il valore 19; se cliccassi su 5 (Aggiorna selezione) aggiornerei solo le quattro righe selezionate.

[![tab_attr](../img/tabella_attributi/tab_attr11.png)](../img/tabella_attributi/tab_attr11.png)

## Corpo della tabella

È possibile interagire con il corpo della tabella usando il tasto destro del mouse: sulla intestazione dei campi oppure sulle celle:

[![tab_attr](../img/tabella_attributi/tab_attr8.png)](../img/tabella_attributi/tab_attr8.png)

nel caso dell'_intestazione colonna_ compare un tendina con la possibilità di: 
1. nascondere la colonna; 
2. definire la larghezza della colonna;
3. Imposta Tutte le larghezze di Colonna (>= QGIS 3.18) 
4. autodimensiona la larghezza colonna; 
5. Autodimensione Tutte le Colonne (>= QGIS 3.18)
6. Organizza le colonne; 
7. Ordina.

[![tab_attr](../img/tabella_attributi/tab_attr9.png)](../img/tabella_attributi/tab_attr9.png)

[![tab_attr](../img/tabella_attributi/tab_attr10.png)](../img/tabella_attributi/tab_attr10.png)


nel caso delle _celle_ (vedi screen sotto) compare un tendina con la possibilità di: 
1. selezionare tutte le righe (Ctrl+A); 
2. Copiare il contenuto della cella; 
3. Zoom alla Geometria;
4. Sposta alla Geometria;
5. Lampeggia Geometria;
6. Apri modalità Modulo ![ico](../img/tabella_attributi/icon/mActionFormView.png)

PS: Find/Replace è un plugin!

[![tab_attr](../img/tabella_attributi/tab_attr7.png)](../img/tabella_attributi/tab_attr7.png)

## dockify tabella

nuovo pulsante (Novità introdotta nella QGIS 3.4) nella barra degli strumenti della tabella degli attributi per passare dalla modalità docked alla modalità finestra

[![tab_attr](../img/tabella_attributi/dockify.gif)](../img/tabella_attributi/dockify.gif)

## Memorizza Filtro tabella attributi

[Salva Filtro](https://github.com/qgis/QGIS/pull/31349)

![screen](https://user-images.githubusercontent.com/28384354/63512424-1aa32d80-c4e4-11e9-96f8-505d9544db8e.gif)

## Opzioni Extra Apertura Tabella

[PR](https://github.com/qgis/QGIS/pull/42026) >= QGIS 3.20

![](../img/tabella_attributi/nuove_icone.png)

## Mostra nella Tabella

[Mostra nella Tabella](https://github.com/qgis/QGIS/pull/46328) >= QGIS 3.24

![](../img/tabella_attributi/mostra_tabella.gif)
