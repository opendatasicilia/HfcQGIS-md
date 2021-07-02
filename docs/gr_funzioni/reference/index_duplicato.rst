Reference
===================================

Questo gruppo è presente SOLO dopo aver installato il `plugin`_
*refFunctions*. Plugin che aggiunge funzioni utente personalizzate al
calcolatore di campi di QGIS per fare riferimento, analiticamente o
spazialmente, tra i livelli, ad esempio recuperare un valore da un
livello usando come valore di campo o una condizione spaziale
(interseca, disgiunti ....) come parametro.

+-----------------------------------+-----------------------------------+
| Funzione                          | Descrizione                       |
+===================================+===================================+
| Funzioni della tabella:           |                                   |
+-----------------------------------+-----------------------------------+
| `dbvalue`_                        | Recupera il primo valore          |
|                                   | targetField da targetLayer quando |
|                                   | keyField è uguale a               |
|                                   | conditionValue                    |
+-----------------------------------+-----------------------------------+
| `dbvaluebyid`_                    | Recupera il valore targetField da |
|                                   | targetLayer usando l'ID della     |
|                                   | caratteristica interna            |
+-----------------------------------+-----------------------------------+
| `dbquery`_                        | Recupera il primo valore          |
|                                   | targetField da targetLayer quando |
|                                   | whereClause è true                |
+-----------------------------------+-----------------------------------+
| `dbsql`_                          | Recupera i risultati dalla query  |
|                                   | SQL                               |
+-----------------------------------+-----------------------------------+
| Funzioni WKT:                     |                                   |
+-----------------------------------+-----------------------------------+
| `WKTcentroid`_                    | Restituisce il centro di massa    |
|                                   | della geometria data come         |
|                                   | geometria del punto WKT           |
+-----------------------------------+-----------------------------------+
| `WKTpointonsurface`_              | Restituisce il punto all'interno  |
|                                   | della geometria data              |
+-----------------------------------+-----------------------------------+
| `WKTlenght`_                      | Restituisce la lunghezza della    |
|                                   | geometria WKT fornita             |
+-----------------------------------+-----------------------------------+
| `WKTarea`_                        | Restituisce l'area della          |
|                                   | geometria WKT indicata            |
+-----------------------------------+-----------------------------------+
| Funzioni geometriche:             |                                   |
+-----------------------------------+-----------------------------------+
| `geomRedef`_                      | ridefinire la geometria della     |
|                                   | feature corrente con una nuova    |
|                                   | geometria WKT (sperimentale!)     |
+-----------------------------------+-----------------------------------+
| `geomnearest`_                    | Recupera il valore del campo      |
|                                   | target dalla funzione di          |
|                                   | destinazione più vicina nel       |
|                                   | livello di destinazione           |
+-----------------------------------+-----------------------------------+
| `geomdistance`_                   | Recupera il valore del campo      |
|                                   | target dalla funzione target nel  |
|                                   | livello di destinazione se la     |
|                                   | funzione target è in distanza     |
+-----------------------------------+-----------------------------------+
| `geomwithin`_                     | Recupera il valore del campo      |
|                                   | obiettivo quando la funzione di   |
|                                   | origine si trova all'interno      |
|                                   | della funzione di destinazione    |
|                                   | nel livello di destinazione       |
+-----------------------------------+-----------------------------------+
| `geomtouches`_                    | Recupera il valore del campo      |
|                                   | obiettivo quando la funzione      |
|                                   | sorgente tocca la funzione di     |
|                                   | destinazione nel livello di       |
|                                   | destinazione                      |
+-----------------------------------+-----------------------------------+
| `geomintersects`_                 | Recupera il valore del campo      |
|                                   | obiettivo quando la               |
|                                   | caratteristica sorgente interseca |
|                                   | la caratteristica obiettivo nel   |
|                                   | livello di destinazione           |
+-----------------------------------+-----------------------------------+
| `geomcontains`_                   | Recupera il valore del campo      |
|                                   | obiettivo quando la funzione di   |
|                                   | origine contiene la funzione di   |
|                                   | destinazione nel livello di       |
|                                   | destinazione                      |
+-----------------------------------+-----------------------------------+
| `geomcwithin`_                    | Recupera il valore del campo      |
|                                   | obiettivo quando la funzione di   |
|                                   | origine è disgiunta dalla         |
|                                   | funzione di destinazione nel      |
|                                   | livello di destinazione           |
+-----------------------------------+-----------------------------------+
| `geomequals`_                     | Recupera il valore del campo      |
|                                   | obiettivo quando la funzione di   |
|                                   | origine è uguale alla funzione di |
|                                   | destinazione nel livello di       |
|                                   | destinazione                      |
+-----------------------------------+-----------------------------------+
| `geomoverlaps`_                   | Recupera il valore del campo      |
|                                   | obiettivo quando la funzione      |
|                                   | sorgente si sovrappone alla       |
|                                   | funzione di destinazione nel      |
|                                   | livello di destinazione           |
+-----------------------------------+-----------------------------------+
| `geomcrosses`_                    | Recupera il valore del campo      |
|                                   | obiettivo quando la               |
|                                   | caratteristica sorgente           |
|                                   | attraversa la caratteristica      |
|                                   | obiettivo nel livello di          |
|                                   | destinazione                      |
+-----------------------------------+-----------------------------------+

|image0|

.. |image0| image:: /img/reference/gruppo_reference1.png

.. _dbvalue: dbvalue.html
.. _dbvaluebyid: dbvaluebyid.html
.. _dbquery: dbquery.html
.. _dbsql: dbsql.html
.. _WKTcentroid: WKTcentroid.html
.. _WKTpointonsurface: WKTpointonsurface.html
.. _WKTlenght: WKTlenght.html
.. _WKTarea: WKTarea.html
.. _geomRedef: geomRedef.html
.. _geomnearest: geomnearest.html
.. _geomdistance: geomdistance.html
.. _geomwithin: geomwithin.html
.. _geomtouches: geomtouches.html
.. _geomintersects: geomintersects.html
.. _geomcontains: geomcontains.html
.. _geomcwithin: geomcwithin.html
.. _geomequals: geomequals.html
.. _geomoverlaps: geomoverlaps.html
.. _geomcrosses: geomcrosses.html
.. _plugin: https://geogear.wordpress.com/2014/11/13/reffunctions-v1-0/

.. toctree::
   :maxdepth: 3
   :hidden:
   
   dbquery
   dbsql
   dbvalue
   dbvaluebyid
   geomcontains
   geomcrosses
   geomdistance
   geomequals
   geomintersects
   geomnearest
   geomoverlaps
   geomredef
   geomtouches
   geomwithin
   wktarea
   wktcentroid
   wktlenght
   wktpointonsurface  
   
