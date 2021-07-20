# map_delete

Restituisce una mappa con il valore della corrispondente chiave passata rimosso.

Sintassi:

map_delete(_<span style="color:red;">map</span>_, _<span style="color:red;">key</span>_)

Argomenti:

* _<span style="color:red;">map</span>_ una mappa
* _<span style="color:red;">key</span>_ la chiave da rimuovere

Esempi:

```
map_delete(map('1','one','2','two'),'2') → map: 1: 'one'
```

![](../../img/maps/map_delete/map_delete1.png)

---
