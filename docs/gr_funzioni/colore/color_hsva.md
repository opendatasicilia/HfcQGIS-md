# color_hsva

Restituisce una rappresentazione stringa di un colore basato sui suoi attributi tonalità, saturazione, valore e alfa (trasparenza).

## Sintassi

color_hsva(_<span style="color:red;">hue</span>, <span style="color:red;">saturation</span>, <span style="color:red;">value</span>, <span style="color:red;">alpha</span>_)

## Argomenti

* _<span style="color:red;">hue</span>_ tonalità del colore, come valore intero da 0 a 360
* _<span style="color:red;">saturation</span>_ percentuale di saturazione del colore come valore intero da 0 a 100
* _<span style="color:red;">value</span>_ valore percentuale del colore come intero da 0 a 100
* _<span style="color:red;">alpha</span>_ componente alfa come valore intero da 0 (completamente trasparente) a 255 (opaco)

## Esempi

* `color_hsva(40,100,100,200) → 255,170,0,200`

![](/img/colore/color_hsva/color_hsva1.png)

## nota bene

--

## osservazioni

`color_hsva(40,100,100,200) = color_rgba( 255,170,0,200 )`
