---
tags:
  - relazioni
  - poligoni
  - area
  - array
---

# Numerazione dei poligoni in base alla relazione spaziale

Etichettare le regioni italiane ISTAT in funzione della superficie, per esempio: la regione più estesa deve avere come etichetta 1 e poi via via aumentare al decrescere dell' area.

[![](../img/esempi/numerazione_poligoni_rel_spaziale/numer_01.png)](../img/esempi/numerazione_poligoni_rel_spaziale/numer_01.png)

espressione da usare:

```
array_find(
    array_reverse( 
        array_sort(array_agg($Area))
                 ), $Area)+1
```


L'espressione significa:

Crea un array (un vettore) e mettici dentro tutti i valori delle aree delle regioni, ordinali in senso crescente (dal più piccolo al più grande) e poi fai l'inverso, cioè, ordinali dal più grande al più piccolo; infine assegna l'indice della posizione del valore dell'area.

**PS**: +1 serve solo a far iniziare il conteggio da 1 in quanto gli array iniziano da zero.

Altro esempio:

Etichettare in funzione della longitudine, cioè mettere la label 1 nella regione più a Ovest e cosi via per le altre:

[![](../img/esempi/numerazione_poligoni_rel_spaziale/numer_02.png)](../img/esempi/numerazione_poligoni_rel_spaziale/numer_02.png)

espressione da usare:

```
array_find(
        array_sort(array_agg(x_min( $geometry)))
                 ,x_min( $geometry))+1
```

Altro esempio:

Etichettare, per ogni regione, le province in ordine alfabetico:

[![](../img/esempi/numerazione_poligoni_rel_spaziale/numer_03.png)](../img/esempi/numerazione_poligoni_rel_spaziale/numer_03.png)

espressione da usare:

```
"sigla"  || '-' || 
(array_find(
        array_sort(
            array_agg(expression:="sigla" , group_by:="cod_reg" )), "sigla" )+1)
```

Altro esempio:

Creata una griglia regolare formata da circa 4000 poligoni. Nominare tutti i poligoni partendo da destra verso sinistra e dall'alto verso il basso con lettere e numeri in sequenza. Quindi la prima maglia della griglia sarà A1, A2, A3 ecc, la seconda B1 B2 B3 e così via. 

[![](../img/esempi/numerazione_poligoni_rel_spaziale/numer_04.png)](../img/esempi/numerazione_poligoni_rel_spaziale/numer_04.png)

espressione da usare:

```
array_get(
    with_variable( 'cucu',
        string_to_array('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'),
            array_cat(
                array_foreach( @cucu ,upper(@element)), -- alfabeto a,b,c...
                array_foreach( @cucu ,upper(@element || @element)))), -- alfabeto raddoppiato aa,bb,cc...
    to_int((array_find(
        array_reverse(
            array_sort(
                array_agg(
                    y_min($geometry)))),
                    y_min($geometry)))/
                    count( expression:=y_min($geometry),group_by:=y_min($geometry))))
||
-- aggiunge il numero finale AA1, ZZ10
(to_int((array_find(
    array_reverse(
        array_sort(
        array_agg(
            x_min($geometry)))),
            x_min($geometry)))/
    count( expression:=y_min($geometry),group_by:=x_min($geometry)))+1 )
```
**PS.** L'espressione di sopra copre solo i casi a,b,c,....aa,bb,cc... per aggiungere anche aaa,bbb,ccc.... occorre aggiungere la stringa:

`array_foreach( @cucu ,upper(@element || @element|| @element))`

ovvero tre volte la variabile `@element`.


## Prova tu

[Geopackage](../prova_tu/dati_esempi.gpkg)
---

Funzioni e variabili utilizzate:

* [@element](../gr_funzioni/variabili/element.md)
* [array_agg](../gr_funzioni/array/array_unico.md#array_agg)
* [array_sort](../gr_funzioni/array/array_unico.md#array_sort)
* [string_to_array](../gr_funzioni/array/array_unico.md#string_to_array)
* [array_get](../gr_funzioni/array/array_unico.md#array_get)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [array_reverse](../gr_funzioni/array/array_unico.md#array_reverse)
* [\$Area](../gr_funzioni/geometria/geometria_unico.md#area)
* [count](../gr_funzioni/aggrega/aggrega_unico.md#y_min)
* [array_foreach](../gr_funzioni/array/array_unico.md#array_foreach)
* [upper](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#upper)
* [to_int](../gr_funzioni/conversioni/conversioni_unico.md#to_int)
* [\$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)

