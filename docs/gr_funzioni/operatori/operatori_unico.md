Gruppo Operatori

!!! Abstract
    **Questo gruppo contiene operatori es. + - ***

---

## AND

Restituisce 1 quando le condizioni a e b sono vere.

Sintassi:

- _<span style="color:red;">a</span>_ AND _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ condizione
- _<span style="color:red;">b</span>_ condizione

Esempi:

```
TRUE AND TRUE → 1
TRUE AND FALSE → 0
4 = 2+2 AND 1 = 1 → 1
4 = 2+2 AND 1 = 2 → 0
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/AND1.png)

---

## <> (diverso)

Confronta due valori e pone a 1 se essi non sono uguali.

Sintassi:

- _<span style="color:red;">a</span>_ <> _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 <> 4 → 1
4 <> 4 → 0
5 <> NULL → NULL
NULL <> NULL → NULL
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/diverso1.png)

---

## / (diviso)

Divisione di due valori.

Sintassi:

- _<span style="color:red;">a</span>_ / _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 / 4 → 1.25
5 / NULL → NULL
NULL / 5 → NULL
```

![](../../img/operatori/divisione1.png)

---

## || (doppio pipe)

Unisce due valori assieme in una stringa.

Se uno dei valori è NULL il risultato sarà NULL. Vedi la funzione CONCAT con caratteristiche differenti.

Sintassi:

- _<span style="color:red;">a</span>_ || _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
'Qui' || ' e ' || 'là' → 'Qui e là'
'Nothing' || NULL → NULL
'Dia: ' || "Diameter" → 'Dia: 25' ("Diameter" - un campo tabella attributi)
1 || 2 → '12'
```

Osservazioni:

Puoi concatenare stringhe usando `||` o `+`. Quest'ultimo significa anche somma nelle espressioni. Quindi se hai un intero (campo o valore numerico) questo può essere soggetto a errori. In questo caso, dovresti usare `||`. Se si concatenano due valori stringa, è possibile utilizzare entrambi.

![](../../img/operatori/doppio_pipe1.png)

---

## ILIKE

Restituisce 1 se il primo parametro soddisfa senza tener conto delle maiuscole o minuscole il modello fornito. LIKE può essere usato al posto di ILIKE per eseguire una comparazione che tenga conto delle maiuscole e minuscole. Funziona anche con i numeri.

Sintassi:

- _<span style="color:red;">string/number</span>_ ILIKE _<span style="color:red;">pattern</span>_

Argomenti:

- _<span style="color:red;">string/number</span>_ stringa da cercare
- _<span style="color:red;">pattern</span>_ pattern di ricerca, puoi usare `'%'` come carattere jolly, `'_'` come un singolo carattere e `'\'` per eseguire l'escape.

Esempi:

```
'A' ILIKE 'A' → 1
'A' ILIKE 'a' → 1
'A' ILIKE 'B' → 0
'ABC' ILIKE 'b' → 0
'ABC' ILIKE 'B' → 0
'ABC' ILIKE '_b_' → 1
'ABC' ILIKE '_B_' → 1
'ABCD' ILIKE '_b_' → 0
'ABCD' ILIKE '_B_' → 0
'ABCD' ILIKE '_b%' → 1
'ABCD' ILIKE '_B%' → 1
'ABCD' ILIKE '%b%' → 1
'ABCD' ILIKE '%B%' → 1
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/ILIKE1.png)

---

## IN

Restituisce 1 se il valore viene trovato in una lista di valori.

Sintassi:

- _<span style="color:red;">a</span>_ IN_<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ lista di valori

Esempi:

```
'A' IN ('A','B') → 1
'A' IN ('C','B') → 0
```

Osservazioni:

La funzione distingue maiuscolo dal minuscolo!!!

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/IN1.png)

---

## IS

Restituisce 1 se _a_ è uguale a _b_.

Sintassi:

- _<span style="color:red;">a</span>_ IS _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ qualsiasi valore
- _<span style="color:red;">b</span>_ qualsiasi valore

Esempi:

```
'A' IS 'A' → 1
*'A' IS 'a' → 0
4 IS 4 → 1
4 IS 2+2 → 1
4 IS 2 → 0
$geometry IS NULL → 0, se la tua geometria non è NULL
```

Osservazioni:

La funzione distingue maiuscolo dal minuscolo!!!

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/IS1.png)

## IS NOT

Restituisce 1 se a non è uguale a b.

Sintassi:

Sintassi:

- _<span style="color:red;">a</span>_ IS NOT _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
'a' IS NOT 'b' → 1
'a' IS NOT 'a' → 0
4 IS NOT 2+2 → 0
```

