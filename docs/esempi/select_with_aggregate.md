---
tags:
  - selezionare
  - aggregare
  - area
---

# Selezionare tramite funzioni di aggregazione - caso minimun

Facciamo un esempio, uso vettore _province_g_ del geopackage allegato e seleziono i comuni che hanno superficie più piccola per ogni provincia: 

seleziono (nel panel layer) il layer dove effettuare la selezione e premo il tasto funzione **F3** oppure come da figura sotto:

[![](../img/esempi/select_with_aggregate/sel_minimum2.png)](../img/esempi/select_with_aggregate/sel_minimum2.png)

scrivo l'espressione:

```
$area = minimum($area, group_by:= "COD_PROV" )
```
e poi clicco su (2) _seleziona elementi_:

[![](../img/esempi/select_with_aggregate/sel_minimum1.png)](../img/esempi/select_with_aggregate/sel_minimum1.png)

il geopackage è scaricabile [qui](../prova_tu/dati_esempi.zip)

---

Funzioni e variabili utilizzate:

* [\$area](../gr_funzioni/geometria/geometria_unico.md#area)
* [minimum](../gr_funzioni/aggrega/aggrega_unico.md#minimum)
* [uguale](../gr_funzioni/operatore/operatore_unico.md#uguale)