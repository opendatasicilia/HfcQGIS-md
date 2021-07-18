# project

Restituisce un punto proiettato da un punto di partenza usando una distanza e una direzione di immersione (azimut) in radianti.

## Sintassi

- project(_<span style="color:red;">point</span>_, _<span style="color:red;">distance</span>_, _<span style="color:red;">azimuth</span>_[,_<span style="color:red;">elevation</span>_])

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">point</span>_ punto di partenza
* _<span style="color:red;">point</span>_ distanza da proiettare
* _<span style="color:red;">azimuth</span>_ azimuth in radianti in senso orario, dove 0 corrisponde a nord
* _<span style="color:red;">elevation</span>_ angolo di inclinazione in radianti

## Esempi

* `project(make_point(1, 2), 3, radians(270)) → Point(-2, 2)`

![](../../img/geometria/project/project1.png)

## nota bene

--

## osservazioni

--

![](../../img/geometria/project/project1.gif)