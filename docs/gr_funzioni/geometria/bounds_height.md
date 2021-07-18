# bounds_height

Restituisce l'altezza del perimetro di delimitazione di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

## Sintassi

bounds_height(_<span style="color:red;">geometry</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria

## Esempi

```
- bounds_height($geometry) → altezza del perimetro di delimitazione dell'elemento geometrico corrente
- bounds_height(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))')) → 1
```

![](../../img/geometria/bounds/bounds_height0.png)

![](../../img/geometria/bounds/bounds_height1.png)

## nota bene

--

## osservazioni

La funzione restituisce un numero che corrisponde all'altezza del rettangolo di ingombro di una geometria.
