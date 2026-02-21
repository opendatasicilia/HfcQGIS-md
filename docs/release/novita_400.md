# Novità rilevanti introdotte in QGIS 4.0

[QGIS 4.0 Norrköping](https://changelog.qgis.org/en/qgis/version/4.0/)

## Espressioni

### Gruppo Geometria

- add funzione [`equals`](../gr_funzioni/geometria/geometria_unico.md#equals): testa l'uguaglianza di due geometrie (analogo a `overlay_equals`)

```
equals($geometry, geometry(@parent))
```

### Gruppo Conversioni

- add funzioni [`extract_degrees`](../gr_funzioni/conversioni/conversioni_unico.md#extract_degrees), [`extract_minutes`](../gr_funzioni/conversioni/conversioni_unico.md#extract_minutes), [`extract_seconds`](../gr_funzioni/conversioni/conversioni_unico.md#extract_seconds): scompongono un valore in gradi decimali nei singoli componenti DMS, utili per personalizzare le annotazioni di griglia nei layout di stampa

```
concat(
  extract_degrees($y), '° ',
  extract_minutes($y), "' ",
  round(extract_seconds($y), 2), '"'
)
```

### Gruppo Magnetico _(nuovo)_

- add nuovo gruppo con 4 funzioni per lavorare con i modelli di campo magnetico terrestre:
  - [`magnetic_declination`](../gr_funzioni/magnetico/magnetico_unico.md#magnetic_declination)
  - [`magnetic_inclination`](../gr_funzioni/magnetico/magnetico_unico.md#magnetic_inclination)
  - [`magnetic_declination_rate_of_change`](../gr_funzioni/magnetico/magnetico_unico.md#magnetic_declination_rate_of_change)
  - [`magnetic_inclination_rate_of_change`](../gr_funzioni/magnetico/magnetico_unico.md#magnetic_inclination_rate_of_change)

```
magnetic_declination($x, $y, now())
```

### Gruppo Stringhe di Testo

- add funzione [`unaccent`](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#unaccent): rimuove accenti e segni diacritici dalle stringhe

```
unaccent("città") → 'citta'
```

- add funzione [`substr_count`](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#substr_count): conta le occorrenze di una sottostringa

```
substr_count("A-B-C-D", "-") → 3
```

### Gruppo Data e Ora

- add 5 funzioni per la gestione dei fusi orari basate sugli ID del database IANA:
  - [`timezone_from_id`](../gr_funzioni/data_ora/data_ora_unico.md#timezone_from_id)
  - [`timezone_id`](../gr_funzioni/data_ora/data_ora_unico.md#timezone_id)
  - [`get_timezone`](../gr_funzioni/data_ora/data_ora_unico.md#get_timezone)
  - [`convert_timezone`](../gr_funzioni/data_ora/data_ora_unico.md#convert_timezone)
  - [`set_timezone`](../gr_funzioni/data_ora/data_ora_unico.md#set_timezone)

```
convert_timezone(now(), timezone_from_id('Europe/Rome'))
```

---

Vedi anche: [blog post QGIS 4.0 – nuove funzioni del gruppo Espressioni](../blog/posts/nuove_funzioni_expressioni_qgis_4_0/index.md)
