# color_cmyk

Restituisce una rappresentazione stringa di un colore basato sui suoi componenti ciano, magenta, giallo e nero

## Sintassi

color_cmyk(_<span style="color:red;">cyan</span>, <span style="color:red;">magenta</span>, <span style="color:red;">yellow</span>, <span style="color:red;">black</span>_)

## Argomenti

* _<span style="color:red;">cyan</span>_ componente ciano del colore, come valore percentuale intero da 0 a 100
* _<span style="color:red;">magenta</span>_ componente magenta del colore, come valore percentuale intero da 0 a 100
* _<span style="color:red;">yellow</span>_ componente giallo del colore, come valore percentuale intero da 0 a 100
* _<span style="color:red;">black</span>_ componente nero del colore, come valore percentuale intero da 0 a 100

## Esempi

* `color_cmyk(100,50,0,10) → 0,115,230`

![](../../img/colore/color_cmyk/color_cmyk1.png)

## nota bene

--

## osservazioni

`color_cmyk(100,50,0,10) = color_rgb( 0,115,230 )`
