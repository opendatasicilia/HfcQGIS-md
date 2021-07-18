# rotate

Restituisce una versione ruotata di una geometria. I calcoli si trovano nel sistema di riferimento spaziale di questa geometria.

## Sintassi

- rotate( _<span style="color:red;">geometry</span>_, _<span style="color:red;">rotation</span>_[, _<span style="color:red;">center</span>_])

[ ] indica componenti opzionali

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">rotation</span>_ rotazione oraria in gradi
*  _<span style="color:red;">center</span>_ punto centrale di rotazione. Se non specificato, viene utilizzato il centro del perimetro di delimitazione della geometria.

## Esempi

* `rotate($geometry, 45, make_point(4, 5)) → la geometria ruotava di 45 gradi in senso orario attorno al punto (4, 5)`
* `rotate($geometry, 45) → la geometria ruotava di 45 gradi in senso orario attorno al centro del riquadro di delimitazione`

![](../../img/geometria/rotate/rotate1.png)

## nota bene

--

## osservazioni

![screen](../../img/novita_312/Image03.png)
