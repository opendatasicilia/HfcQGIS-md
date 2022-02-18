---
tags:
  - etichette
  - formattare
  - x
  - y
---

# Etichettare usando attibuto _geometry_

L'attributo _geometry_ è l'unico campo non visibile nella tabella attributi, ma c'è!!!

La geometry è espressa in un modo non comprensibile dall'uomo e quindi si evita di farla vedere, questo attibuto porta con se altri attibuti impliciti alla geometria stessa come:

- nel caso di geometry (MULTI)POINT(ZM): le coordinate x,y,z,m;
- nel caso di geometry (MULTI)LINESTRING(ZM): lunghezza della linea e coordinate dei nodi/vertici;
- nel caso di geometry (MULTI)POLYGON(ZM): area, perimetro e coordinate dei vertici;

le caratteristiche sono sempre richiamabili (se presenti, cioè se ha la Z o m) e quindi non occorre esplicitarle, anzi se esplicitate creano un dataset ridontate.

Un modo per richiamarle è attraverso l'etichettatura:

* caso (MULTI)POINT(ZM):

espressione da scrivere nel calcolatore di campi
****
```
'x= ' || to_int($x)  
|| '\n'  || 
'y= ' || to_int($y)
|| '\n'  || 
'z= ' || z($geometry)
|| '\n'  || 
'm= ' || m($geometry)
```
[![](../img/esempi/etichette/etichette1.png)](../img/esempi/etichette/etichette1.png)

* caso (MULTI)LINESTRING(ZM):

espressione da scrivere nel calcolatore di campi
```
to_int($length)
||'/'|| 
z(start_point($geometry))
```
[![](../img/esempi/etichette/etichette2.png)](../img/esempi/etichette/etichette2.png)

* caso (MULTI)POLYGON(ZM):

espressione da scrivere nel calcolatore di campi
```
'Area= ' || 
 format_number( $area,1) || 
 ' mq'
 ```
 ![](../img/esempi/etichette/etichette3.png)

 Geopackage è [qui](../prova_tu/dati_esempi.zip)

---

Funzioni e variabili utilizzate:

* [to_int](../gr_funzioni/conversioni/conversioni_unico.md#to_int)
* [format_number](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#format_number)
* [\$x](../gr_funzioni/geometria/geometria_unico.md#x)
* [\$y](../gr_funzioni/geometria/geometria_unico.md#y)
* [z](../gr_funzioni/geometria/geometria_unico.md#z)
* [m](../gr_funzioni/geometria/geometria_unico.md#m)
* [\$length](../gr_funzioni/geometria/geometria_unico.md#length)
* [start_point](../gr_funzioni/geometria/geometria_unico.md#start_point)
* [\$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)