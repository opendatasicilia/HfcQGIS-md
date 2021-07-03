# is_selected

Restituisce Vero se è selezionata una funzione. Può essere usato con zero, uno o due argomenti, vedi sotto per i dettagli.

## Senza parametri

Se chiamata senza parametri, la funzione restituirà vero se è selezionata la feature corrente nel layer corrente.

## Esempi

* `is_selected() → True (vero) se l'elemento corrente è selezionato.`

## Una Feature come parametro

Se chiamata con solo un parametro 'feature', la funzione restituisce true se viene selezionata la funzione specificata dal layer corrente.

## Sintassi

* is_selected(*<span style="color:red;">feature</span>*)

## Argomenti

* *<span style="color:red;">feature</span>* L'elemento che deve essere controllata per la selezione.

## Due parametri

Se la funzione viene chiamata sia con un layer che con una feature, tornerà vera se la feature specificata dal layer specificato è selezionata.

## Sintassi

* is_selected(*<span style="color:red;">layer</span>, <span style="color:red;">feature</span>*)

## Argomenti

* `layer` Il layer (o il suo ID o nome) su cui verrà selezionata la selezione.
* `feature` L'elemento che deve essere controllato per la selezione.

## Esempi

* `is_selected ('streets', get_feature ('streets', 'name', "street_name"))` → Vero se viene selezionata la strada corrente (supponendo che il layer della strada abbia un campo chiamato 'street_name' e il layer 'streets' abbia un campo chiamato 'nome').

Esempio etichettatura tramite regola:

![](../../img/record_e_attributi/is_selected1.gif)

Esempio tematizzazione tramite regola:

![](../../img/record_e_attributi/is_selected3.png)

![](../../img/record_e_attributi/is_selected2.gif)
