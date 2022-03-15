---
tags:
  - selezionare
  - duplicati
  - tabella
  - array
  - attributi
---

# Selezionare primo record per ogni duplicato per attributo

Supponiamo di avere una layer con tabella attributi in cui un attributo contiene dei duplicati, selezionare un solo record per ogni duplicato. Questo esempio prende spunto da questa domanda posta su [StackExchange](https://gis.stackexchange.com/questions/426162/exctract-one-record-from-duplicates-values).

Usando solo le espressioni di QGIS e `Select by Expression` ![](../img/icon/mIconExpressionSelect.png), l'espressione da usare è:

id | rischio
---|--------
1  | R1
2  | R2
3  | R2
4  | R3
5  | R3
6  | R3

```
with_variable ('your_field','rischio',
if(
	count(eval(@your_field),eval(@your_field))>1 
	AND 
	$id = array_agg($id,eval(@your_field))[0],true,false)
	)
```

selezionerà la riga 2 e 4

![](../img/esempi/seleziona_primo_record_per_ogni_duplicato/img_01.png)

---

Funzioni e variabili utilizzate:

* [@with_variable](../gr_funzioni/variabili/with_variable.md)
* [array_agg](../gr_funzioni/array/array_unico.md#array_agg)
* [if](../gr_funzioni/condizioni/condizioni_unico.md/#if)
* [count](../gr_funzioni/aggrega/aggrega_unico.md#count)

