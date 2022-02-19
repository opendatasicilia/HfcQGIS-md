---
tags:
  - vestizione
  - x
  - y
---

# Effetto riempimento recipiente d'acqua

In questo breve tutorial vedremo come realizzare una tematizzazione, tramite espressioni geometriche, che simuli il riempimento di un recipente di acqua, e lo applicheremo ai nostri poligoni.

[![](https://i.imgur.com/bmRtkxl.png)](https://i.imgur.com/bmRtkxl.png)

espressione utilizzata nel generatore di geometrie:

```
difference(
$geometry,
-- bounding Box
make_rectangle_3points(
point_n(bounds($geometry),4),
point_n(bounds($geometry),3),
-- punto altezza rettangolo
 make_point(x(point_n(bounds($geometry),1)),
		   (y(point_n(bounds($geometry),1)))
		+ bounds_height($geometry)*(second(now()))/60),1))
```

espressione utilizzate per le etichette:

```
format_number((
-- area intersezione
area(intersection(
$geometry,
-- bounding Box
make_rectangle_3points(
point_n(bounds($geometry),2),
point_n(bounds($geometry),1),
-- punto altezza rettangolo
 make_point(x(point_n(bounds($geometry),1)),
		   (y(point_n(bounds($geometry),1)))
	 + bounds_height($geometry)*(second(now()))/60),1)))
-- area feature corrente
     /area($geometry))*100,1)||' %'
```

**NB:** per ottenere l'effetto dinamico occorre attivare, da proprietà layer | Visualizzazione, `Aggiorna layer a intervalli`.

qui video demo:

<https://youtu.be/uUEGSdWraPY>

---

Funzioni e variabili utilizzate:

* [difference](../gr_funzioni/geometria/geometria_unico.md#difference)
* [make_rectangle_3points](../gr_funzioni/geometria/geometria_unico.md#make_rectangle_3points)
* [point_n](../gr_funzioni/geometria/geometria_unico.md#point_n)
* [bounds](../gr_funzioni/geometria/geometria_unico.md#bounds)
* [make_point](../gr_funzioni/geometria/geometria_unico.md#make_point)
* [x](../gr_funzioni/geometria/geometria_unico.md#x_1)
* [y](../gr_funzioni/geometria/geometria_unico.md#y_1)
* [bounds_height](../gr_funzioni/geometria/geometria_unico.md#bounds_height)
* [intersection](../gr_funzioni/geometria/geometria_unico.md#intersection)
* [area](../gr_funzioni/geometria/geometria_unico.md#area_1)
* [second](../gr_funzioni/data_ora/data_ora_unico.md#second)
* [now](../gr_funzioni/data_ora/data_ora_unico.md#now)
* [area](../gr_funzioni/geometria/geometria_unico.md#area_1)
* [format_number](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#format_number)
* [$geometry](../gr_funzioni/geometria/geometria_unico.md#geometry)