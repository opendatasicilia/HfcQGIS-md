---
tags:
  - etichette
  - caratteri
---

# Aggiungere caratteri speciali alle etichette

Come aggiungere nelle etichette gli apici come `km²` e similari?

La funzione `char` restituisce il carattere associato ad un codice unicode, quindi è possibile usare i codici _unicode_ per qualsiasi altro carattere speciale per esempio:

descrizione | espressione  | risultato
------------|--------------|----------
apice 2     | `char(178)`  | `²`
apice 3     | `char(179)`  | `³`
gradi       | `char(176)`  | `°`
circa       | `char(8776)` | `≈`
diametro    | `char(8709)` | `∅`
euro        | `char(8364)` | `€`
alfa        | `char(945)`  | `α`
beta        | `char(946)`  | `β`
epsilon     | `char(949)`  | `ε`
teta        | `char(952)`  | `θ`
diverso     | `char(8800)` | `≠`


![](https://pigrecoinfinito.files.wordpress.com/2021/10/image-1.png)

## osservazione:

per trovare il codice di un carattere basta utilizzare la funzione `ascii('⭐') → 11088`

blog post : <https://pigrecoinfinito.com/2021/10/11/qgis-e-le-unita-di-misura-nel-si/>

---

Funzioni e variabili utilizzate:

* [char](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico/#char)