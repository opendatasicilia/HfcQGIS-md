## Aggregare elementi adiacenti

* Qual è la regione italiana che ha più regioni confinanti??
* Qual è la regione italiana (tranne le isole) che ha meno regioni confinanti??
* Qual è la regione italiana che ha una sola regione confinante??
* Per ogni regione quali sono le regioni confinante??

a questa e altre domande è possibile rispondere utilizzando le funzioni di aggregazione del calcolatore di campi di QGIS.

**Numero di regioni:**

[![](../img/esempi/aggregare_elementi_adiacenti/img_01.png)](../img/esempi/aggregare_elementi_adiacenti/img_01.png)

espressione da usare:

```
aggregate(
	layer:= 'regioni_g',
	aggregate:='count',
	expression:=to_string("COD_REG")
	filter:=touches($geometry, geometry(@parent))
 )
```

**Regioni confinanti:**

[![](../img/esempi/aggregare_elementi_adiacenti/img_02.png)](../img/esempi/aggregare_elementi_adiacenti/img_02.png)

```
aggregate(
	layer:= 'regioni_g',
	aggregate:='concatenate',
	expression:=to_string("DEN_REG"),
	concatenator:=', ',
	filter:=touches($geometry, geometry(@parent))
 )
```

funzione [aggregate](../gr_funzioni/aggrega/aggrega_unico.md#aggregate)


**Prova tu**

[Geopackage](../prova_tu/dati_esempi.zip)

