---
tags:
  - area
  - poligoni
  - reticolo
  - aggregare
---

# Calcolo area poligoni all'interno di un reticoli

Calcolare l’area delle porzioni di poligoni che ricadono dentro ad una cella di un reticolo.

**Esempio**: lo strato è un _dusaf_ (Destinazione d’Uso dei Suoli Agricoli e forestali ndr), la domanda a cui rispondere è: quanta superficie di quegli usi del suolo ricadono nella singola maglia del reticolo?

[![](../img/esempi/calcolo_area_poligoni_reticolo/calcolo_area_pol1.png)](../img/esempi/calcolo_area_poligoni_reticolo/calcolo_area_pol1.png)

Aggiungere un campo `sup` (tipo Real) nella tabella attributi del layer **reticolo** e popolarlo – usando il calcolatore di campi di QGIS – con la seguente espressione:


[![](../img/esempi/calcolo_area_poligoni_reticolo/calcolo_area_pol2.png)](../img/esempi/calcolo_area_poligoni_reticolo/calcolo_area_pol2.png)

```
aggregate(
layer:='dusaf_5', 
aggregate:='sum',
expression:=area(intersection(geometry(@parent),$geometry )), 
filter:=intersects( $geometry,geometry(@parent)))
```

[![](../img/esempi/calcolo_area_poligoni_reticolo/calcolo_area_pol3.png)](../img/esempi/calcolo_area_poligoni_reticolo/calcolo_area_pol3.png)

La funzione di aggregazione calcola l’area della porzione di dusaf che interseca ogni rettangolo del reticolo e poi somma per ogni rettangolo.

Funzione 

il geopackage è scaricabile [qui](../prova_tu/dati_esempi.zip)

---

Funzioni e variabili utilizzate:

- [aggregate](../gr_funzioni/aggrega/aggrega_unico.md#aggregate)
