Geometria
=========

`Manuale QGIS - in Inglese!`_

.. _Manuale QGIS - in Inglese!: https://docs.qgis.org/testing/en/docs/user_manual/working_with_vector/expression.html#geometry-functions

+---------------------------+--------------------------------+-----------+
| Funzione                  | Descrizione                    |   QGIS    |
+===========================+================================+===========+
| `$area`_                  | Restituisce l’area della       |   2.18    |
|                           | geometria corrente             |           |
+---------------------------+--------------------------------+-----------+
| `$geometry`_              | Restituisce la geometria       |   2.18    |
|                           | dell’elemento attuale. Può     |           |
|                           | essere usato per il            |           |
|                           | processamento con altre        |           |
|                           | funzioni                       |           |
+---------------------------+--------------------------------+-----------+
| `$length`_                | Restituisce la lunghezza di    |   2.18    |
|                           | una linestring                 |           |
+---------------------------+--------------------------------+-----------+
| `$perimeter`_             | Restituisce la lunghezza del   |   2.18    |
|                           | perimetro della geometria      |           |
|                           | corrente                       |           |
+---------------------------+--------------------------------+-----------+
| `$x`_                     | Restituisce la coordinata x    |   2.18    |
|                           | della geometria corrente       |           |
+---------------------------+--------------------------------+-----------+
| `$x_at`_                  | Recupera una coordinata x per  |   2.18    |
|                           | la geometria dell’elemento     |           |
|                           | corrente                       |           |
+---------------------------+--------------------------------+-----------+
| `$y`_                     | Restituisce la coordinata y    |   2.18    |
|                           | della geometria corrente       |           |
+---------------------------+--------------------------------+-----------+
| `$y_at`_                  | Recupera una coordinata y per  |   2.18    |
|                           | la geometria dell’elemento     |           |
|                           | corrente                       |           |
+---------------------------+--------------------------------+-----------+
| `angle_at_vertex`_        | Restituisce l’angolo della     |   >=2.18  |
|                           | bisettrice (angolo medio)      |           |
|                           | della geometria per un vertice |           |
|                           | specifico di una geometria di  |           |
|                           | tipo linestring.               |           |
+---------------------------+--------------------------------+-----------+
| `area`_                   | Restituisce l’area di un       |   2.18    |
|                           | oggetto a geometria poligonale |           |
+---------------------------+--------------------------------+-----------+
| `azimuth`_                | Restituisce l’azimut dal nord  |   2.18    |
|                           | quale angolo in radianti       |           |
|                           | misurato in senso orario dalla |           |
|                           | verticale del punto_a al       |           |
|                           | punto_b.                       |           |
+---------------------------+--------------------------------+-----------+
| `boundary`_               | Restituisce l’area minima      |   >=2.18  |
|                           | della combinazione dei confini |           |
|                           | della geometria (cioè il       |           |
|                           | confine topologico della       |           |
|                           | geometria)                     |           |
+---------------------------+--------------------------------+-----------+
| `bounds`_                 | Restituisce la geometria che   |   2.18    |
|                           | rappresenta il perimetro di    |           |
|                           | delimitazione di una geometria |           |
|                           | in ingresso. I calcoli sono    |           |
|                           | effettuati nel sistema di      |           |
|                           | riferimento spaziale di tale   |           |
|                           | geometria                      |           |
+---------------------------+--------------------------------+-----------+
| `bounds_height`_          | Restituisce l’altezza del      |   2.18    |
|                           | perimetro di delimitazione di  |           |
|                           | una geometria. I calcoli sono  |           |
|                           | effettuati nel sistema di      |           |
|                           | riferimento spaziale di tale   |           |
|                           | geometria                      |           |
+---------------------------+--------------------------------+-----------+
| `bounds_width`_           | Restituisce la larghezza del   |   2.18    |
|                           | perimetro di delimitazione una |           |
|                           | geometria. I calcoli sono      |           |
|                           | effettuati nel sistema di      |           |
|                           | riferimento spaziale di tale   |           |
|                           | geometria                      |           |
+---------------------------+--------------------------------+-----------+
| `buffer`_                 | Restituisce una geometria che  |   2.18    |
|                           | rappresenta tutti i punti la   |           |
|                           | cui distanza dalla geometria è |           |
|                           | minore o uguale alla distanza  |           |
|                           | inserita                       |           |
+---------------------------+--------------------------------+-----------+
| `buffer_by_m`_            | Crea un buffer lungo una       | **>=3.2** |
|                           | geometria della linea in cui   |           |
|                           | il diametro del buffer varia   |           |
|                           | in base ai valori m nei        |           |
|                           | vertici della linea            |           |
+---------------------------+--------------------------------+-----------+
| `centroid`_               | Restituisce il centro          |   2.18    |
|                           | geometrico di una geometria    |           |
+---------------------------+--------------------------------+-----------+
| `closest_point`_          | Restituisce il punto sulla     |   >=2.14  |
|                           | geometria 1 che è più vicino   |           |
|                           | alla geometria 2               |           |
+---------------------------+--------------------------------+-----------+
| `combine`_                | Restituisce la combinazione di |    2.18   |
|                           | due geometrie                  |           |
+---------------------------+--------------------------------+-----------+
| `contains`_               | Verifica se una geometria ne   |    2.18   |
|                           | contiene un’altra              |           |
+---------------------------+--------------------------------+-----------+
| `convex_hull`_            | Restituisce il poligono        |   2.18    |
|                           | convesso di una geometria      |           |
+---------------------------+--------------------------------+-----------+
| `crosses`_                | Verifica se una geometria      |   2.18    |
|                           | interseca un’altra             |           |
+---------------------------+--------------------------------+-----------+
| `difference`_             | Restituisce una geometria che  |   2.18    |
|                           | rappresenta la porzione della  |           |
|                           | *geometry_a* che non interseca |           |
|                           | la *geometry_b*                |           |
+---------------------------+--------------------------------+-----------+
| `disjoint`_               | Controlla qualora una          |   2.18    |
|                           | geometria non ne interseca     |           |
|                           | spazialmente un’altra.         |           |
|                           | Restituisce true (1) se le     |           |
|                           | geometrie non condividono      |           |
|                           | nessuno spazio comune          |           |
+---------------------------+--------------------------------+-----------+
| `distance`_               | Restituisce la distanza minima |   2.18    |
|                           | (basata su riferimento         |           |
|                           | spaziale) tra due geometrie in |           |
|                           | unità proiettate               |           |
+---------------------------+--------------------------------+-----------+
| `distance_to_vertex`_     | Restituisce la distanza lungo  |   >=2.18  |
|                           | un geometria ad un vertice     |           |
|                           | specificato                    |           |
+---------------------------+--------------------------------+-----------+
| `end_point`_              | Restituisce l’ultimo nodo di   |   2.18    |
|                           | una geometria                  |           |
+---------------------------+--------------------------------+-----------+
| `extend`_                 | Estende l’inizio e la fine di  | **>=3.0** |
|                           | una geometria di tipo          |           |
|                           | linestring di una quantità     |           |
|                           | specificata                    |           |
+---------------------------+--------------------------------+-----------+
| `exterior_ring`_          | Restituisce una linestring che |   >=2.14  |
|                           | rappresenta l’anello esterno   |           |
|                           | di una geometria poligonale.   |           |
|                           | Se la geometria non è un       |           |
|                           | poligono, il risultato sarà    |           |
|                           | nullo.                         |           |
+---------------------------+--------------------------------+-----------+
| `extrude`_                | Restituisce una versione       |   2.18    |
|                           | estrusa della geometria        |           |
|                           | (Multi-)Curve o                |           |
|                           | (Multi-)Linestring in          |           |
|                           | ingresso, con un’estensione    |           |
|                           | specificata da x e y.          |           |
+---------------------------+--------------------------------+-----------+
| `flip_coordinates`_       | Restituisce una copia della    | **>=3.2** |
|                           | geometria con le coordinate x  |           |
|                           | e y scambiate                  |           |
+---------------------------+--------------------------------+-----------+
| `force_rhr`_              | Forza una geometria a          |           |
|                           | rispettare la regola           |           |
|                           | della mano destra              | **>=3.6** |
+---------------------------+--------------------------------+-----------+
| `geom_from_gml`_          | Restituisce una geometria da   |   2.18    |
|                           | una rappresentazione GML di    |           |
|                           | una geometria                  |           |
+---------------------------+--------------------------------+-----------+
| `geom_from_wkt`_          | Restituisce una geometria      |   2.18    |
|                           | creata da una rappresentazione |           |
|                           | Well-Known Text (WKT)          |           |
+---------------------------+--------------------------------+-----------+
| `geom_to_wkt`_            | Restituisce la                 |   2.18    |
|                           | rappresentazione Well-Known    |           |
|                           | Text (WKT) della geometria     |           |
|                           | senza metadati del SR          |           |
+---------------------------+--------------------------------+-----------+
| `geometry`_               | Restituisce la geometria di un |   2.18    |
|                           | elemento                       |           |
+---------------------------+--------------------------------+-----------+
| `geometry_n`_             | Restituisce una geometria      |   >=2.14  |
|                           | specifica da una raccolta di   |           |
|                           | geometrie, o null se la        |           |
|                           | geometria in ingresso non è    |           |
|                           | una raccolta                   |           |
+---------------------------+--------------------------------+-----------+
| `hausdorff_distance`_     | Restituisce la distanza di     | **>=3.0** |
|                           | Hausdorff tra due geometrie    |           |
+---------------------------+--------------------------------+-----------+
| `inclination`_            | Restituisce l’inclinazione     | **>=3.0** |
|                           | misurata dallo zenit (0) al    |           |
|                           | nadir (180) del punto_a al     |           |
|                           | punto_b                        |           |
+---------------------------+--------------------------------+-----------+
| `interior_ring_n`_        | Restituisce un anello interno  |   >=2.14  |
|                           | specifico da una geometria     |           |
|                           | poligonale, o null se la       |           |
|                           | geometria non è un poligono    |           |
+---------------------------+--------------------------------+-----------+
| `intersection`_           | Restituisce una geometria che  |   2.18    |
|                           | rappresenta la porzione        |           |
|                           | condivisa fra le due geometrie |           |
+---------------------------+--------------------------------+-----------+
| `intersects`_             | Controlla qualora una          |   2.18    |
|                           | geometria ne interseca         |           |
|                           | un’altra                       |           |
+---------------------------+--------------------------------+-----------+
| `intersects_bbox`_        | Controlla se il perimetro di   |   2.18    |
|                           | delimitazione della geometria  |           |
|                           | si sovrappone a quello di      |           |
|                           | un’altra geometria             |           |
+---------------------------+--------------------------------+-----------+
| `is_closed`_              | Restituisce vero se una line   |   >=2.14  |
|                           | string è chiusa (i punti di    |           |
|                           | inizio e di fine coincidono),  |           |
|                           | o falso se una linea string    |           |
|                           | non è chiusa                   |           |
+---------------------------+--------------------------------+-----------+
| `length`_                 | Restituisce il numero di       |   2.18    |
|                           | caratteri in una stringa o la  |           |
|                           | lunghezza di una geometria di  |           |
|                           | tipo linestring                |           |
+---------------------------+--------------------------------+-----------+
| `line_interpolate_angle`_ | Restituisce l’angolo parallelo |   >=2.18  |
|                           | alla geometria ad una distanza |           |
|                           | specifica lungo una geometria  |           |
|                           | di tipo linestring             |           |
+---------------------------+--------------------------------+-----------+
| `line_interpolate_point`_ | Restituisce il punto           |   >=2.18  |
|                           | interpolato ad una specifica   |           |
|                           | distanza lungo un geometria di |           |
|                           | tipo linestring                |           |
+---------------------------+--------------------------------+-----------+
| `line_locate_point`_      | Restituisce la distanza lungo  |   >=2.18  |
|                           | una linestring corrispondente  |           |
|                           | alla posizione più vicina alla |           |
|                           | linestring di una geometria    |           |
|                           | puntuale specificata           |           |
+---------------------------+--------------------------------+-----------+
| `line_merge`_             | Restituisce una geometria di   |   >=2.18  |
|                           | tipo LineString o              |           |
|                           | MultiLineString, dove          |           |
|                           | qualsiasi LineString connessa  |           |
|                           | dalla geometria in ingresso è  |           |
|                           | stata fusa (merge) in una      |           |
|                           | linestring singola             |           |
+---------------------------+--------------------------------+-----------+
| `line_substring`_         | Restituisce la porzione di una | >=3.4     |
|                           | geometria di linea (o curva)   |           |
|                           | che rientra tra le distanze    |           |
|                           | iniziale e finale specificate  |           |
+---------------------------+--------------------------------+-----------+
| `m`_                      | Restituisce il valore m di una |   >=2.14  |
|                           | geometria puntuale             |           |
+---------------------------+--------------------------------+-----------+
| `make_circle`_            | Crea un poligono circolare     | **>=3.0** |
|                           |                                |           |
+---------------------------+--------------------------------+-----------+
| `make_ellipse`_           | Crea un poligono ellittico     | **>=3.0** |
|                           |                                |           |
+---------------------------+--------------------------------+-----------+
| `make_line`_              | Crea una geometria linea da    |   >=2.14  |
|                           | una serie di geometrie punto   |           |
+---------------------------+--------------------------------+-----------+
| `make_point`_             | Crea una geometria punto da    |   >=2.14  |
|                           | valori x ed y (e opzionalmente |           |
|                           | z ed m)                        |           |
+---------------------------+--------------------------------+-----------+
| `make_point_m`_           | Crea una geometria punto da    |   >=2.14  |
|                           | una coordinata x, y ed un      |           |
|                           | valore m                       |           |
+---------------------------+--------------------------------+-----------+
| `make_polygon`_           | Crea una geometria poligono da |   >=2.14  |
|                           | un’anello esterno e            |           |
|                           | opzionalmente da geometrie ad  |           |
|                           | anello interne                 |           |
+---------------------------+--------------------------------+-----------+
| `make_rectangle_3points`_ |Crea un rettangolo da tre punti |**>=3.6**  |
+---------------------------+--------------------------------+-----------+
| `make_regular_polygon`_   | Crea un poligono regolare      | **>=3.0** |
|                           |                                |           |
+---------------------------+--------------------------------+-----------+
| `make_square`_            |Crea un quadrato da una         |           |
|                           |  diagonale                     |**>=3.6**  |
+---------------------------+--------------------------------+-----------+
| `make_triangle`_          | Crea un poligono triangolare   | **>=3.0** |
|                           |                                |           |
+---------------------------+--------------------------------+-----------+
| `minimal_circle`_         | Restituisce la circonferenza   | **>=3.0   |
|                           | circoscritta minima di una     |           |
|                           | geometria                      |           |
+---------------------------+--------------------------------+-----------+
| `nodes_to_points`_        | Restituisce una geometria      |   >=2.14  |
|                           | multi linea costituita da ogni |           |
|                           | nodo della geometria in        |           |
|                           | ingresso                       |           |
+---------------------------+--------------------------------+-----------+
| `num_geometries`_         | Restituisce il numero di       |   >=2.14  |
|                           | geometrie in una raccolta di   |           |
|                           | geometrie, o null se la        |           |
|                           | geometria in ingresso non è    |           |
|                           | una raccolta                   |           |
+---------------------------+--------------------------------+-----------+
| `num_interior_rings`_     | Restituisce il numero di       |   >=2.14  |
|                           | anelli interni in un poligono  |           |
|                           | o in una raccolta di           |           |
|                           | geometrie, o null se la        |           |
|                           | geometria in ingresso non è un |           |
|                           | poligono o una raccolta        |           |
+---------------------------+--------------------------------+-----------+
| `num_points`_             | Restituisce il numero di       |   2.18    |
|                           | vertici in una geometria       |           |
+---------------------------+--------------------------------+-----------+
| `num_rings`_              | Restituisce il numero di       |   >=2.14  |
|                           | anelli (includendo anche       |           |
|                           | anelli esterni) in un poligono |           |
|                           | o in una raccolta di           |           |
|                           | geometrie, o null se la        |           |
|                           | geometria in ingresso non è un |           |
|                           | poligono o una raccolta        |           |
+---------------------------+--------------------------------+-----------+
| `offset_curve`_           | Restituisce una geometria      | **>=3.0** |
|                           | formata facendo l’offset di    |           |
|                           | una geometria di tipo          |           |
|                           | linestring a lato              |           |
+---------------------------+--------------------------------+-----------+
| `order_parts`_            | Ordina le parti di una         |   2.18    |
|                           | MultiGeometria secondo un dato |           |
|                           | criterio                       |           |
+---------------------------+--------------------------------+-----------+
| `oriented_bbox`_          | Restituisce una geometria che  | **>=3.0** |
|                           | rappresenta il perimetro di    |           |
|                           | delimitazione minimo orientato |           |
|                           | di una geometria               |           |
+---------------------------+--------------------------------+-----------+
| `overlaps`_               | Controlla qualora una          |   2.18    |
|                           | geometria si sovrapponga ad    |           |
|                           | un’altra                       |           |
+---------------------------+--------------------------------+-----------+
| `perimeter`_              | Calcola il perimetro di un     |   2.18    |
|                           | oggetto a geometria poligonale |           |
+---------------------------+--------------------------------+-----------+
| `point_n`_                | Restituisce un nodo specifico  |   2.18    |
|                           | da una geometria               |           |
+---------------------------+--------------------------------+-----------+
| `point_on_surface`_       | Restituisce un punto           |   >=2.14  |
|                           | garantendo che sia giacente    |           |
|                           | sulla superficie della         |           |
|                           | geometria                      |           |
+---------------------------+--------------------------------+-----------+
| `pole_of_inaccessibility`_| Calcola il polo                | **>=3.0** |
|                           | dell’inaccessibilità           |           |
|                           | approssimato per una           |           |
|                           | superficie, che è il punto     |           |
|                           | interno più distante dal       |           |
|                           | contorno della superficie      |           |
+---------------------------+--------------------------------+-----------+
| `project`_                | Restituisce un punto           |   2.18    |
|                           | proiettato da un punto di      |           |
|                           | partenza usando una distanza e |           |
|                           | una direzione di immersione    |           |
|                           | (azimut) in radianti           |           |
+---------------------------+--------------------------------+-----------+
| `relate`_                 | Testa la rappresentazione      |   >=2.14  |
|                           | Dimensional Extended 9         |           |
|                           | Intersection Model (DE-9IM)    |           |
|                           | della relazione tra due        |           |
|                           | geometrie                      |           |
+---------------------------+--------------------------------+-----------+
| `reverse`_                | Inverte la direzione di una    |   >=2.14  |
|                           | line string invertendo         |           |
|                           | l’ordine dei sui vertici       |           |
+---------------------------+--------------------------------+-----------+
| `segments_to_lines`_      | Restituisce una geometria      |   >=2.14  |
|                           | multi linea consistente in una |           |
|                           | linea per ogni segmento nella  |           |
|                           | geometria in ingresso          |           |
+---------------------------+--------------------------------+-----------+
| `shortest_line`_          | Restituisce la linea più corta |   >=2.14  |
|                           | che unisce la geometria 1 alla |           |
|                           | geometria 2                    |           |
+---------------------------+--------------------------------+-----------+
| `simplify`_               | Semplifica una geometria       | **>=3.0** |
|                           | rimuovendo nodi usando una     |           |
|                           | soglia basata sulla distanza   |           |
|                           | (cioè, l’algoritmo Douglas     |           |
|                           | Peucker)                       |           |
+---------------------------+--------------------------------+-----------+
| `simplify_vw`_            | Semplifica una geometria       | **>=3.0** |
|                           | rimuovendo nodi usando una     |           |
|                           | soglia basata sull’area (cioè, |           |
|                           | l’algoritmo Visvalingam-Whyatt |           |
|                           | )                              |           |
+---------------------------+--------------------------------+-----------+
| `single_sided_buffer`_    | Restituisce una geometria      | **>=3.0** |
|                           | formata facendo un buffer solo |           |
|                           | da un lato di una geometria di |           |
|                           | tipo linestring                |           |
+---------------------------+--------------------------------+-----------+
| `smooth`_                 | Smussa una geometria con       | **>=3.0** |
|                           | l’aggiunta di ulteriori nodi   |           |
|                           | che arrotondano gli angoli     |           |
|                           | nella geometria                |           |
+---------------------------+--------------------------------+-----------+
| `start_point`_            | Restituisce il primo nodo di   |   2.18    |
|                           | una geometria                  |           |
+---------------------------+--------------------------------+-----------+
| `sym_difference`_         | Restituisce una geometria che  |   2.18    |
|                           | rappresenta la porzione di due |           |
|                           | geometrie che non si interseca |           |
+---------------------------+--------------------------------+-----------+
| `tapered_buffer`_         | Crea un buffer lungo una       | **>=3.2** |
|                           | geometria della linea in cui   |           |
|                           | il diametro del buffer varia   |           |
|                           | in modo uniforme sulla         |           |
|                           | lunghezza della linea          |           |
+---------------------------+--------------------------------+-----------+
| `touches`_                | Verifica se una geometria      |   2.18    |
|                           | tocca un’altra                 |           |
+---------------------------+--------------------------------+-----------+
| `transform`_              | Restituisce la geometria       |   2.18    |
|                           | trasformata da un SR sorgente  |           |
|                           | ad un SR di destinazione       |           |
+---------------------------+--------------------------------+-----------+
| `translate`_              | Restituisce una versione       |   >=2.14  |
|                           | traslata di una geometria      |           |
+---------------------------+--------------------------------+-----------+
| `union`_                  | Restituisce una geometria che  |   2.18    |
|                           | rappresenta l’insieme dei      |           |
|                           | punti dell’unione delle        |           |
|                           | geometrie                      |           |
+---------------------------+--------------------------------+-----------+
| `wedge_buffer`_           | Restituisce un buffer a forma  | **>=3.2** |
|                           | di cuneo che ha origine da una |           |
|                           | geometria del punto            |           |
+---------------------------+--------------------------------+-----------+
| `within`_                 | Controlla qualora una          |   2.18    |
|                           | geometria sia interna ad       |           |
|                           | un’altra                       |           |
+---------------------------+--------------------------------+-----------+
| `x`_                      | Restituisce la coordinata x di |   2.18    |
|                           | una geometria punto, o la      |           |
|                           | coordinata x del centroide di  |           |
|                           | una geometria non puntuale     |           |
+---------------------------+--------------------------------+-----------+
| `x_min`_                  | Restituisce la coordinata x    |   2.18    |
|                           | minima di una geometria. I     |           |
|                           | calcoli sono effettuati nel    |           |
|                           | sistema di riferimento         |           |
|                           | spaziale di tale geometria     |           |
+---------------------------+--------------------------------+-----------+
| `x_max`_                  | Restituisce la coordinata x    |   2.18    |
|                           | massima di una geometria. I    |           |
|                           | calcoli sono effettuati nel    |           |
|                           | sistema di riferimento         |           |
|                           | spaziale di tale geometria     |           |
+---------------------------+--------------------------------+-----------+
| `y`_                      | Restituisce la coordinata y di |   2.18    |
|                           | una geometria puntuale, o la   |           |
|                           | coordinata y del centroide di  |           |
|                           | una geometria non puntuale     |           |
+---------------------------+--------------------------------+-----------+
| `y_min`_                  | Restituisce la coordinata y    |   2.18    |
|                           | minima di una geometria. I     |           |
|                           | calcoli sono effettuati nel    |           |
|                           | sistema di riferimento         |           |
|                           | spaziale di tale geometria     |           |
+---------------------------+--------------------------------+-----------+
| `y_max`_                  | Restituisce la coordinata y    |   2.18    |
|                           | massima di una geometria. I    |           |
|                           | calcoli sono effettuati nel    |           |
|                           | sistema di riferimento         |           |
|                           | spaziale di tale geometria     |           |
+---------------------------+--------------------------------+-----------+
| `z`_                      | Restituisce la coordinata z di |   >=2.14  |
|                           | una geometria puntuale         |           |
+---------------------------+--------------------------------+-----------+


