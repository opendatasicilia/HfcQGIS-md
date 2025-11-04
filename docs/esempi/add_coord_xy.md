---
tags:
  - attributi
  - x
  - y
  - tabella
  - coordinate
  - calcolatore_campi
  - geometria
---

# Come aggiungere le coordinate x e y alla tabella attributi

## Introduzione

Spesso è necessario avere le coordinate X e Y dei punti direttamente nella tabella attributi per analisi, esportazioni o elaborazioni successive. QGIS permette di calcolare automaticamente queste coordinate utilizzando il **Calcolatore di campi** e le funzioni geometriche `$x` e `$y`.

!!! note "Nota importante"
    Le coordinate vengono calcolate nel sistema di riferimento (CRS) del layer. Assicurati che il layer abbia il CRS corretto prima di procedere.

## Procedimento

### Passo 1: Aprire la tabella attributi

Partiamo da un esempio con un geopackage contenente un vettore puntuale:

[![](../img/esempi/add_coord_xy/add_coord1.png)](../img/esempi/add_coord_xy/add_coord1.png)

Per aprire la tabella attributi, puoi:
- Selezionare il layer nel **Pannello Layer** → tasto destro del mouse → **'Apri tabella attributi'**
- Cliccare sull'icona ![icona_tab_attr](https://docs.qgis.org/2.18/it/_images/mActionOpenTable.png) nella barra degli strumenti
- Premere il tasto <kbd>F6</kbd>

[![](../img/esempi/add_coord_xy/add_coord2.png)](../img/esempi/add_coord_xy/add_coord2.png)

### Passo 2: Creare il campo per la coordinata X

1. **Attivare la modalità editing** cliccando sull'icona ![edit](https://docs.qgis.org/testing/en/_images/mActionToggleEditing.png) o premendo <kbd>Ctrl</kbd>+<kbd>E</kbd>
2. **Aprire il Calcolatore di campi** cliccando sull'icona ![calc](https://docs.qgis.org/testing/en/_images/mActionCalculateField.png) o premendo <kbd>Ctrl</kbd>+<kbd>I</kbd>
3. Selezionare **"Crea nuovo campo"**
4. Inserire il nome del campo: **`coord_x`**
5. Impostare:
   - **Tipo campo di uscita**: `Real (numero decimale)`
   - **Lunghezza di uscita**: `13`
   - **Precisione**: `2` (numero di decimali)
6. Cercare la funzione [`$x`](../gr_funzioni/geometria/geometria_unico.md#x) nella casella di ricerca
7. Fare doppio clic sulla funzione `$x` per inserirla nell'editor delle espressioni
8. Cliccare <kbd>OK</kbd> per eseguire il calcolo

Il campo `coord_x` verrà creato e popolato automaticamente con le coordinate X di tutti i punti.

### Passo 3: Creare il campo per la coordinata Y

Ripetere gli stessi passi per creare il campo **`coord_y`**, utilizzando la funzione [`$y`](../gr_funzioni/geometria/geometria_unico.md#y) invece di `$x`:

[![](../img/esempi/add_coord_xy/add_coord3.png)](../img/esempi/add_coord_xy/add_coord3.png)

### Risultato finale

Ecco il risultato con le due colonne contenenti le coordinate X e Y:

[![](../img/esempi/add_coord_xy/add_coord4.png)](../img/esempi/add_coord_xy/add_coord4.png)

## Note tecniche

!!! tip "Suggerimenti"
    - Le coordinate vengono espresse nell'unità di misura del sistema di riferimento del layer
    - Per coordinate geografiche (lat/lon), considera l'uso di più decimali per una maggiore precisione
    - I campi creati sono permanenti e si aggiornano automaticamente solo se ricalcolati manualmente

!!! warning "Attenzione"
    - Se modifichi la geometria dei punti, le coordinate nei campi **NON** si aggiornano automaticamente
    - Per aggiornare i valori dopo modifiche geometriche, ripeti il calcolo sovrascrivendo i campi esistenti

## Funzioni correlate

- [`$x`](../gr_funzioni/geometria/geometria_unico.md#x) - Restituisce la coordinata X
- [`$y`](../gr_funzioni/geometria/geometria_unico.md#y) - Restituisce la coordinata Y
- Vedi anche: [Gruppo funzioni Geometria](../gr_funzioni/geometria/index.md)

## Dati di esempio

Il geopackage utilizzato in questo esempio è scaricabile [qui](../prova_tu/dati_esempi.zip).
