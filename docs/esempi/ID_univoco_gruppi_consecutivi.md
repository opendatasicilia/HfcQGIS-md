# ID univoco per gruppi consecutivi

L'esempio è preso da qui:

**stackexchange**: <https://gis.stackexchange.com/questions/418137/adding-unique-id-for-consecutive-groups-using-field-calculator-in-qgis>

ovvero, come creare un campo `group1` che contenga `ID` univoco per gruppi consecutivi (vedi immagine e numeri in bianco)

![](https://i.stack.imgur.com/53mF9.jpg)

```
with_variable('cucu',
   aggregate( 
		layer:=@layer_name,
   		aggregate:='array_agg',
   		expression:= (array_find(array_agg("ID", "PortCluster_ID"),"ID"))-"ID"),
with_variable('cucu2',
   (array_find(array_agg("ID", "PortCluster_ID"),"ID"))-"ID",
   array_find(array_distinct(@cucu),@cucu2)+1))
```

risultato:

![](https://i.stack.imgur.com/eBtZR.png)

In linguaggio umano:

- Primo passo, creare un campo `temp1` e popolarlo con `array_agg("ID", "PortCluster_ID")`, ovvero, aggrego tutti gli `ID` ragguppandoli per `PortCluster_ID` (per poterlo visualizzare devo usare anche la funzione `array_to_string`, quindi: `array_to_string(array_agg("ID", "PortCluster_ID"))`);
- secondo passo, creo un campo `temp2` e lo popolo con l'indice che possiede il valore del campo `ID` dentro l'array calcolato nel campo `temp1` usando l'espressione `array_find(array_agg("ID", "PortCluster_ID"),"ID"))`;
- terzo passo, faccio la differenza tra il campo `temp2` e il campo `ID`;
- quarto passo, creo un array del campo `temp3` usando la funzione `aggregate` (variabile `cucu`);
- quinto passo, creo un campo `temp4` e lo popolo con l'indice che i valori del campo `temp3` hanno nell'array creato nel quarto passo;
- infine, mettendo tutto assieme viene fuori l'espressione utilizzata che in un unico passaggio popola il campo `group1`.

[![](../img/esempi/id_univoco_gruppi_consecutivi/img_01.png)](../img/esempi/id_univoco_gruppi_consecutivi/img_01.png)

### prova tu

[dati di esempio](https://gist.github.com/pigreco/48cf061c183809b0e69628a13493f771)

---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/variabili/with_variable.md)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [array_distinct](../gr_funzioni/array/array_unico.md#array_distinct)
* [array_agg](../gr_funzioni/aggrega/aggrega_unico.md#array_agg)
* [aggregate](../gr_funzioni/aggrega/aggrega_unico/#aggregate)
