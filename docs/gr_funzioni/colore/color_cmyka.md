# color_cmyka

Restituisce una rappresentazione stringa di un colore basato sui suoi componenti ciano, magenta, giallo, nero e alfa (trasparenza)

## Sintassi

color_cmyka(_<span style="color:red;">cyan</span>, <span style="color:red;">magenta</span>, <span style="color:red;">yellow</span>, <span style="color:red;">black</span>, <span style="color:red;">alpha</span>_)

## Argomenti

* _<span style="color:red;">cyan</span>_ componente ciano del colore, come valore percentuale intero da 0 a 100
* _<span style="color:red;">magenta</span>_ componente magenta del colore, come valore percentuale intero da 0 a 100
* _<span style="color:red;">yellow</span>_ componente giallo del colore, come valore percentuale intero da 0 a 100
* _<span style="color:red;">black</span>_ componente nero del colore, come valore percentuale intero da 0 a 100
* _<span style="color:red;">alpha</span>_ componente alfa come valore intero da 0 (completamente trasparente) a 255 (opaco).

## Esempi

* `color_cmyka(100,50,0,10,200) → 0,115,230,2000`

![](/img/colore/color_cmyka/color_cmyka1.png)

## nota bene

--

## osservazioni

`color_cmyka(100,50,0,10,200) = color_rgba(0,115,230,200)`
