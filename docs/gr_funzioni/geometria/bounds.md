# bounds

Restituisce la geometria che rappresenta il perimetro di delimitazione di una geometria in ingresso. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

## Sintassi

bounds(*<span style="color:red;">geometry</span>*)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria

## Esempi

```
- bounds($geometry) → perimetro di delimitazione dell'elemento geometrico corrente
- geom_to_wkt(bounds(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))'))) → 'Polygon ((-1 0, 1 0, 1 1, -1 1, -1 0))'
```
![](../../img/geometria/bounds/bounds0.png)

![](../../img/geometria/bounds/bounds1.png)

## nota bene

--

## osservazioni

funzione molto utile per la tematizzazione aggiungendo un nuovo layer con geometry generator

![](../../img/geometria/bounds/bounds2.png)
