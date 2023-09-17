---
social_image: img/card_social/hfc_blog.png
draft: true
date: 2023-09-18
authors:
  - pigreco
categories:
  - espressioni
tags:
  - blog
  - cerca_valori
  - get_feature
---

# Le variabili in QGIS

## Introduzione

Le variabili sono una nuova funzionalità introdotta in **QGIS 2.12 Lyon** (2015) che consente di creare valori preimpostati da utilizzare ovunque sia possibile utilizzare un'espressione. 

!!! Abstract "Variabili"
    **Rappresentano un nuovo concetto che dà la possibilità di impostare variabili personalizzate da utilizzare nel motore delle espressioni di **QGIS**

<!-- more -->

<!-- TOC -->

- [Le variabili in QGIS](#le-variabili-in-qgis)
  - [Introduzione](#introduzione)
  - [Cassetti](#cassetti)
    - [Esempio chiarificatore](#esempio-chiarificatore)
  - [Contesto](#contesto)
  - [Ambito](#ambito)
  - [Atlante](#atlante)
  - [Dinamiche contestuali](#dinamiche-contestuali)
  - [Creare variabile al volo](#creare-variabile-al-volo)
  - [Variabili predefinite](#variabili-predefinite)
    - [simbologia](#simbologia)
    - [etichette](#etichette)
    - [print layout](#print-layout)
  - [Variabile speciale value](#variabile-speciale-value)
  - [Formattazione condizionale](#formattazione-condizionale)
- [RIFERIMENTI](#riferimenti)
- [RINGRAZIAMENTI](#ringraziamenti)
- [Esempi di uso](#esempi-di-uso)

<!-- /TOC -->

## Cassetti

Possiamo immaginare le variabili come dei cassetti all'interno dei quali possiamo immagazinnare _qualcosa_ da utilizzare quando necessario. Il contenuto dei cassetti può essere un _testo_, un _numero_, una _espressione_. Le variabili possono essere _statiche_, ovvero, il loro contenuto è sempre lo stesso, oppure _dinamico_, ovvero, cambia in funzione del contesto.

```mermaid
flowchart LR;
   style id0 fill:#dd8c73,stroke:#343,color:#000000,stroke-width:2px
   style id1 fill:#ee7a13,stroke:#343,color:#000000,stroke-width:2px
   style id2 fill:#ed7b88,stroke:#343,color:#000000,stroke-width:2px
   id0[TESTO]
   id1[1234]
   id2[$area/10000]
```

### Esempio chiarificatore

Ecco un primo esempio che far capire le potenzialità delle variabili: supponiamo che nel nostro progetto QGIS ci siano 5 layer vettoriali e per ognuno avessimo attivato e configurato le etichette. Supponiamo di voler cambiare la dimensione dell'etichette a tutte e 5 i layer, occorrerebbe aprire le proprietà del layer ben 5 volte, una per ogni layer. Ma se impostassimo, _a livello di progetto_, una variabile `altezza_etichetta` e mettessimo dentro il valore 15, basterebbe modificare una sola volta questa variabile per vedere le modifiche su tutti i layer in cui l'avessimo utilizzata.

## Contesto

Come detto prima, le variabili sono sensibili al **_contesto_**, quindi alcune variabili sono utilizzabili ovunque, altre no; per esempio la variabile  `@grid_axis` è utilizzabile solo nel compositore di stampe. Nel _gruppo_ delle funzioni, presente sia nel Field Calc che in ogni altro _Costruttore stringhe espressioni_, l'elenco delle variabile è molto variabile! perché, ripeto, dipende dal contesto.

[![](./img_01.png)](./img_01.png)

## Ambito

Oltre al contesto, le variabili, dipendono anche dall'_**ambito**_, ovvero, esisitono 4 ambiti principali: _Globale_, _Progetto_, _Layer_, _Print Layout_, _Oggetto del print layout_, questi ambiti sono tutti impilati uno sopra l'altro in ordine dal meno specifico al più specifico. Gli ambiti più specifici _sovrascrivono_ eventuali variabili in conflitto esistenti da ambiti meno specifici: supponiamo di aver creato una variabile Globale `mio_nome` e successivamente altra variabile a livello di Progetto con stesso nome, la variabile globale verrebbe _sovrascritta_ da quella di progetto.

```mermaid
flowchart LR;
   style id0 fill:#ed7b13,stroke:#343,color:#000000,stroke-width:2px
   style id1 fill:#ed7b13,stroke:#343,color:#000000,stroke-width:2px
   style id2 fill:#ed7b13,stroke:#343,color:#000000,stroke-width:2px
   style id3 fill:#ed7b13,stroke:#343,color:#000000,stroke-width:2px
   style id4 fill:#ed7b13,stroke:#343,color:#000000,stroke-width:2px
   id0((("GLOBALE")))--> 
   id1(((Progetto)))-->
   id2(((Layer)))-->
   id3(((Print Layout)))-->
   id4(((Oggetto \n Print Layout)))
```

[![](./img_03.png)](./img_03.png)

La variabile `Blog` definita a livello Globale è utile in quanto la ritrovo sempre se lavoro nel mio PC e per qualsiasi sessione di lavoro. La variabile `Blog` definita a livello di Progetto è usabile SOLO in questo progetto.

- Per definire una variabile _**Globale**_: Menu _Impostazioni | Opzioni | Variabili_ e cliccare l'icona ![](./symbologyAdd.png) in basso a destra;
- per definire una variabile di **Progetto**: Menu _Progetto | Proprietà | Variabili_ e cliccare l'icona ![](./symbologyAdd.png) in basso a destra;
- per definire una variabile di **Layer**: Tasto destro del mouse sul nome del layer presente nel _Pannello Layer | Proprietà | Variabili_ e cliccare l'icona ![](./symbologyAdd.png) in basso a destra;

[![](./img_04.png)](./img_04.png)

## Atlante

Alcune variabili dipendono anche dalla creazione dell'**atlante**, ovvero, fin quanto non è stato creato un altlante, le relative variabili (@atlas_feature, @atla_geometry ecc...) non saranno né visibili né utilizzabili da nessuna parte, come è ovvio.

```mermaid
flowchart TD
    A[Progetto QGIS] --> B{Atlas?}
    B -->|Impostato| C[OK per le variabili] -->D["@atlas_feature\n@atlas_geometry\n@atlas_pagename\n..."] 
    B -->|Non impostato| E[Variabili NON usabili]
```

[![](./img_02.png)](./img_02.png)

Qui sfruttando sempre l'icona ![](./symbologyAdd.png) in basso a destra, è possibile aggiungere variabili in funzione all'oggetto selezionato, nel caso specifico sarebbe l'atlante.

## Dinamiche contestuali

Alcune variabili dinamiche, come per esempio `@map_scale`, restituiscono valori diversi a seconda di dove viene utilizzata: _map canvas_, _mappe nuove_, _mappa print layout_; questo perché la variabile riconosce dove è stata richiamata.

Ho etichettato lo stesso layer con la variabile  `@map_scale` ma in tre contesti diversi visualizzo tre valori diversi!!!

[![](./img_06.png)](./img_06.png)

## Creare variabile al volo

Infine, esiste una funzione `with_variable` che permette di creare, al volo, una variabile all'interno di una espressione complessa. Questo è molto utile quando, in espressioni lunghe e complesse, ci sono parti di espressioni che si ripetono più volte, per esempio `$area/10000`, potrei crearla come variabile e chiamrla `@areaEttari`, questo ha un duplice vantaggio: 1. rende l'espresione più leggibile; 2. rende l'espressione più veloce, perché quel valore verrebbe calcolato solo una volta e non enne volte.

[![](./img_05.png)](./img_05.png)

**Osservazione**: tutte le variabili iniziano con `@`, quindi se volessi usare la variabile `row_number` dovrei necessariamente scrivere `@row_number`

[![](./img_09.png)](./img_09.png)

## Variabili predefinite

Quando utiliziamo il Filed Calc o un qualsiasi costruttore Stringhe Espressione, nel gruppo funzioni ci sono, in cima all'elenco e in neretto, una serie di variabili predefinete pronte all'uso e contestualizzate, ovvero cambiano a seconda del contesto:

### simbologia
in questo caso il contesto è simbologia:

[![](./img_10.png)](./img_10.png)

### etichette
in questo caso è etichettatura:

[![](./img_11.png)](./img_11.png)

### print layout
in questo caso Print Layout, reticolo

[![](./img_12.png)](./img_12.png)

## Variabile speciale value

È stata introdotta, sempre da **Nyall**, una variabile speciale che viene utilizzata soprattutto nella _**sovrascrittura definita dai dati**_ ![](./mIconDataDefine.png), ovvero, in tutti quei casi in cui è possibile _pilotare_ le caratterisitiche delle etichette o della simbologia tramite dati o espressioni. La variabile si chiama `@value`.

Questa variabile rientra tra le variabili _dinamiche e contestuali_ perché può assumere vari valori a seconda della caratteristica utilizzata. In sostanza la variabile `@value` assume il _**valore corrente**_ presente nel _widget_ di riferimento. (l'esempio che segue chiarirà il concetto).

[![](./img_07.png)](./img_07.png)

La variabile `@value` nel caso di `Dimensione` assume il valore presente nel relativo widget, nel caso in esame `@value=14`;
nel caso di colore sarà nero, nel caso di Stile sarà Regular.

La prima cosa interessante è che appena modifico il valore nel widget, cambia anche il valore associato alla variabile; la seconda cosa interessante è che posso usare la variabile in una espressione, per esempio:

```
IF (@value <= 14, 0, @value)
```
ovvero, per qualsiasi valore inserito nel widget minore o uguale a 14, la dimensione del testo sarà 0, ovvero non visibile, altrimenti lascia il valore corrente!!!

[![](./img_08.png)](./img_08.png)

Non fate caso all'anteprima, segnerà sempre `NULL` e nell'Help ci sarà sempre scritto `non impostato`.

## Formattazione condizionale

nella stessa versione di QGIS 2.12 Lyon, Nathan Woodrow introduce la possibilità di realizzare la formattazione consizionale nelle tabelle degli attributi, un po' come in Excel.

In questo contesto esiste una varianile `@value` che rappresente sempre il valore corrente dell'attributi usato.

[![](./img_13.png)](./img_13.png)

Da punto di vista del codice, sembrerebbero due variabile che non hanno nulla a che fare l'una con l'altra, infatti l'una è stata implementata da Nyall, l'altra da Nathan; unica cosa in comune è che sono state rilascite nella stessa versione di QGIS.

# RIFERIMENTI

- [Changelog 2.12 - Le variabili](https://www.qgis.org/en/site/forusers/visualchangelog212/index.html?highlight=changelog#feature-variables-in-expressions)
- [Formattazione condizionale by Nathan Woodrow](https://woostuff.wordpress.com/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/)
- [DOC QGIS Variabili](https://docs.qgis.org/3.28/it/docs/user_manual/expressions/functions_list.html?highlight=variable#variables)
- [Variabile @value](https://www.youtube.com/live/h-mpUkwDdOQ?t=3104&si=7GxR8qlDUGDFzXcv)
- <https://mermaid-js.github.io/mermaid/#/flowchart>

# RINGRAZIAMENTI

- **Gabriel De Luca**, [qui](https://t.me/c/1176908051/44129) suo messaggio;
- Andrea Giudiceandrea, [qui](https://lists.osgeo.org/pipermail/qgis-it-user/2023-September/010427.html) i suoi contributi.

# Esempi di uso

- Nella sezione Funzioni, [gruppo Variabili](https://hfcqgis.opendatasicilia.it/gr_funzioni/variabili/variabili/), trovate l'elenco di tutte le variabili, però non sono documentate, occorre tempo che non ho per adesso :-);
- Nella sezione [Esempi svolti](https://hfcqgis.opendatasicilia.it/esempi/lista_esempi/), trovate molti esercizi in cui utilizzo la funzione `with_variable`.
