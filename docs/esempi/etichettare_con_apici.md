# Aggiungere caratteri speciali alle etichette

Come aggiungere nelle etichette gli apici come `km²` e similari?

La funzione `char` restituisce il carattere associato ad un codice unicode, quindi è possibile usare i codici _unicode_ per qualsiasi altro carattere speciale per esempio:

- apice 2 è `char(178)` → `²`
- apice 3 è `char(179)` → `³`

![](https://pigrecoinfinito.files.wordpress.com/2021/10/image-1.png)


blog post : <https://pigrecoinfinito.com/2021/10/11/qgis-e-le-unita-di-misura-nel-si/>

---

Funzioni e variabili utilizzate:

* [char](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico/#char)