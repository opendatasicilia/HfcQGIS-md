Operatori
===================================

Questo gruppo contiene operatori es. + - \*

+-----------------------------------+-----------------------------------+
| Funzione                          | Descrizione                       |
+===================================+===================================+
| `a + b`_                          | Addizione di due valori           |
+-----------------------------------+-----------------------------------+
| `a - b`_                          | Sottrazione di due valori.        |
+-----------------------------------+-----------------------------------+
| `a \* b`_                         | Moltiplicazione di due valori     |
+-----------------------------------+-----------------------------------+
| `a / b`_                          | Divisione di due valori           |
+-----------------------------------+-----------------------------------+
| `a % b`_                          | Resto della divisione             |
+-----------------------------------+-----------------------------------+
| `a ^ b`_                          | Elevazione a potenza di due       |
|                                   | valori                            |
+-----------------------------------+-----------------------------------+
| `a < b`_                          | Confronta due valori e pone a 1   |
|                                   | se il valore a sinistra è minore  |
|                                   | del valore a destra               |
+-----------------------------------+-----------------------------------+
| `a <= b`_                         | Confronta due valori e pone a 1   |
|                                   | se il valore a sinistra è minore  |
|                                   | o uguale del valore a destra      |
+-----------------------------------+-----------------------------------+
| `a <> b`_                         | Confronta due valori e pone a 1   |
|                                   | se essi non sono uguali           |
+-----------------------------------+-----------------------------------+
| `a = b`_                          | Confronta due valori e pone a 1   |
|                                   | se essi sono uguali.              |
+-----------------------------------+-----------------------------------+
| a != b                            | a e b non sono uguali             |
+-----------------------------------+-----------------------------------+
| `a > b`_                          | Confronta due valori e pone a 1   |
|                                   | se il valore a sinistra è         |
|                                   | maggiore del valore a destra      |
+-----------------------------------+-----------------------------------+
| `a >= b`_                         | Confronta due valori e pone a 1   |
|                                   | se il valore a sinistra è         |
|                                   | maggiore o uguale del valore a    |
|                                   | destra.                           |
+-----------------------------------+-----------------------------------+
| `a ~ b`_                          | Esegue un'espressione regolare su |
|                                   | di una stringa.                   |
+-----------------------------------+-----------------------------------+
| `\|\|`_                           | Unisce due valori assieme in una  |
|                                   | stringa. Se uno dei valori è NULL |
|                                   | il risultato sarà NULL. Vedi la   |
|                                   | funzione CONCAT con               |
|                                   | caratteristiche differenti.       |
+-----------------------------------+-----------------------------------+
| ‘\\n’                             | Inserisce una nuova linea         |
+-----------------------------------+-----------------------------------+
| `LIKE`_                           | Restituisce 1 se il primo         |
|                                   | parametro soddisfa il modello     |
|                                   | fornito. Funziona anche con i     |
|                                   | numeri                            |
+-----------------------------------+-----------------------------------+
| `ILIKE`_                          | Restituisce 1 se il primo         |
|                                   | parametro soddisfa senza tener    |
|                                   | conto delle maiuscole o minuscole |
|                                   | il modello fornito. LIKE può      |
|                                   | essere usato al posto di ILIKE    |
|                                   | per eseguire una comparazione che |
|                                   | tenga conto delle maiuscole e     |
|                                   | minuscole. Funziona anche con i   |
|                                   | numeri                            |
+-----------------------------------+-----------------------------------+
| `a IS b`_                         | Restituisce 1 se *a* è uguale a   |
|                                   | *b*.                              |
+-----------------------------------+-----------------------------------+
| `a OR b`_                         | Restituisce 1 quando la           |
|                                   | condizione a oppure b è vera      |
+-----------------------------------+-----------------------------------+
| `a AND b`_                        | Restituisce 1 quando le           |
|                                   | condizioni a e b sono vere.       |
+-----------------------------------+-----------------------------------+
| `NOT`_                            | Nega una condizione               |
+-----------------------------------+-----------------------------------+
| "column"                          | nome "nome colonna" nome della    |
|                                   | colonna del campo, fare           |
|                                   | attenzione a non confondere con   |
|                                   | la citazione semplice, vedere     |
|                                   | sotto                             |
+-----------------------------------+-----------------------------------+
| ‘string’                          | un valore stringa, fare           |
|                                   | attenzione a non confondere con   |
|                                   | virgolette doppie, vedi sopra     |
+-----------------------------------+-----------------------------------+
| NULL                              | null value                        |
+-----------------------------------+-----------------------------------+
| a IS NULL                         | *a* non è valorizzato             |
+-----------------------------------+-----------------------------------+
| a IS NOT NULL                     | *a* è valorizzato                 |
+-----------------------------------+-----------------------------------+
| `a IN (a,b,..)`_                  | Restituisce 1 se il valore viene  |
|                                   | trovato in una lista di valori    |
+-----------------------------------+-----------------------------------+
| a NOT IN (value[,value])          | *a* non è presente nella lista    |
+-----------------------------------+-----------------------------------+

|image0|

.. _a + b: somma.html
.. _a - b: meno.html
.. _a \* b: prodotto.html
.. _a / b: divisione.html
.. _a % b: resto_divisione.html
.. _a ^ b: potenza.html
.. _a < b: minore.html
.. _a <= b: minoreuguale.html
.. _a <> b: diverso.html
.. _a = b: uguale.html
.. _a > b: maggiore.html
.. _a >= b: maggioreuguale.html
.. _a ~ b: tilde.html
.. _\|\|: doppio_pipe.html
.. _LIKE: like.html
.. _ILIKE: ilike.html
.. _a IS b: is.html
.. _a OR b: or.html
.. _a AND b: and.html
.. _NOT: not.html
.. _a IN (a,b,..): in.html

.. |image0| image:: /img/operatori/gruppo_operatori1.png

**Elenco funzioni Operatori**

.. toctree::
   :maxdepth: 3
   
   and
   diverso
   divisione
   doppio_pipe
   ilike
   in
   is
   like
   maggiore
   maggioreuguale
   meno
   minore
   minoreuguale
   not
   or
   potenza
   prodotto
   resto_divisione
   somma
   tilde
   uguale
   
