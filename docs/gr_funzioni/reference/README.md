# Reference

Questo gruppo è presente SOLO dopo aver installato il [plugin](https://geogear.wordpress.com/2014/11/13/reffunctions-v1-0/) _refFunctions_. Plugin che aggiunge funzioni utente personalizzate al calcolatore di campi di QGIS per fare riferimento, analiticamente o spazialmente, tra i livelli, ad esempio recuperare un valore da un livello usando come valore di campo o una condizione spaziale (interseca, disgiunti ....) come parametro.

 Funzione  | Descrizione
:----------:|:-----------
Funzioni della tabella:|
[dbvalue](dbvalue.html) | Recupera il primo valore targetField da targetLayer quando keyField è uguale a conditionValue
[dbvaluebyid](dbvaluebyid.html) | Recupera il valore targetField da targetLayer usando l'ID della caratteristica interna
[dbquery](dbquery.html) | Recupera il primo valore targetField da targetLayer quando whereClause è true
[dbsql](dbsql.html) | Recupera i risultati dalla query SQL
Funzioni WKT:|
[WKTcentroid](WKTcentroid.html)| Restituisce il centro di massa della geometria data come geometria del punto WKT
[WKTpointonsurface](WKTpointonsurface.html) | Restituisce il punto all'interno della geometria data
[WKTlenght](WKTlenght.html) | Restituisce la lunghezza della geometria WKT fornita
[WKTarea](WKTarea.html) | Restituisce l'area della geometria WKT indicata
Funzioni geometriche:|
[geomRedef](geomRedef.html) | ridefinire la geometria della feature corrente con una nuova geometria WKT (sperimentale!)
[geomnearest](geomnearest.html) | Recupera il valore del campo target dalla funzione di destinazione più vicina nel livello di destinazione
[geomdistance](geomdistance.html) | Recupera il valore del campo target dalla funzione target nel livello di destinazione se la funzione target è in distanza
[geomwithin](geomwithin.html) | Recupera il valore del campo obiettivo quando la funzione di origine si trova all'interno della funzione di destinazione nel livello di destinazione
[geomtouches](geomtouches.html) | Recupera il valore del campo obiettivo quando la funzione sorgente tocca la funzione di destinazione nel livello di destinazione
[geomintersects](geomintersects.html) | Recupera il valore del campo obiettivo quando la caratteristica sorgente interseca la caratteristica obiettivo nel livello di destinazione
[geomcontains](geomcontains.html) | Recupera il valore del campo obiettivo quando la funzione di origine contiene la funzione di destinazione nel livello di destinazione
[geomcwithin](geomcwithin.html) | Recupera il valore del campo obiettivo quando la funzione di origine è disgiunta dalla funzione di destinazione nel livello di destinazione
[geomequals](geomequals.html) | Recupera il valore del campo obiettivo quando la funzione di origine è uguale alla funzione di destinazione nel livello di destinazione
[geomoverlaps](geomoverlaps.html) | Recupera il valore del campo obiettivo quando la funzione sorgente si sovrappone alla funzione di destinazione nel livello di destinazione
[geomcrosses](geomcrosses.html) | Recupera il valore del campo obiettivo quando la caratteristica sorgente attraversa la caratteristica obiettivo nel livello di destinazione
[geomdisjoint](geomdisjoint.html)|Recupera il valore del campo obiettivo quando la funzione di origine è disgiunta dalla funzione di destinazione nel livello di destinazione
[intersecting_geom_count](intersecting_geom_count.html)|Ottieni il conteggio delle funzionalità nel livello di destinazione intersecate dalla funzione di origine
[intersecting_geom_sum](intersecting_geom_sum.html)|Somma gli attributi delle geometrie del livello di destinazione intersecati dalla funzione di origine

![](../../img/reference/gruppo_reference1.png)
