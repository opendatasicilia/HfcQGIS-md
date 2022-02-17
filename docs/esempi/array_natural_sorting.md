---
tags:
  - ordinare
  - array
  - tabella
  - valori
---

# Ordinare numericamente un array alfanumerico

(problema noto come _**Natural Sorting**_)

Data una lista di numeri civici, una per ogni via di una città, una lista del tipo: 

| nome     | lista                            | lista_ordinata                   |
|----------|----------------------------------|----------------------------------|
| strada A | 5/A-5-4-8-3-6-9-7-1-10-7/B-2-7/A | 1,2,3,4,5,5/A,6,7,7/A,7/B,8,9,10 |
| strada B | 10-1-2/A-2-3                     | 1,2,2/A,3,10                     |


l'obiettivo di questo esempio è di ordinare (_[Natural sorting](https://en.wikipedia.org/wiki/Natural_sort_order)_) i valori della colonna `lista` in modo da ottenere la colonna `lista_ordinata`. 

In pratica, ordinare i civici come se fossero solo numerici e nel caso ci fossero `5/A` o `7/B`, questi devono posizionarsi correttamente dentro l'ordine numerico (quindi un ordinamento umano). 

- **NB1:** `-` è il separatore dei civici, `/` è il separatore tra numero e lettera;
- **NB2:** nel numero civico, il primo valore è un numero seguito da `/` e da caratteri;

Una prima soluzione è la seguente:

```py
array_to_string(
array_foreach(
	array_sort(
		with_variable('lista',
			string_to_array('5/A-5-4-8-3-14-6-9-7-1-10-7/B-2-7/A' ,'-'),
			array_foreach(generate_series(0, array_length(@lista)-1),
			lpad(regexp_substr( (@lista[@element]),'(\\d+)'),3,'0') -- per muneri < 999
			||'|'||
			if(regexp_substr((@lista[@element]),'([a-zA-Z/]+)') !='',
			   regexp_substr((@lista[@element]),'([a-zA-Z/]+)'),
			   ' ') -- uno spazio
			||'|'||
			@lista[@element]))),
regexp_replace( @element,'^.+\\|(.+)$','\\1'))
)
```

![](https://user-images.githubusercontent.com/7631137/149634099-9022cc08-d93c-4209-8abd-0ea143ed384d.png)

## osservazione
Il **natural sorting** è un problema noto (c'è molta letteratura) e la soluzione non è univoca, dipende dall'algoritmo utilizzato, per maggiori info vedi i riferimenti. 

## Riferimenti

1. domanda posta su SE: <https://gis.stackexchange.com/questions/421166/sorting-alphanumeric-array-numerically-using-qgis-field-calculator>
2. Natural sorting : <https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/>

---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/generale/generale_unico.md/#with_variable)
* [array_sort](../gr_funzioni/array/array_unico.md/#array_sort)
* [array_foreach](../gr_funzioni/array/array_unico.md/#array_foreach)
* [array_to_string](../gr_funzioni/array/array_unico.md/#array_to_string)
* [string_to_array](../gr_funzioni/array/array_unico.md/#string_to_array)
* [generate_series](../gr_funzioni/array/array_unico.md/#generate_series)
* [regexp_substr](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#regexp_substr)
* [regexp_replace](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#regexp_replace)
* [lpad](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md/#lpad)
