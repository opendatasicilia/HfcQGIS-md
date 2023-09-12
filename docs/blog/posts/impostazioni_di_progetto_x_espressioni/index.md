---
social_image: img/card_social/hfc_blog.png
draft: false
date: 2023-09-13
authors:
  - pigreco
categories:
  - espressioni
  - progetto
  - misure
tags:
  - blog
  - progetto
  - impostazioni
  - ellissoide
  - misure
---

# Impostazioni di progetto influenzano alcune funzioni

## Introduzione

Alcune funzioni di **QGIS** dipendono dalle impostazioni di progetto, questo significa che le stesse funzioni in progetti diversi possono restituire valori diversi. In questo post vedremo le principali funzioni di **QGIS** da attenzionare.

!!! Abstract "esempio"
    **$area _<span style="color:red;"><></span>_ area(@geometry)**

<!-- more -->

## Impostazioni dell'ellissoide di progetto

In realtà la schermata di sotto è raggiungibile dal menu _Progetto_ | _Proprietà_... (Ctrl + Shift + P) sezione _Generale_ | _Misure_

[![](./img_01.png)](./img_01.png)

qui è possibile settare l'_Ellissoide_, le unità di misura per le distanze e per le aree.

Se l'_Ellissoide_ è attivo, i calcoli saranno fatti secondo la selezione, se invece è spento o c'è scritto `None / Planimetric`, tutte le funzioni che dipendevano da questa impostazione restituiranno un risultato compatibile alla scelta e quindi misure `planimetriche`: in questo caso $area _<span style="color:red;">=</span>_ area(@geometry).

## Lista funzioni

sotto una breve lista di funzioni che dipendono dalle impostazioni dell'ellissoide di progetto:

- [$area](../../../gr_funzioni/geometria/geometria_unico.md#area)
- [$perimeter](../../../gr_funzioni/geometria/geometria_unico.md#perimeter)
- [$length](../../../gr_funzioni/geometria/geometria_unico.md#length)

## Esempi

Impostazioni dell'Ellissoide di Progetto attivo:

- $area _<span style="color:red;"><></span>_ area(@geometry)
- $perimeter _<span style="color:red;"><></span>_ perimeter(@geometry)
- $length _<span style="color:red;"><></span>_ length(@geometry)

[![](./img_02.png)](./img_02.png)

Impostazioni dell'Ellissoide di Progetto spento:

- $area _<span style="color:red;">=</span>_ area(@geometry)
- $perimeter _<span style="color:red;">=</span>_ perimeter(@geometry)
- $length _<span style="color:red;">=</span>_ length(@geometry)

[![](./img_03.png)](./img_03.png)

**NOTA BENE**: Anche le _**Unità di misura**_ influenzano il risultato, quindi occhio a come sono impostate: perché se fossero impostare in _chilomentri_ e _chilometri quadrati_, le relative funzioni restituirebbero valori con queste unità!.

## RIFERIMENTI

- [QGIS](https://www.qgis.org/it/site/)
- [DOCS QGIS](https://www.qgis.org/it/docs/index.html)
