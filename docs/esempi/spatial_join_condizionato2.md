---
tags:
  - spatial-join
  - aggregare
  - challenge
---

# Spatial join con condizione

L’unione spaziale di attributi è un problema frequente in ambito GIS - si tratta di trasferire attributi da un layer ad un altro basandosi solo sulle loro reciproche relazioni spaziali, in questo esempio aggiungiamo una difficoltà in più, ovvero, una condizione. 

Il quesito nasce da [questa](https://twitter.com/spatialthoughts/status/1695021747177951435) challenge, proposta da [Ujaval Gandhi](https://twitter.com/spatialthoughts) e chiede:

Collegare ciascuna scuola (schools) all'università (college) più vicina nella stessa regione amministrativa. Vedere l'immagine allegata per l'output desiderato.

[![](https://pbs.twimg.com/media/F4Xs3mOb0AAeO6F?format=jpg&name=large)](https://pbs.twimg.com/media/F4Xs3mOb0AAeO6F?format=jpg&name=largee)

qui i dati: <https://t.co/SyCbIQWnAy>

## Soluzione proposta da Ujaval Gandhi

```

```

nel linguaggio umano:<br>

video youtube: <>

## Soluzione proporta da Totò Fiandaca

nel linguaggio umano:<br>
Crea una variabile e la popola con il valore massimo della popolazione dei punti che ricadono dentro ogni poligono (ma non so ancora il nome della città), quindi ripeto la ricerca creando una mappa (_map("name","pop_max")_) e tra le varie mappe, prendo quella con popolazione maggiore (quest'ultima ricerca la fa array_find).

```
make_line(
  eval('overlay_nearest(\'colleges\',$geometry,filter:=IDp='||"IDp"||')')[0],$geometry)
```
![](https://pbs.twimg.com/media/F4YuPazXsAArWvV?format=jpg&name=large)

Issue <https://github.com/qgis/QGIS/issues/43146>

---

Funzioni e variabili utilizzate:

* [@parent](../gr_funzioni/variabili/parent.md)
* [with_variable](../gr_funzioni/variabili/with_variable.md)
* [aggregate](../gr_funzioni/aggrega/aggrega_unico.md#aggregate)
* [geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)
* [to_string](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#to_string)
* [intersects](../gr_funzioni/geometria/geometria_unico.md#intersects)
* [$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)
* [overlay_contains](../gr_funzioni/geometria/geometria_unico.md#overlay_contains)
* [map](../gr_funzioni/maps/maps_unico.md#map)
* [map_akeys](../gr_funzioni/maps/maps_unico.md#map_akeys)
