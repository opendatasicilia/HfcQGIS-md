# area

Restituisce l'area di un oggetto a geometria poligonale. I calcoli sono sempre planimetrici nel Sistema di Riferimento Spaziale (SR) di detta geometria, e l'unità di misura dell'area restituita è conforme all'unità di misura del SR. Ciò differisce dal calcolo eseguito dalla funzione $area, la quale esegue calcoli ellisoidici basati sull'ellissoide del progetto e sulle impostazioni delle unità di misura dell'area.

## Sintassi

area(_<span style="color:red;">geometry</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ oggetto geometria poligono

## Esempi

![](../../img/geometria/area/area001.png)

![](../../img/geometria/area/area004.png)

## nota bene

Se il _<span style="color:red;">SR del layer</span>_ in cui si sta calcolando l'area (_**area()**_) fosse un sistema proiettato (es:EPSG 3003/4; 32632/33/34 ecc..) l'unità di misura sarebbe il metro, invece se il _<span style="color:red;">SR del layer</span>_ fosse EPSG 4326, cioè un sistema geografico, allora l'unità di misura dell'area sarebbe in gradi e quindi poco comprensibile e valori piccoli.

## osservazioni

in generale `area($geometry) <> $area`
