# buffer

Restituisce una geometria che rappresenta tutti i punti la cui distanza dalla geometria è minore o uguale alla distanza inserita. I calcoli vengono effettuati nel sistema di riferimento spaziale della geometria.

## Sintassi

buffer(*<span style="color:red;">geometry</span>*,*<span style="color:red;">distance</span>*[,_<span style="color:red;">segments=8</span>_])

## Argomenti

* *<span style="color:red;">geometry</span>* una geometria
* *<span style="color:red;">distance</span>* distanza buffer nelle unità del layer
* *<span style="color:red;">segments</span>* numero di segmenti da usare per rappresentare un quarto di cerchio quando è utilizzato uno stile di unione arrotondato. Un numero grande risulta in un buffer più morbido, con più nodi.

## Esempi

`buffer($geometry, 10.5) → poligono di $geometry bufferizzato di 10.5 unità`

![](../../img/geometria/buffer/buffer0.png)

![](../../img/geometria/buffer/buffer1.png)

## nota bene

Utilizzando SR proiettati l'unità di misura è il metro, mentre, per SR geografici è il grado, quindi attenzione al valore della distanza.

## osservazioni

La Funzione restituisce SEMPRE un poligono sia per geometry **POINT**, **LINESTRING** o **POLYGON**

![](../../img/geometria/buffer/buffer2.png)
