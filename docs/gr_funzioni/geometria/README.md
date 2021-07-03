# Geometria
[Manuale QGIS - in Inglese!](https://docs.qgis.org/testing/en/docs/user_manual/working_with_vector/expression.html#geometry-functions)

Questo gruppo contiene funzioni che operano sugli oggetti geometrici es. **lunghezza**, **area**.

 Funzione  | Descrizione | QGIS
----------:|:------------|:---
[$area]($area.html)|Restituisce l'area della geometria corrente|2.18
[$geometry]($geometry.html)|Restituisce la geometria dell'elemento attuale. Può essere usato per il processamento con altre funzioni|2.18
[$length]($length.html)|Restituisce la lunghezza di una linestring|2.18
[$perimeter]($perimeter.html)|Restituisce la lunghezza del perimetro della geometria corrente|2.18
[$x]($x.html)|Restituisce la coordinata x della geometria corrente|2.18
[$x_at]($x_at.html)|Recupera una coordinata x per la geometria dell'elemento corrente|2.18
[$y]($y.html)|Restituisce la coordinata y della geometria corrente|2.18
[$y_at]($y_at.html)|Recupera una coordinata y per la geometria dell'elemento corrente|2.18
[angle_at_vertex](angle_at_vertex.html)|Restituisce l'angolo della bisettrice (angolo medio) della geometria per un vertice specifico di una geometria di tipo linestring.|>=2.18
[area](area.html)|Restituisce l'area di un oggetto a geometria poligonale|2.18
[azimuth](azimuth.html)|Restituisce l'azimut dal nord quale angolo in radianti misurato in senso orario dalla verticale del punto_a al punto_b.|2.18
[boundary](boundary.html)|Restituisce l'area minima della combinazione dei confini della geometria (cioè il confine topologico della geometria)|>=2.18
[bounds](bounds.html)|Restituisce la geometria che rappresenta il perimetro di delimitazione di una geometria in ingresso. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria|2.18
[bounds_height](bounds_height.html)|Restituisce l'altezza del perimetro di delimitazione di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria|2.18
[bounds_width](bounds_width.html)|Restituisce la larghezza del perimetro di delimitazione una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria|2.18
[buffer](buffer.html)|Restituisce una geometria che rappresenta tutti i punti la cui distanza dalla geometria è minore o uguale alla distanza inserita|2.18
[buffer_by_m](buffer_by_m.html)|Crea un buffer lungo una geometria della linea in cui il diametro del buffer varia in base ai valori m nei vertici della linea|**>=3.2**
[centroid](centroid.html)|Restituisce il centro geometrico di una geometria|2.18
[close_line](close_line.html)|Restituisce una linestring chiusa della linestring|>=3.14
[closest_point](closest_point.html)|Restituisce il punto sulla geometria 1 che è più vicino alla geometria 2|>=2.14
[collect_geometries](funzioni/collect_geometries.md)|Raccoglie un set di geometrie in un oggetto geometria multiparte.|**>=3.10**
[combine](combine.html)|Restituisce la combinazione di due geometrie|2.18
[contains](contains.html)|Verifica se una geometria ne contiene un'altra|2.18
[convex_hull](convex_hull.html)|Restituisce il poligono convesso di una geometria|2.18
[crosses](crosses.html)|Verifica se una geometria interseca un'altra|2.18
[difference](difference.html)|Restituisce una geometria che rappresenta la porzione della _geometry_a_ che non interseca la _geometry_b_|2.18
[disjoint](disjoint.html)|Controlla qualora una geometria non ne interseca spazialmente un'altra. Restituisce true (1) se le geometrie non condividono nessuno spazio comune|2.18
[distance](distance.html)|Restituisce la distanza minima (basata su riferimento spaziale) tra due geometrie in unità proiettate|2.18
[distance_to_vertex](distance_to_vertex.html)|Restituisce la distanza lungo un geometria ad un vertice specificato|>=2.18
[end_point](end_point.html)|Restituisce l'ultimo nodo di una geometria|2.18
[extend](extend.html)| Estende l'inizio e la fine di una geometria di tipo linestring di una quantità specificata |**>=3.0**
[exterior_ring](exterior_ring.html)|Restituisce una linestring che rappresenta l'anello esterno di una geometria poligonale. Se la geometria non è un poligono, il risultato sarà nullo.|>=2.14
[extrude](extrude.html)|Restituisce una versione estrusa della geometria (Multi-)Curve o (Multi-)Linestring in ingresso, con un'estensione specificata da x e y.|2.18
[flip_coordinates](flip_coordinates.html)|Restituisce una copia della geometria con le coordinate x e y scambiate|**>=3.2**
[geom_from_gml](geom_from_gml.html)|Restituisce una geometria da una rappresentazione GML di una geometria|2.18
[geom_from_wkb](geom_from_wkb.html)|Restituisce una geometria creata da una rappresentazione binaria ben nota (WKB).|**>=3.12**
[geom_from_wkt](geom_from_wkt.html)|Restituisce una geometria creata da una rappresentazione Well-Known Text (WKT)|2.18
[geom_to_wkb](geom_to_wkb.html)|Restituisce la rappresentazione binaria ben nota (WKB) di una geometria come BLOB binario.|**>=3.12**
[geom_to_wkt](geom_to_wkt.html)|Restituisce la rappresentazione Well-Known Text (WKT) della geometria senza metadati del SR|2.18
[geometry](geometry.html)|Restituisce la geometria di un elemento|2.18
[geometry_n](geometry_n.html)|Restituisce una geometria specifica da una raccolta di geometrie, o null se la geometria in ingresso non è una raccolta|>=2.14
[hausdorff_distance](hausdorff_distance.html)|Restituisce la distanza di Hausdorff tra due geometrie |**>=3.0**
[inclination](inclination.html)|Restituisce l'inclinazione misurata dallo zenit (0) al nadir (180) del punto_a al punto_b |**>=3.0**
[interior_ring_n](interior_ring_n.html)|Restituisce un anello interno specifico da una geometria poligonale, o null se la geometria non è un poligono|>=2.14
[intersection](intersection.html)|Restituisce una geometria che rappresenta la porzione condivisa fra le due geometrie|2.18
[intersects](intersects.html)|Controlla qualora una geometria ne interseca un'altra|2.18
[intersects_bbox](intersects_bbox.html)|Controlla se il perimetro di delimitazione della geometria si sovrappone a quello di un'altra geometria|2.18
[is_closed](is_closed.html)|Restituisce vero se una line string è chiusa (i punti di inizio e di fine coincidono), o falso se una linea string non è chiusa|>=2.14
[is_empty](is_empty.html)|Restituisce vero se una geometria è vuota (senza coordinate), falso se la geometria non è vuota e NULL se non c'è geometria. Vedi anche `is_empty_or_null`.|**>=3.12**
[is_empty_or_null](is_empty_or_null.html)|Restituisce vero se una geometria è NULL o vuota (senza coordinate) o false in caso contrario. Questa funzione è come l'espressione "$ geometry IS NULL o is_empty ($ geometry)".|**>=3.12**
[is_multipart](is_multipart.html)|Restituisce vero se la geometria è Multi.|**>=3.14**
[is_valid](is_valid.html)|Restituisce vero se una geometria è valida; se è ben formato in 2D secondo le regole **OGC**|**>=3.12**
[length](length.html)|Restituisce il numero di caratteri in una stringa o la lunghezza di una geometria di tipo linestring|2.18
[line_interpolate_angle](line_interpolate_angle.html)|Restituisce l'angolo parallelo alla geometria ad una distanza specifica lungo una geometria di tipo linestring|>=2.18
[line_interpolate_point](line_interpolate_point.html)|Restituisce il punto interpolato ad una specifica distanza lungo un geometria di tipo linestring|>=2.18
[line_locate_point](line_locate_point.html)|Restituisce la distanza lungo una linestring corrispondente alla posizione più vicina alla linestring di una geometria puntuale specificata|>=2.18
[line_merge](line_merge.html)|Restituisce una geometria di tipo LineString o MultiLineString, dove qualsiasi LineString connessa dalla geometria in ingresso è stata fusa (merge) in una linestring singola|>=2.18
[line_substring](line_substring.html)|Restituisce la porzione di una geometria di linea (o curva) che rientra tra le distanze iniziale e finale specificate|**>=3.4**
[m](m.html)|Restituisce il valore m di una geometria puntuale|>=2.14
[m_max](m_max.html)|Restituisce il valore massimo m (misura) di una geometria|>=3.14
[m_min](m_min.html)|Restituisce il valore minimo m (misura) di una geometria|>=3.14
[main_angle](main_angle.html)|Restituisce l'angolo principale di una geometria (senso orario, in gradi dal Nord), il quale rappresenta l'angolo dell'orientamento del rettangolo minimo che copre completamente la geometria.|>=3.16
[make_circle](make_circle.html)|Crea un poligono circolare |**>=3.0**
[make_ellipse](make_ellipse.html)|Crea un poligono ellittico |**>=3.0**
[make_line](make_line.html)|Crea una geometria linea da una serie di geometrie punto|>=2.14
[make_point](make_point.html)|Crea una geometria punto da valori x ed y (e opzionalmente z ed m)|>=2.14
[make_point_m](make_point_m.html)|Crea una geometria punto da una coordinata x, y ed un valore m|>=2.14
[make_polygon](make_polygon.html)|Crea una geometria poligono da un'anello esterno e opzionalmente da geometrie ad anello interne|>=2.14
[make_rectangle_3points](make_rectangle_3points.md)|Crea un rettangolo da tre punti|**>=3.6**
[make_regular_polygon](make_regular_polygon.html)|Crea un poligono regolare |**>=3.0**
[make_square](make_square.md)|Crea un quadrato da una diagonale|**>=3.6**
[make_triangle](make_triangle.html)|Crea un poligono triangolare |**>=3.0**
[minimal_circle](minimal_circle.html)|Restituisce la circonferenza circoscritta minima di una geometria |**>=3.0**
[nodes_to_points](nodes_to_points.html)|Restituisce una geometria multi linea costituita da ogni nodo della geometria in ingresso|>=2.14
[num_geometries](num_geometries.html)|Restituisce il numero di geometrie in una raccolta di geometrie, o null se la geometria in ingresso non è una raccolta|>=2.14
[num_interior_rings](num_interior_rings.html)|Restituisce il numero di anelli interni in un poligono o in una raccolta di geometrie, o null se la geometria in ingresso non è un poligono o una raccolta|>=2.14
[num_points](num_points.html)|Restituisce il numero di vertici in una geometria|2.18
[num_rings](num_rings.html)|Restituisce il numero di anelli (includendo anche anelli esterni) in un poligono o in una raccolta di geometrie, o null se la geometria in ingresso non è un poligono o una raccolta|>=2.14
[offset_curve](offset_curve.html)|Restituisce una geometria formata facendo l'offset di una geometria di tipo linestring a lato |**>=3.0**
[order_parts](order_parts.html)|Ordina le parti di una MultiGeometria secondo un dato criterio|2.18
[oriented_bbox](oriented_bbox.html)|Restituisce una geometria che rappresenta il perimetro di delimitazione minimo orientato di una geometria |**>=3.0**
[overlaps](overlaps.html)|Controlla qualora una geometria si sovrapponga ad un'altra|2.18
[overlay_contains](overlay_contains.html)|Restituisce se l'elemento corrente contiene spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target contenuti nell'elemento corrente.|>=3.16
[overlay_crosses](overlay_crosses.html)|Restituisce se l'elemento corrente attraversa spazialmente almeno un elemento da un layer destinazione o un array di risultati basati su espressioni per gli elementi nel layer destinazione attraversati dall'elemento corrente.|>=3.16
[overlay_disjoint](overlay_disjoint.html)|Restituisce se l'elemento corrente è spazialmente disgiunto da tutti gli elementi di un layer destinazione, o un array di risultati basati su espressione per gli elementi nel layer destinazione che sono disgiunti dall'elemento corrente. |>=3.16
[overlay_equals](overlay_equals.html)|Restituisce se l'elemento corrente è spazialmente uguale ad almeno un elemento da un layer di destinazione o una matrice di risultati basati su espressioni per gli elementi nel layer di destinazione che sono spazialmente uguali all'elemento corrente.|>=3.16
[overlay_intersects](overlay_intersects.html)|Restituisce se l'elemento corrente interseca spazialmente almeno un elemento da un layer di destinazione o un array di risultati basati su espressioni per gli elementi nel layer di destinazione intersecati dall'elemento corrente.|>=3.16
[overlay_nearest](overlay_nearest.html)|Restituisce se l'elemento corrente ha elementi da un layer di destinazione entro una data distanza o una matrice di risultati basati su espressioni per gli elementi nel layer di destinazione entro una distanza dall'elemento corrente.|>=3.16
[overlay_touches](overlay_touches.html)|Restituisce se l'elemento corrente tocca spazialmente almeno un elemento da un layer di destinazione o un array di risultati basati su espressioni per gli elementi nel layer di destinazione toccati dall'elemento corrente.|>=3.16
[overlay_within](overlay_within.html)|Restituisce se l'elemento corrente è spazialmente all'interno di almeno un elemento da layer destinazione, o un array di risultati basati su espressione per gli elementi nel layer destinazione che contengono l'elemento corrente. |>=3.16
[perimeter](perimeter.html)|Calcola il perimetro di un oggetto a geometria poligonale|2.18
[point_n](point_n.html)|Restituisce un nodo specifico da una geometria|2.18
[point_on_surface](point_on_surface.html)|Restituisce un punto garantendo che sia giacente sulla superficie della geometria|>=2.14
[pole_of_inaccessibility](pole_of_inaccessibility.html)|Calcola il polo dell'inaccessibilità approssimato per una superficie, che è il punto interno più distante dal contorno della superficie |**>=3.0**
[project](project.html)|Restituisce un punto proiettato da un punto di partenza usando una distanza e una direzione di immersione (azimut) in radianti|2.18
[relate](relate.html)|Testa la rappresentazione Dimensional Extended 9 Intersection Model (DE-9IM) della relazione tra due geometrie|>=2.14
[reverse](reverse.html)|Inverte la direzione di una line string invertendo l'ordine dei sui vertici|>=2.14
[rotate](rotate.html)|Restituisce una versione ruotata di una geometria. I calcoli si trovano nel sistema di riferimento spaziale di questa geometria.|**>=3.12**
[segments_to_lines](segments_to_lines.html)|Restituisce una geometria multi linea consistente in una linea per ogni segmento nella geometria in ingresso|>=2.14
[shortest_line](shortest_line.html)|Restituisce la linea più corta che unisce la geometria 1 alla geometria 2|>=2.14
[simplify](simplify.html)|Semplifica una geometria rimuovendo nodi usando una soglia basata sulla distanza (cioè, l'algoritmo Douglas Peucker) |**>=3.0**
[simplify_vw](simplify_vw.html)|Semplifica una geometria rimuovendo nodi usando una soglia basata sull'area (cioè, l'algoritmo Visvalingam-Whyatt ) |**>=3.0**
[single_sided_buffer](single_sided_buffer.html)|Restituisce una geometria formata facendo un buffer solo da un lato di una geometria di tipo linestring |**>=3.0**
[smooth](smooth.html)|Smussa una geometria con l'aggiunta di ulteriori nodi che arrotondano gli angoli nella geometria |**>=3.0**
[start_point](start_point.html)|Restituisce il primo nodo di una geometria|2.18
[sym_difference](sym_difference.html)|Restituisce una geometria che rappresenta la porzione di due geometrie che non si interseca|2.18
[tapered_buffer](tapered_buffer.html)|Crea un buffer lungo una geometria della linea in cui il diametro del buffer varia in modo uniforme sulla lunghezza della linea|**>=3.2**
[touches](touches.html)|Verifica se una geometria tocca un'altra|2.18
[transform](transform.html)|Restituisce la geometria trasformata da un SR sorgente ad un SR di destinazione|2.18
[translate](translate.html)|Restituisce una versione traslata di una geometria|>=2.14
[union](union.html)|Restituisce una geometria che rappresenta l'insieme dei punti dell'unione delle geometrie|2.18
[wedge_buffer](wedge_buffer.html)|Restituisce un buffer a forma di cuneo che ha origine da una geometria del punto |**>=3.2**
[within](within.html)|Controlla qualora una geometria sia interna ad un'altra|2.18
[x](x.html)|Restituisce la coordinata x di una geometria punto, o la coordinata x del centroide di una geometria non puntuale|2.18
[x_min](x_min.html)|Restituisce la coordinata x minima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria|2.18
[x_max](x_max.html)|Restituisce la coordinata x massima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria|2.18
[y](y.html)|Restituisce la coordinata y di una geometria puntuale, o la coordinata y del centroide di una geometria non puntuale|2.18
[y_min](y_min.html)|Restituisce la coordinata y minima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria|2.18
[y_max](y_max.html)|Restituisce la coordinata y massima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria|2.18
[z](z.html)|Restituisce la coordinata z di una geometria puntuale|>=2.14
[z_max](z_max.html)|Restituisce la coordinata z massima di una geometria.|>=3.14
[z_min](z_min.html)|Restituisce la coordinata z minima di una geometria.|>=3.14

![](../../img/geometria/gruppo_geometria1.png)

## Evoluzione funzioni

![](../../img/geometria/gruppo_geometria2.png)