![](../../img/operatori/is_not1.png)

---

## LIKE

Restituisce 1 se il primo parametro soddisfa il modello fornito. Funziona anche con i numeri.

Sintassi:

- _<span style="color:red;">string/number</span>_ LIKE _<span style="color:red;">pattern</span>_

Argomenti:

- _<span style="color:red;">string/number</span>_ valore
- _<span style="color:red;">pattern</span>_ pattern con cui confrontare il valore, puoi usare `'%'` come carattere jolly, `'_'` come un singolo carattere e `'\'` per eseguire l'escape.

Esempi:

```
'A' LIKE 'A' → 1
'A' LIKE 'a' → 0
'A' LIKE 'B' → 0
'ABC' LIKE 'B' → 0
'ABC' LIKE '_B_' → 1
'ABCD' LIKE '_B_' → 0
'ABCD' LIKE '_B%' → 1
'ABCD' LIKE '%B%' → 1
'1%' LIKE '1\%' → 1
'1_' LIKE '1\%' → 0
```

Osservazioni:

La funzione distingue maiuscolo dal minuscolo!!!

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/LIKE1.png)

---

## > (maggiore)

Confronta due valori e pone a 1 se il valore a sinistra è maggiore del valore a destra.

Sintassi:

- _<span style="color:red;">a</span>_ > _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 > 4 → 1
5 > 5 → 0
4 > 5 → 0
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/maggiore1.png)

---

## >= (maggiore uguale)

Confronta due valori e pone a 1 se il valore a sinistra è maggiore o uguale del valore a destra.

Sintassi:

- _<span style="color:red;">a</span>_ >= _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 >= 4 → 1
5 >= 5 → 1
4 >= 5 → 0
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/maggioreuguale1.png)

---

# Operatore - (meno)

Sottrazione di due valori. Se uno dei due valori è NULL il risultato sarà NULL.

Sintassi

- _<span style="color:red;">a</span>_-_<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 - 4 → 1
5 - NULL → NULL
to_datetime('2012-05-05 12:00:00') - to_interval('1 day 2 hours') → 2012-05-04T10:00:00
```

![](../../img/operatori/meno1.png)

---

## < (minore)

Confronta due valori e pone a 1 se il valore a sinistra è minore del valore a destra.

Sintassi:

- _<span style="color:red;">a</span>_ < _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 < 4 → 0
5 < 5 → 0
4 < 5 → 1
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/minore1.png)

---

## <= (minore uguale)

Confronta due valori e pone a 1 se il valore a sinistra è minore o uguale del valore a destra.

Sintassi:

- _<span style="color:red;">a</span>_ <= _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 <= 4 → 0
5 <= 5 → 1
4 <= 5 → 1
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/minoreuguale1.png)

---

## NOT

Nega una condizione.

Sintassi

- NOT _<span style="color:red;">a</span>_

Argomenti:

- _<span style="color:red;">a</span>_

Esempi:

```
NOT 1 → 0
NOT 0 → 1
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/NOT1.png)

---

## OR

Restituisce 1 quando la condizione a oppure b è vera.

Sintassi

- <span style="color:red;">a</span> OR _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ condizione
- _<span style="color:red;">b</span>_ condizione

Esempi:

```
4 = 2+2 OR 1 = 1 → 1
4 = 2+2 OR 1 = 2 → 1
4 = 2 OR 1 = 2 → 0
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/OR1.png)

---

## [] Indice operatore

Restituisce un elemento da un array o valore mappa.

Sintassi:

- [] _<span style="color:red;">index</span>_

Argomenti:

- _<span style="color:red;">index</span>_ indice array o valore chiave della mappa

Esempi:

```
array(1,2,3)[0] → 1
array(1,2,3)[2] → 3
array(1,2,3)[-1] → 3
map('a',1,'b',2)['a'] → 1
map('a',1,'b',2)['b'] → 2
```

![](../../img/operatori/indice_operatore1.png)

---

## ^ (potenza)

Elevazione a potenza di due valori.

Sintassi:

- _<span style="color:red;">a</span>_ ^ _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 ^ 4 → 625
5 ^ NULL → NULL
NULL ^ 5 → NULL
```

