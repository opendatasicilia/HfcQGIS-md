# Novità rilevanti introdotte in QGIS 4.2

[QGIS 4.2](https://changelog.qgis.org/en/qgis/version/4.2/)

## Espressioni

### Gruppo Matematica

- add funzione [`scale_cubic_bezier`](../gr_funzioni/matematica/matematica_unico.md#scale_cubic_bezier): completa le funzioni `scale_linear` e `scale_exp` aggiungendo un metodo di interpolazione basato su curva di Bézier cubica

```
scale_cubic_bezier(val, domain_min, domain_max, range_min, range_max, cp1, cp2)
```

### Gruppo Stringhe di Testo

- add funzione [`concat_ws`](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#concat_ws): concatena più valori usando il primo argomento come separatore; gli argomenti NULL vengono ignorati

```
concat_ws('-', 'a', 'b', 'c') → 'a-b-c'
```

## Tabella attributi

### Feature: Adding "Field Calculator" menu item to the attribute table header

- nuova voce **"Field Calculator"** nel menu contestuale delle intestazioni di colonna della tabella attributi; apre la calcolatrice di campo con l'opzione "Aggiorna campo esistente" già spuntata e il campo corrispondente già selezionato (disponibile solo sui campi modificabili)

## Correzioni rilevanti (Notable Fixes)

Fix relativi a espressioni e calcolatrice di campi:

- [`concat()`](../gr_funzioni/stringhe_di_testo/stringhe_di_testo_unico.md#concat) ora restituisce una stringa vuota invece di NULL quando tutti gli argomenti sono NULL ([#65808](https://github.com/qgis/QGIS/issues/65808), [PR #66618](https://github.com/qgis/QGIS/pull/66618))
- fix dell'operatore **IN** con `nodes()` ([#66313](https://github.com/qgis/QGIS/issues/66313), [PR #66485](https://github.com/qgis/QGIS/pull/66485))
- fix crash della calcolatrice di campi con l'operazione stringa \* float su campo di tipo stringa ([#66507](https://github.com/qgis/QGIS/issues/66507), [PR #66508](https://github.com/qgis/QGIS/pull/66508))
- fix crash della calcolatrice di campi calcolando un campo intero con `"id"=@row_number` in fase di salvataggio ([#66268](https://github.com/qgis/QGIS/issues/66268), [PR #66508](https://github.com/qgis/QGIS/pull/66508))

---

Vedi anche: [changelog completo QGIS 4.2](https://changelog.qgis.org/en/qgis/version/4.2/)
