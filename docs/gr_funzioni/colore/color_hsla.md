# color_hsla

Restituisce una rappresentazione stringa di un colore basato sui suoi attributi tonalità, saturazione, luminosità e alfa (trasparenza)

## Sintassi

color_hsl(_<span style="color:red;">hue</span>, <span style="color:red;">saturation</span>, <span style="color:red;">lightness</span>, <span style="color:red;">alpha</span>_)

## Argomenti

* _<span style="color:red;">hue</span>_ tonalità del colore, come valore intero da 0 a 360
* _<span style="color:red;">saturation</span>_ percentuale di saturazione del colore come valore intero da 0 a 100
* _<span style="color:red;">lightness</span>_ percentuale di luminosità del colore come valore intero da 0 a 100
* _<span style="color:red;">alpha</span>_ componente alfa come valore intero da 0 (completamente trasparente) a 255 (opaco).

## Esempi

* `color_hsla(100,50,70,200) → 166,217,140,200`

![](../../img/colore/color_hsla/color_hsla1.png)

## nota bene

--

## osservazioni

`color_hsla(100,50,70,200) =  color_rgba( 166,217,140,200)`
