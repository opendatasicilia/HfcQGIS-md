---
tags:
  - selezionare
  - tabella
  - attributi
  - relazioni
---

# Selezionare i record senza riferimenti in una relazione padre figlio

In una relazione padre-figlio (1:m), può verificarsi che la tabella figlia abbia dei record senza alcun riferimento alla tabella padre, come selezionare questi record?  [Esempio preso da StackExchange](https://gis.stackexchange.com/questions/432303/filtering-missing-corresponding-values-in-1-to-n-relationship-in-qgis).

Usando solo le espressioni di QGIS e `Select by Expression` ![](../img/icon/mIconExpressionSelect.png), l'espressione da usare è:

```py
NOT aggregate (
      layer:= 'tabellaPadre',
      aggregate:= 'count',
      expression:= $id,
      filter:= "campoCorrelato" = attribute (@parent,'campoCorrelato'))> 0
```

_la logica dell'espressione è la seguente_: per ogni record padre, conta il numero di figli che saranno certamente `>0`, negare l'espressione corrisponde a selezionare i record figli che NON hanno un genitore.

---

Funzioni e variabili utilizzate:

* [@parent](../gr_funzioni/variabili/parent.md/)
* [NOT](../gr_funzioni/array/array_unico.md#array_agg)
* [aggregate](../gr_funzioni/aggrega/aggrega_unico.md/#aggregate)
* [count](../gr_funzioni/aggrega/aggrega_unico.md#count)

