---
tags:
  - gui
  - interfaccia
  - propedeutico
---

# Interfaccia calcolatore di campi

!!! Abstract "Intro"
    **In questa sezioni descriveremo tutte le parti dell'interfaccia del Field Calc.**

[![interfaccia](../img/interfaccia_v2.png)](../img/interfaccia_v2.png)

1. se attivato aggiorna solo le geometrie selezionate (indica anche il numero delle feature selezionate);
2. se attivato crea un nuovo campo;
3. se attivato crea un campo virtuale;
4. permette di digitare nome del campo (per shapefile NON più di 10 caratteri);
5. permette di selezionare il Tipo di campo in uscita;
6. permette di digitare la Lunghezzacampo in uscita e relativa precisione in caso di numeri Reali;
7. permette di accedere al tab Editor delle Funzioni personalizzate (occorre conoscere il linguaggio Python);
8. icone che permettono di:
   1. ![](../img/icon/mActionFileNew.png) cancellare l'editor delle espressioni;
   2. ![](../img/icon/mActionFileSave.png) salvare le espressioni utente;
   3. ![](../img/icon/symbologyEdit.png) modificare le espressioni utente salvate;
   4. ![](../img/icon/mActionDeleteSelected.png) cancellare le espressioni utente salvate;
   5. ![](../img/icon/mActionSharingImport.png) importa espressioni utente;
   6. ![](../img/icon/mActionSharingExport.png) esporta funzioni utente.
9. operatori più usati:
   1. `=` uguale;
   2. `+` somma;
   3. `-` differenza;
   4. `/` divisione;
   5. `*` moltiplicazione;
   6. `^` potenza;
   7. `||` unione stringhe (doppio pipe);
   8. `()` parentesi;
   9. `'\n'`nuova riga;
10. editore delle espressioni;
11. se attivato aggiorna campo esistente (anche la geometria);
12. elenco di tutti i campi aggiornabili relativi al layer selezionato;
13. permette di cercare le funzioni, il bottone `Mostra Guida` permette di abilitare l'area dell'Help;
14. area dei gruppi funzione;
15. gruppo Campi e valori relativi al layer selezionato;
16. permette di visualizzare i valori dei campi presenti nel gruppo Campi e valori;
17. permette di selezionare l'Elemento per cui visualizzare l'Anteprima;
18. tasto OK per applicare l'espressione;
19. Help sulla funzione selezionata.

## Commenti espressione

[![screen](../img/finestra_field_calc/commenti.png)](../img/finestra_field_calc/commenti.png)

È possibile aggiungere commenti alle espressioni nell'area dell'editor espressioni:
1. per riga intera `/*commento*/`
2. per commentare una riga `--commento`


## Campi e valori nel Gruppo Layer Mappa

A partire da >= QGIS 3.24

![](https://user-images.githubusercontent.com/142164/146177919-8a235423-a131-4e9a-a999-06cb449666f7.png)

## Interfaccia e finestre nascoste

Nel caso risulti nascosta la sezione Gruppi funzioni (vale fino alla QGIS 3.4):

[![interfaccia](../img/finestra_field_calc/hfcqgis_gruppi.gif)](../img/finestra_field_calc/hfcqgis_gruppi.gif)

Nel caso risulti nascosta la sezione help in linea:

[![interfaccia](../img/finestra_field_calc/hfcqgis_Help.gif)](../img/finestra_field_calc/hfcqgis_Help.gif)

Per aumentare dimensione caratteri:

[![interfaccia](../img/interfaccia/fieldCalc.gif)](../img/interfaccia/fieldCalc.gif)

