# concat

Concatena svariate stringhe in una sola. Valori NULL sono convertiti in stringhe vuote. Altri valori (come i numeri) sono convertiti in stringa.

## Sintassi

concat(_<span style="color:red;">string1</span>, <span style="color:red;">string2</span>, <span style="color:red;">…</span>_)

## Argomenti

* _<span style="color:red;">string</span>_ un valore stringa

## Esempi

* `concat('To', 'tò') → 'Totò'`
* `concat('a','b','c','d','e') → 'abcde'`
* `concat('Anno ', 2018) → 'Anno 2018'`
* `concat('QGIS 3.0', NULL) → 'QGIS 3.0'`

![](../../img/stringhe_di_testo/concat/concat1.png)

## nota bene

--

## osservazioni

--
