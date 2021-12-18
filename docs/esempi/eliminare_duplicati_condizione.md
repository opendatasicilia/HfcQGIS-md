# Rimuovere elementi duplicati in base a una condizione su un'altra colonna di attributi

gis.stackexchange : <https://gis.stackexchange.com/questions/419159/removing-duplicate-features-based-on-a-condition-on-another-attribute-column-in>

Rimuovere elementi duplicati in base a una condizione su un’altra colonna di attributi in QGIS. Esempio, tabella degli attributi di uno shapefile poligonale:

![](https://pigrecoinfinito.files.wordpress.com/2021/12/image-10.png)

## Selezione per espressione

```
Column_A != minimum (Column_A, group_by:=Column_B)
```

In linguaggio umano:

Seleziona tutte le righe per cui la `Column_A` è diversa `!=` dal valore minimo `minumum` calcolato nel campo `Column_A` dopo aver raggruppato usando i valori della `Column_B`.

Si utilizza il `!=` in quanto occorre rimuovere i dati duplicati.

## Geoprocessing

Utilizzando l'algoritmo `aggrega`:

![](https://pigrecoinfinito.files.wordpress.com/2021/12/image-11.png)

espressione utilizzata:

```
with_variable(
    'cucu',
    array_agg( "Column_A" , "Column_B" ),
array_agg( "Column_C" , "Column_B" )
                          [array_find(@cucu,array_min(@cucu))]
                     )
```

per maggiori info, leggi qui: <https://pigrecoinfinito.com/2021/12/18/rimozione-di-elementi-duplicati-in-base-a-una-condizione-su-unaltra-colonna-di-attributi-in-qgis/>

il file di esempio è scaricabile [qui](https://gist.github.com/pigreco/0ad8205396093557dad8b2d3864a6ddf)

---

Funzioni e variabili utilizzate:

* [minimum](../gr_funzioni/aggrega/aggrega_unico.md#minimum)
* [uguale](../gr_funzioni/operatore/operatore_unico.md#uguale)
* [array_agg](../gr_funzioni/array/array_unico.md#array_agg)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [with_variable](../gr_funzioni/variabili/with_variable.md)