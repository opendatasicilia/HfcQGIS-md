---
tags:
  - fieldCalc
  - propedeutico
---

# Calcolatore di campi

!!! Abstract "Intro"
    **Il pulsante ![calc](https://docs.qgis.org/testing/en/_images/mActionCalculateField.png) nella tabella degli attributi consente di eseguire calcoli sulla base di valori di attributo esistenti o funzioni definite, ad esempio, per calcolare la lunghezza o l'area delle caratteristiche geometriche. I risultati possono essere scritti in un nuovo campo di attributo, un campo virtuale, oppure possono essere utilizzati per aggiornare i valori in un campo esistente.**

## Perché usarlo

Il **Field Calc** di **QGIS** ha oltre 400 funzioni (in evoluzione) e di queste oltre 140[^1] sono funzioni geometriche. Tutta questa potenza di calcolo permette di risolvere molti problemi GIS come la vicinanza, sovrapposizione, aggregazioni, selezioni ecc... inoltre permette di **scrivere/aggiornare** i risultati di espressioni direttamente nella tabella degli attributi senza creare altri layer.

## Dove usarlo

Il calcolatore di campi è ora disponibile su qualsiasi livello che supporti la modifica[^2]. Il Calcolatore in realtà è solo una interfaccia che ci permette di accedere alle funzioni e di creare semplici o complesse espressioni. Le espressioni di QGIS vengono utilizzate in molti contesti, per esempio:

1. [tabella degli attributi](../esempi/trova_nella_tabella_attributi.md);
2. [tematizzazione](../esempi/tematizzare.md);
3. [etichettatura](../esempi/etichette.md);
4. [sovrascrittura definita dai dati](../esempi/nascondi_etichette.md);
5. [selezione](../esempi/selezionare_punti_vicini_punto.md);
6. [compositore di stampe, atlas e report](../esempi/atlas_righe_verticale.md);
7. [legenda](../esempi/espressione_regolare.md);
8. strumenti di processing: ([Calcolatore campi](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectortable.html#qgisfieldcalculator); [Seleziona tramite espressione](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorselection.html#qgisselectbyexpression); [Estrai tramite espressione](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorselection.html#qgisextractbyexpression); [Geometria da espressione](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#qgisgeometrybyexpression); [Ordina tramite espressione](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html#qgisorderbyexpression)); 
9. [moduli inserimento dati e widget](../esempi/drilldown_form_multiple.md);
10. azioni;
11. modellatore grafico;
12. diagrammi;
13. filtri;
14. decorazioni;
15. proprietà layer: variabili;
16. statistiche;
17. suggerimenti mappa;
18. plugin;
19. ecc..

## Campo virtuale

Un [campo virtuale](../esempi/add_campo_virtuale.md) è un campo basato su un'espressione calcolata al volo, il che significa che il suo valore viene automaticamente aggiornato non appena il parametro sottostante cambia. L'espressione è impostata una volta; non è più necessario calcolare nuovamente il campo se i valori sottostanti cambiano. Ad esempio, è possibile utilizzare un campo virtuale se è necessario calcolare i valori dell'area durante un processo di digitalizzazione (creazione, unione, divisione di feature) o calcolare una durata che deve essere aggiornata di volta in volta.

## Aggiorna geometria

Attraverso il calcolatore di campi è possibile aggiornare tutti gli attributi di un layer editabile, ma è possibile anche [aggiornare la geometria](../esempi/agg_geom.md), per esempio diminuire il numero di vertici di una linea o di un poligono; spostare/traslare i punti ecc...

## Field Calc rapido

La barra del _calcolatore di campo rapido_, nella parte superiore della tabella degli attributi, è visibile solo se il livello è modificabile:

[![field_calc](../img/field_calc_rapida1.png)](../img/field_calc_rapida1.png)

[^1]: nella versione QGIS 3.24
[^2]: sono layer vettoriali e semplici tabelle editabili