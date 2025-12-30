---
social_image: img/card_social/hfc_blog.png
draft: false
date: 2025-12-30
authors:
  - pigreco
categories:
  - espressioni
  - matematica
tags:
  - blog
  - fattoriale
  - funzioni matematiche
  - calcolatore campi
---

# Perché in QGIS manca la funzione Fattoriale

## Introduzione

Vi siete mai chiesti perché QGIS, pur avendo un ricchissimo set di funzioni matematiche nel calcolatore di campi, non include la funzione fattoriale? In questo articolo esploreremo le ragioni di questa assenza e scopriremo come implementare facilmente questa funzione quando necessario.

!!! Abstract "La funzione Fattoriale"
    **Il fattoriale di un numero naturale n (indicato con n!) è il prodotto di tutti i numeri interi positivi minori o uguali a n. Ad esempio: 5! = 5 × 4 × 3 × 2 × 1 = 120**

<!-- more -->

## Cos'è la funzione Fattoriale

La funzione fattoriale è una delle funzioni matematiche più conosciute, definita per i numeri naturali come:

**n! = 1** se n = 0  
**n! = n × (n-1)!** se n > 0

Alcuni esempi pratici:

- 0! = 1 (per convenzione)
- 1! = 1
- 2! = 2 × 1 = 2
- 3! = 3 × 2 × 1 = 6
- 4! = 4 × 3 × 2 × 1 = 24
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 10! = 3.628.800

## Perché QGIS non ha una funzione fattoriale nativa?

Ci sono diverse ragioni valide per cui QGIS non include una funzione fattoriale nativa nel calcolatore di campi:

### 1. Casi d'uso limitati nell'ambito GIS

Il fattoriale è una funzione principalmente utilizzata in contesti di:

- **Combinatoria** (calcolo di combinazioni e permutazioni)
- **Statistica** (distribuzioni di probabilità)
- **Analisi matematica** (sviluppi in serie di Taylor)

Tuttavia, questi calcoli sono raramente necessari nell'analisi spaziale quotidiana. A differenza di funzioni come `area()`, `distance()`, o `buffer()`, che sono utilizzate costantemente, il fattoriale avrebbe un utilizzo marginale.

### 2. Crescita estremamente rapida

I valori fattoriali crescono in modo esplosivo:

- 20! ≈ 2,43 × 10¹⁸
- 50! ≈ 3,04 × 10⁶⁴
- 100! ≈ 9,33 × 10¹⁵⁷

Questo rende la funzione utile solo per valori molto piccoli (tipicamente n < 20), limitandone ulteriormente l'applicabilità pratica.

### 3. Facilità di implementazione quando necessario

QGIS privilegia un design modulare ed estensibile. Anziché includere ogni possibile funzione matematica, permette agli utenti di:

- Creare **funzioni personalizzate** tramite Python
- Utilizzare **espressioni composte** per calcoli specifici
- Sviluppare **plugin** per esigenze particolari

## Come implementare il Fattoriale in QGIS

### Metodo 1: Funzione personalizzata in Python

Il modo più elegante è creare una funzione personalizzata nell'editor delle espressioni. Apri il **Calcolatore di Campi** e accedi all'**Editor delle Funzioni**:

```python
from qgis.core import *
from qgis.gui import *
import math

@qgsfunction(args='auto', group='Custom')
def fattoriale(n, feature, parent):
    """
    Calcola il fattoriale di un numero.
    
    <h4>Sintassi</h4>
    <p>fattoriale(<i>n</i>)</p>
    
    <h4>Argomenti</h4>
    <p><i>n</i> → numero intero non negativo</p>
    
    <h4>Esempi</h4>
    <ul>
      <li>fattoriale(5) → 120</li>
      <li>fattoriale(0) → 1</li>
      <li>fattoriale(10) → 3628800</li>
    </ul>
    """
    if n is None:
        return None
    
    n = int(n)
    
    if n < 0:
        return None  # Il fattoriale non è definito per numeri negativi
    
    if n > 170:
        return None  # Evita overflow (170! è l'ultimo valore rappresentabile)
    
    return math.factorial(n)
```

