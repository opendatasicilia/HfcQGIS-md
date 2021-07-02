# to_dm

Converte una coordinata in gradi, minuti

## Sintassi

* to_dm(_<span style="color:red;">coordinate</span>,<span style="color:red;">axis</span>,<span style="color:red;">precision</span>[,<span style="color:red;">formatting</span>]_)

[ ] marks optional components

## Argomenti

* _<span style="color:red;">coordinate</span>_ Un valore di latitudine o longitudine
* _<span style="color:red;">axis</span>_ L'asse della coordinata 'x' o 'y'
* _<span style="color:red;">precision</span>_ Numero di decimali
* _<span style="color:red;">formatting</span>_ Designa il tipo di formattazione. I valori accettabili sono NULL, 'aligned' o 'suffix'

## Esempi

* `to_dm(6.3545681, 'x', 3) → 6°21.274′`
* `to_dm(6.3545681, 'y', 4, 'suffix') → 6°21.2741′N`

![](/img/conversioni/to_dm1.png)

## Nota bene
