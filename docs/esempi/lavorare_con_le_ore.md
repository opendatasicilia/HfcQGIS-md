---
tags:
  - data
  - ora
  - regex
---

# Lavorare con il formato ora

Supponiamo di avere un file CSV con questi dati, che dovrebbero rappresentare un oraio, ma non sono correttamente definiti come formato `Ora`; come convertirlo correttamente?

|time|
|----|
|0d 00:45:38|
|0d 00:05:00|
|0d 00:09:59|
|0d 00:14:58|
|0d 00:19:57|
|0d 00:24:56|

Il problema è legato alla presenza di `0d `, sotto due possibili modi per trasformarlo correttamente in `Ora`:

in questo esempio tolgo i primi tre caratteri, ovvero `0d `:
```
to_time(regexp_replace("time",'^...',''),'HH:mm:ss','en') → <ora: 00:05:00>
```

in questo secondo esempio, nascondo la prima parte della stringa con `\'0d\'`, cove lo `\` ha la funzione di `escape` del `'`
```
to_time("time",'\'0d\' HH:mm:ss','en') → <ora: 00:05:00>
```

---

Funzioni utilizzate:

- [to_time](../gr_funzioni/data_ora/data_ora_unico.md/#to_time)
- [regexp_replace](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md/#regexp_replace)
 