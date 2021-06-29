# collect

Restituisce la geometria a parti multiple di geometrie aggregate da una espressione

## Sintassi

collect(_<span style="color:red;">expression</span>, <span style="color:red;">group_by</span>, <span style="color:red;">filter</span>_)

## Argomenti

* _<span style="color:red;">expression</span>_ espressione geometria da aggregare
* _<span style="color:red;">group_by</span>_ espressione opzionale da usarsi per raggruppare i calcoli aggregati
* _<span style="color:red;">filter</span>_ espressione opzionale da usare per filtrare gli elementi usati per calcolare il valore aggregato

## Esempi

* `collect( $geometry ) → geometria a parti multiple delle geometrie aggregate`

![](/img/aggregates/collect/collect1.png)

## nota bene

--

## osservazioni

--

![](/img/aggregates/collect/collect2.png)

![](/img/aggregates/collect/collect3.png)
