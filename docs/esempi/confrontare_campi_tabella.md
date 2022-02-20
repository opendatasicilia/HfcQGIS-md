---
tags:
  - attributi
  - array
  - tabella
  - valori
  - confrontare
---

# Confrontare due campi tabella attributi

Ho una tabella con due campi che raccolgono una lista di numeri di fogli catastali, come confrontarle e estrarre solo i numeri fogli uguali?

![](https://user-images.githubusercontent.com/7631137/135644652-eb6a065f-5861-47c8-8384-d9ce5b9413b7.png)

## Espressioni di QGIS

Importo la tabella in QGIS come testo delimitato, creo una colonna testo `output` e la popolo con la seguente espressione:

```
array_to_string(
    array_majority( array_cat(
      string_to_array(replace("fogli1",'-',',')),
      string_to_array(replace("fogli2",'-',','))
)))
```

Tradotto in linguaggio umano:<br>
Trasforma i valori dei due campi in `array` (`string_to_array(replace("fogli1",'|',','))`) e poi concatenali (`array_cat`), cioè crea unico `array`, successivamente estrai l'array dei valori che maggiormente sono presenti (`array_majority`), infine converti l'array in stringa.

## provaci tu

[qui](https://github.com/opendatasicilia/tansignari/files/7268411/test_qgis3.txt) file di esempio

---

Funzioni e variabili utilizzate:

* [array_to_string](../gr_funzioni/array/array_unico.md#array_to_string)
* [array_majority](../gr_funzioni/array/array_unico.md#array_majority)
* [array_cat](../gr_funzioni/array/array_unico.md#array_cat)
* [string_to_array](../gr_funzioni/arrayarray_unico.md#string_to_array)
