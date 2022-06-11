# Novità rilevanti introdotte in QGIS 3.26

[![](../img/splashscreen/splash_3_26rc.png)](../img/splashscreen/splash_3_26rc.png)

"La versione ricca di funzionalità di QGIS 3.26 **Buenos Aires** include un vasto numero di miglioramenti a una gamma di funzionalità di base avanzate. Ciò include numerosi miglioramenti alle funzionalità 3D, strumenti migliorati per le nuvole di punti e l'introduzione di un nuovo framework di tracciatura dei profili per la creazione di sezioni trasversali e profili di elevazione. Soprattutto, il nuovo framework di plottaggio utilizza le funzionalità di rendering QGIS native e viene fornito con tutte le proprietà di stile, simbologia e guida dei dati che tutti conosciamo e amiamo subito!"

<https://changelog.qgis.org/en/qgis/version/3.26/>

## Espressioni

### Gruppi
funzione              | link PR                                   | descrizione
----------------------|-------------------------------------------|------------
BETWEEN e NOT BETWEEN | <https://github.com/qgis/QGIS/pull/47771> | Nuovo Operatore
@symbol_frame         | <https://github.com/qgis/QGIS/pull/48152> | Nuova variabile
@parent               | <https://github.com/qgis/QGIS/pull/48488> | Miglioramento

## GUI Field Calc
- `copia valore espressione anteprima fielc calc`: <https://github.com/qgis/QGIS/pull/47680>
- `omogenizzate i valori booleani`: <https://github.com/qgis/QGIS/pull/47866>
- `aggiorna descrizione operatore AND`: <https://github.com/qgis/QGIS/pull/48118>

![](../img/novita_326/copia_anteprima_field_calc.gif)

- `scorrimento tabella attributi in orizzontale` : <https://github.com/qgis/QGIS/pull/47764>

![](../img/novita_326/scroll_oriz.gif)

## Tabella attributi

Nomi dei campi definiti dall'utente nell'esportazione: <https://github.com/qgis/QGIS/pull/47630>

![](https://user-images.githubusercontent.com/9881900/156719947-6e2183f0-27cb-41c4-a65b-9855822da233.gif)
