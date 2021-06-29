# replace

Restituisce una stringa con la stringa, array o mappa di stringhe passate sostituite.

## Variabile stringa & array
Restituisce una stringa con la stringa o array di stringa passate sostituite da una stringa o un array di stringhe.

## Sintassi

replace(_<span style="color:red;">string</span>, <span style="color:red;">before</span>, <span style="color:red;">after</span>_)

## Argomenti

* _<span style="color:red;">string</span>_ la stringa in ingresso
* _<span style="color:red;">before</span>_ la stringa o array di stringhe da sostituire
* _<span style="color:red;">after</span>_ la stringa o l'array di stringe da usare come sostituzione

## Esempi

* `replace('QGIS SHOULD ROCK','SHOULD','DOES') → 'QGIS DOES ROCK'`
* `replace('QGIS ABC',array('A','B','C'),array('X','Y','Z')) → 'QGIS XYZ'`
* `replace('QGIS',array('Q','S'),'') → 'GI'`

![](/img/stringhe_di_testo/replace/replace1.png)

## Variabile mappa

Restituisce una stringa con le chiavi mappa fornite sostituite da valori accoppiati.

## Sintassi
replace(_<span style="color:red;">string</span>, <span style="color:red;">map</span>_)

## Argomenti

* _<span style="color:red;">string</span>_ la stringa in ingresso
* _<span style="color:red;">map</span>_ la mappa che contiene le chiavi e i valori

## Esempi

* `replace('APP SHOULD ROCK',map('APP','QGIS','SHOULD','DOES')) → 'QGIS DOES ROCK'`

![](/img/stringhe_di_testo/replace/replace2.png)

## nota bene

--

## osservazioni

--
