---
tags:
  - categoria
  - array
  - tabella
  - prevalenza
  - confusionMatrix
---

# Calcolare la accuracy di una Matrice di Confusione

L'accuratezza in una matrice di confusione rappresenta la proporzione di classificazioni corrette rispetto al totale delle classificazioni effettuate da un modello di machine learning. In altre parole, indica quanto spesso il modello ha previsto correttamente la classe a cui appartiene un dato campione.

```py
SUM(
  CASE
    WHEN "Classified" = "GrndTruth" THEN 1
    ELSE 0
  END
)
/
array_length(array_agg(@id))
```

---

Funzioni e variabili utilizzate:

- [SUM](../gr_funzioni/aggrega/aggrega_unico.md#sum)
- [CASE](../gr_funzioni/condizioni/condizioni_unico#case)
- [array_length](../gr_funzioni/array/array_unico.md#array_length)
- [array_agg](../gr_funzioni/array/array_unico.md#array_agg)