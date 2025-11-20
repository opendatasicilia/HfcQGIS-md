---
tags:
  - contare
  - array
  - attributi
  - progressivo
---

# Conteggio progressivo di ripetizioni

Come creare un campo calcolato che conta progressivamente le ripetizioni di valori in un **CAMPO**, ripartendo da 1 ogni volta che il valore cambia, come riportato nella colonna **COUNT**.

## Esempio del risultato desiderato:

| CAMPO | COUNT |
|-------|-------|
| A     | 1     |
| B     | 1     |
| B     | 2     |
| B     | 3     |
| C     | 1     |
| C     | 2     |
| D     | 1     |
| D     | 2     |
| D     | 3     |

## Soluzione con espressione

### Espressione completa

```py
with_variable('hist',
    array_slice(
        array_agg("CAMPO"),
        0,
        $id-1
    ),
    if(
        $id = 1,
        1,
        if(
            "CAMPO" = @hist[-1],
            array_length(@hist) - array_length(
                array_slice(
                    @hist,
                    0,
                    array_find(@hist, "CAMPO")
                )
            ) + 1,
            1
        )
    )
)
```

**IMPORTANTE**: Sostituire `"CAMPO"` con il nome effettivo del campo da analizzare.

[![](../img/esempi/conteggio_progressivo/count_prog_01.png)](../img/esempi/conteggio_progressivo/count_prog_01.png)

## Spiegazione dettagliata

### 1. Creazione dello storico dei valori precedenti

```py
with_variable('hist',
    array_slice(
        array_agg("CAMPO"),
        0,
        $id-1
    ),
    ...
)
```

**Cosa fa:**

- `array_agg("CAMPO")` → Crea un array con TUTTI i valori del campo dall'inizio del layer
- `array_slice(..., 0, $id-1)` → Taglia l'array prendendo solo i valori dalla posizione 0 fino alla riga precedente a quella corrente
- `with_variable('hist', ...)` → Salva questo array in una variabile chiamata `@hist` che possiamo riutilizzare

**Esempio pratico:**

Se siamo alla riga 4, `@hist` conterrà i valori delle righe 1, 2 e 3. Se il layer ha valori [A, B, B, B, C], alla riga 4 `@hist` = [A, B, B]

### 2. Controllo della prima riga

```py
if($id = 1, 1, ...)
```

**Cosa fa:**

- Se siamo alla prima riga del layer (`$id = 1`), restituisce semplicemente `1`
- Altrimenti, procede con il controllo successivo

**Perché è necessario:** La prima riga non ha valori precedenti da confrontare, quindi il conteggio parte sempre da 1

### 3. Confronto con il valore precedente

```py
if("CAMPO" = @hist[-1], ..., 1)
```

**Cosa fa:**

- `@hist[-1]` → Prende l'ultimo elemento dell'array (il valore della riga immediatamente precedente)
- Confronta il valore corrente con quello precedente:
  - Se sono **uguali** → continua il conteggio (va al calcolo successivo)
  - Se sono **diversi** → restituisce `1` (ripartenza del conteggio)

**Esempio pratico:**

- Riga 3 con valore "B", riga precedente aveva "B" → sono uguali, continua
- Riga 5 con valore "C", riga precedente aveva "B" → sono diversi, restituisce 1

### 4. Calcolo del conteggio progressivo

```py
array_length(@hist) - array_length(
    array_slice(
        @hist,
        0,
        array_find(@hist, "CAMPO")
    )
) + 1
```

**Cosa fa (passo per passo):**

1. **`array_find(@hist, "CAMPO")`** → Cerca la **prima** occorrenza del valore corrente nell'array storico e restituisce la posizione (indice)

2. **`array_slice(@hist, 0, array_find(@hist, "CAMPO"))`** → Taglia l'array dallo storico fino alla prima occorrenza del valore corrente. Questo rappresenta tutti i valori "prima" della sequenza corrente

3. **`array_length(...)`** → Conta quanti elementi ci sono prima della sequenza corrente

4. **`array_length(@hist) - array_length(...) + 1`** → Sottrae dal totale degli elementi storici quelli prima della sequenza, aggiunge 1 per includere la riga corrente

**Esempio numerico:**

Supponiamo di essere alla riga 4 con valore "B":

- `@hist` = [A, B, B] (prime 3 righe)
- `array_find(@hist, "B")` = 1 (prima B trovata in posizione 1)
- `array_slice(@hist, 0, 1)` = [A] (elementi prima della sequenza di B)
- `array_length([A])` = 1
- `array_length(@hist)` = 3
- Calcolo: 3 - 1 + 1 = **3** ← Terza ripetizione di "B"!

