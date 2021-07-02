# to_dms

Converte una coordinata in gradi, minuti e secondi

## Sintassi

* to_dms(_<span style="color:red;">coordinate</span>,<span style="color:red;">axis<span style="color:red;">,<span style="color:red;">precision</span>[,<span style="color:red;">formatting</span>]_)

[ ] marks optional components

## Argomenti

* _<span style="color:red;">coordinate</span>_ Un valore di latitudine o longitudine
* _<span style="color:red;">axis</span>_ L'asse della coordinata 'x' o 'y'
* _<span style="color:red;">precision</span>_ Numero di decimali
* _<span style="color:red;">formatting</span>_ Designa il tipo di formattazione. I valori accettabili sono NULL, 'aligned' o 'suffix'

## Esempi

* `to_dms(6.3545681, 'x', 3) → 6°21′16.445″`
* `to_dms(6.3545681, 'y', 4, 'suffix') → 6°21′16.4452″N`

![](/img/conversioni/to_dms1.png)

## Nota bene
