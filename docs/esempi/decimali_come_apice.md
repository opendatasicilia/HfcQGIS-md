---
tags:
  - decimali
  - etichette
  - coordinate
  - x
  - y
---

# Decimali come apice per le etichette delle coordinate

Etichettare punti con le coordinate `x` e `y` mettendo i decimali come apice:


[![](../img/esempi/decimali_come_apice/img_01.png)](../img/esempi/decimali_come_apice/img_01.png)

Espressione da usare:

```python
'x = '||
with_variable(
   'caratteri_normali',
      array('0','1','2','3','4','5','6','7','8','9'),
with_variable(
   'numeri_apice',
      array('⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹'),

      format_number(regexp_replace( $x,'^(.+)\\.(.+)','\\1'),0)
  ||' '||
      replace(
         left(regexp_replace( $x,'^(.+)\\.(.+)','\\2'),3),
         @caratteri_normali,
         @numeri_apice ))) ||' m'

 ||  '\n'  || -- va a capo

 'y = '||
with_variable(
   'caratteri_normali',
    array('0','1','2','3','4','5','6','7','8','9'),
with_variable(
    'numeri_apice',
      array('⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹'),
      format_number(regexp_replace( $y,'^(.+)\\.(.+)','\\1'),0)
  ||' '||
      replace(
         left(regexp_replace( $y,'^(.+)\\.(.+)','\\2'),3),
         @caratteri_normali,
         @numeri_apice ))) ||' m'
```


le funzioni `replace()` sostituisce i numeri normali con quelli ad `apice`.

---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/variabili/with_variable.md)
* [regexp_replace](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#regex_replace)
* [left](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#left)
* [array](../gr_funzioni/array/array_unico.md#array)
* [$x](../gr_funzioni/geometria/geometria_unico.md#x)
* [$y](../gr_funzioni/geometria/geometria_unico.md#y)
* [replace](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#replace)

