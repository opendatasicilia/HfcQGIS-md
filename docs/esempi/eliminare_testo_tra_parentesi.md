# Eliminare testo tra parentesi

Supponiamo di vare una tabella degli attributi con un campo che contiene del testo, come l'esempio di sotto:

prima|dopo
-----|-----
ciao a tutti (si fa per dire), sono Totò|ciao a tutti, sono Totò
"come state oggi? (come prima, non ci fare caso) test"|come state oggi?  test
serata bella|serata bella
facile usare le regex, vero? ()|facile usare le regex| vero?

per ottenere il campo `dopo`, basta utilizzare la seguente espressione

```
regexp_replace( "nome", '\\(.*\\)','')
```

oppure aggiornare il campo `prima` con la stessa espressione.

---

Funzioni e variabili utilizzate:

* [regexp_replace](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#regexp_replace)
