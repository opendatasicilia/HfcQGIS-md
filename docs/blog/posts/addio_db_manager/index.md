---
social_image: img/card_social/hfc_blog_db_manager.png
draft: false
date: 2026-07-04
authors:
  - pigreco
categories:
  - novita
  - qgis-4-2
tags:
  - blog
  - db manager
  - plugin
  - QGIS
---

# QGIS 4.2: DB Manager lascia il core (ma non subito)

## Introduzione

Chi usa QGIS da anni conosce bene **DB Manager**: il pannello che permette di sfogliare, interrogare e gestire i database supportati (PostGIS, SpatiaLite, GeoPackage...) direttamente dall'interfaccia, senza uscire dal programma. Con QGIS 4.2 questo strumento smette di essere parte del core e diventa un plugin di terze parti, con un percorso di transizione più complicato del previsto.

Ne ho parlato in una [discussione aperta su OSGeo Discourse](https://discourse.osgeo.org/t/drop-db-manager/154234): questo post riprende e approfondisce quel filo, incrociando la proposta ufficiale, le pull request e la mailing list degli sviluppatori.

!!! Abstract "In breve"
    DB Manager viene "degradato" a plugin community per il [QEP-426](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-426-demote_dbmanager.md): troppa duplicazione con il Browser Panel, poca copertura di test, manutenzione onerosa. La rimozione completa dal core ([PR #66545](https://github.com/qgis/QGIS/pull/66545)) è ancora **aperta e discussa**; per la 4.2 è stato invece mergiato un approccio più graduale ([PR #66613](https://github.com/qgis/QGIS/pull/66613)): un avviso di deprecazione all'avvio con un pulsante per installare la versione community. Il plugin, però, è al momento **bloccato** nel repository ufficiale da oltre 100 warning di sicurezza.

<!-- more -->

## Perché "degradare" DB Manager

Il [QEP-426](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-426-demote_dbmanager.md) parte da una constatazione semplice: da tempo QGIS sta spostando la gestione dei database nel **Browser Panel**, che offre un'esperienza più integrata con gli altri strumenti di gestione dati. DB Manager, nato molto prima, mantiene una logica separata, con scarsissima copertura di test e un codice che duplica funzionalità ormai presenti altrove: un costo di manutenzione che nessuno vuole più coprire come strumento core.

Per chi dipende da funzionalità di DB Manager non ancora replicate nel Browser Panel, il QEP indica due strade: sponsorizzare uno sviluppatore core perché porti quelle funzionalità mancanti nel Browser Panel, oppure trovare manutentori volontari per il plugin community.

## Due pull request, due strategie

Sul come e quando togliere DB Manager dal core, gli sviluppatori non sono stati subito d'accordo:

- **[PR #66545](https://github.com/qgis/QGIS/pull/66545)** (nyalldawson) — implementa il QEP-426 alla lettera: rimozione completa del plugin dal repository `qgis/QGIS`, come bonus elimina anche la dipendenza da `pygments`. È tuttora **aperta**: nella discussione, Guts e altri chiedono più tempo tra l'annuncio e l'impatto sui flussi di lavoro professionali, mentre Rouault propone un compromesso — disabilitare il plugin di default in 4.2 e rimuoverlo del tutto solo in 4.4. Nyall Dawson ritiene invece che il momento giusto sia proprio prima di un LTR (Long Term Release), per non trascinarsi il problema su più versioni stabili.
- **[PR #66613](https://github.com/qgis/QGIS/pull/66613)** (nyalldawson) — la strategia poi effettivamente **mergiata** (1° luglio 2026) per QGIS 4.2: DB Manager resta nel core, ma mostra un avviso all'avvio ("The DB Manager plugin will be removed in a future QGIS release") con un pulsante che apre direttamente il gestore plugin per installare la versione community. Dopo il merge sono emersi due problemi: un errore di sintassi in una regex (segnalato da agiudiceandrea, dovuto a un carattere di escape non gestito con raw string) e il fatto che l'avviso continua a comparire anche dopo aver installato la versione community.

Quindi, in sintesi: **in QGIS 4.2 DB Manager c'è ancora**, ma con un banner che invita a migrare. La rimozione vera e propria è rimandata a una versione successiva (verosimilmente la 4.4, se il compromesso di Rouault verrà seguito).

## Il plugin community e un imprevisto: il muro della sicurezza

Il codice è stato spostato in un repository dedicato, [qgis/db_manager_plugin](https://github.com/qgis/db_manager_plugin), che si descrive esplicitamente come "archived, read-only copy" e "unsupported": **serve un manutentore volontario** che se ne faccia carico, altrimenti il plugin resta congelato allo stato in cui è stato estratto dal core.

Il passaggio da "plugin core" a "plugin di terze parti" ha rivelato un problema inatteso, raccontato da Nyall Dawson sulla [mailing list qgis-developer](https://lists.osgeo.org/pipermail/qgis-developer/2026-June/068377.html): quando ha provato a caricare la versione 1.0.0 sul repository ufficiale ([plugins.qgis.org](https://plugins.qgis.org/plugins/db_manager/)), la scansione automatica di sicurezza ha sollevato **oltre 100 segnalazioni**, dovute soprattutto all'uso estensivo di `exec` e a possibili rischi di SQL injection nel codice. Dawson ha dichiarato di non voler affrontare quei problemi e ha chiesto che il plugin venga temporaneamente inserito in una whitelist per bypassare lo scanner — con una punta di ironia, dato che lo stesso codice era installato di default nel core senza che nessuno lo controllasse con lo stesso rigore. Al momento in cui scrivo, il plugin **non risulta ancora pubblicato** sul repository ufficiale.

## Cosa cambia per chi usa QGIS

- **Con QGIS 4.2**: DB Manager funziona ancora, ma all'avvio compare l'avviso di deprecazione con l'invito a installare la versione community.
- **Per le funzionalità di base** (sfogliare tabelle, connessioni, semplici query): il **Browser Panel** copre già gran parte dei casi d'uso quotidiani ed è la strada consigliata per il futuro.
- **Per chi usa funzionalità avanzate** di DB Manager non ancora presenti nel Browser Panel: attenzione, perché il plugin community non è al momento manutenuto attivamente e la sua pubblicazione sul repository ufficiale è bloccata dai problemi di sicurezza sopra descritti. Vale la pena seguire il repository [qgis/db_manager_plugin](https://github.com/qgis/db_manager_plugin) prima di aggiornare a occhi chiusi.

## Conclusioni

La storia di DB Manager (nato da un'idea di Giuseppe Sucameli, oggi transitato nelle mani di Nyall Dawson e della community) mostra bene le tensioni tipiche di un progetto open source maturo: da un lato la necessità di alleggerire un core sempre più difficile da mantenere, dall'altro il timore di rompere flussi di lavoro consolidati da chi usa quello strumento tutti i giorni. Per ora QGIS 4.2 sceglie la via prudente dell'avviso di deprecazione; la rimozione definitiva resta una questione aperta, complicata ulteriormente dal fatto che il plugin community, per poter sopravvivere, deve prima superare lo scanner di sicurezza del repository ufficiale.

## Discussioni

Per commenti o domande: <https://github.com/opendatasicilia/HfcQGIS-md/discussions>

Discussione originale su OSGeo Discourse: <https://discourse.osgeo.org/t/drop-db-manager/154234>

## Link utili

- [QEP-426: Demote db manager plugin](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-426-demote_dbmanager.md)
- [PR #66545 — Drop db manager](https://github.com/qgis/QGIS/pull/66545)
- [PR #66613 — Deprecation warning e prompt di installazione](https://github.com/qgis/QGIS/pull/66613)
- [Repository qgis/db_manager_plugin](https://github.com/qgis/db_manager_plugin)
- [Thread mailing list qgis-developer sul blocco di sicurezza](https://lists.osgeo.org/pipermail/qgis-developer/2026-June/068377.html)
