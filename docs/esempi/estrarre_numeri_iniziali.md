---
tags:
  - ricerca
  - caratteri
  - regex
  - array
---

# Estrarre i numeri iniziali

[Domanda](https://t.me/Postgres_PostGIS_IT/378) posta su un gruppo telegram:

Buona sera, chiedo qualche dritta sulle regexp in PG:

Ho una tabella con un campo di tipo text, che contiene informazioni sul numero di tubi e diametri a mo' di etichetta statica,
vorrei estrarre solo la quantità, e listarla a modo di array, come faccio?

es.
```
'1TØ50' --> atteso: [1]
'3TØ120 + 8TØ60' --> atteso: [3, 8]
'5TØ30 + 7TØ60 + 12TØ25' --> atteso: [5, 7, 12]
```

## soluzione

```
array_foreach(
  string_to_array("tubi",' + '),
  regexp_replace(@element,'(\\d+)(.+)','\\1')
)
```

la prima parte dell'espressione crea un array  e gli elementi sono i testi compresi tra i ` + `

dove:

- `'(\\d+)(.+)'` significa, crea due gruppi e nel primo metti solo i numeri iniziali;
- `\\1` significa prendi e sostituisci il primo gruppo

---

Funzioni e variabili utilizzate:

* [regexp_replace](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#regexp_replace)
* [array_foreach](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#array_foreach)
* [string_to_array](../gr_funzioni/array/array_unico/#string_to_array)