## Come utilizzare l'espressione

### Passaggi:

1. Aprire la **tabella degli attributi** del layer
2. Aprire il **Calcolatore di Campi** (icona dell'abaco o `Ctrl+I`)
3. Configurare il nuovo campo:
   - Crea un nuovo campo
   - Nome campo: `COUNT` (o il nome che si preferisce)
   - Tipo di campo: **Numero intero (integer)**
   - Lunghezza: 10
4. Incollare l'espressione nell'editor
5. Modificare il nome del campo: sostituire tutte le occorrenze di `"CAMPO"` con il nome effettivo del campo da analizzare
6. Cliccare **OK** per calcolare il campo

## Note importanti

### Ordine delle righe

L'espressione conta le ripetizioni **nell'ordine in cui le righe appaiono nel layer**. Se si vuole un ordine specifico:

1. Prima di calcolare il campo, ordinare il layer:
   - Cliccare con il tasto destro sull'intestazione del campo
   - Scegliere "Ordina..." 
   - Selezionare ordine crescente o decrescente
2. Poi calcolare il campo COUNT

### Aggiornamento del campo

Se si modificano i dati o l'ordine delle righe dopo aver calcolato COUNT:

- Il campo COUNT **non si aggiornerà automaticamente**
- È necessario ricalcolarlo manualmente usando nuovamente l'espressione

### Tipo di layer

L'espressione funziona con:

- Shapefile
- GeoPackage
- Layer PostGIS
- CSV/Delimitati
- Qualsiasi layer vettoriale

## Soluzioni alternative

### Metodo 1: Espressione semplificata con array_sort

Una soluzione più semplice e leggibile che utilizza le funzioni di aggregazione e ordinamento:

```py
array_find(
    array_sort(
        array_agg( $id, group_by:= "CAMPO" )
    ),
    $id
) + 1
```

**Cosa fa:**

- `array_agg($id, group_by:="CAMPO")` → Crea un array con tutti gli ID delle righe raggruppate per valore del campo
- `array_sort(...)` → Ordina gli ID in modo crescente
- `array_find(..., $id)` → Trova la posizione dell'ID corrente nell'array ordinato
- `+ 1` → Aggiunge 1 perché gli indici degli array partono da 0

**Vantaggi:**

- Molto più semplice e leggibile
- Più efficiente in termini di performance
- Non necessita di gestire manualmente lo storico

**Esempio pratico:**

Per una riga con valore "B" e ID 3:

- `array_agg($id, group_by:="CAMPO")` → [2, 3, 4] (tutti gli ID con valore "B")
- `array_sort([2, 3, 4])` → [2, 3, 4] (già ordinati)
- `array_find([2, 3, 4], 3)` → 1 (posizione di ID 3)
- `1 + 1` → **2** (secondo elemento con valore "B")

**IMPORTANTE**: Anche in questo caso, sostituire `"CAMPO"` con il nome effettivo del campo.

### Metodo 2: Virtual Layer (SQL)

Se si preferisce usare SQL standard, è possibile creare un Virtual Layer:

**Menu: Layer → Aggiungi Layer → Aggiungi/Modifica Virtual Layer**

```sql
SELECT *,
  ROW_NUMBER() OVER (PARTITION BY CAMPO ORDER BY rowid) as COUNT
FROM nome_del_tuo_layer
```

**Vantaggi:**

- Sintassi SQL standard (window functions)
- Più leggibile
- Più efficiente su grandi dataset

**Svantaggi:**

- Crea un nuovo layer virtuale (non modifica l'originale)
- Richiede di specificare esplicitamente l'ordinamento

## Quale soluzione scegliere?

- **Espressione semplificata (Metodo 1)**: Ideale per la maggior parte dei casi, semplice e veloce
- **Espressione completa**: Utile quando serve maggiore controllo sull'ordine delle righe basato su `$id`
- **Virtual Layer (Metodo 2)**: Preferibile per dataset molto grandi o quando si lavora già con SQL



---

Funzioni e variabili utilizzate:

* [with_variable](../gr_funzioni/generale/generale_unico.md#with_variable)
* [array_slice](../gr_funzioni/array/array_unico.md#array_slice)
* [array_agg](../gr_funzioni/array/array_unico.md#array_agg)
* [array_sort](../gr_funzioni/array/array_unico.md#array_sort)
* [$id](../gr_funzioni/record_e_attributi/record_e_attributi_unico.md#id)
* [array_length](../gr_funzioni/array/array_unico.md#array_length)
* [array_find](../gr_funzioni/array/array_unico.md#array_find)
* [if](../gr_funzioni/condizioni/condizioni_unico.md#if)
