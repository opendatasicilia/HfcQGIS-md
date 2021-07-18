# eval_template

Valuta un modello che viene passato in una stringa. Molto utile per espandere parametri dinamici passati come variabili contestuali o campi.

## Sintassi

* eval_template(*<span style="color:red;">template</span>*)

## Argomento

* *<span style="color:red;">template</span>* una stringa modello

## Esempi

- `eval_template('QGIS [% upper(\'rocks\') %]') → QGIS ROCKS`

![](../../img/generale/eval_template1.png)
