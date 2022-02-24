---
tags:
  - immagini
  - blob
  - geopackage
---

IN LAVORAZIONE


# Come memorizzare e riutilizzare immagini memorizzate in un GeoPackage

Per memorizzare immagini all'interno di un GeoPackage e in particolare in un layer vettoriale, per esempio un layer puntuale, possiamo utilizzare un campo di tipo BLOB.
Successivamente, per visualizzarle possiamo utilizzando le espressioni di QGIS, in particolare la funzione `to_base64`.

Immaginiamo di avere realizzato un rilievo della pubblica illuminazione, ogni punto del layer vettoriale rappresenta un palo della luce; assieme ad altri dati memorizzo anche la foto all'interno del geopackage, in un campo definito BLOB:



```
'base64:' || to_base64("campoBLOB")
```

La stringa `'base64:'` iniziale è necessaria per indicare che ciò che segue è una stringa base64 che codifica un'immagine, come 'http:' o 'https:' per indicare che si tratta di un URL.


---

Funzioni e variabili utilizzate:

* [to_base64](../gr_funzioni/conversioni/conversioni_unico.md#to_base64)
