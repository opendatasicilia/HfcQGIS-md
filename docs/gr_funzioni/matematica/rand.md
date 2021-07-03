# rand

Restituisce un intero casuale nell'intervallo specificato fra un minimo ed un massimo (inclusi). Se viene fornito un seme, il reso sarà sempre lo stesso, a seconda del seme.

## Sintassi

rand(_<span style="color:red;">min</span>, <span style="color:red;">max</span><span style="color:red;">[,seed=null]</span>_)

[ ] indica componenti opzionali

## Argomenti

* _<span style="color:red;">min</span>_ un intero indicante il numero casuale più piccolo desiderato
* _<span style="color:red;">max</span>_ un intero che indica il numero casuale più alto desiderato
* _<span style="color:red;">seed</span>_ qualsiasi valore da utilizzare come seme (**>= QGIS 3.12**)

## Esempi

* `rand(1, 10) → 8`
* `rand( 10, 100,1) → 68`

![](../../img/matematica/rand/rand1.png)

## nota bene

--

## osservazioni

Novità introdotta nella **QGIS 3.12**

![](../../img/matematica/rand/rand2.png)