Salva la funzione con il nome `fattoriale` e potrai utilizzarla in qualsiasi espressione:

```
fattoriale(5)  -- restituisce 120
fattoriale("valore_campo")  -- calcola il fattoriale dal campo
```

### Metodo 2: Espressione ricorsiva (per piccoli valori)

Per valori molto piccoli (n ≤ 5), puoi utilizzare una espressione diretta:

```python
CASE 
  WHEN "n" = 0 OR "n" = 1 THEN 1
  WHEN "n" = 2 THEN 2
  WHEN "n" = 3 THEN 6
  WHEN "n" = 4 THEN 24
  WHEN "n" = 5 THEN 120
  ELSE NULL
END
```

### Metodo 3: Calcolo combinatorio

Se hai bisogno del fattoriale per calcolare combinazioni o permutazioni, puoi utilizzare formule composite. Ad esempio, per calcolare le combinazioni:

**C(n,k) = n! / (k! × (n-k)!)**

```python
-- Combinazioni semplici
-- Esempio: C(10,3) = 10!/(3!*7!)
-- Implementazione diretta senza fattoriale completo
CASE
  WHEN "k" > "n" THEN NULL
  WHEN "k" = 0 OR "k" = "n" THEN 1
  ELSE (fattoriale("n") / (fattoriale("k") * fattoriale("n" - "k")))
END
```

## Casi d'uso pratici nel GIS

Anche se rari, ci sono alcuni scenari in cui il fattoriale può essere utile:

### 1. Analisi statistica spaziale

Calcolo di probabilità binomiali per analisi di pattern spaziali:

```python
-- Probabilità binomiale: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
(fattoriale("n") / (fattoriale("k") * fattoriale("n"-"k"))) 
  * power("p", "k") 
  * power(1-"p", "n"-"k")
```

### 2. Calcolo di permutazioni

Numero di percorsi possibili tra punti (problema del commesso viaggiatore semplificato):

```python
-- Numero di percorsi possibili attraverso n punti
fattoriale("numero_punti" - 1)
```

### 3. Analisi combinatoria di attributi

Calcolo del numero di combinazioni possibili di categorie:

```python
-- Quante combinazioni di k elementi da n categorie disponibili?
fattoriale("tot_categorie") / 
  (fattoriale("k") * fattoriale("tot_categorie" - "k"))
```

## Conclusioni

L'assenza della funzione fattoriale in QGIS è una scelta progettuale sensata, basata su:

- **Priorità funzionali**: QGIS si concentra sulle funzioni più richieste nell'analisi spaziale
- **Flessibilità**: Il sistema di funzioni personalizzate permette di aggiungere facilmente qualsiasi funzione necessaria
- **Efficienza**: Evita di appesantire il software con funzioni raramente utilizzate

Quando hai effettivamente bisogno del fattoriale, implementarlo è questione di pochi minuti grazie all'eccellente integrazione Python di QGIS. Questo approccio mantiene il software snello e allo stesso tempo infinitamente estensibile.

!!! tip "Suggerimento"
    Se ti trovi spesso a utilizzare funzioni matematiche avanzate, considera di creare una libreria personale di funzioni personalizzate che puoi riutilizzare in tutti i tuoi progetti QGIS!

## Risorse utili

- [Documentazione QGIS - Funzioni personalizzate](https://docs.qgis.org/latest/it/docs/user_manual/expressions/expression.html#function-editor)
- [Python math.factorial()](https://docs.python.org/3/library/math.html#math.factorial)
- [Calcolatore di campi HfcQGIS](../../calcolatore_campi/field_calc.md)

---

Scritto interamente da Claude Sonnet 4.5 in vscode!