.. _$area: $area.html
.. _$geometry: $geometry.html
.. _$length: $length.html
.. _$perimeter: $perimeter.html
.. _$x: $x.html
.. _$x_at: $x_at.html
.. _$y: $y.html
.. _$y_at: $y_at.html
.. _angle_at_vertex: angle_at_vertex.html
.. _area: area.html
.. _azimuth: azimuth.html
.. _boundary: boundary.html
.. _bounds: bounds.html
.. _bounds_height: bounds_height.html
.. _bounds_width: bounds_width.html
.. _buffer: buffer.html
.. _buffer_by_m: buffer_by_m.html
.. _centroid: centroid.html
.. _closest_point: closest_point.html
.. _combine: combine.html
.. _contains: contains.html
.. _convex_hull: convex_hull.html
.. _crosses: crosses.html
.. _difference: difference.html
.. _disjoint: disjoint.html
.. _distance: distance.html
.. _distance_to_vertex: distance_to_vertex.html
.. _end_point: end_point.html
.. _extend: extend.html
.. _exterior_ring: exterior_ring.html
.. _extrude: extrude.html
.. _flip_coordinates: flip_coordinates.html
.. _force_rhr: force_rhr.html
.. _geom_from_gml: geom_from_gml.html
.. _geom_from_wkt: geom_from_wkt.html
.. _geom_to_wkt: geom_to_wkt.html
.. _geometry: geometry.html
.. _geometry_n: geometry_n.html
.. _hausdorff_distance: hausdorff_distance.html
.. _inclination: inclination.html
.. _interior_ring_n: interior_ring_n.html
.. _intersection: intersection.html
.. _intersects: intersects.html
.. _intersects_bbox: intersects_bbox.html
.. _is_closed: is_closed.html
.. _length: length.html
.. _line_interpolate_angle: line_interpolate_angle.html
.. _line_interpolate_point: line_interpolate_point.html
.. _line_locate_point: line_locate_point.html
.. _line_merge: line_merge.html
.. _line_substring: line_substring.html
.. _m: m.html
.. _make_circle: make_circle.html
.. _make_ellipse: make_ellipse.html
.. _make_line: make_line.html
.. _make_point: make_point.html
.. _make_point_m: make_point_m.html
.. _make_polygon: make_polygon.html
.. _make_rectangle_3points: make_rectangle_3points.html
.. _make_regular_polygon: make_regular_polygon.html
.. _make_square: make_square.html
.. _make_triangle: make_triangle.html
.. _minimal_circle: minimal_circle.html
.. _nodes_to_points: nodes_to_points.html
.. _num_geometries: num_geometries.html
.. _num_interior_rings: num_interior_rings.html
.. _num_points: num_points.html
.. _num_rings: num_rings.html
.. _offset_curve: offset_curve.html
.. _order_parts: order_parts.html
.. _oriented_bbox: oriented_bbox.html
.. _overlaps: overlaps.html
.. _perimeter: perimeter.html
.. _point_n: point_n.html
.. _point_on_surface: point_on_surface.html
.. _pole_of_inaccessibility: pole_of_inaccessibility.html
.. _project: project.html
.. _relate: relate.html
.. _reverse: reverse.html
.. _segments_to_lines: segments_to_lines.html
.. _shortest_line: shortest_line.html
.. _simplify: simplify.html
.. _simplify_vw: simplify_vw.html
.. _single_sided_buffer: single_sided_buffer.html
.. _smooth: smooth.html
.. _start_point: start_point.html
.. _sym_difference: sym_difference.html
.. _tapered_buffer: tapered_buffer.html
.. _touches: touches.html
.. _transform: transform.html
.. _translate: translate.html
.. _union: union.html
.. _wedge_buffer: wedge_buffer.html
.. _within: within.html
.. _x: x.html
.. _x_min: x_min.html
.. _x_max: x_max.html
.. _y: y.html
.. _y_min: y_min.html
.. _y_max: y_max.html
.. _z: z.html

