# array_lambda

Applica una funzione personalizzata a ciascun elemento (x)

## Sintassi

array_lambda(_<span style="color:red;">array</span>, <span style="color:red;">lambda function</span>_) 

## Argomenti

* _<span style="color:red;">array</span>_ un array o stringa (valori separati da virgola) 
* _<span style="color:red;">lambda function</span>_ una stringa che rappresenta la funzione da applicare. L'elemento array è rappresentato come 'x'

## Esempi

* `array_lambda(array(1,2,3),'x+10') → <array: 11,12,13>`
*  `array_lambda( '1,2,3', '10') → <array: 11,12,13>`

![](/img/arrays/array_lambda/array_lambda1.png)

dalla versione 1.4 del plugin:
![](/img/arrays/array_lambda/array_lambda2.png)

## nota bene

Questa funzione sarà presente, nel calcolatore, solo dopo l'installazione del plugin [ArrayPlus](https://framagit.org/jbdesbas/arrayPlus)

## osservazioni

--
