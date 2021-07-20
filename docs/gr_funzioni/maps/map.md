# map

Restituisce una mappa con tutte le chiavi ed i valori passati come coppie di parametri.

Sintassi:

map(_<span style="color:red;">key1</span>_, _<span style="color:red;">value1</span>_, _<span style="color:red;">key2</span>_, _<span style="color:red;">value2</span>_ , …_)

Argomenti:

* _<span style="color:red;">key</span>_ una chiave (stringa)
* _<span style="color:red;">value</span>_ un valore

Esempi:

```
map('1','one','2', 'two') → map: 1: 'one', 2: 'two'
```

![](../../img/maps/map/map1.png)
--

Altri esempi:

Definisco una _map_ con:

* chiave **Area_Ha**  -- Area in Ettari
* valore **$area/10000**
* chiave **Perimetro_km**  -- Perimetro in km
* valore **$perimeter/1000**

![](../../img/maps/map/map2.png)