|image0|

**Evoluzione funzioni**

|image1|

.. |image0| image:: /img/geometria/gruppo_geometria1.png
.. |image1| image:: /img/geometria/gruppo_geometria2.png


**Elenco funzioni Geometria**

.. toctree::
   :maxdepth: 3
   
   $area
   $geometry
   $length
   $perimeter
   $x
   $x_at
   $y
   $y_at
   angle_at_vertex
   area
   azimuth
   boundary
   bounds
   bounds_height
   bounds_width
   buffer
   buffer_by_m
   centroid
   closest_point
   combine
   contains
   convex_hull
   crosses
   difference
   disjoint
   distance
   distance_to_vertex
   end_point
   extend
   exterior_ring
   extrude
   flip_coordinates
   force_rhr
   geom_from_gml
   geom_from_wkt
   geom_to_wkt
   geometry
   geometry_n
   hausdorff_distance
   inclination
   interior_ring_n
   intersection
   intersects
   intersects_bbox
   is_closed
   length
   line_interpolate_angle
   line_interpolate_point
   line_locate_point
   line_merge
   line_substring
   m
   make_circle
   make_ellipse
   make_line
   make_point
   make_point_m
   make_polygon
   make_rectangle_3points
   make_regular_polygon
   make_square
   make_triangle
   minimal_circle
   nodes_to_points
   num_geometries
   num_interior_rings
   num_points
   num_rings
   offset_curve
   order_parts
   oriented_bbox
   overlaps
   perimeter
   point_n
   point_on_surface
   pole_of_inaccessibility
   project
   relate
   reverse
   segments_to_lines
   shortest_line
   simplify
   simplify_vw
   single_sided_buffer
   smooth
   start_point
   sym_difference
   tapered_buffer
   touches
   transform
   translate
   union
   wedge_buffer
   within
   x
   x_min
   x_max
   y
   y_min
   y_max
   z 
