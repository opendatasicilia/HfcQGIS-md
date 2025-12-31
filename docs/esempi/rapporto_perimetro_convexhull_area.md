---
tags:
  - geometria
  - convex_hull
  - area
  - perimetro
  - compattezza
---

# Calcolare il rapporto tra perimetro del Convex Hull e area del poligono

**Quesito:** Come calcolare l'indice di compattezza di un poligono usando il rapporto tra il perimetro del suo inviluppo convesso (Convex Hull) e la sua area? Questo indice è utile per identificare poligoni irregolari o molto frastagliati.

![](../img/esempi/convex_hull_ratio/convex_hull_ratio_01.png)

*Esempio: poligoni con forme irregolari hanno valori più alti dell'indice*

### Soluzione

L'indice di compattezza basato sul Convex Hull permette di misurare quanto un poligono si discosta dalla sua forma convessa ideale. Valori più alti indicano forme più irregolari, frastagliate o allungate.

#### Passo 1: Calcolare il perimetro del Convex Hull

Nel calcolatore di campi, creare un nuovo campo `perim_convex` di tipo `decimale (double)`:

```py
perimeter(convex_hull($geometry))
```

Questa espressione:
- Calcola il Convex Hull (inviluppo convesso) del poligono
- Restituisce il perimetro di questa geometria convessa

#### Passo 2: Calcolare l'indice di compattezza

Creare un nuovo campo `indice_compattezza` di tipo `decimale (double)`:

```py
round(
  perimeter(convex_hull($geometry)) / $area,
  4
)
```

Oppure, per un indice normalizzato (0-1), dove valori vicini a 1 indicano maggiore compattezza:

```py
round(
  (4 * pi() * $area) / power(perimeter(convex_hull($geometry)), 2),
  4
)
```

#### Passo 3: Interpretare i risultati

Ordinare il campo `indice_compattezza` per identificare:
- **Valori alti** (primo metodo): Poligoni molto irregolari, frastagliati o allungati
- **Valori bassi** (secondo metodo normalizzato): Poligoni molto irregolari

### Soluzione completa con una singola espressione

Per ottenere direttamente l'indice di compattezza con informazioni aggiuntive:

```py
map(
  'nome', "NOME_CAMPO",
  'area_mq', round($area, 2),
  'perim_convex', round(perimeter(convex_hull($geometry)), 2),
  'perim_effettivo', round($perimeter, 2),
  'indice_frastagli', round(perimeter(convex_hull($geometry)) / $area * 1000, 4),
  'compattezza_norm', round((4 * pi() * $area) / power(perimeter(convex_hull($geometry)), 2), 4)
)
```

Questa espressione restituisce una mappa con:
- Il nome dell'elemento
- L'area in metri quadrati
- Il perimetro del convex hull
- Il perimetro effettivo del poligono
- L'indice di frastagliatura (perimetro convex/area)
- L'indice di compattezza normalizzato

### Selezione dei poligoni più irregolari

Per selezionare i poligoni con maggiore irregolarità (es. top 10%):

```py
perimeter(convex_hull(@geometry)) / $area >= 
  array_get(
    array_sort(
      array_agg(perimeter(convex_hull(@geometry)) / $area)
    ),
    floor(count($id) * 0.9)
  )
```

### Applicazioni pratiche

Questo indice è particolarmente utile per:

1. **Analisi urbanistica**: Identificare lotti edilizi irregolari o difficili da edificare
2. **Catasto**: Validare la regolarità delle particelle catastali
3. **Ecologia del paesaggio**: Analizzare la frammentazione di habitat naturali
4. **Agricoltura**: Valutare l'efficienza di appezzamenti agricoli
5. **Pianificazione territoriale**: Identificare aree che potrebbero beneficiare di ricomposizione fondiaria

### Confronto tra forme

| Forma | Indice frastagl. | Compattezza norm. |
|-------|------------------|-------------------|
| Cerchio | ~0.0035 | 1.0 |
| Quadrato | ~0.004 | ~0.7854 |
| Rettangolo 2:1 | ~0.006 | ~0.628 |
| Poligono frastagliato | >0.01 | <0.5 |

### Note

- La funzione `convex_hull()` genera il più piccolo poligono convesso che contiene la geometria originale
- L'indice è sensibile alla scala: normalizzare dividendo per l'area rende il confronto indipendente dalle dimensioni
- Per geometrie multipart, considerare l'uso di `num_geometries()` per filtrarle prima dell'analisi
- L'indice di compattezza normalizzato (Circle Ratio) varia tra 0 e 1, con 1 che rappresenta un cerchio perfetto
- Valori dell'indice di frastagliatura dipendono dall'unità di misura dell'area e del perimetro

### Riferimenti

- [convex_hull](../gr_funzioni/geometria/geometria_unico.md#convex_hull)
- [perimeter](../gr_funzioni/geometria/geometria_unico.md#perimeter)
- [$area](../gr_funzioni/geometria/geometria_unico.md#area)
- [$perimeter](../gr_funzioni/geometria/geometria_unico.md#perimeter)
- [pi](../gr_funzioni/matematica/matematica_unico.md#pi)
- [power](../gr_funzioni/matematica/matematica_unico.md#power)
- [round](../gr_funzioni/matematica/matematica_unico.md#round)
- [map](../gr_funzioni/maps/maps_unico.md#map)
