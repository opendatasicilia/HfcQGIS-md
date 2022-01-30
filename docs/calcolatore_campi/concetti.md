# Concetti fondamentali sul calcolatore di campi di QGIS

!!! Abstract "Intro"
    **In questa sezioni sono raccolti i concetti fondamentali sul Field Calc espressi tramite un elenco puntato. La conoscenza di questi concetti permette di velocizzare il lavoro e capire il comportamento del Field Calc.**

1. il calcolatore di campi è attivabile solo per layer **vettoriale**[^1] e tabelle **editabili**[^2];
2. la creazione di un **nuovo campo** è relativo al layer selezionato nella TOC (Pannello Layer);
3. il calcolatore popola **un campo per volta** (la modifica multipla è un caso particolare);
4. l'output del calcolatore popola, in generale, tutte le celle (della colonna) della tabella attributi o solo quelle selezionate (caso particolare);
5. nella tabella attributi tutte le operazioni **agiscono riga per riga** (questo è uno dei motivi della lentezza di alcuni processi);
6. è possibile richiamare altri layer tramite le funzione _get_feature_, _get_feature_by_id_ e _aggregate_ e _overlay_*_;
7. il risultato delle funzioni di aggregazione verrà ripetuto in tutte le righe (questo è uno dei motivi della lentezza di alcuni processi);
8. è possibile **aggiornare** la *geometry* >= QGIS 2.14;
9. `$area`, `$perimeter` ecc.. il `$` davanti ad una funzione significa che riguarda la geometry corrente;
10. i nomi dei layer vanno scritti tra apici semplici ('nome_layer') mentre i nomi dei campi con doppi apici ("nome_campo") ma funziona anche senza apici, ma per evitare problemi è consigliato i doppi apici;
11. i valori numerici vanno scritti senza apici es: 10, mentre i valori alfanumerici vanno scritti tra apici semplici es: 'Sicilia';
12. l'anteprima del calcolatore (pto 17 - vedi screenshot) è utile ma non sempre corretta o completa; provate la funzione _to_datetime_ o usare funzioni che restituiscono un output lungo;
13. con il doppio clic è possibile aggiungere funzioni o valori nelle espressioni nell'area di editing;
14. è possibile aggiungere funzioni personalizzate tramite codice Python nel gruppo _Custom_;
15. è possibile aggiungere altri gruppi di funzioni tramite plugin es:refFunction → gruppo Reference;
16. è possibile editare/salvare/importare/esportare e condividere espressioni utente; >= QGIS 3.12;
17. è possibile cambiare l'attributo visualizzabile in `Elemento` dalle proprietà _Suggerimenti_ del layer;
18. è possibile aumentare la dimenzione del testo all'interno dell'editor tramite la rotellina del mouse (`Ctrl+rotellina`)
19. è possibile personalizzare i colori e i font utilizzati nell'area di scrittura espressioni da Impostazioni|Opzioni|IDE;
20. Campi e valori sono visibili sia per il layer corrente che per tutti i layer vettoriali (nel Gruppo Layer Mappa)


Video 1 |   Video 2   | Video 3
--------|-------------|--------
[![field_calc01](https://img.youtube.com/vi/454-t4_NcSs/0.jpg)](https://www.youtube.com/watch?v=454-t4_NcSs&index=7&list=PLqDFjeQq7NBjz5PWb66PNUqMgN1fce4cu "fiel_calc01") | [![field_calc02](https://img.youtube.com/vi/i0mLFq4MSOY/0.jpg)](https://www.youtube.com/watch?v=i0mLFq4MSOY&index=6&list=PLqDFjeQq7NBjz5PWb66PNUqMgN1fce4cu "fiel_calc02") | [![field_calc03](https://img.youtube.com/vi/IymSgXmbAFM/0.jpg)](https://www.youtube.com/watch?v=IymSgXmbAFM&list=PLqDFjeQq7NBjz5PWb66PNUqMgN1fce4cu&index "fiel_calc03")

[^1]: in contrapposizione ai layer raster

[^2]: non tutti i layer in QGIS sono editabili, come per esempio layer CSV