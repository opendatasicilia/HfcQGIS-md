# randf

Restituisce un numero in virgola mobile casuale nell'intervallo specificato da un minimo ed un massimo (inclusi). Se viene fornito un seme, il reso sarà sempre lo stesso, a seconda del seme.

## Sintassi

randf(_<span style="color:red;">[min=0.0]</span><span style="color:red;">[,max=1.0]</span><span style="color:red;">[,seed=null]</span>_)

## Argomenti

* _<span style="color:red;">min</span>_ un numero in virgola mobile indicante il numero casuale più piccolo desiderato
* _<span style="color:red;">max</span>_ un numero in virgola mobile indicante il numero casuale più grande desiderato
* _<span style="color:red;">seed</span>_ qualsiasi valore da utilizzare come seme (**>= QGIS 3.12**)

## Esempi

* `randf(1, 10) → 4.59258286403147`
* `randf(1, 10,3) → 6.028893906608612`

## Esempi

![](../../img/matematica/randf/randf1.png)

## nota bene

--

## osservazioni

Novità introdotta nella **QGIS 3.12**

![](../../img/matematica/randf/randf2.png)
