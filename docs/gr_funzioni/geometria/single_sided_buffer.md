# single_sided_buffer

Restituisce una geometria formata facendo un buffer solo da un lato di una geometria di tipo linestring. Le distanze sono espresse nel SR di tale geometria.

## Sintassi

- single_sided_buffer( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">distance</span>_[,  _<span style="color:red;">segments=8</span>_][,  _<span style="color:red;">join=1</span>_][,  _<span style="color:red;">miter_limit=2.0</span>_])

[ ] indica componenti opzionali

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria (multi)linestring
*  _<span style="color:red;">distance</span>_ distanza di buffer. Valori positivi saranno bufferizzati a sinistra delle linee, valori negativi a destra
*  _<span style="color:red;">segments</span>_ numero di segmenti da usare per rappresentare un quarto di cerchio quando è utilizzato uno stile di unione arrotondato. Un numero grande risulta in un buffer più morbido, con più nodi.
*  _<span style="color:red;">join</span>_ stile di unione per gli angoli, dove 1 = arrotondato, 2 = seghettato e 3 = smussato
*  _<span style="color:red;">miter_limit</span>_ limite sul rapporto di seghettatura usato per angoli molto appuntiti (solamente quando si usano le unioni seghettate)

## Esempi

* `single_sided_buffer($geometry, 10.5) → linea bufferizzata a sinistra di 10.5 unità`
* `single_sided_buffer($geometry, -10.5) → linea bufferizzata a destra di 10.5 unità`
* `single_sided_buffer($geometry, 10.5, segments:=16, join:=1) → linea bufferizzata a sinistra di 10.5 unità, usando più segmenti per risultare in un buffer più morbido`
* `single_sided_buffer($geometry, 10.5, join:=3) → linea bufferizzata a sinistra di 10.5 unità, usando un'unione smussata`

![](../../img/geometria/single_sided_buffer/single_sided_buffer1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/single_sided_buffer/single_sided_buffer2.png)