--

![](../../img/operatori/potenza1.png)

---

## * (prodotto)

Moltiplicazione di due valori.

Sintassi

- <span style="color:red;">a</span> * _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 * 4 → 20
5 NULL → NULL
NULL 5 → NULL
```

![](../../img/operatori/prodotto1.png)

---

## % (resto divisione)

Resto della divisione.
In aritmetica il resto è la quantità di *dividendoche è _avanzata_ dalla divisione, cioè quella quantità che non è stata possibile dividere per il divisore affinché il risultato rimanga nell'insieme dei `numeri interi`.
Per definizione: Il resto di una divisione denota la quantità da sottrarre a un dividendo al fine di renderlo divisibile per un divisore.

Sintassi

- <span style="color:red;">a</span> % _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempio:

17 : 2 = 8 resto 1

Sottraendo a 17 il resto di 1 si ottiene 16, numero divisibile per due (la cui metà è 8). Nella divisione tra 17 e 2, va tenuto da parte il resto, ossia quel numero che, se diviso, farebbe rientrare il risultato in un altro insieme numerico.

Il resto di una divisione denota la quantità da sottrarre a un dividendo al fine di renderlo
divisibile per un divisore.

Esempi:

```
5 % 4 → 1
5 % NULL → NULL
NULL % 5 → NULL
```

![](../../img/operatori/resto1.png)

Altri esempi:

Un esempio molto utile nel campo GIS riguarda l'etichettatura curve di livello: supponiamo di voler etichettare le curve di livello (con passo 50 m) e visualizzare solo le etichette con passo 200 m, l'espressione da usare è la seguente:

```
CASE WHEN   ( "ELEV" % 200 )  = 0 THEN  "ELEV"  END
```

ecco il risultato:

PRIMA:

![](../../img/operatori/resto2.png)

DOPO:

![](../../img/operatori/resto3.png)

---

## + (somma)

Addizione di due valori. Se uno dei due valori è NULL il risultato sarà NULL.

Sintassi

- <span style="color:red;">a</span> + _<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 + 4 → 9
5 + NULL → NULL
'QGIS ' + 'ROCKS' → 'QGIS ROCKS'
to_datetime('2020-08-01 12:00:00') + '1 day 2 hours' → 2020-08-02T14:00:00
```

Osservazioni:

Puoi concatenare stringhe usando `||` o `+`. Quest'ultimo significa anche somma nelle espressioni. Quindi se hai un intero (campo o valore numerico) questo può essere soggetto a errori. In questo caso, dovresti usare `||`. Se si concatenano due valori stringa, è possibile utilizzare entrambi.

![](../../img/operatori/somma1.png)

---

## ~ (tilde)

Esegue un'espressione regolare su di una stringa.

Sintassi

- _<span style="color:red;">a</span>_~_<span style="color:red;">regex</span>_

Argomenti:

- _<span style="color:red;">string</span>_ Un valore stringa
- _<span style="color:red;">regex</span>_ Un'espressione regolare. Le slash devono essere precedute da caratteri di escape, es. `\\d`

Esempi:

```
'hello' ~ 'll' → 1
'hello' ~ '^ll' → 0
'hello' ~ 'llo$' → 1
```

![](../../img/operatori/tilde1.png)

---

## = (uguale)

Confronta due valori e pone a 1 se essi sono uguali.

Sintassi

- _<span style="color:red;">a</span>_=_<span style="color:red;">b</span>_

Argomenti:

- _<span style="color:red;">a</span>_ valore
- _<span style="color:red;">b</span>_ valore

Esempi:

```
5 = 4 → 0
4 = 4 → 1
5 = NULL → NULL
NULL = NULL → NULL
```

Osservazioni:

1 significa **Vero**

0 significa **falso**

![](../../img/operatori/uguale1.png)
