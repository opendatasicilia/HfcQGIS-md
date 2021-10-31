---
social_image: img/card_social/hfc_lista_esempi.png
---

!!! Abstract
    **Questa sezione raccoglie degli esempi pratici e svolti step by step, con molti screenshot per rendere facile la comprensione di alcune funzioni di base come Area, lunghezza, Buffer ecc... | La sezione è in continua evoluzione e sono benvenuti contributi esterni**

---

Attualmente ci sono **58** esempi svolti! (in evoluzione)

... e **50** esempi da svolgere: [mettiti alla prova](../mettiti_alla_prova.md)

---

## Elenco esempi

**(Livello di difficoltà: 1 -> Facile -- 5 -> Difficile)**

nro|Esempio|Descrizione|Autore | Livello | funzioni utilizzate
---:|------:|:----------|:------:|:------:|---------
1|[aggiungi campo](add_col_area.md)|aggiungere colonna area per calcolo superficie|Salvatore Fiandaca | 2 | $area
2|[campi coordinate](add_coord_xy.md)|aggiungere colonne coordinate x e y|Salvatore Fiandaca | 2 | $x, $y
3|[campo virtuale](add_campo_virtuale.md)|aggiungere campo virtuale|Salvatore Fiandaca | 2 | $length
4|[campo quota z](add_col_z.md)|aggingere colonna quota con valori z|Salvatore Fiandaca | 2 | z, start_point, $geometry
5|[etichettare](etichette.md)|etichettare usando il campo geometry|Salvatore Fiandaca | 2 | to_int, format_number, $x, $y, z, m, $length, start_point, $geometry
6|[aggiornare geometria](agg_geom.md)|aggiornare il campo geometry|Salvatore Fiandaca | 2 | semplify, $geometry
7|[conversione](conversione.md)|etichettare punti da sessadecimali a sessagesimali|Salvatore Fiandaca | 2 | floor, format_number, to_real, $x, $y
8|[tematizzare](tematizzare.md)|Tematizzare utilizzando la sovrascrittura definita dai dati|Salvatore Fiandaca |2 | CASE, length
9|[legenda](espressione_regolare.md)|Legenda con testo lungo, inserimento carattere speciale|Salvatore Fiandaca |2 | CASE, regexp_replace
10|[selezione](select_with_aggregate.md)|Seleziona usando le funzioni di aggregazione|Salvatore Fiandaca |2 | $area, minimum, =
11|[core area](core_area.md)|Calcola la core area di un poligono | Ludovico Frate |2 | area, buffer
12|[sposta etichette](sposta_etichetta_linea.md)|Sposta etichetta e genera segmento|Salvatore Fiandaca |3 | x, y, $geometry
13|[conteggio valori](conteggio.md)|Conteggio valori in un campo|Salvatore Fiandaca |2 | count
14|[centroidi linee curve](centroid_linee.md)|Centroide lungo le linee curve|Salvatore Fiandaca |2 | $geometry, $length, line_interpolate_point, geom_to_wkt
15|[conta i punti nel poligono](conta_punti_in_poligono.md)|Conta i punti nel poligono|Salvatore Fiandaca |2 | aggregate
16|[somma lunghezze nel poligono](somma_lunghezze_nel_poligono.md)|Somma le lunghezze delle linee dentro il poligono|Salvatore Fiandaca |2 | @parent, aggregate, length, geometry, intersection, intersects, transform, $geometry
17|[conta punti nel poligono per categorie](punti_in_poligoni_categorie.md)|Contare i punti nel poligono per categorie|Martina Savarese |2 | @parent, aggregate, AND, geometry
18|[nascondi etichette](nascondi_etichette.md)|Nasconde etichette non desiderate |Salvatore Fiandaca |2 | @parent, not, aggregate, intersects, point_on_surface, $geometry
19|[calcolo area poligoni nel reticolo](calcolo_area_poligoni_reticolo.md)|Calcolare l’area delle porzioni di poligoni che ricadono dentro ad una cella di un reticolo|Salvatore Fiandaca |2 | @parent, aggregate, geometry, intersection, intersects, $geometry
20|[spatial join](spatial_join.md)|Trasferire un attributo usando le relazioni spaziali|Salvatore Fiandaca |2 | @parent, aggregate, geometry, to_string, intersects, $geometry
21|[unica label](unica_etichetta_più_poligoni.md)|Unica label per più poligoni|Salvatore Fiandaca |2 | x, y, make_point, centroid, collect, $geometry
22|[elenco comuni](elenco_comuni_attraversati_fiume.md)|Come ottenere l'elenco dei Comuni attraversati da un fiume|Salvatore Fiandaca |2 | aggregate, crosses, $geometry, geometry, @parent 
23|[rotazione pattern lineare](rotazione_pattern.md)|Come ruotare un pattern lineare in funzione della feature|Salvatore Fiandaca |2 | angle_at_vertex, shortest_line, centroid, oriented_bbox, boundary, $geometry
24|[numerazione poligoni in base a relazione spaziale](numerazione_poligoni_rel_spaziale.md)|Numerazione poligoni in base a relazioni spaziali|Salvatore Fiandaca |3 | @element, array_agg, array_sort, string_to_array, array_get, array_find, array_reverse, $Area, count, array_foreach, upper, to_int, $geometry
25|[assegnare categoria prevalente](assegnare_cat_prevalente.md)|Assegnare categoria prevalente|Salvatore Fiandaca |2 | array_majority, string_to_array, aggregate, intersects, $geometry, geometry, @parent
26|[creare Hub lines](hub_lines.md)|Creare Hub lines|Salvatore Fiandaca |2 | doppio pipe
27|[aggrega con SR differenti](aggregare_con_sr_differenti.md)|Aggrega con SR differenti|Salvatore Fiandaca |3 | aggregate, count, intersects, transform, $geometry, geometry, @parent
28|[distanze progressive chilometriche](distanze_progressive_chilometriche.md)|Formatta le distanze progressive chilometriche tipo Autostrade|Salvatore Fiandaca |2 | CASE
29|[aggregare elementi adiacenti](aggregare_elementi_contigui.md)|Aggrega elementi adiacenti|Salvatore Fiandaca |3 | aggregate, count, to_string, touches, $geometry, geometry, @parent
30|[linea minima distanza tra due punti](linea_min_distanza.md)|Traccia una linea di minima distanza usando il generatore di geometrie|Salvatore Fiandaca |2 | aggregate, shortest_line, $geometry
31|[creare campo somma cumulativa](add_campo_sum_cumulativo.md)|Espressione per popolare campo con somma cumulativa|Salvatore Fiandaca |2 | if, $id,array_agg, eval, replace, array_to_string, array_slice, array_sum
32|[aggiungere punto a linea](aggiungere_punto_a_linea.md)|Aggiunge un nodo di disegno ad una linea|Salvatore Fiandaca |2 | make_line, start_point, $geometry, end_point, geometry, get_feature_by_id
33|[drilldown form multiple](drilldown_form_multiple.md)|Creare Form con filtro dinamico drillDown (cascade)|Salvatore Fiandaca | 3 | aggregate, eval, array
34|[selezionare primi n valori](selezionare_primi_n_valori.md)|Come selezionare i primi n poligoni più grandi|Salvatore Fiandaca |2 | doppio-pipe, uguale, array_contains, array_slice, array_sort, array_agg, $area, $geometry
35|[generalizzare isoipse](generalizzare_linee.md)|Generalizzare le linee di contorno|Valerio Pinna | 3 | CASE, $length, simplify, smooth, $geometry
36|[campo coord in lat lon](campo_coord_in_lat_lon.md)|Generare due campi lon lat a partire da un unico campo|Salvatore Fiandaca | 2 | regexp_match
37|[calcolo incrementi giornalieri](calcolo_incrementi_giornalieri.md)|Calcola gli incrementi giornalieri di un attributo|Salvatore Fiandaca | 4 | with_variable, if, array_find, array_agg
38|[tracciare un grafico](tracciare_grafico_generatore_geometrie.md)|Come tracciare un grafico per ogni feature usando il generatore di geometrie|Salvatore Fiandaca | 4 | @with_variable, relation_aggregate, array_to_string, array_get, array_foreach, generate_series, translate, make_line, make_point, centroid, end_point, round, \$geometry
39|[elenco ordinato di Comuni](elenco_ordinato_comuni_attraversati.md)|Come ottenere l'elenco ordinato dei Comuni attraversati da un itinerario|Salvatore Fiandaca | 3 | @with_variable, array_find, array_filter, array_agg, line_locate_point, line_interpolate_point, intersection, length, $geometry
40|[etichettare con chiave-valore](etichettare_chiave_valore.md)|Etichettare facendo vedere sia il nome del campo che il corrispondente valore|Salvatore Fiandaca | 2 | replace, map_to_hstore, attributes
41|[etichettare itinerario con elenco ordinato Comuni](etichettare_itinerario_elenco_comuni_attraversati.md)|Etichettare itinerario con elenco ordinato di Comuni attraversti|Valerio Pinna | 4 | @parent, aggregate, array_to_string, array_get, array_foreach, generate_series, num_geometries, collect_geometries, intersection, start_point, concat, $geometry
42|[etichette formattate diversi stili](etichette_formattate_diversi_stili.md)|Etichette formattate con diversi stili|Valerio Pinna | 2 | with_variable, array, string_to_array, replace
43|[selezionare vertici duplicati](select_duplicate_vertices.md)|Selezionare vertici duplicati|Salvatore Fiandaca |3 | if, $id, get_feature_by_id, array_agg, array_sort, string_to_array, array_last, array_find, array_reverse, geom_to_wkt, count, array_length, $geometry
44|[conteggio caratteri diversi](conteggio_caratteri_diversi.md)|Conta i caratteri diversi in un testo|Salvatore Fiandaca | 2 |array_length, array_distinct, string_to_array, substr, regexp_replace
45|[distanza minima tra due vettori](linea_min_distanza2.md)|Lunghezza della linea di minima distanza tra due vettori|Salvatore Fiandaca | 2 | aggregate,shortest_line, overlay_nearest, $geometry
46|[lunghezze segmenti di un poligono](lunghezze_segmenti_poligono.md)|Lunghezze dei segmenti di un poligono|Salvatore Fiandaca | 3 | segments_to_lines, num_geometries, length, round, geometry_n, segments_to_lines, array_to_string, generate_series, array_foreach, $geometry
47|[fill-down con QGIS](fill-down.md)|riempire le celle sottostanti con il primo valore non nullo|Salvatore Fiandaca | 3 | @layer, if, attribute, $id, get_feature_by_id
48|[finestra temporale](finestra_temporale.md)|Fissata una data, calcolare la somma di un attributo relativo ai 6 giorni precedenti|Salvatore Fiandaca | 4 | with_variable, array_find, array_filter, array_agg, array_length, array_sum, array_slice
49|[rotazione simbolo parallelo ad una linea](rotazione_simbolo_parallelo_linea.md)|Lunghezze dei segmenti di un poligono|Salvatore Fiandaca | 3 | with_variable, overlay_nearest, line_interpolate_angle, closest_point, $geometry
50|[livello acqua](livello_acqua.md)|Effetto riempimento recipiente d'acqua|Salvatore Fiandaca | 4 | difference, make_rectangle_3points, point_n, bounds, make_point, x, y, bounds_height, intersection, area, second, now, area, format_number, $geometry
51|[layer vicino](layer_vicino.md)|Come determinare il layer più vicino ad un altro|Salvatore Fiandaca | 4 | @with_variable, array_get, array_foreach, array_find, array_min, overlay_nearest, distance, array, shortest_line, $geometry
52|[eliminare testo tra parentesi](eliminare_testo_tra_parentesi.md)|Eliminare il testo tra parentesi tonde |Salvatore Fiandaca | 3 | regexp_replace
53|[segmento minimo facciata-strada](segmento_minimo_facciata_strada.md)|Determinare il segmento minimo tra centroide facciata edifici e strada più vicina |Salvatore Fiandaca | 4 | @with_variable, generate_series, array_foreach, array_find, num_geometries, collect_geometries, geometry_n, segments_to_lines, overlay_nearest, distance, centroid, shortest_line, $geometry
54|[selezionare punti più vicini](selezionare_punti_vicini_punto.md)|Selezionare 'n' punti più vicini a partire da un punto selezionato |Salvatore Fiandaca | 4 | @with_variable, array_find, array_agg, array_foreach, aggregate, geom_to_wkt, make_circle, distance, overlay_nearest, intersects, is_selected, $geometry
55|[Nome del campo con massimo valore](maxValoreCampoNome.md)|Determina il nome del campo che contiene il valore massimo su un record |Salvatore Fiandaca | 4 | @with_variable, hstore_to_map, array_max, array_find, attributes, map_delete, map_avals, map_akeys
56|[Ricerca caratteri speciali](ricerca_caratteri_speciali.md)|Ricerca e selezione di record con campi che contengono caratteri speciali |Salvatore Fiandaca | 3 | regexp_substr, <>
57|[confrontare campi tabella](confrontare_campi_tabella.md)|Ricercare valori uguali in due campi diversi |Salvatore Fiandaca | 3 | array_to_string, array_majority, array_cat, string_to_array
58|[estrarre campo da un hstore](estrarre_campo_hstore.md)|Aggiungere un campo a partire da un altro campo in formato hstore (tipico di OSM) |Salvatore Fiandaca | 3 | hstore_to_map, map_get, to_int
59|[geometrie vicine ma con condizione](geometria_vicina_filtro_condizionato.md)|tracciare un segmento tra punti vicini che soddisfano la condizione `id1` <> `id2` |Salvatore Fiandaca | 4 | overlay_nearest, array_filter, attribute, make_line, collect_geometries, $geometry, geometry

## Partecipa

Se hai un esempio svolto e vuoi condividerlo puoi farlo, vedi sezione [Lavora con Noi](https://hfcqgis.opendatasicilia.it/contributing/#suggerire-esempiesercizi):

per maggiori info [scrivi all'autore](https://hfcqgis.opendatasicilia.it/autore/#contatti)

## Licenza
In questa sezione [Esempi svolti](docs/esempi/lista_esempi.md) e tutti gli esercizi svolti, la licenza è [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)