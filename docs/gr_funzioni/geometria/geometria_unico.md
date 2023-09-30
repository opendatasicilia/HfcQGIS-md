---
social_image: img/card_social/hfc_gr_geom.png
tags:
  - gruppo
---

# Gruppo Geometria  

!!! Abstract
	**Questo gruppo contiene funzioni che operano sugli oggetti geometrici es: _lunghezza_, _area_.**

---

## affine_transform

Restituisce la geometria dopo una trasformazione affine. I calcoli sono nel sistema di riferimento spaziale di questa geometria. Le operazioni vengono eseguite in un ordine di scala, rotazione, traslazione. Se c'è un offset Z o M ma la coordinata non è presente nella geometria, verrà aggiunta.

Sintassi

- affine_transform(_<span style="color:red;">geometry</span>_,_<span style="color:red;">deltaX</span>_,_<span style="color:red;">deltaY</span>_,_<span style="color:red;">rotationZ</span>_,_<span style="color:red;">scaleX</span>_,_<span style="color:red;">scaleY</span>_[,_<span style="color:red;">deltaZ=0</span>_][,_<span style="color:red;">deltaM=0</span>_][,_<span style="color:red;">scaleZ=1</span>_][,_<span style="color:red;">scaleM=1</span>_])

[ ] indica componenti opzionali

Argomenti

- _<span style="color:red;">geometry</span>_ una geometria
- _<span style="color:red;">deltaX</span>_ x-axis traslazione
- _<span style="color:red;">deltaY</span>_ y-axis traslazione
- _<span style="color:red;">rotationZ</span>_ rotation around z-axis in degrees counter-clockwise
- _<span style="color:red;">scaleX_</span>_ x-axis fattore di scala
- _<span style="color:red;">scaleY</span>_ y-axis fattore di scala
- _<span style="color:red;">deltaZ</span>_ z-axis traslazione
- _<span style="color:red;">deltaM</span>_ m-axis traslazione
- _<span style="color:red;">scaleZ</span>_ z-axis fattore di scala
- _<span style="color:red;">scaleM</span>_ m-axis fattore di scala

Esempi

```
geom_to_wkt(affine_transform(geom_from_wkt('LINESTRING(1 1, 2 2)'), 2, 2, 0, 1, 1)) → 'LineString (3 3, 4 4)'
geom_to_wkt(affine_transform(geom_from_wkt('POLYGON((0 0, 0 3, 2 2, 0 0))'), 0, 0, -90, 1, 2)) → 'Polygon ((0 0, 6 0, 4 -2, 0 0))'
geom_to_wkt(affine_transform(geom_from_wkt('POINT(3 1)'), 0, 0, 0, 1, 1, 5, 0)) → 'PointZ (3 1 5)'
```

[![](../../img/geometria/affine_transform/affine_transform1.png)](../../img/geometria/affine_transform/affine_transform1.png)

Osservazione

La funzione trasforma le geometrie a partire dall'origine delle coordinate del sistema di riferimento del layer, sotto un esempio:

```
 affine_transform( 
 		geometry:= $geometry,
 		deltaX:=0,
 		deltaY:=0,
 		rotationZ:=45,
 		scaleX:=1,
 		scaleY:=1)
```

[![](../../img/geometria/affine_transform/affine_transform2.png)](../../img/geometria/affine_transform/affine_transform2.png)

---

## $area

Restituisce l'area della geometria corrente. L'area calcolata da questa funzione rispetta sia le impostazioni dell'ellissoide del progetto corrente sia delle unità di misura. Per esempio, se è stato impostato un ellissoide per il progetto allora l'area calcolata sarà ellisoidica altrimenti se non è stato impostato alcun ellissoide l'area calcolata sarà planimetrica.

Sintassi:

- $area

Esempi:

```
$area → 131196498,619546
```

[![](../../img/geometria/area/area1.png)](../../img/geometria/area/area1.png)

Nota bene:

Se il _<span style="color:red;">SR del progetto</span>_ in cui si sta calcolando l'area (**$area**) fosse un sistema proiettato (es:EPSG 3003/4; 32632/33/34 ecc..) allora l'unità di misura sarebbe il metro, invece se il _<span style="color:red;">SR del progetto</span>_ fosse EPSG 4326, cioè un sistema geografico, allora l'unità di misura dell'area sarebbe _**gradi**_ e quindi poco comprensibile e valori piccoli (0.00001).

Osservazione:

1. in generale $area <> area($geometry)
2. da >= **QGIS 3.20** le misure legate all'uso degli ellissoidi, per esempio `$area` e `$length`, utilizzano lo stesso metodo di PostGIS ([le routine GeographicLib](https://github.com/qgis/QGIS/pull/41726)) quindi le misure risulteranno più 'precise' rispetto alle versioni precedenti di QGIS. (vedi: [discussione](https://lists.osgeo.org/pipermail/qgis-user/2021-January/047638.html), [feature request](https://github.com/qgis/QGIS/issues/40888), [pull request](https://github.com/qgis/QGIS/pull/41726)).

---

## $geometry

Restituisce la geometria dell'elemento attuale. Può essere usato per il processamento con altre funzioni. **ATTENZIONE**: Questa funzione è deprecata (a partire da _**QGIS 3.28.0 Firenze**_). Si consiglia di utilizzare la variabile sostitutiva _<span style="color:red;">@geometry</span>_

NB: `$geometry` richiama l'attributo geometria!!!

Sintassi:

- _<span style="color:red;">$geometry</span>_

Esempi:

```
geomToWKT( $geometry ) → POINT(6 50)
area($geoamtry) → 1234567.89
perimeter($geometry) → 25689.25
area(@geoamtry) → 1234567.89
```

[![](../../img/geometria/_geometry/_geometry1.png)](../../img/geometria/_geometry/_geometry1.png)

[![](../../img/geometria/_geometry/_geometry2.png)](../../img/geometria/_geometry/_geometry2.png)

Osservazioni:

il `$` indica che è relativo all'elemento corrente e non ha bisogno di argomenti.

---

## $length

Restituisce la lunghezza di una linestring. Se hai bisogno della lunghezza del bordo di un poligono, utilizza invece [$perimeter](#perimeter). La lunghezza calcolata da questa funzione rispetta le impostazioni sia dell'ellissoide sia delle unità di misura del progetto corrente. Per esempio, se è stato impostato un ellissoide per il progetto allora la lunghezza calcolata sarà ellisoidica altrimenti se non è stato impostato alcun ellissoide la lunghezza calcolata sarà planimetrica.

Sintassi:

- $length

Esempi:

```
$length → 42.4711 
```

[![](../../img/geometria/_length/_length1.png)](../../img/geometria/_length/_length1.png)

Osservazione:

1. Come evidenziano nella definizione della funzione, [$length](#length) calcola la lunghezza rispettando le impostazioni di progetto:

[![](../../img/geometria/_length/_length2.png)](../../img/geometria/_length/_length2.png)

[![](../../img/geometria/_length/_length3.png)](../../img/geometria/_length/_length3.png)

Occorre cambiare entrambe le impostazioni, sia quelle dell'ellissoide → 'None/Planimetric' sia le Unità di misura per le distanze' → Gradi

[![](../../img/geometria/_length/_length4.png)](../../img/geometria/_length/_length4.png)

Queste modofiche non valgono per l'etichettatura, la lunghezza sarà quella relativa alla geometria e quindi al suo SR.

2. da >= **QGIS 3.20** le misure legate all'uso degli ellissoidi, per esempio `$area` e `$length`, utilizzano lo stesso metodo di PostGIS ([le routine GeographicLib](https://github.com/qgis/QGIS/pull/41726)) quindi le misure risulteranno più 'precise' rispetto alle versioni precedenti di QGIS. (vedi: [discussione](https://lists.osgeo.org/pipermail/qgis-user/2021-January/047638.html), [feature request](https://github.com/qgis/QGIS/issues/40888), [pull request](https://github.com/qgis/QGIS/pull/41726)).

Nota:

il `$` indica che è relativo all'elemento corrente e non ha bisogno di argomenti.

---

## $perimeter

Restituisce la lunghezza del perimetro della geometria corrente. Il perimetro calcolato da questa funzione rispetta le impostazioni sia dell'ellissoide sia delle unità di misura del progetto corrente. Per esempio, se è stato impostato un ellissoide per il progetto allora il perimetro calcolato sarà ellisoidico altrimenti se non è stato impostato alcun ellissoide il perimetro calcolato sarà planimetrico.

Sintassi:

- $perimeter

Esempi:

```
$perimeter → 2545897.26
```

[![](../../img/geometria/_perimeter/_perimeter1.png)](../../img/geometria/_perimeter/_perimeter1.png)

Osservazione:

1. Si utilizza SOLO per i poligoni, nel caso di feature lineari [$length ](#length)
2. da >= **QGIS 3.20** le misure legate all'uso degli ellissoidi, per esempio `$area` e `$length`, utilizzano lo stesso metodo di PostGIS ([le routine GeographicLib](https://github.com/qgis/QGIS/pull/41726)) quindi le misure risulteranno più 'precise' rispetto alle versioni precedenti di QGIS. (vedi: [discussione](https://lists.osgeo.org/pipermail/qgis-user/2021-January/047638.html), [feature request](https://github.com/qgis/QGIS/issues/40888), [pull request](https://github.com/qgis/QGIS/pull/41726)).

Nota:

il `$` indica che è relativo all'elemento corrente e non ha bisogno di argomenti.

---

## $x

Restituisce la coordinata x della geometria corrente.

Sintassi:

- $x

Esempi:

```
$x → 12.2568971
```

[![](../../img/geometria/_x/_x1.png)](../../img/geometria/_x/_x1.png)

Osservazione:

- La funzione [$x](#x) restituisce la coordinata `x` della geometria corrente purchè sia un POINT altrimenti restituisce NULL (vedi screenshot)
- Per ottenere le coordinate `x` o `y` occorre utilizzare una combinazione di funzioni ed: `x($geometry)` che vale per qualunque tipologia di geometria (point, linestring, polygon)

---

## $x_at

Recupera una coordinata x per la geometria dell'elemento corrente. **ATTENZIONE: Questa funzione è deprecata (>= QGIS 3.30). Si raccomanda di utilizzare la funzione sostitutiva x_at con la variabile @geometry**.

Sintassi:

- $x_at(_<span style="color:red;">i</span>_)

Argomenti:

* _<span style="color:red;">i</span>_ indice del punto di una linea (indici partono da 0; valori negativi si applicano dall'ultimo indice, partendo da -1)

Esempi:

```
$x_at(1) → 12.6882843
```

[![](../../img/geometria/_x_at/_x_at1.png)](../../img/geometria/_x_at/_x_at1.png)

Osservazioni:

Le lineastring hanno un verso e quindi l'indice 0 indica il primo vertice mentre indici negativi significano che la conta inizia dalla l'ultimo vertice: -10 significa il 10-mo vertice partendo dall'ultimo vertice.

---

## x_at

(>= QGIS 3.30)

Recupera una coordinata x della geometria.

Sintassi:

- x_at(_<span style="color:red;">geometry</span>_,_<span style="color:red;">vertex</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria
* _<span style="color:red;">vertex</span>_ indice del vertice della geometria (gli indici partono da 0; i valori negativi si applicano a partire dall'ultimo indice, a partire da -1)

Esempi:

```
x_at( geom_from_wkt( 'POINT(4 5)' ), 0 ) → 4
```

[![](../../img/geometria/_x_at/x_at330.png)](../../img/geometria/_x_at/x_at330.png)

---

## $y

Restituisce la coordinata y della geometria corrente.

Sintassi:

- $y

Esempi:

```
$y → 12.2568971
```

[![](../../img/geometria/_y/_y1.png)](../../img/geometria/_y/_y1.png)

Osservazione:

- La funzione [$y](#y_1) restituisce la coordinata `y` della geometria corrente purchè sia un POINT altrimenti restituisce NULL (vedi screenshot)
- Per ottenere le coordinate x o y occorre utilizzare una combinazione di funzioni es: y($geometry) che vale per qualunque tipologia di geometria (point, linestring, polygon)

---

## $y_at

Recupera una coordinata y per la geometria dell'elemento corrente. **ATTENZIONE: Questa funzione è deprecata (>= QGIS 3.30). Si raccomanda di utilizzare la funzione sostitutiva x_at con la variabile @geometry**.

Sintassi:

- $y_at(_<span style="color:red;">i_</span>)

Argomenti:

* _<span style="color:red;">i</span>_ indice del punto di una linea (indici partono da 0; valori negativi si applicano dall'ultimo indice, partendo da -1)

Esempi:

```
$y_at(1) → 2
```

[![](../../img/geometria/_y_at/_y_at1.png)](../../img/geometria/_y_at/_y_at1.png)

Osservazioni:

Le lineastring hanno un verso e quindi l'indice 0 indica il primo vertice mentre indici negativi significano che la conta inizia dalla l'ultimo vertice: -10 significa il 10-mo vertice partendo dall'ultimo vertice.

---

## y_at

(>= QGIS 3.30)

Recupera una coordinata y della geometria.

Sintassi:

- Y_at(_<span style="color:red;">geometry</span>_,_<span style="color:red;">vertex</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria
* _<span style="color:red;">vertex</span>_ indice del vertice della geometria (gli indici partono da 0; i valori negativi si applicano a partire dall'ultimo indice, a partire da -1)

Esempi:

```
y_at( geom_from_wkt( 'POINT(4 5)' ), 0 ) → 5
```

[![](../../img/geometria/_y_at/y_at330.png)](../../img/geometria/_y_at/y_at330.png)

---
## angle_at_vertex

Restituisce l'angolo della bisettrice (angolo medio) della geometria per un vertice specifico di una geometria di tipo linestring. Gli angoli sono in gradi in senso orario dal nord.

Sintassi:

- angle_at_vertex(_<span style="color:red;">geometry</span>, <span style="color:red;">vertex</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">vertex</span>_ indice vertice, partendo da 0

Esempi:

```
angle_at_vertex(geometry:=geom_from_wkt('LineString(0 0, 10 0, 10 10)'),vertex:=1) → 45.0
```

[![](../../img/geometria/angle_at_vertex/angle_at_vertex1.png)](../../img/geometria/angle_at_vertex/angle_at_vertex1.png)

Osservazione:

Il primo ed ultimo vertice di una lineastring aperta la funzione restituisce il valore dell'angolo e non la bisettrice.

[![](../../img/geometria/angle_at_vertex/angle_at_vertex2.png)](../../img/geometria/angle_at_vertex/angle_at_vertex2.png)

---

## apply_dash_pattern

Applica un modello di trattino ad una geometria, restituendo una geometria MultiLineString che è la geometria di input rappresentata lungo ogni linea/anello con il modello specificato.

Sintassi:

- apply_dash_pattern( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">pattern</span>_, _[,<span style="color:red;">start_rule=no_rule</span>]_, _[,<span style="color:red;">end_rule=no_rule</span>]_, _[,<span style="color:red;">adjustment=both</span>]_, _[,<span style="color:red;">pattern_offset=0</span>]_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria (accetta (multi)linee o (multi)poligoni).
*  _<span style="color:red;">pattern</span>_ modello di trattino, come un array di numeri che rappresentano la lunghezza dei trattini e degli spazi. Deve contenere un numero pari di elementi.
*  _<span style="color:red;">start_rule</span>_ regola opzionale per vincolare l'inizio del modello. I valori validi sono 'no_rule', 'full_dash', 'half_dash', 'full_gap', 'half_gap'.
*  _<span style="color:red;">end_rule</span>_ regola facoltativa per vincolare la fine del pattern. I valori validi sono 'no_rule', 'full_dash', 'half_dash', 'full_gap', 'half_gap'.
*  _<span style="color:red;">adjustment</span>_ regola opzionale atta a specificare quale parte dei modelli sono adattate alle regole del modello desiderato. I valori validi sono 'both', 'dash', 'gap'. 
*  _<span style="color:red;">pattern_offset</span>_ Distanza opzionale che indica una distanza specifica lungo il modello da cui iniziare.

Esempi:

```
geom_to_wkt(apply_dash_pattern(geom_from_wkt('LINESTRING(1 1, 10 1)'), array(3, 1))) → MultiLineString ((1 1, 4 1),(5 1, 8 1),(9 1, 10 1, 10 1))
geom_to_wkt(apply_dash_pattern(geom_from_wkt('LINESTRING(1 1, 10 1)'), array(3, 1), start_rule:='half_dash')) → MultiLineString ((1 1, 2.5 1),(3.5 1, 6.5 1),(7.5 1, 10 1, 10 1))
```

[![](../../img/geometria/apply_dash_pattern/apply_dash_pattern_01.png)](../../img/geometria/apply_dash_pattern/apply_dash_pattern_01.png)

---

## area

Restituisce l'area di un oggetto a geometria poligonale. I calcoli sono sempre planimetrici nel Sistema di Riferimento Spaziale (SR) di detta geometria, e l'unità di misura dell'area restituita è conforme all'unità di misura del SR. Ciò differisce dal calcolo eseguito dalla funzione $area, la quale esegue calcoli ellisoidici basati sull'ellissoide del progetto e sulle impostazioni delle unità di misura dell'area.

Sintassi:

- area(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria poligono

Esempi:

```
area($geometry) → 1234.567
```

[![](../../img/geometria/area/area001.png)](../../img/geometria/area/area001.png)

[![](../../img/geometria/area/area004.png)](../../img/geometria/area/area004.png)

Nota bene:

Se il _<span style="color:red;">SR del layer</span>_ in cui si sta calcolando l'area (_**area()**_) fosse un sistema proiettato (es:EPSG 3003/4; 32632/33/34 ecc..) l'unità di misura sarebbe il metro, invece se il _<span style="color:red;">SR del layer</span>_ fosse EPSG 4326, cioè un sistema geografico, allora l'unità di misura dell'area sarebbe in gradi e quindi poco comprensibile e valori piccoli.

Osservazioni:

in generale area($geometry) <> $area

---

## Azimuth

Restituisce l'azimut dal nord quale angolo in radianti misurato in senso orario dalla verticale del punto_a al punto_b.

Sintassi:

- azimuth(<span style="color:red;">point_a</span>, <span style="color:red;">point_b</span>)

Argomenti:

* <span style="color:red;">point_a</span> geometria punto
* <span style="color:red;">point_b</span> geometria punto

Esempi:

```
degrees( azimuth( make_point(25, 45), make_point(75, 100) ) ) → 42.273689
degrees( azimuth( make_point(75, 100), make_point(25,45) ) ) → 222.273689
```

[![](../../img/geometria/azimuth/azimuth003.png)](../../img/geometria/azimuth/azimuth003.png)

[![](../../img/geometria/azimuth/azimuth001.png)](../../img/geometria/azimuth/azimuth001.png)

[![](../../img/geometria/azimuth/azimuth002.png)](../../img/geometria/azimuth/azimuth002.png)

Osservazione:

Azimuth per definizione restituisce un angolo in radianti, per trasformarlo in gradi usare la funzione [degrees()](../matematica/degrees.md)

[![](../../img/geometria/azimuth/azimuth004.png)](../../img/geometria/azimuth/azimuth004.png)

---

## Bearing

Introdotta in >= QGIS 3.34

Restituisce la direzione basata sul nord come l'angolo in radianti misurato in senso orario sull'ellissoide dalla verticale dal punto_a al punto_b. ([funzione per calcolare l'azimut geodetico sull'ellissoide](https://github.com/qgis/QGIS/issues/45474).)

Sintassi:

- bearing(<span style="color:red;">point_a</span>, <span style="color:red;">point_b</span>[,<span style="color:red;">source_crs</span>][,<span style="color:red;">ellipsoid</span>])

[ ] indica componenti opzionali

Argomenti:

* <span style="color:red;">point_a</span> geometria punto
* <span style="color:red;">point_b</span> geometria punto
* <span style="color:red;">source_crs</span> una stringa opzionale che rappresenta il SR di origine dei punti. Per impostazione predefinita viene utilizzato il SR del layer corrente.
* <span style="color:red;">ellipsoid</span> una stringa opzionale che rappresenta l'acronimo o l'authority:ID (es. 'EPSG:7030') dell'ellissoide su cui misurare il rilevamento. Per impostazione predefinita viene utilizzata l'impostazione dell'ellissoide del progetto corrente.

Esempi:

```
- degrees( bearing( make_point(16198544, -4534850), make_point(18736872, -1877769), 'EPSG:3857', 'EPSG:7030') ) → 49.980071
- degrees( bearing( make_point(18736872, -1877769), make_point(16198544, -4534850), 'EPSG:3857', 'WGS84') ) → 219.282386
```

---

## boundary

Restituisce l'area minima della combinazione dei confini della geometria (cioè il confine topologico della geometria). Per esempio, una geometria poligonale avrà un confine costituito dalle linee di ogni anello nel poligono. Alcuni tipi di geometrie non hanno confini, es collezioni di punti o geometrie e pertanto verrà restituito `NULL`.

Sintassi:

- boundary(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geom_to_wkt(boundary(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))'))) → 'LineString(1 1,0 0,-1 1,1 1)'
geom_to_wkt(boundary(geom_from_wkt('LineString(1 1,0 0,-1 1)'))) → 'MultiPoint ((1 1),(-1 1))'
```

[![](../../img/geometria/boundary/boundari0.png)](../../img/geometria/boundary/boundari0.png)

[![](../../img/geometria/boundary/boundari1.png)](../../img/geometria/boundary/boundari1.png)

Osservazioni:

funzione molto utile per la tematizzazione aggiungendo un nuovo layer con geometry generator

[![](../../img/geometria/boundary/boundari2.png)](../../img/geometria/boundary/boundari2.png)

---

## bounds

Restituisce la geometria che rappresenta il perimetro di delimitazione di una geometria in ingresso. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- bounds(*<span style="color:red;">geometry</span>*)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
bounds($geometry) → perimetro di delimitazione dell'elemento geometrico corrente
geom_to_wkt(bounds(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))'))) → 'Polygon ((-1 0, 1 0, 1 1, -1 1, -1 0))'
```

[![](../../img/geometria/bounds/bounds0.png)](../../img/geometria/bounds/bounds0.png)

[![](../../img/geometria/bounds/bounds1.png)](../../img/geometria/bounds/bounds1.png)

Osservazioni:

funzione molto utile per la tematizzazione aggiungendo un nuovo layer con geometry generator

[![](../../img/geometria/bounds/bounds2.png)](../../img/geometria/bounds/bounds2.png)

---

## bounds_height

Restituisce l'altezza del perimetro di delimitazione di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- bounds_height(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
bounds_height($geometry) → altezza del perimetro di delimitazione dell'elemento geometrico corrente
bounds_height(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))')) → 1
```

[![](../../img/geometria/bounds/bounds_height0.png)](../../img/geometria/bounds/bounds_height0.png)

[![](../../img/geometria/bounds/bounds_height1.png)](../../img/geometria/bounds/bounds_height1.png)

Osservazioni:

La funzione restituisce un numero che corrisponde all'altezza del rettangolo di ingombro di una geometria.

---

## bounds_width

Restituisce la larghezza del perimetro di delimitazione di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- bounds_width(*<span style="color:red;">geometry</span>*)

Argomenti:

* <span style="color:red;">geometry</span> una geometria

Esempi:

```
bounds_width($geometry) → larghezza del perimetro di delimitazione di $geometry
```

[![](../../img/geometria/bounds/bounds_width0.png)](../../img/geometria/bounds/bounds_width0.png)

[![](../../img/geometria/bounds/bounds_width1.png)](../../img/geometria/bounds/bounds_width1.png)

Osservazioni:

La funzione restituisce un numero che corrisponde alla larghezza del rettangolo di ingombro di una geometria.

---

## buffer

Restituisce una geometria che rappresenta tutti i punti la cui distanza dalla geometria è minore o uguale alla distanza inserita. I calcoli vengono effettuati nel sistema di riferimento spaziale della geometria.

Sintassi:

- buffer(*<span style="color:red;">geometry</span>*,*<span style="color:red;">distance</span>*[,_<span style="color:red;">segments=8</span>_])

Argomenti:

* *<span style="color:red;">geometry</span>* una geometria
* *<span style="color:red;">distance</span>* distanza buffer nelle unità del layer
* *<span style="color:red;">segments</span>* numero di segmenti da usare per rappresentare un quarto di cerchio quando è utilizzato uno stile di unione arrotondato. Un numero grande risulta in un buffer più morbido, con più nodi.

Esempi:

```
buffer($geometry, 10.5) → poligono di $geometry bufferizzato di 10.5 unità
```

[![](../../img/geometria/buffer/buffer0.png)](../../img/geometria/buffer/buffer0.png)

[![](../../img/geometria/buffer/buffer1.png)](../../img/geometria/buffer/buffer1.png)

!!! Danger
	Utilizzando SR proiettati l'unità di misura è il metro, mentre, per SR geografici è il grado, quindi attenzione al valore della distanza.

Nota bene:

La Funzione restituisce SEMPRE un poligono sia per geometry **POINT**, **LINESTRING** o **POLYGON

[![](../../img/geometria/buffer/buffer2.png)](../../img/geometria/buffer/buffer2.png)

---

## buffer_by_m

Crea un _buffer_ lungo una geometria _linestring_ in cui il diametro del buffer varia in base ai valori _m_ nei vertici della linea.

Sintassi:

- buffer_by_m(_<span style="color:red;">geometry</span>, <span style="color:red;">segments</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ la geometria deve essere una (multi) geometria linestring con valori m.
* _<span style="color:red;">segments</span>_ numero di segmenti per approssimare le curve del quarto di cerchio nel buffer


Esempi:

```
buffer_by_m(geometry:=geom_from_wkt('LINESTRINGM(1 2 0.5, 4 2 0.2)'),segments:=8) → Un buffer di larghezza variabile che inizia con un diametro di 0,5 e termina con un diametro di 0,2 lungo la linea.
```

[![](../../img/geometria/buffer_by_m/buffer_by_m1.png)](../../img/geometria/buffer_by_m/buffer_by_m1.png)

relativa all'esempio di sopra:

[![](../../img/geometria/buffer_by_m/buffer_by_m2.png)](../../img/geometria/buffer_by_m/buffer_by_m2.png)

[![](../../img/geometria/buffer_by_m/buffer_by_m3.png)](../../img/geometria/buffer_by_m/buffer_by_m3.png)

Osservazioni:

[QGIS - feature](https://github.com/qgis/QGIS/pull/6882)

---

## centroid

Restituisce il centro geometrico di una geometria.

Sintassi:

- centroid(*<span style="color:red;">geometry</span>*)

Argomenti:

* *<span style="color:red;">geometry</span>* una geometria

Esempi:

```
centroid($geometry) → una geometria punto
```

[![](../../img/geometria/centroid/centroid0.png)](../../img/geometria/centroid/centroid0.png)

[![](../../img/geometria/centroid/centroid1.png)](../../img/geometria/centroid/centroid1.png)

Osservazioni:

La Funzione restituisce SEMPRE una geometry **POINT

[![](../../img/geometria/centroid/centroid2.png)](../../img/geometria/centroid/centroid2.png)

---

## close_line

Restituisce una linestring chiusa della linestring di input aggiungendo il primo punto alla fine della linea, se non è già chiusa. Se la geometria non è una linestring o una MultiLinestring, il risultato sarà NULL.

Sintassi:

* close_line(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria linestring

Esempi:

```
geom_to_wkt(close_line(geom_from_wkt('LINESTRING(0 0, 1 0, 1 1)'))) → LineString (0 0, 1 0, 1 1, 0 0)
geom_to_wkt(close_line(geom_from_wkt('LINESTRING(0 0, 1 0, 1 1, 0 0)'))) → LineString (0 0, 1 0, 1 1, 0 0)
```

[![](../../img/geometria/close_line/close_line1.png)](../../img/geometria/close_line/close_line1.png)

---

## closest_point

Restituisce il punto sulla geometria1 che è più vicino alla geometria2.

Sintassi:

- closest_point(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

Argomenti:

* _<span style="color:red;">geometry1</span>_ geometria _sulla_ quale cercare il punto più vicino
* _<span style="color:red;">geometry</span>_ geometria _dalla_ quale cercare il punto più vicino

Esempi:

```
geom_to_wkt(closest_point(geom_from_wkt('LINESTRING (20 80, 98 190, 110 180, 50 75 )'),geom_from_wkt('POINT(100 100)'))) → Point(73.0769 115.384)
```

[![](../../img/geometria/closest_point/closest_point1.png)](../../img/geometria/closest_point/closest_point1.png)

[![](../../img/geometria/closest_point/closest_point2.png)](../../img/geometria/closest_point/closest_point2.png)

Osservazioni:

Utilizzando il _geometry generator_ per i temi (il layer strade è una unica feature):

* `closest_point( geometry(get_feature('strade', 'reg',19)),$geometry)`

[![](../../img/geometria/closest_point/closest_point3.png)](../../img/geometria/closest_point/closest_point3.png)

Gif animata: _geometry 1_ è la rete stradale; _geometry 2_ sono i punti; in rosso i closestpoint

[![](../../img/geometria/closest_point/closestpoint.png)](../../img/geometria/closest_point/closestpoint.png)

---

## collect_geometries

Raccoglie un set di geometrie in un oggetto geometria multiparte.

### Variante geometry

Sintassi:

- collect_geometries(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>_...)

Argomenti:

* _<span style="color:red;">geometry</span>_ geometria sulla quale cercare il punto più vicino

Esempi:

```
geom_to_wkt(collect_geometries(make_point(1,2), make_point(3,4), make_point(5,6))) → 'MultiPoint ((1 2),(3 4),(5 6))'
```

[![](../../img/geometria/collect_geometries/collect_geometries2.png)](../../img/geometria/collect_geometries/collect_geometries2.png)

### Variante con array

Sintassi:

- collect_geometries(_<span style="color:red;">array</span>_)

Argomenti:

* _<span style="color:red;">array</span>_ array con oggetti geometrici


Esempi:

```
geom_to_wkt(collect_geometries(array(make_point(1,2), make_point(3,4), make_point(5,6)))) → 'MultiPoint ((1 2),(3 4),(5 6))'
```

[![](../../img/geometria/collect_geometries/collect_geometries1.png)](../../img/geometria/collect_geometries/collect_geometries1.png)

Osservazioni:

[![screen](https://user-images.githubusercontent.com/1829991/63907352-6ca4ff80-ca5e-11e9-9b18-82a1618e1eba.png)](https://user-images.githubusercontent.com/1829991/63907352-6ca4ff80-ca5e-11e9-9b18-82a1618e1eba.png)

---

## combine

Restituisce la combinazione di due geometrie.

Sintassi:

- combine(_<span style="color:red;">geometry1</span>, <span style="color:red;">geometry2</span>_)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
geom_to_wkt( combine( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 2 1)' ) ) ) → MULTILINESTRING((4 4, 2 1), (3 3, 4 4), (4 4, 5 5))
geom_to_wkt( combine( geom_from_wkt( 'LINESTRING(3 3, 4 4)' ), geom_from_wkt( 'LINESTRING(3 3, 6 6, 2 1)' ) ) ) → LINESTRING(3 3, 4 4, 6 6, 2 1)
```

[![](../../img/geometria/combine/combine1.png)](../../img/geometria/combine/combine1.png)

---

## concave_hull

\>= QGIS 3.18 Firenze e Geos 3.11+

Restituisce un poligono possibilmente concavo che contiene tutti i punti della geometria

Sintassi:

- concave_hull(_<span style="color:red;">geometry</span>, <span style="color:red;">target_percent</span>[,<span style="color:red;">allow_holes</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">target_percent</span>_ la percentuale di area del poligono convesso a cui la soluzione cerca di avvicinarsi. Una percentuale-obbiettivo di 1 dà lo stesso risultato del poligono convesso. Una percentuale_obbiettivo compresa tra 0 e 0.99 produce un risultato che dovrebbe avere un'area inferiore a quella del poligono convesso.
* _<span style="color:red;">allow_holes</span>_ argomento opzionale che specifica se consentire i buchi nella geometria di output. L'impostazione predefinita è FALSE; impostare TRUE per evitare di includere i buchi nella geometria di output.

Esempi:

```
geom_to_wkt(concave_hull(geom_from_wkt('MULTILINESTRING((106 164,30 112,74 70,82 112,130 94,130 62,122 40,156 32,162 76,172 88),(132 178,134 148,128 136,96 128,132 108,150 130,170 142,174 110,156 96,158 90,158 88),(22 64,66 28,94 38,94 68,114 76,112 30,132 10,168 18,178 34,186 52,184 74,190 100,190 122,182 148,178 170,176 184,156 164,146 178,132 186,92 182,56 158,36 150,62 150,76 128,88 118))'), 0.99)) → 'Polygon ((30 112, 36 150, 92 182, 132 186, 176 184, 190 122, 190 100, 186 52, 178 34, 168 18, 132 10, 112 30, 66 28, 22 64, 30 112))'
```

[![](../../img/geometria/concave_hull/concave_hull.png)](../../img/geometria/concave_hull/concave_hull.png)
---

## contains

Verifica se una geometria ne contiene un'altra. Restituisce vero se e solo se nessun punto di geometry2 giace all'esterno di geometry1 e almeno un punto dell'interno di geometry2 si trova all'interno di geometry1.

Sintassi:

- contains(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

Argomenti:

* _<span style="color:red;">geometry1</span>_  una geometria
* _<span style="color:red;">geometry2</span>_  una geometria

Esempi:

```
contains( geom_from_wkt( 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))' ), geom_from_wkt( 'POINT(0.5 0.5 )' ) ) → vero
contains( geom_from_wkt( 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → falso
```

[![](../../img/geometria/contains/contains1.png)](../../img/geometria/contains/contains1.png)

Osservazioni:

Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (Ctrl+F3):

```
contains(geometry(get_feature( 'province_rt_rt','pk_uid','46')),$geometry)
```

dove:

* _geometry1_ è `geometry(get_feature( 'province_rt_rt','pk_uid','46'))`
* _geometry2_ è `$geometry`

[![](../../img/geometria/contains/contains2.png)](../../img/geometria/contains/contains2.png)

seleziono tutti i comuni `contains` (contenuti) nella provincia con `pk_uid`46 (Lucca)

PS:** potrei anche negare (`NOT`) l'espressione per selezionare il complementare (tutti i comuni tranne quelli contenuti nella provincia di Lucca).

`NOT contains(geometry(get_feature( 'province_rt_rt','pk_uid','46')),$geometry)`

---

## convex_hull

Restituisce il poligono convesso di una geometria. Rappresenta la minima geometria convessa che racchiude tutte le geometria contenute nell'insieme.

Sintassi:

- convex_hull(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geom_to_wkt( convex_hull( geom_from_wkt( 'LINESTRING(3 3, 4 4, 4 10)' ) ) ) → POLYGON((3 3,4 10,4 4,3 3))
```

[![](../../img/geometria/convex_hull/convex_hull1.png)](../../img/geometria/convex_hull/convex_hull1.png)

Osservazioni:

La funzione restituisce sempre un poligono.

[![](../../img/geometria/convex_hull/convex_hull2.png)](../../img/geometria/convex_hull/convex_hull2.png)

---

## crosses

Verifica se una geometria interseca un'altra. Restituisce vero (1) se le geometrie interessate hanno qualche, ma non tutti, punto interno in comune.

Sintassi:

- crosses(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
crosses( geom_from_wkt( 'LINESTRING(3 5, 4 4, 5 3)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → vero
crosses( geom_from_wkt( 'POINT(4 5)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → falso
```

[![](../../img/geometria/crosses/crosses1.png)](../../img/geometria/crosses/crosses1.png)

Osservazioni:

Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (Ctrl+F3):

```
crosses(geometry(get_feature( 'fiume_arno','nome','ARNO')), $geometry)
```
dove:

* _geometry1_ è `geometry(get_feature( 'fiume_arno','nome','ARNO'))`
* _geometry2_ è `$geometry`

[![](../../img/geometria/crosses/crosses2.png)](../../img/geometria/crosses/crosses2.png)

seleziono tutti i comuni `crosses` (attraversati) dal fiume ARNO

PS:** potrei anche negare (`NOT`) l'espressione per selezionare il complementare (tutti i comuni tranne quelli attraversati dal fiume ARNO).

`NOT crosses(geometry(get_feature( 'fiume_arno','nome','ARNO')), $geometry)`

---

## densify_by_count

Prende una geometria di un livello poligonale o lineare e ne genera una nuova in cui le geometrie hanno un numero di vertici maggiore di quella originale.

Sintassi:

- densify_by_count(_<span style="color:red;">geometry</span>_, _<span style="color:red;">vertices</span>)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria (accetta (multi)linee o (multi)poligoni).
* _<span style="color:red;">vertices</span>_ numero di vertici da aggiungere (per segmento)

Esempi:

```
geom_to_wkt(densify_by_count(geom_from_wkt('LINESTRING(1 1, 10 1)'), 3)) → LineString (1 1, 3.25 1, 5.5 1, 7.75 1, 10 1)
```

[![](../../img/geometria/densify_by_count/densify_by_count_01.png)](../../img/geometria/densify_by_count/densify_by_count_01.png)

---

## densify_by_distance

Prende una geometria di un livello poligono o lineare e ne genera una nuova in cui le geometrie sono densificate aggiungendo ulteriori vertici sui bordi che hanno una distanza massima dell'intervallo di distanza specificato.

Sintassi:

- densify_by_distance(_<span style="color:red;">geometry</span>_, _<span style="color:red;">distance</span>)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria (accetta (multi)linee o (multi)poligoni).
* _<span style="color:red;">distance</span>_ distanza massima dell'intervallo tra i vertici nella geometria in uscita

Esempi:

```
geom_to_wkt(densify_by_distance(geom_from_wkt('LINESTRING(1 1, 10 1)'), 4)) → LineString (1 1, 4 1, 7 1, 10 1)
```

[![](../../img/geometria/densify_by_distance/densify_by_distance_01.png)](../../img/geometria/densify_by_distance/densify_by_distance_01.png)

---

## difference

Restituisce una geometria che rappresenta la porzione della _geometry_a_ che non interseca la _geometry_b_.

Sintassi:

- difference(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
geom_to_wkt( difference( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4)' ) ) ) → LINESTRING(4 4, 5 5)
```

[![](../../img/geometria/difference/difference1.png)](../../img/geometria/difference/difference1.png)

[![](../../img/geometria/difference/difference31.png)](../../img/geometria/difference/difference31.png)

Espressione:

!!! Tip "Espressione"
```
	-- differenza linea a - linea b
	difference( 
	make_line(  -- linea a
		start_point(geometry(get_feature_by_id('linea_a',0))), 
		start_point($geometry),
		end_point(geometry(get_feature_by_id('linea_a',0)))),
	make_line(  -- linea b
		start_point($geometry), 
		end_point(geometry(get_feature_by_id('linea_a',0))),
		end_point($geometry))
					)
	-- NB: -- è importante ordine delle geometrie
	-- a - b è diverso da b - a
```

[![](../../img/geometria/difference/difference32.png)](../../img/geometria/difference/difference32.png)

!!! Tip "Espressione"
```
	-- differenza linea b - linea a
	difference( 
	make_line( -- linea b
		start_point($geometry), 
		end_point(geometry(get_feature_by_id('linea_a',0))),
		end_point($geometry)),
	make_line(  -- linea a
		start_point(geometry(get_feature_by_id('linea_a',0))), 
		start_point($geometry),
		end_point(geometry(get_feature_by_id('linea_a',0))))
					)
	-- NB: -- è importante ordine delle geometrie
	-- a - b è diverso da b - a
```

!!! Question "Prova tu"
	[Dati e progetto qgz](https://github.com/gbvitrano/HfcQGIS/raw/master/prova_tu/DIFFERENCE.zip)

Esempio di sopra:

[![](../../img/geometria/difference/difference2.png)](../../img/geometria/difference/difference2.png)

---

## disjoint

Controlla qualora una geometria non ne interseca spazialmente un'altra. Restituisce true (1) se le geometrie non condividono nessuno spazio comune.

Sintassi:

- disjoint(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
*_<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
disjoint( geom_from_wkt( 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0 ))' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → vero
disjoint( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'POINT(4 4)' )) → falso
```

[![](../../img/geometria/disjoint/disjoint.png)](../../img/geometria/disjoint/disjoint.png)

Osservazione:

Vero = 1; Falso= 0

Osservazioni:

Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (Ctrl+F3):

```
disjoint(geometry(get_feature( 'fiume_arno','nome','ARNO')), $geometry)
```

dove:

* _geometry1_ è `geometry(get_feature( 'fiume_arno','nome','ARNO'))`
* _geometry2_ è `$geometry`


[![](../../img/geometria/disjoint/disjoint2.png)](../../img/geometria/disjoint/disjoint2.png)

seleziono tutti i comuni `disjoint` (disgiunti) dal fiume ARNO

---

## distance

Restituisce la distanza minima (basata su riferimento spaziale) tra due geometrie in unità proiettate.

Sintassi:

- distance(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria


Esempi:

```
distance( geom_from_wkt( 'POINT(4 4)' ), geom_from_wkt( 'POINT(4 8)' ) ) → 4
```

[![](../../img/geometria/distance/distance1.png)](../../img/geometria/distance/distance1.png)

--

[![](../../img/geometria/distance/distance2.png)](../../img/geometria/distance/distance2.png)

---

## distance_to_vertex

Restituisce la distanza lungo una geometria ad un vertice specificato.

Sintassi:

- distance_to_vertex(_<span style="color:red;">geometry</span>_, _<span style="color:red;">vertex</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">vertex</span>_ indice vertice, partendo da 0; se il valore è negativo, l'indice del vertice selezionato sarà il suo conteggio totale meno il valore assoluto


Esempi:

```
distance_to_vertex(geometry:=geom_from_wkt('LineString(0 0, 10 0, 10 10)'),vertex:=1) → 10.0
```

[![](../../img/geometria/distance_to_vertex/distance_to_vertex1.png)](../../img/geometria/distance_to_vertex/distance_to_vertex1.png)

--

esempio di sopra:

[![](../../img/geometria/distance_to_vertex/distance_to_vertex3.png)](../../img/geometria/distance_to_vertex/distance_to_vertex3.png)

---

## end_point

Restituisce l'ultimo nodo di una geometria.

Sintassi:

- end_point(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria

Esempi:

```
geom_to_wkt(end_point(geom_from_wkt('LINESTRING(4 0, 4 2, 0 2)'))) → 'Point (0 2)'
```

[![](../../img/geometria/end_point/end_point1.png)](../../img/geometria/end_point/end_point1.png)

--

End_point di geometria poligonale:

[![](../../img/geometria/end_point/end_point2.png)](../../img/geometria/end_point/end_point2.png)

End_point di geometria lineare:

[![](../../img/geometria/end_point/end_point3.png)](../../img/geometria/end_point/end_point3.png)

---

## exif_geotag

Crea una geometria puntuale dai geotag dell'exif di un file di immagine.

Sintassi

- exif_geotag(_<span style="color:red;">path</span>_)

Descrizione

- _<span style="color:red;">path</span>_ Un percorso di file immagine.

Esempi

```
geom_to_wkt(exif_geotag('/my/photo.jpg')) → 'Point (2 4)'
```

[![](../../img/geometria/exif_geotag/exif_geotag1.png)](../../img/geometria/exif_geotag/exif_geotag1.png)

---

## extend

Estende l'inizio e la fine di una geometria di tipo linestring di una quantità specificata. Le linee sono estese usando la direzione di immersione del primo e dell'ultimo segmento nella linea. Le distanze sono espresse nel SR di tale geometria.

Sintassi:

- extend(_<span style="color:red;">geometry</span>_, _<span style="color:red;">start_distance</span>_, _<span style="color:red;">end_distance</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria (multi)linestring
* _<span style="color:red;">start_distance</span>_ distanza alla quale estendere l'_inizio_ della linea
* _<span style="color:red;">end_distance</span>_ distanza alla quale estendere la _fine_ della linea.


Esempi:

```
geom_to_wkt(extend(geom_from_wkt('LineString(0 0, 1 0, 1 1)'),1,2)) → 'LineString (-1 0, 1 0, 1 3)'
geom_to_wkt(extend(geom_from_wkt('MultiLineString((0 0, 1 0, 1 1), (2 2, 0 2, 0 5))'),1,2)) → 'MultiLineString ((-1 0, 1 0, 1 3),(3 2, 0 2, 0 7))'
```

[![](../../img/geometria/extend/extend1.png)](../../img/geometria/extend/extend1.png)

--

[![](../../img/geometria/extend/extend1.png)](../../img/geometria/extend/extend1.png)

---

## exterior_ring

Restituisce una linestring che rappresenta l'anello esterno di una geometria poligonale. Se la geometria non è un poligono, il risultato sarà NULL.

Sintassi:

- exterior_ring(_<span style="color:red;">geometry</span>_)

Argomenti:


* _<span style="color:red;">geometry</span>_ una geometria poligono

Esempi:

```
geom_to_wkt(exterior_ring(geom_from_wkt('POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1),( 0.1 0.1, 0.1 0.2, 0.2 0.2, 0.2, 0.1, 0.1 0.1))'))) → 'LineString (-1 -1, 4 0, 4 2, 0 2, -1 -1)'
```

[![](../../img/geometria/exterior_ring/exterior_ring1.png)](../../img/geometria/exterior_ring/exterior_ring1.png)

--

[![](../../img/geometria/exterior_ring/exterior_ring2.png)](../../img/geometria/exterior_ring/exterior_ring2.png)

---

## extrude

Restituisce una versione estrusa della geometria (Multi-)Curve o (Multi-)Linestring in ingresso, con un'estensione specificata da x e y.

Sintassi:

- extrude(_<span style="color:red;">geometry</span>_,_<span style="color:red;">x</span>_, _<span style="color:red;">y</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria poligono
* _<span style="color:red;">x</span>_ estensione x, valore numerico
* _<span style="color:red;">y</span>_ estensione y, valore numerico


Esempi:

```
extrude(geom_from_wkt('LineString(1 2, 3 2, 4 3)'), 1, 2) → Polygon ((1 2, 3 2, 4 3, 5 5, 4 4, 2 4, 1 2))
extrude(geom_from_wkt('MultiLineString((1 2, 3 2), (4 3, 8 3)'), 1, 2) → MultiPolygon (((1 2, 3 2, 4 4, 2 4, 1 2)),((4 3, 8 3, 9 5, 5 5, 4 3)))
```

[![](../../img/geometria/extrude/extrude1.png)](../../img/geometria/extrude/extrude1.png)

Osservazioni:

	Nell'esempio ho utilizzato la funzione [boundary()](boundary.md) perché la geometria di ingresso deve essere lineare.

[![](../../img/geometria/extrude/extrude1.png)](../../img/geometria/extrude/extrude1.png)

---

## flip_coordinates

Restituisce una copia della geometria con le coordinate x e y scambiate. Utile per riparare le geometrie che hanno invertito i valori di latitudine e longitudine.

Sintassi:

- flip_coordinates(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geom_to_wkt(flip_coordinates(make_point(1, 2))) → Point (2 1)
```

[![](../../img/geometria/flip_coordinates/flip_coordinates1.png)](../../img/geometria/flip_coordinates/flip_coordinates1.png)

--

Esempio con vettore poligonale (aggiorno la geometry): 

[![](../../img/geometria/flip_coordinates/flip_coordinates2.png)](../../img/geometria/flip_coordinates/flip_coordinates2.png)

il flip è da usare con cautela perché cambia radicalemnte la posizione del vettore

[![](../../img/geometria/flip_coordinates/flip_coordinates3.png)](../../img/geometria/flip_coordinates/flip_coordinates3.png)

---

## force_polygon_ccw

Forza una geometria a rispettare la convenzione per cui gli anelli esterni sono in senso antiorario, quelli interni in senso orario.

Sintassi:

- force_polygon_ccw(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria. Qualunque geometria non poligonale è restituita non modificata

Esempi:

```
geom_to_wkt(force_polygon_ccw(geometry:=geom_from_wkt('Polygon ((-1 -1, 0 2, 4 2, 4 0, -1 -1)))'))) → 'Polygon ((-1 -1, 0 2, 4 2, 4 0, -1 -1))'
```

[![](../../img/geometria/force_polygon_ccw/force_polygon_ccw_01.png)](../../img/geometria/force_polygon_ccw/force_polygon_ccw_01.png)

---

## force_polygon_cw

Forza una geometria a rispettare la convenzione per cui gli anelli esterni sono in senso orario, quelli interni in senso antiorario.

Sintassi:

- force_polygon_cw(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria. Qualunque geometria non poligonale è restituita non modificata

Esempi:

```
geom_to_wkt(force_polygon_cw(geometry:=geom_from_wkt('POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1))'))) → 'Polygon ((-1 -1, 0 2, 4 2, 4 0, -1 -1))'
```

[![](../../img/geometria/force_polygon_cw/force_polygon_cw_01.png)](../../img/geometria/force_polygon_cw/force_polygon_cw_01.png)

---

## force_rhr

Forza una geometria a rispettare la regola della mano destra, in cui l'area delimitata da un poligono si trova a destra del limite. In particolare, l'anello esterno è orientato in senso orario e l'interno in senso antiorario.

Sintassi:

- force_rhr(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria. Qualsiasi geometria non poligonale viene restituita invariata.

Esempi:

```
geom_to_wkt(force_rhr(geometry:=geom_from_wkt('POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1))'))) → Polygon ((-1 -1, 0 2, 4 2, 4 0, -1 -1))
```

[![](../../img/geometria/force_rhr/force_rhr1.png)](../../img/geometria/force_rhr/force_rhr1.png)

Osservazioni:

	Ecco un esempio pratico della funzione (presente anche nelgli strumenti fi processing) ovvero un poligono disegnato in senso antiorario viene forzato in senso orario e l'etichettature è visibile correttamente.

[![](../../img/geometria/force_rhr/force_rhr.gif)](../../img/geometria/force_rhr/force_rhr.gif)

---

## geom_from_gml

Restituisce una geometria da una rappresentazione GML di una geometria.

Sintassi:

- geom_from_gml(_<span style="color:red;"></span>_gml</span>_)

Argomenti:

* _<span style="color:red;">gml</span>_ Rappresentazione GML di una geometria come stringa

Esempi:

```
geom_to_wkt(geom_from_gml('<gml:LineString srsName="EPSG:4326"><gml:coordinates>4,4 5,5 6,6</gml:coordinates></gml:LineString>') )  → 'LineString (4 4, 5 5, 6 6)'
```

[![](../../img/geometria/geom_from_gml/geom_from_gml1.png)](../../img/geometria/geom_from_gml/geom_from_gml1.png)

---

## geom_from_wkb

Restituisce una geometria creata da una rappresentazione binaria ben nota (WKB).

Sintassi:

- geom_from_wkb(_<span style="color:red;">binari</span>_)

Argomenti:

* _<span style="color:red;">binari</span>_ Rappresentazione binaria ben nota (WKB) di una geometria (come BLOB binario)

Esempi:

```
geom_from_wkb( geom_to_wkb( make_point(4,5) ) ) → un oggetto geometria punto
```

[![](../../img/geometria/geom_from_wkb/geom_from_wkb1.png)](../../img/geometria/geom_from_wkb/geom_from_wkb1.png)

---

## geom_from_wkt

Restituisce una geometria creata da una rappresentazione Well-Known Text (WKT).

Sintassi:

- geom_from_wkt(_<span style="color:red;">text</span>_)

Argomenti:

* _<span style="color:red;">text</span>_ Rappresentazione Well-Known Text (WKT) di una geometria


Esempi:

```
geom_from_wkt( 'POINT(4 5)' ) → un oggetto geometria
```

[![](../../img/geometria/geom_from_wkt/geom_from_wkt1.png)](../../img/geometria/geom_from_wkt/geom_from_wkt1.png)

---

## geom_to_wkb

Restituisce la rappresentazione binaria ben nota (WKB) di una geometria come BLOB binario.

Sintassi:

- geom_to_wkb(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geom_to_wkb( $geometry ) → BLOB binario contenente un oggetto geometria
```

[![](../../img/geometria/geom_to_wkb/geom_to_wkb1.png)](../../img/geometria/geom_to_wkb/geom_to_wkb1.png)

---

## geom_to_wkt

Restituisce la rappresentazione Well-Known Text (WKT) della geometria senza metadati del SR

Sintassi:

- geom_to_wkt(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geom_to_wkt( make_point(6, 50) ) → 'POINT(6 50)'
geom_to_wkt(centroid(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))'))) → 'POINT(0 0.66666667)'
geom_to_wkt(centroid(geom_from_wkt('Polygon((1 1, 0 0, -1 1, 1 1))')), 2) → 'POINT(0 0.67)'
```

[![](../../img/geometria/geom_to_wkt/geom_to_wkt1.png)](../../img/geometria/geom_to_wkt/geom_to_wkt1.png)

---

## geometry

Restituisce la geometria di un elemento con geometria

Sintassi:

- geometry(_<span style="color:red;">feature</span>_)

Argomenti:

* _<span style="color:red;">feature</span>_ un oggetto elemento con geometria

Esempi:

```
geom_to_wkt( geometry( get_feature( layer, attributeField, value ) ) ) → 'POINT(6 50)'`
intersects( $geometry, geometry( get_feature( layer, attributeField, value ) ) ) → vero`
```

[![](../../img/geometria/geometry/geometry1.png)](../../img/geometria/geometry/geometry1.png)

--

Usando il **Select by Expression**: selezionare le feature di un layer (quartieri) in funzione di altro layer (test):

[![](../../img/geometria/geometry/geometry2.png)](../../img/geometria/geometry/geometry2.png)

---

## geometry_n

Restituisce una geometria specifica da una collezione di geometrie, o NULL se la geometria in ingresso non è una collezione. Restituisce anche una parte da una geometria a più parti.

Sintassi:

- geometry_n(_<span style="color:red;">geometry</span>_, _<span style="color:red;">index</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ raccolta di geometrie
* _<span style="color:red;">index</span>_ indice della geometria da restituire, dove 1 è la prima geometria nella raccolta

Esempi:

```
geom_to_wkt(geometry_n(geom_from_wkt('GEOMETRYCOLLECTION(POINT(0 1), POINT(0 0), POINT(1 0), POINT(1 1))'),3)) → 'Point (1 0)'
```

[![](../../img/geometria/geometry_n/geometry_n1.png)](../../img/geometria/geometry_n/geometry_n1.png)

---

## geometry_type

Restituisce un valore stringa che descrive il tipo di una geometria (Punto, Linea o Poligono)

Sintassi:

- geometry_type(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geometry_type( geom_from_wkt( 'LINESTRING(2 5, 3 6, 4 8)') ) → 'Line'
geometry_type( geom_from_wkt( 'MULTILINESTRING((2 5, 3 6, 4 8), (1 1, 0 0))') ) → 'Line'
geometry_type( geom_from_wkt( 'POINT(2 5)') ) → 'Point'
geometry_type( geom_from_wkt( 'POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1))') ) → 'Polygon'
```

[![](../../img/geometria/geometry_type/img_01.png)](../../img/geometria/geometry_type/img_01.png)

---

## hausdorff_distance

Restituisce la distanza di _Hausdorff_ tra due geometrie. Questa è in sostanza una misura di come le 2 geometrie sono simili o dissimili: una distanza più bassa indica geometrie più simili. La funzione può essere eseguita con un argomento opzionale di densificazione della frazione. Se non viene specificato, viene utilizzata una approssimazione alla distanza standard di Hausdorff. Questa approssimazione è esatta o abbastanza vicina per un grande sottoinsieme di casi utili. Esempi di questi sono:

  * calcolare la distanza tra Linestrings che sono approssimativamente paralleli tra loro e sono sostanzialmente uguali in lunghezza. Ciò si verifica nelle verifica di reti lineari. 
  * testare la somiglianza di geometrie. 

Se l'approssimazione predefinita fornita da questo metodo è insufficiente, specifica l'argomento opzionale di densificazione della frazione. Specificando questo argomento si esegue una densificazione del segmento prima di calcolare la distanza Hausdorff discreta. Il parametro imposta la frazione con cui densificare ogni segmento. Ogni segmento sarà suddiviso in un numero di subsegmenti di uguale lunghezza, la cui frazione della lunghezza totale è la più vicina alla frazione data. Riducendo il parametro di densificazione della frazione, la distanza restituita si avvicinerà alla vera distanza Hausdorff per le geometrie.

Sintassi:

- hausdorff_distance(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>_, _<span style="color:red;">densify_fraction</span>_)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria
* _<span style="color:red;">densify_fraction</span>_ quantità di densificazione della frazione

Esempi:

```
hausdorff_distance( geometry1:= geom_from_wkt('LINESTRING (0 0, 2 1)'),geometry2:=geom_from_wkt('LINESTRING (0 0, 2 0)')) → 2
hausdorff_distance( geom_from_wkt('LINESTRING (130 0, 0 0, 0 150)'),geom_from_wkt('LINESTRING (10 10, 10 150, 130 10)')) → 14.142135623
hausdorff_distance( geom_from_wkt('LINESTRING (130 0, 0 0, 0 150)'),geom_from_wkt('LINESTRING (10 10, 10 150, 130 10)'),0.5) → 70.0
```

[![](../../img/geometria/hausdorff_distance/hausdorff_distance1.png)](../../img/geometria/hausdorff_distance/hausdorff_distance1.png)

--

Nel caso di geometrie puntuali la [hausdorff_distance](#hausdorff_distance) coincide con la funzione [distance](#distance), segue un esempio:

!!! Tip "Espressione"
```
	format_number(
	hausdorff_distance( 
	transform($geometry,'EPSG:4326','EPSG:3004'), 
	transform(geometry(get_feature('fontanelle','n',1)),'EPSG:4326','EPSG:3004'))/1000,4) || ' km'  
	|| '\n'|| 
	format_number(
	distance( 
	transform($geometry,'EPSG:4326','EPSG:3004'), 
	transform(geometry(get_feature('fontanelle','n',1)),'EPSG:4326','EPSG:3004'))/1000,4) || ' km'
```

[![](../../img/geometria/hausdorff_distance/hausdorff_distance3.png)](../../img/geometria/hausdorff_distance/hausdorff_distance3.png)

--

In questo esempio confronto due layer: il numero più piccolo indica il poligono più simile a al poligono più grande.

[![](../../img/geometria/hausdorff_distance/hausdorff_distance2.png)](../../img/geometria/hausdorff_distance/hausdorff_distance2.png)

---

## inclination

Restituisce l'inclinazione misurata dallo zenit (0) al nadir (180) del _punto_a_ al _punto_b_.

Sintassi:

- inclination(_<span style="color:red;">point_a</span>_, _<span style="color:red;">point_b</span>_)

Argomenti:

* _<span style="color:red;">point_a</span>_ geometria punto
* _<span style="color:red;">point_b</span>_ geometria punto

Esempi:

```
inclination( make_point( 5, 10, 0 ), make_point( 5, 10, 5 ) ) → 0.0
inclination( make_point( 5, 10, 0 ), make_point( 5, 10, 0 ) ) → 90.0
inclination( make_point( 5, 10, 0 ), make_point( 50, 100, 0 ) ) → 90.0
inclination( make_point( 5, 10, 0 ), make_point( 5, 10, -5 ) ) → 180.0
```

[![](../../img/geometria/inclination/inclination1.png)](../../img/geometria/inclination/inclination1.png)

--

[![](../../img/geometria/inclination/inclination2.png)](../../img/geometria/inclination/inclination2.png)

---

## interior_ring_n

Restituisce un anello interno specifico da una geometria poligonale, o null se la geometria non è un poligono.

Sintassi:

- interior_ring_n(_<span style="color:red;">geometry</span>_, _<span style="color:red;">index</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ geometria poligono
* _<span style="color:red;">index</span>_ Indice dell'anello interno da restituire, dove 1 è il primo anello interno

Esempi:

```
geom_to_wkt(interior_ring_n(geom_from_wkt('POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1),(-0.1 -0.1, 0.4 0, 0.4 0.2, 0 0.2, -0.1 -0.1),(-1 -1, 4 0, 4 2, 0 2, -1 -1))'),1)) → 'LineString (-0.1 -0.1, 0.4 0, 0.4 0.2, 0 0.2, -0.1 -0.1))'
```

[![](../../img/geometria/interior_ring_n/interior_ring_n1.png)](../../img/geometria/interior_ring_n/interior_ring_n1.png)

Osservazioni:

Restituisce una lineastring!!!

[![](../../img/geometria/interior_ring_n/interior_ring_n2.png)](../../img/geometria/interior_ring_n/interior_ring_n2.png)

---

## intersection

Restituisce una geometria che rappresenta la porzione condivisa fra le due geometrie.

Sintassi:

- intersection(<span style="color:red;">_geometry1_</span>, <span style="color:red;">_geometry2_</span>)

Argomenti:

* <span style="color:red;">_geometry1_</span> una geometria
* <span style="color:red;">_geometry2_</span> una geometria

Esempi:

```
geom_to_wkt( intersection( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4)' ) ) ) → 'LINESTRING(3 3, 4 4)'
geom_to_wkt( intersection( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'MULTIPOINT(3.5 3.5, 4 5)' ) ) ) → 'POINT(3.5 3.5)'
```

[![](../../img/geometria/intersection/intersection1.png)](../../img/geometria/intersection/intersection1.png)

[![](../../img/geometria/intersection/intersection3.png)](../../img/geometria/intersection/intersection3.png)

!!! Tip "Espressione"
```
	-- intersezione tra le due linee
	intersection( 
	make_line( -- linea a
		start_point($geometry), 
		end_point(geometry(get_feature_by_id('linea_a',0))),
		end_point($geometry)),
	make_line(  -- linea b
		start_point(geometry(get_feature_by_id('linea_a',0))), 
		start_point($geometry),
		end_point(geometry(get_feature_by_id('linea_a',0))))
					)
	-- NB: -- l' ordine delle geometrie è indifferente
```

!!! Question "Prova tu"
	[Dati e progetto qgz](https://github.com/gbvitrano/HfcQGIS/raw/master/prova_tu/DIFFERENCE.zip)

--

[![](../../img/geometria/intersection/intersection2.png)](../../img/geometria/intersection/intersection2.png)

---

## intersects

Controlla qualora una geometria ne interseca un'altra. Restituisce true (1) se la geometrie si intersecano spazialmente (condividono una porzione di spazio) altrimenti da false (0).

Sintassi:

- intersects(<span style="color:red;">_geometry1_</span>, <span style="color:red;">_geometry2_</span>)

Argomenti:

* <span style="color:red;">_geometry1_</span> una geometria
* <span style="color:red;">_geometry2_</span> una geometria

Esempi:

```
intersects( geom_from_wkt( 'POINT(4 4)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → vero
intersects( geom_from_wkt( 'POINT(4 5)' ), geom_from_wkt( 'POINT(5 5)' ) ) → falso
```

[![](../../img/geometria/intersects/intersects1.png)](../../img/geometria/intersects/intersects1.png)

Osservazioni:

Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (Ctrl+F3):

```
intersects(geometry(get_feature( 'province_rt_rt','pk_uid','46')),$geometry)
```

dove:

* _geometry1_ è `geometry(get_feature( 'province_rt_rt','pk_uid','46'))`
* _geometry2_ è `$geometry`


[![](../../img/geometria/intersects/intersects2.png)](../../img/geometria/intersects/intersects2.png)

seleziono tutti i comuni `intersects` (interseca) nella provincia con `pk_uid`46 (Lucca)

PS:** potrei anche negare (`NOT`) l'espressione per selezionare il complementare (tutti i comuni tranne quelli intersecati con la provincia di Lucca).

`NOT intersects(geometry(get_feature( 'province_rt_rt','pk_uid','46')),$geometry)`

---

## intersects_bbox

Controlla se il perimetro di delimitazione della geometria si sovrappone a quello di un'altra geometria. Restituisce vero (1) se le geometrie intersecano spazialmente il perimetro di delimitazione definito e falso (0) se non lo intersecano.

Sintassi:

- intersects_bbox(<span style="color:red;">_geometry1_</span>, <span style="color:red;">_geometry2_</span>)

Argomenti:

* <span style="color:red;">_geometry1_</span> una geometria
* <span style="color:red;">_geometry2_</span> una geometria

Esempi:

```
intersects_bbox( geom_from_wkt( 'POINT(4 5)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → vero
intersects_bbox( geom_from_wkt( 'POINT(6 5)' ), geom_from_wkt( 'POLYGON((3 3, 4 4, 5 5, 3 3))' ) ) → falso
```
[![](../../img/geometria/intersects_bbox/intersects_bbox1.png)](../../img/geometria/intersects_bbox/intersects_bbox1.png)

---

## is_closed

Restituisce vero (true) se una linestring è chiusa (i punti di inizio e di fine coincidono), o falso (false) se una linestring non è chiusa. Se la geometria non è una linestring, il risultato sarà NULL.

Sintassi:

- is_closed(<span style="color:red;">_geometry_</span>)

Argomenti:

* <span style="color:red;">_geometry_</span> una geometria linestring

Esempi:

```
is_closed(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2)')) → falso
is_closed(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2, 0 0)')) → vero
```

[![](../../img/geometria/is_closed/is_closed1.png)](../../img/geometria/is_closed/is_closed1.png)

--

[![](../../img/geometria/is_closed/is_closed2.png)](../../img/geometria/is_closed/is_closed2.png) 

---

## is_empty

Restituisce vero se una geometria è vuota (senza coordinate), falso se la geometria non è vuota e NULL se non c'è geometria. Vedi anche `is_empty_or_null`.

Sintassi:

- is_empty(<span style="color:red;">_geometry_</span>)

Argomenti:

* <span style="color:red;">_geometry_</span> una geometria

Esempi:

```
is_empty(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2)')) → falso
is_empty(geom_from_wkt('LINESTRING EMPTY')) → vero
is_empty(geom_from_wkt('POINT(7 4)')) → falso
is_empty(geom_from_wkt('POINT EMPTY')) → vero
```

[![](../../img/geometria/is_empty/is_empty1.png)](../../img/geometria/is_empty/is_empty1.png)

[![screen](../../img/novita_312/Image02.png)](../../img/novita_312/Image02.png)

---

## is_empty_or_null

Restituisce vero se una geometria è vuota (senza coordinate), falso se la geometria non è vuota e NULL se non c'è geometria. Vedi anche `is_empty`.

Sintassi:

- is_empty_or_null(<span style="color:red;">_geometry_</span>)

Argomenti:

* <span style="color:red;">_geometry_</span> una geometria

Esempi:

```
is_empty_or_null(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2)')) → falso
iis_empty_or_null(geom_from_wkt('POINT(7 4)')) → falso
is_empty_or_null(geom_from_wkt('POINT EMPTY')) → vero
```

[![](../../img/geometria/is_empty_or_null/is_empty_or_null1.png)](../../img/geometria/is_empty_or_null/is_empty_or_null1.png)

[![screen](../../img/novita_312/Image02.png)](../../img/novita_312/Image02.png)

---

## is_multipart

Restituisce vero se la geometria è di tipo Multi.

Sintassi:

- is_multipart(<span style="color:red;">_geometry_</span>)

Argomenti:

* <span style="color:red;">_geometry_</span> una geometria

Esempi:

```
is_multipart(geom_from_wkt('MULTIPOINT ((0 0),(1 1),(2 2))')) → vero
is_multipart(geom_from_wkt('POINT (0 0)')) → falso
```

[![](../../img/geometria/is_multipart/is_multipart1.png)](../../img/geometria/is_multipart/is_multipart1.png)

---

## is_valid

Restituisce vero se una geometria è valida; se è ben formato in 2D secondo le regole **OGC**

Sintassi:

- is_valid(<span style="color:red;">_geometry_</span>)

Argomenti:

* <span style="color:red;">_geometry_</span> una geometria

Esempi:

```
is_valid(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2, 0 0)')) → vero
is_valid(geom_from_wkt('LINESTRING(0 0)')) → falso
```

[![](../../img/geometria/is_valid/is_valid1.png)](../../img/geometria/is_valid/is_valid1.png)

---

## length

Restituisce il numero di caratteri in una stringa o la lunghezza di una geometria di tipo linestring.

### Variabile stringa

Restituisce il numero di caratteri contenuti in una stringa.

Sintassi:

- length(_<span style="color:red;">string</span>_)

Argomenti:

* _<span style="color:red;">string</span>_ stringa della quale calcolare la lunghezza

Esempi:

```
length('hello') → 5
```

[![](../../img/geometria/length/length1.png)](../../img/geometria/length/length1.png)

### Variabile geometria

Calcola la lunghezza di un oggetto a geometria lineare. I calcoli sono sempre _planimetrici_ nel Sistema di Riferimento Spaziale (SR) di detta geometria, e l'unità di misura della lunghezza restituita è conforme all'unità di misura del SR. Ciò differisce dal calcolo eseguito dalla funzione [$length](#length), la quale esegue calcoli _ellissoidici_ basati sull'ellissoide del progetto e sulle impostazioni delle unità di distanza.

Sintassi:

- length(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria linea

Esempi:


* `length(geom_from_wkt('LINESTRING(0 0, 4 0)')) → 4.0`

[![](../../img/geometria/length/length2.png)](../../img/geometria/length/length2.png)

---

## length3D

Calcola la lunghezza 3D di un oggetto linea geometrica. Se la geometria non è un oggetto linea 3D, restituisce la sua lunghezza 2D. I calcoli sono sempre planimetrici nel Sistema di Riferimento Spaziale (SR) di questa geometria, e le unità della lunghezza restituita corrisponderanno alle unità per l'SR. Questo differisce dai calcoli eseguiti dalla funzione [$length](#length), che eseguirà calcoli ellissoidali basati sulle impostazioni dell'ellissoide e dell'unità di distanza del progetto.

Sintassi:

- length3D(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria linea

Esempi:

```
length3D(geom_from_wkt('LINESTRINGZ(0 0 0, 3 0 4)')) → 5.0
```

[![](../../img/geometria/length3d/img_01.png)](../../img/geometria/length3d/img_01.png)

---

## line_interpolate_angle

Restituisce l'angolo parallelo alla geometria ad una distanza specifica lungo una geometria di tipo linestring. Gli angoli sono in gradi in senso orario dal nord.

Sintassi:

- line_interpolate_angle(_<span style="color:red;">geometry</span>_, _<span style="color:red;">distance</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">distance</span>_ distanza lungo la linea a cui interpolare l'angolo

Esempi:

```
line_interpolate_angle(geometry:=geom_from_wkt('LineString(0 0, 10 0)'),distance:=5) → 90.0
```

[![](../../img/geometria/line_interpolate_angle/line_interpolate_angle1.png)](../../img/geometria/line_interpolate_angle/line_interpolate_angle1.png)

--

[![](../../img/geometria/line_interpolate_angle/line_interpolate_angle2.png)](../../img/geometria/line_interpolate_angle/line_interpolate_angle2.png)

---

## line_interpolate_point

Restituisce il punto interpolato ad una specifica distanza lungo una geometria di tipo linestring.

Sintassi:

- line_interpolate_point(_<span style="color:red;">geometry</span>_, _<span style="color:red;">distance</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">distance</span>_ distanza lungo la linea

Esempi:

```
geom_to_wkt(line_interpolate_point(geometry:=geom_from_wkt('LineString(0 0, 10 0)'),distance:=5)) → 'Point (4 0)'
```

[![](../../img/geometria/line_interpolate_point/line_interpolate_point1.png)](../../img/geometria/line_interpolate_point/line_interpolate_point1.png)

--

[![](../../img/geometria/line_interpolate_point/line_interpolate_point2.png)](../../img/geometria/line_interpolate_point/line_interpolate_point2.png)

---

## line_locate_point

Restituisce la distanza lungo una linestring corrispondente alla posizione più vicina alla linestring di una geometria puntuale specificata.

Sintassi:

- line_locate_point(_<span style="color:red;">geometry</span>_, _<span style="color:red;">point</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria di tipo linestring
* _<span style="color:red;">point</span>_ geometria puntuale per cui ricercare la posizione più vicina sulla linestring

Esempi:

```
line_locate_point(geometry:=geom_from_wkt('LineString(0 0, 10 0)'),point:=geom_from_wkt('Point(5 1)')) → 5.0
```

[![](../../img/geometria/line_locate_point/line_locate_point1.png)](../../img/geometria/line_locate_point/line_locate_point1.png)

---

## line_merge

Restituisce una geometria di tipo LineString o MultiLineString, dove qualsiasi LineString connessa dalla geometria in ingresso è stata fusa (merge) in una linestring singola. Questa funzione restituirà `NULL` se la geometria considerata non è una LineString/MultiLineString.

Sintassi:

- line_merge(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria di tipo LineString/MultiLineString

Esempi:

```
geom_to_wkt(line_merge(geom_from_wkt('MULTILINESTRING((0 0, 1 1),(1 1, 2 2))'))) → 'LineString(0 0,1 1,2 2)'
geom_to_wkt(line_merge(geom_from_wkt('MULTILINESTRING((0 0, 1 1),(11 1, 21 2))'))) → 'MultiLineString((0 0, 1 1),(11 1, 21 2)'
```

[![](../../img/geometria/line_merge/line_merge1.png)](../../img/geometria/line_merge/line_merge1.png)

--

[![](../../img/geometria/line_merge/line_merge2.png)](../../img/geometria/line_merge/line_merge2.png)

---

## line_substring

Restituisce la porzione di una geometria di linea (o curva) che rientra tra le distanze iniziale e finale specificate (misurata dall'inizio della linea). I valori Z e M sono linearmente interpolati dai valori esistenti.

Sintassi:

- line_substring(_<span style="color:red;">geometry</span>,<span style="color:red;">start_distance</span>,<span style="color:red;">end_distance</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria lineare o curva
* _<span style="color:red;">start_distance</span>_ distanza all'inizio della sottostringa
* _<span style="color:red;">end_distance</span>_ distanza alla fine della sottostringa

Esempi:

```
geom_to_wkt(line_substring(geometry:=geom_from_wkt('LineString(0 0, 10 0)'),start_distance:=2,end_distance:=6)) → 'LineString (2 0,6 0)'
line_substring( $geometry,  $length *.1,$length *.6) → <geometria: LineString>
```

[![](../../img/geometria/line_substring/line_substring1.png)](../../img/geometria/line_substring/line_substring1.png)

--

Funzione utile per la tematizzazione

[![](../../img/geometria/line_substring/line_substring2.png)](../../img/geometria/line_substring/line_substring2.png)

---

## m

Restituisce il valore m di una geometria puntuale.

Sintassi:

- m(_<span style="color:red;">geometry</span>_) 

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria punto

Esempi:

```
( geom_from_wkt( 'POINTM(2 5 4)' ) ) → 4
```

[![](../../img/geometria/m/m1.png)](../../img/geometria/m/m1.png)

---

## m_at

(>= QGIS 3.30)

Recupera una coordinata m della geometria, o un NULL se la geometria non ha valore m.

Sintassi:

- m_at(_<span style="color:red;">geometry</span>_,_<span style="color:red;">vertex</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria
* _<span style="color:red;">vertex</span>_ indice del vertice della geometria (gli indici partono da 0; i valori negativi si applicano a partire dall'ultimo indice, a partire da -1)

Esempi:

```
m_at(geom_from_wkt('LineStringZM(0 0 0 0, 10 10 0 5, 10 10 0 0)'), 1) → 5
```

[![](../../img/geometria/m_at/m_at330.png)](../../img/geometria/m_at/m_at330.png)

---

## m_max

Restituisce il valore minimo m (misura) di una geometria.

Sintassi:

* m_max(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria contenente m valori

Esempi:

```
m_max( make_point_m( 0,0,1 ) ) → 1
m_max(make_line( make_point_m( 0,0,1 ), make_point_m( -1,-1,2 ), make_point_m( -2,-2,0 ) ) ) → 2
```

[![](../../img/geometria/m_max/m_max1.png)](../../img/geometria/m_max/m_max1.png)

---

## m_min

Restituisce il valore minimo m (misura) di una geometria.

Sintassi:

* m_min(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria contenente m valori

Esempi:

```
m_min( make_point_m( 0,0,1 ) ) → 1
m_min(make_line( make_point_m( 0,0,1 ), make_point_m( -1,-1,2 ), make_point_m( -2,-2,0 ) ) ) → 0
```

[![](../../img/geometria/m_min/m_min1.png)](../../img/geometria/m_min/m_min1.png)

---

## main_angle

Restituisce l'angolo principale di una geometria (senso orario, in gradi dal Nord), il quale rappresenta l'angolo dell'orientamento del rettangolo minimo che copre completamente la geometria.

Sintassi:

* main_angle(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria poligono

Esempi:

```
main_angle(geom_from_wkt('Polygon ((321577 129614, 321581 129618, 321585 129615, 321581 129610, 321577 129614))')) → 38.66
```

[![](../../img/geometria/main_angle/img_01.png)](../../img/geometria/main_angle/img_01.png)


Osservazioni:

[![](https://user-images.githubusercontent.com/1829991/87367553-aae7d680-c5be-11ea-923a-e81200f2b90c.gif)](https://user-images.githubusercontent.com/1829991/87367553-aae7d680-c5be-11ea-923a-e81200f2b90c.gif)

---

## make_circle

Crea un poligono circolare.

Sintassi:

- make_circle(_<span style="color:red;">center</span>_, _<span style="color:red;">radius</span>_[, _<span style="color:red;">segments=36</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">center</span>_ centro del cerchio
* _<span style="color:red;">radius</span>_ raggio del cerchio
* _<span style="color:red;">segments</span>_ argomento opzionale per la segmentazione del poligono. Valore predefinito pari a 36

Esempi:

```
geom_to_wkt(make_circle(make_point(10,10), 5, 4)) → 'Polygon ((10 15, 15 10, 10 5, 5 10, 10 15))'
geom_to_wkt(make_circle(make_point(10,10,5), 5, 4)) → 'PolygonZ ((10 15 5, 15 10 5, 10 5 5, 5 10 5, 10 15 5))''
geom_to_wkt(make_circle(make_point(10,10,5,30), 5, 4)) → 'PolygonZM ((10 15 5 30, 15 10 5 30, 10 5 5 30, 5 10 5 30, 10 15 5 30))'
```

[![](../../img/geometria/make_circle/make_circle1.png)](../../img/geometria/make_circle/make_circle1.png)

[![](../../img/geometria/make_circle/make_circle2.png)](../../img/geometria/make_circle/make_circle2.png)

---

## make_ellipse

Crea un poligono ellittico.

Sintassi:

- make_ellipse(_<span style="color:red;">center</span>_, _<span style="color:red;">semi_major_axis</span>_, _<span style="color:red;">semi_minor_axis</span>_, _<span style="color:red;">azimuth</span>_[, _<span style="color:red;">segments=36</span>_])

Argomenti:

* _<span style="color:red;">center</span>_ centro dell'ellisse
* _<span style="color:red;">semi_major_axis</span>_ semi-asse maggiore dell'ellisse
* _<span style="color:red;">semi_minor_axis</span>_ semi-asse minore dell'ellisse
* _<span style="color:red;">azimuth</span>_ orientazione dell'ellisse
* _<span style="color:red;">segments</span>_ argomento opzionale per la segmentazione del poligono. Valore predefinito pari a 36

Esempi:

```
geom_to_wkt(make_ellipse(make_point(10,10), 5, 2, 90, 4)) → 'Polygon ((15 10, 10 8, 5 10, 10 12, 15 10))
geom_to_wkt(make_ellipse(make_point(10,10,5), 5, 2, 90, 4)) → 'PolygonZ ((15 10 5, 10 8 5, 5 10 5, 10 12 5, 15 10 5))'
geom_to_wkt(make_circle(make_point(10,10,5,30), 5, 2, 90, 4)) → 'PolygonZM ((15 10 5 30, 10 8 5 30, 5 10 5 30, 10 12 5 30, 15 10 5 30))'
```

[![](../../img/geometria/make_ellipse/make_ellipse1.png)](../../img/geometria/make_ellipse/make_ellipse1.png)

[![](../../img/geometria/make_ellipse/make_ellipse2.png)](../../img/geometria/make_ellipse/make_ellipse2.png)

---

## make_line

Crea una geometria linea da una serie di geometrie punto.

Sintassi:

- make_line(_<span style="color:red;">point1</span>_, _<span style="color:red;">point2</span>_, …_)

Argomenti:

* _<span style="color:red;">point</span>_ una geometria punto

Esempi:

```
geom_to_wkt(make_line(make_point(2,4),make_point(3,5))) → 'LineString (2 4, 3 5)'
geom_to_wkt(make_line(make_point(2,4),make_point(3,5),make_point(9,7))) → 'LineString (2 4, 3 5, 9 7)'
```

[![](../../img/geometria/make_line/make_line1.png)](../../img/geometria/make_line/make_line1.png)

### Array variant

I vertici di linea sono specificati come una matrice di punti.

Sintassi:

- make_line(_<span style="color:red;">array</span>_)

Argomenti:

* _<span style="color:red;">array</span>_ Matrice di punti

Esempi:

```
geom_to_wkt(make_line(array(make_point(2,4),make_point(3,5),make_point(9,7)))) → 'LineString (2 4, 3 5, 9 7)'
```

[![](../../img/geometria/make_line/make_line3.png)](../../img/geometria/make_line/make_line3.png)

!!! Tip "Espressione"
```
	make_line(
	array(geometry(
		get_feature_by_id('fontanelle_Palermo',$id))),
	array(geometry(
		get_feature_by_id('fontanelle_Palermo',not $id%2)))
			) 
```

[![](../../img/geometria/make_line/make_line2.png)](../../img/geometria/make_line/make_line2.png)

---

## make_point

Crea una geometria punto da valori x ed y (e opzionalmente z ed m).

Sintassi:

- make_point(_<span style="color:red;">x</span>_, _<span style="color:red;">y</span>_, _<span style="color:red;">z</span>_, _<span style="color:red;">m</span>_)

Argomenti:

* _<span style="color:red;">x</span>_ coordinata x del punto
* _<span style="color:red;">y</span>_ coordinata y del punto
* _<span style="color:red;">z</span>_ coordinata opzionale z del punto
* _<span style="color:red;">m</span>_ valore m del punto

Esempi:

```
geom_to_wkt(make_point(2,4,6,8)) → 'PointZM (2 4 6 8)'
```

[![](../../img/geometria/make_point/make_point1.png)](../../img/geometria/make_point/make_point1.png)

---

## make_point_m

Crea una geometria punto da una coordinata x, y ed un valore m.

Sintassi:

- make_point_m_(_<span style="color:red;">x</span>_, _<span style="color:red;">y</span>_, _<span style="color:red;">m</span>_)

Argomenti:

* _<span style="color:red;">x</span>_ coordinata x del punto
* _<span style="color:red;">y</span>_ coordinata y del punto
* _<span style="color:red;">m</span>_ valore m del punto

Esempi:

```
geom_to_wkt(make_point_m(2,4,6)) → 'PointM (2 4 6)'
```

[![](../../img/geometria/make_point_m/make_point_m1.png)](../../img/geometria/make_point_m/make_point_m1.png)

---

## make_polygon

Crea una geometria poligono da un'anello esterno e opzionalmente da geometrie ad anello interne.

Sintassi:

- make_polygon(_<span style="color:red;">outerRing</span>_[, _<span style="color:red;">innerRing1</span>_][, _<span style="color:red;">innerRing2</span>_] …_)

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">outerRing</span>_ geometria a linea chiusa per l'anello esterno del poligono
* _<span style="color:red;">innerRing</span>_ geometria a linea chiusa opzionale per anello interno

Esempi:

```
geom_to_wkt(make_polygon(geom_from_wkt('LINESTRING( 0 0, 0 1, 1 1, 1 0, 0 0 )'))) → 'Polygon ((0 0, 0 1, 1 1, 1 0, 0 0))'
geom_to_wkt(make_polygon(geom_from_wkt('LINESTRING( 0 0, 0 1, 1 1, 1 0, 0 0 )'),geom_from_wkt('LINESTRING( 0.1 0.1, 0.1 0.2, 0.2 0.2, 0.2 0.1, 0.1 0.1 )'),geom_from_wkt('LINESTRING( 0.8 0.8, 0.8 0.9, 0.9 0.9, 0.9 0.8, 0.8 0.8 )'))) → 'Polygon ((0 0, 0 1, 1 1, 1 0, 0 0),(0.1 0.1, 0.1 0.2, 0.2 0.2, 0.2 0.1, 0.1 0.1),(0.8 0.8, 0.8 0.9, 0.9 0.9, 0.9 0.8, 0.8 0.8))'
```
[![](../../img/geometria/make_polygon/make_polygon1.png)](../../img/geometria/make_polygon/make_polygon1.png)

---

## make_rectangle_3points

Crea un rettangolo da 3 punti.

Sintassi:

- make_rectangle_3points(_<span style="color:red;">point1</span>_,_<span style="color:red;">point2</span>_,_<span style="color:red;">point3</span>_[,option=0]…)

Argomenti:

* _<span style="color:red;">point1</span>_ Primo punto
* _<span style="color:red;">point2</span>_ Secondo punto
* _<span style="color:red;">point3</span>_ Terzo punto
* _<span style="color:red;">option</span>_ Un argomento facoltativo per costruire il rettangolo. Di default questo valore è 0. Il valore può essere 0 (distanza) o 1 (proiettato). Distanza opzione: la seconda distanza è uguale alla distanza tra il 2 ° e il 3 ° punto. Opzione proiettata: la seconda distanza è uguale alla distanza della proiezione perpendicolare del terzo punto sul segmento o della sua estensione.

Esempi:

```
geom_to_wkt(make_rectangle_3points(make_point(0, 0), make_point(0,5), make_point(5, 5), 0))) → 'Polygon ((0 0, 0 5, 5 5, 5 0, 0 0))'
geom_to_wkt(make_rectangle_3points(make_point(0, 0), make_point(0,5),make_point(5, 3), 1))) → 'Polygon ((0 0, 0 5, 5 5, 5 0, 0 0))'
```

[![](../../img/geometria/make_rectangle_3points/make_rectangle_3points1.png)](../../img/geometria/make_rectangle_3points/make_rectangle_3points1.png)

--

## make_regular_polygon

Crea un poligono regolare.

Sintassi:

- make_regular_polygon(_<span style="color:red;">center</span>_, _<span style="color:red;">radius</span>_, _<span style="color:red;">number_sides</span>_[, _<span style="color:red;">circle=0</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">center</span>_ centro del poligono regolare
* _<span style="color:red;">radius</span>_ secondo punto. Il primo se il poligono regolare è inscritto. Il punto intermedio del primo lato se il poligono regolare è circoscritto.
* _<span style="color:red;">number_sides</span>_ Numero di lati del poligono regolare
* _<span style="color:red;">circle</span>_ Argomento opzionale per la costruzione del poligono regolare. Il valore predefinito è 0. Il valore può essere 0 (poligono iscritto) o 1 (poligono circoscritto)

Esempi:

```
geom_to_wkt(make_regular_polygon(make_point(0,0), make_point(0,5), 5)) → 'Polygon ((0 5, 4.76 1.55, 2.94 -4.05, -2.94 -4.05, -4.76 1.55, 0 5))'
geom_to_wkt(make_regular_polygon(make_point(0,0), project(make_point(0,0), 4.0451, radians(36)), 5)) → 'Polygon ((0 5, 4.76 1.55, 2.94 -4.05, -2.94 -4.05, -4.76 1.55, 0 5))'
```

[![](../../img/geometria/make_regular_polygon/make_regular_polygon1.png)](../../img/geometria/make_regular_polygon/make_regular_polygon1.png)

[![](../../img/geometria/make_regular_polygon/make_regular_polygon2.png)](../../img/geometria/make_regular_polygon/make_regular_polygon2.png)

---

## make_square

Crea un quadrato da una diagonale.

Sintassi:

- make_square(_<span style="color:red;">point1</span>_,_<span style="color:red;">point2</span>_)

Argomenti:

- _<span style="color:red;">point1</span>_ Primo punto della diagonale
- _<span style="color:red;">point2</span>_ Secondo punto della diagonale

Esempi:

```
geom_to_wkt(make_square( make_point(0,0), make_point(5,5))) → 'Polygon ((0 0, -0 5, 5 5, 5 0, 0 0))'
geom_to_wkt(make_square( make_point(5,0), make_point(5,5))) → 'Polygon ((5 0, 2.5 2.5, 5 5, 7.5 2.5, 5 0))'
```

[![](../../img/geometria/make_square/make_square1.png)](../../img/geometria/make_square/make_square1.png)

---

## make_triangle

Crea un poligono triangolare

Sintassi:

- make_triangle(_<span style="color:red;">point1</span>_,_<span style="color:red;">point2</span>_,_<span style="color:red;">point3</span>_)

Argomenti:

- _<span style="color:red;">point1</span>_ Primo punto del triangolo
- _<span style="color:red;">point2</span>_ Secondo punto del triangolo
- _<span style="color:red;">point3</span>_ Secondo punto del triangolo
- 
Esempi:

```
geom_to_wkt(make_triangle(make_point(0,0), make_point(5,5), make_point(0,10))) → 'Triangle ((0 0, 5 5, 0 10, 0 0))'
geom_to_wkt(boundary(make_triangle(make_point(0,0), make_point(5,5), make_point(0,10)))) → 'LineString (0 0, 5 5, 0 10, 0 0)'
```

[![](../../img/geometria/make_triangle/make_triangle1.png)](../../img/geometria/make_triangle/make_triangle1.png)

---

## make_valid

\>=QGIS 3.28 Firenze

Restituisce una geometria valida o una geometria vuota se non è stato possibile renderla valida.

Sintassi:

- make_triangle(_<span style="color:red;">geometry</span>_[,_<span style="color:red;">method=structure</span>_][,_<span style="color:red;">keep_collapsed=false</span>_])

[ ] indica componenti opzionali

Argomenti:

- _<span style="color:red;">geometry</span>_ Una geometria
- _<span style="color:red;">method</span>_ algoritmo di riparazione. Può essere 'struttura' o 'tracciato'. L'opzione 'tracciato' combina tutti gli anelli in un insieme di linee con nodi e quindi estrae poligoni validi da tale tracciato. Il metodo 'struttura' rende prima validi tutti gli anelli e poi unisce le conchiglie e sottrae i fori dalle conchiglie per generare risultati validi. Si presuppone che i fori e le conchiglie siano classificati correttamente.
- _<span style="color:red;">keep_collapsed</span>_ se impostato a true, i componenti che sono collassati in una dimensione inferiore saranno mantenuti. Ad esempio, un anello che collassa in una linea o una linea che collassa in un punto.

Esempi:

```
- geom_to_wkt(make_valid(geom_from_wkt('POLYGON((3 2, 4 1, 5 8, 3 2, 4 2))'))) → 'Polygon ((3 2, 3 4, 1 4, 1 2, 3 2))'
- geom_to_wkt(make_valid(geom_from_wkt('POLYGON((3 2, 4 1, 5 8, 3 2, 4 2))'), 'linework')) → 'GeometryCollection (Polygon ((5 8, 4 1, 3 2, 5 8)),LineString (3 2, 4 2))'
- geom_to_wkt(make_valid(geom_from_wkt('POLYGON((3 2, 4 1, 5 8))'), method:='linework')) → 'Polygon ((3 2, 3 4, 1 4, 1 2, 3 2))'
- make_valid(geom_from_wkt('LINESTRING(0 0)')) → Una geometria vuota
```

[![](../../img/geometria/make_valid/make_valid.png)](../../img/geometria/make_valid/make_valid.png)
---

## minimal_circle

Restituisce la circonferenza circoscritta minima di una geometria. Rappresenta il cerchio minimo che circoscrive tutte le geometrie presenti in un dataset.

Sintassi:

- minimal_circle(_<span style="color:red;">geometry</span>_[, _<span style="color:red;">segments=36</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">segments</span>_ argomento opzionale per la segmentazione del poligono. Valore predefinito pari a 36

Esempi:

```
geom_to_wkt( minimal_circle( geom_from_wkt( 'LINESTRING(0 5, 0 -5, 2 1)' ), 4 ) ) → Polygon ((0 5, 5 -0, -0 -5, -5 0, 0 5))
geom_to_wkt( minimal_circle( geom_from_wkt( 'MULTIPOINT(1 2, 3 4, 3 2)' ), 4 ) ) → Polygon ((3 4, 3 2, 1 2, 1 4, 3 4))
```

[![](../../img/geometria/minimal_circle/minimal_circle1.png)](../../img/geometria/minimal_circle/minimal_circle1.png)

--

[![](../../img/geometria/minimal_circle/minimal_circle2.png)](../../img/geometria/minimal_circle/minimal_circle2.png)

---

## nodes_to_points

Restituisce una geometria multi-punti costituita da ogni nodo della geometria in ingresso.

Sintassi:

- nodes_to_points(_<span style="color:red;">geometry</span>_[, _<span style="color:red;">ignore_closing_nodes=false</span>_])

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria
* _<span style="color:red;">ignore_closing_nodes</span>_ argomento opzionale che specifica se includere i nodi duplicati che chiudono linee o poligoni ad anello. Normalmente false, impostare a true per evitare di includere questi nodi duplicati nella raccolta in uscita.

Esempi:

```
geom_to_wkt(nodes_to_points(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2)'))) → 'MultiPoint ((0 0),(1 1),(2 2))'
geom_to_wkt(nodes_to_points(geom_from_wkt('POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1))'),true)) → 'MultiPoint ((-1 -1),(4 0),(4 2),(0 2))'
```

[![](../../img/geometria/nodes_to_points/nodes_to_points1.png)](../../img/geometria/nodes_to_points/nodes_to_points1.png)

--

[![](../../img/geometria/nodes_to_points/nodes_to_points1.png)](../../img/geometria/nodes_to_points/nodes_to_points1.png)

---

## num_geometries

Restituisce il numero di geometrie in una raccolta di geometrie, o il numero di parti in una geometria multiparte. La funzione restituisce NULL se la geometria di input non è una raccolta.

Sintassi:

- num_geometries(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ raccolta di geometrie

Esempi:

```
num_geometries(geom_from_wkt('GEOMETRYCOLLECTION(POINT(0 1), POINT(0 0), POINT(1 0), POINT(1 1))')) → 4
```

[![](../../img/geometria/num_geometries/num_geometries1.png)](../../img/geometria/num_geometries/num_geometries1.png)

---

## num_interior_rings

Restituisce il numero di anelli interni in un poligono o in una raccolta di geometrie, o null se la geometria in ingresso non è un poligono o una raccolta.

Sintassi:

- num_interior_rings(_<span style="color:red;">geometry</span>_) 

Argomenti:

* _<span style="color:red;">geometry</span>_ geometria in ingresso

Esempi:

```
num_interior_rings(geom_from_wkt('POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1),(-0.1 -0.1, 0.4 0, 0.4 0.2, 0 0.2, -0.1 -0.1))')) → 1
```

[![](../../img/geometria/num_interior_rings/num_interior_rings1.png)](../../img/geometria/num_interior_rings/num_interior_rings1.png)

[![](../../img/geometria/num_interior_rings/num_interior_rings2.png)](../../img/geometria/num_interior_rings/num_interior_rings2.png)

---

## num_points

Restituisce il numero di vertici in una geometria.

Sintassi:

- num_points(_<span style="color:red;">geometry</span>_) 

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
num_points($geometry) → numero di vertici in $geometry
```

[![](../../img/geometria/num_points/num_points1.png)](../../img/geometria/num_points/num_points1.png)

---

## num_rings

Restituisce il numero di anelli (includendo anche anelli esterni) in un poligono o in una raccolta di geometrie, o null se la geometria in ingresso non è un poligono o una raccolta.

Sintassi:

- num_rings(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ geometria in ingresso

Esempi:

```
num_rings(geom_from_wkt('POLYGON((-1 -1, 4 0, 4 2, 0 2, -1 -1),(-0.1 -0.1, 0.4 0, 0.4 0.2, 0 0.2, -0.1 -0.1))')) → 2
```

[![](../../img/geometria/num_rings/num_rings1.png)](../../img/geometria/num_rings/num_rings1.png)

--

[![](../../img/geometria/num_rings/num_rings2.png)](../../img/geometria/num_rings/num_rings2.png)

---

## offset_curve

Restituisce una geometria formata facendo l'offset di una geometria di tipo linestring a lato. Le distanze sono espresse nel SR di tale geometria.

Sintassi:

- offset_curve(_<span style="color:red;">geometry</span>_, _<span style="color:red;">distance</span>_[, _<span style="color:red;">segments=8</span>_][, _<span style="color:red;">join=1</span>_][, _<span style="color:red;">miter_limit=2.0</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria (multi)linestring
* _<span style="color:red;">distance</span>_ distanza di offset. Valori positivi saranno bufferizzati a sinistra delle linee, valori negativi a destra
* _<span style="color:red;">segments</span>_ numero di segmenti da usare per rappresentare un quarto di cerchio quando è utilizzato uno stile di unione arrotondato. Un numero grande risulta in una linea più morbida, con più nodi.
* _<span style="color:red;">join</span>_ stile di unione per gli angoli, dove 1 = arrotondato, 2 = seghettato e 3 = smussato
* _<span style="color:red;">miter_limit</span>_ limite sul rapporto di seghettatura usato per angoli molto appuntiti (solamente quando si usano le unioni seghettate)

Esempi:

```
offset_curve($geometry, 10.5) → linea scostata a sinistra di 10.5 unità
offset_curve($geometry, -10.5) → linea scostata a destra di 10.5 unità
offset_curve($geometry, 10.5, segments=16, join=1) → linea scostata a sinistra di 10.5 unità, usando più segmenti per risultare in una curva più morbida
offset_curve($geometry, 10.5, join=3) → linea scostata a sinistra di 10.5 unità, usando un'unione smussata
```

[![](../../img/geometria/offset_curve/offset_curve1.png)](../../img/geometria/offset_curve/offset_curve1.png)

Osservazioni:

	La linea è scostata a sinistra o destra rispetto al verso della linea:

[![](../../img/geometria/offset_curve/offset_curve2.png)](../../img/geometria/offset_curve/offset_curve2.png)

---

## order_parts

Ordina le parti di una MultiGeometria secondo un dato criterio

Sintassi:

- order_parts(_<span style="color:red;">geometry</span>_, _<span style="color:red;">orderby</span>_[, _<span style="color:red;">ascending=true</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria multi-tipo
* _<span style="color:red;">orderby</span>_ un espressione stringa che definisce il criterio di ordinamento
* _<span style="color:red;">ascending</span>_ booleano, True per ascendente, False per discendente

Esempi:

```
order_parts(geom_from_wkt('MultiPolygon (((1 1, 5 1, 5 5, 1 5, 1 1)),((1 1, 9 1, 9 9, 1 9, 1 1)))'), 'area($geometry)', False) → MultiPolygon (((1 1, 9 1, 9 9, 1 9, 1 1)),((1 1, 5 1, 5 5, 1 5, 1 1)))
order_parts(geom_from_wkt('LineString(1 2, 3 2, 4 3)'), '1', True) → LineString(1 2, 3 2, 4 3)
```

[![](../../img/geometria/order_parts/order_parts1.png)](../../img/geometria/order_parts/order_parts1.png)

---

## oriented_bbox

Restituisce una geometria che rappresenta il perimetro di delimitazione minimo orientato di una geometria.

Sintassi:

- oriented_bbox(_<span style="color:red;">geometry</span>_) 

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geom_to_wkt(oriented_bbox(geom_from_wkt('MULTIPOINT(1 2, 3 4, 3 2)'))) → 'Polygon ((1 2, 2 1, 4 3, 3 4, 1 2))'
```

[![](../../img/geometria/oriented_bbox/oriented_bbox1.png)](../../img/geometria/oriented_bbox/oriented_bbox1.png)

[![](../../img/geometria/oriented_bbox/oriented_bbox2.png)](../../img/geometria/oriented_bbox/oriented_bbox2.png)

---

## overlaps

Controlla qualora una geometria si sovrapponga ad un'altra. Restituisce true (1) se le geometrie condividono aree, ma non sono completamente contenute una nell'altra.

Sintassi:

- overlaps(_<span style="color:red;">geometry1</span>_, _<span style="color:red;">geometry2</span>_)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
overlaps( geom_from_wkt( 'LINESTRING(3 5, 4 4, 5 5, 5 3)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → 1
overlaps( geom_from_wkt( 'LINESTRING(0 0, 1 1)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → 0
```

[![](../../img/geometria/overlaps/overlaps1.png)](../../img/geometria/overlaps/overlaps1.png)

Osservazioni:

Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (Ctrl+F3):

```
overlaps(geometry(get_feature( 'cerchio','id','1')), $geometry)
```

dove:

* _geometry1_ è `geometry(get_feature('cerchio','id','1'))`
* _geometry2_ è `$geometry`

[![](../../img/geometria/overlaps/overlaps2.png)](../../img/geometria/overlaps/overlaps2.png)

seleziono tutti i comuni `overlaps` (sovrapposti) al cerchio in figura.

PS:** potrei anche negare (`NOT`) l'espressione per selezionare il complementare (tutti i comuni tranne quelli sovrapposti con il cerchio).

`NOT overlaps(geometry(get_feature('cerchio','id','1')),$geometry)`

---

## overlay_contains

Restituisce se l'elemento corrente contiene spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target contenuti nell'elemento corrente. Ulteriori informazioni sul predicato GEOS "Contains" sottostante, come descritto nella funzione PostGIS [ST_CONTAINS](https://postgis.net/docs/ST_Contains.html).

Sintassi:

- overlay_contains(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

Esempi:

```
overlay_contains('regions') → true se l'elemento corrente contiene spazialmente una regione
overlay_contains('regions', filter:= population > 10000) → vero se l'elemento corrente contiene spazialmente una regione con una popolazione maggiore di 10000
overlay_contains('regions', name) → un array di nomi, per le regioni contenute nell'elemento corrente
array_to_string(overlay_contains('regions', name)) → una stringa come una lista di nomi separata da virgola, per le regioni contenute nell'elemento corrente
overlay_contains('regions', name)[0] → una stringa con il nome della regione contenuta nell'elemento corrente
array_sort(overlay_contains(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni contenute nell'elemento corrente e con una popolazione superiore a 10000
overlay_contains(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni contenute nell'elemento corrente
```

[![](../../img/geometria/overlay_/overlay_contains1.png)](../../img/geometria/overlay_/overlay_contains1.png)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

---

## overlay_crosses

Restituisce se l'elemento corrente attraversa spazialmente almeno un elemento di un layer target o un array di risultati basati su espressioni per gli elementi nel layer target attraversati dall'elemento corrente. Ulteriori informazioni sul predicato GEOS "Crosses" sottostante, come descritto nella funzione PostGIS [ST_Crosses](https://postgis.net/docs/ST_Crosses.html).

Sintassi:

- overlay_crosses(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

Esempi:

```
overlay_crosses('regions') → true se l'elemento corrente attraversa spazialmente una regione
overlay_crosses('regions', filter:= population > 10000) → vero se l'elemento corrente attraversa spazialmente una regione con una popolazione maggiore di 10000
overlay_crosses('regions', name) → un array di nomi, per le regioni attraversate dall'elemento corrente
array_to_string(overlay_crosses('regions', name)) → una stringa come una lista di nomi separata da virgola, per le regioni attraversate dall'elemento corrente
overlay_crosses('regions', name)[0] → una stringa con il nome della prima regioni attraversata dall'elemento corrente
array_sort(overlay_crosses(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni attraversate dall'elemento corrente e con una popolazione superiore a 10000
overlay_crosses(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni attraversate dall'elemento corrente
```

[![](../../img/geometria/overlay_/overlay_crosses1.png)](../../img/geometria/overlay_/overlay_crosses1.png)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

---

## overlay_disjoint

Restituisce se l'elemento corrente è spazialmente disgiunto da tutti gli elementi di un layer target, o un array di risultati basati su espressione per gli elementi nel layer target che sono disgiunti dall'elemento corrente. Ulteriori informazioni sul sottostante predicato GEOS "Disjoint", come descritto nella funzione PostGIS [ST_Disjoint](https://postgis.net/docs/ST_Disjoint.html).

Sintassi:

- overlay_disjoint(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

Esempi:

```
overlay_disjoint('regions') → true se l'elemento corrente è spazialmente disgiunto da tutte le regioni
overlay_disjoint('regions', filter:= population > 10000) → vero se l'elemento corrente è spazialmente disgiunto da tutte le regioni con una popolazione maggiore di 10000
overlay_disjoint('regions', name) → un array di nomi, per le regioni spazialmente disgiunte dall'elemento corrente
array_to_string(overlay_disjoint('regions', name)) → una stringa come una lista di nomi separata da virgola, per le regioni spazialmente disgiunte dall'elemento corrente
overlay_disjoint('regions', name)[0] → una stringa con il nome della regione spazialmente disgiunte dall'elemento corrente
array_sort(overlay_disjoint(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni spazialmente disgiunte dall'elemento corrente e con una popolazione superiore a 10000
overlay_disjoint(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni spazialmente disgiunte dall'elemento corrente
```

[![](../../img/geometria/overlay_/overlay_disjoint1.png)](../../img/geometria/overlay_/overlay_disjoint1.png)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

---

## overlay_equals

Restituisce se l'elemento corrente è spazialmente uguale ad almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target che sono spazialmente uguali all'elemento corrente. Ulteriori informazioni sul predicato GEOS "Equals" sottostante, come descritto nella funzione PostGIS [ST_Equals](https://postgis.net/docs/ST_Equals.html).

Sintassi:

- overlay_equals(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

Esempi:

```
overlay_equals('regions') → true se l'elemento corrente è spazialmente uguale ad una regione
overlay_equals('regions', filter:= population > 10000) → vero se l'elemento corrente è spazialmente uguale ad una regione con una popolazione maggiore di 10000
overlay_equals('regions', name) → un array di nomi, per le regioni spazialmente uguali all'elemento corrente
array_to_string(overlay_equals('regions', name)) → una stringa come lista di nomi separati da virgole, per le regioni spazialmente uguali all'elemento corrente
overlay_equals('regions', name)[0] → una stringa con il nome della regione spazialmente uguale all'elemento corrente
array_sort(overlay_equals(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni spazialmente uguali all'elemento corrente e con una popolazione superiore a 10000
overlay_equals(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni spazialmente uguali all'elemento corrente
```

[![](../../img/geometria/overlay_/overlay_equals1.png)](../../img/geometria/overlay_/overlay_equals1.png)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

---

## overlay_intersects

aggiornato a QGIS 3.24 Tisler

Restituisce se l'elemento corrente interseca spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target intersecati dall'elemento corrente. Ulteriori informazioni sul predicato GEOS "Intersects" sottostante, come descritto nella funzione PostGIS [ST_INTERSECTS](https://postgis.net/docs/ST_Intersects.html).

Sintassi <= **QGIS 3.22.x**

- overlay_intersects(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_])

Sintassi >= **QGIS 3.24.x**

- overlay_intersects(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_][,_<span style="color:red;">min_overlap</span>_][,_<span style="color:red;">min_inscribed_circle_radius</span>_][,_<span style="color:red;">return_details</span>_][,_<span style="color:red;">sort_by_intersection_size</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);
* _<span style="color:red;">min_overlap</span>_ definisce un filtro opzionale di esclusione: per i poligoni un'area minima in unità quadrate dell'elemento corrente per l'intersezione (se l'intersezione risulta in più poligoni l'intersezione sarà restituita se almeno uno dei poligoni ha un'area maggiore o uguale al valore), per le linee una lunghezza minima in unità dell'elemento corrente (se l'intersezione risulta in più linee l'intersezione sarà restituita se almeno una delle linee ha una lunghezza maggiore o uguale al valore).
* _<span style="color:red;">min_inscribed_circle_radius</span>_ definisce un filtro opzionale di esclusione (solo per i poligoni): raggio minimo in unità dell'elemento corrente per il cerchio massimo inscritto dell'intersezione (se l'intersezione risulta in più poligoni l'intersezione sarà restituita se almeno uno dei poligoni ha un raggio per il cerchio massimo inscritto maggiore o uguale al valore).
Leggi di più sul predicato GEOS sottostante, come descritto nella funzione PostGIS [ST_MaximumInscribedCircle](https://postgis.net/docs/ST_MaximumInscribedCircle.html). Questo argomento richiede GEOS >= 3.9.
* _<span style="color:red;">return_details</span>_ Imposta questo a true per restituire una lista di mappe contenenti (nomi chiave tra virgolette) l'elemento 'id', l'espressione 'result' e il valore 'overlap'. Il 'raggio' del cerchio massimo inscritto viene anche restituito quando il layer di destinazione è un poligono. Valido solo se usato con il parametro espressione.
* _<span style="color:red;">sort_by_intersection_size</span>_ valido solo se usato con un'espressione, impostalo a 'des' per restituire i risultati ordinati dal valore di sovrapposizione in ordine decrescente o impostalo a 'asc' per un ordine crescente.

[ ] indica componenti opzionali

Esempi:

```
overlay_intersects('regions') → vero se l'elemento corrente interseca spazialmente una regione
overlay_intersects('regions', filter:= population > 10000) → vero se l'elemento corrente interseca spazialmente una regione con una popolazione maggiore di 10000
overlay_intersects('regions', name) → un array di nomi, per le regioni intersecate dall'elemento corrente
array_to_string(overlay_intersects('regions', name)) → una stringa come una lista di nomi separata da virgola, per le regioni intersecate dall'elemento corrente
array_sort(overlay_intersects(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni intersecate dall'elemento corrente e con una popolazione maggiore di 10000
overlay_intersects(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni intersecate dall'elemento corrente
overlay_intersects(layer:='regions', min_overlap:=0.54) → true se l'elemento corrente interseca spazialmente una regione e l'area di intersezione (di almeno una delle parti in caso di multipoligoni) è maggiore o uguale a 0.54
overlay_intersects(layer:='regions', min_inscribed_circle_radius:=0.54) → true se l'elemento corrente interseca spazialmente una regione e il raggio massimo del cerchio inscritto nell'area di intersezione (di almeno una delle parti in caso di parti multiple) è maggiore o uguale a 0.54
overlay_intersects(layer:='regions', expression:= geom_to_wkt($geometry), return_details:=true) → un array di mappe contenente 'id', 'result', 'overlap' e 'radius'
overlay_intersects(layer:='regions', expression:= geom_to_wkt($geometry), sort_by_intersection_size:='des') → un array di geometrie (in WKT) ordinate per il valore di sovrapposizione in ordine decrescente
```

[![](../../img/geometria/overlay_/overlay_intersects1.png)](../../img/geometria/overlay_/overlay_intersects1.png)

[![](../../img/geometria/overlay_/overlay_intersects2.png)](../../img/geometria/overlay_/overlay_intersects2.png)

Esempio pratico:

Assegnare l'ID del poligono sovrapposto con maggiore area intersecata:

```
overlay_intersects(
           'Reg01012022_G_Wgs84',
           "cod_reg",
            sort_by_intersection_size:='des')[0] -- sort_by_intersection_size Nuovo parametro
```

[![](../../img/geometria/overlay_/overlay_intersects3.png)](../../img/geometria/overlay_/overlay_intersects3.png)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

---

## overlay_nearest

Restituisce se l'elemento corrente ha elementi da un layer target entro una data distanza o un array di risultati basati su espressioni per gli elementi nel layer di target entro una distanza dall'elemento corrente. Nota: questa funzione può essere lenta e consuma molta memoria per layer con molte feature.

Sintassi:

- overlay_nearest(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit=1</span>_][,_<span style="color:red;">max_distance</span>_][,_<span style="color:red;">cache</span>_])

NB: per **QGIS >= 3.22.x**, il parametro `filter` è dimanico, vedi [qui](https://github.com/qgis/QGIS/pull/45744).

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">max_distance</span>_ una distanza opzionale per limitare la ricerca di elementi corrispondenti. Se non impostato, verranno usati tutti gli elementi nel layer di destinazione, (misurata in maniera cartesiana nel sistema di riferimento dal layer sorgente)
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

Esempi:

```
overlay_nearest('airports') → true se il layer "airports" ha almeno un elemento
overlay_nearest('airports', max_distance:= 5000) → vero se è presente un aeroporto entro una distanza di 5000 unità dall'elemento corrente (misurata in maniera cartesiana nel sistema di riferimento dal layer sorgente)
overlay_nearest('airports', name) → il nome dell'aereoporto più vicino all'elemento corrente, come array
array_to_string(overlay_nearest('airports', name)) → il nome dell'aereoporto più vicino all'elemento corrente, come stringa
overlay_nearest(layer:='airports', expression:= name, max_distance:= 5000) → il nome dell'aereoporto più vicino entro una distanza di 5000 unità dall'elemento corrente, come array
overlay_nearest(layer:='airports', expression:="name", filter:= "Use"='Civilian', limit:=3) → un array di nomi, per un massimo di tre aeroeporti civili più vicini ordinati per distanza
overlay_nearest(layer:='airports', expression:="name", limit:= -1, max_distance:= 5000) → un array di nomi, per tutti gli aeroporti entro una distanza di 5000 unità dall'elemento corrente, ordinato per distanza.
```

[![](../../img/geometria/overlay_/overlay_nearest1.png)](../../img/geometria/overlay_/overlay_nearest1.png)

[Esempio 45](https://hfcqgis.opendatasicilia.it/esempi/linea_min_distanza2/)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

**Non documentato:**<br>
La funzione, usata su uno stesso layer, esclude i casi banali, ovvero: se dovessi ricercare il punto più vicino appartenente allo stesso layer. Chiaramente il punto più vicino appartenente allo stesso layer è il punto stesso, ma il codice è fatto in modo che in questo caso venga escluso il punto stesso (che sarebbe un risultato banale) e cerca il secondo punto più vicino nello stesso layer.

```
overlay_nearest(@layer_name, $geometry)
```

---

## overlay_touches

Restituisce se l'elemento corrente tocca spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target toccati dall'elemento corrente. Leggi ulteriori informazioni sul predicato GEOS "Touches", come descritto nella funzione PostGIS [ST_TOUCHES](https://postgis.net/docs/ST_Touches.html).

Sintassi:

- overlay_touches(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

Esempi:

```
overlay_touches('regions') → true se l'elemento corrente tocca spazialmente una regione
overlay_touches('regions', filter:= population > 10000) → vero se l'elemento corrente tocca spazialmente una regione con una popolazione maggiore di 10000
overlay_touches('regions', name) → un array di nomi, per le regioni tocacte dall'elemento corrente
string_to_array(overlay_touches('regions', name)) → una stringa come lista di nomi separati da virgole, per le regioni toccate dall'elemento corrente
overlay_touches('regions', name)[0] → una stringa con il nome della regione toccata dall'elemento corrente
array_sort(overlay_touches(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni toccate dall'elemento attuale e con una popolazione superiore a 10000
overlay_touches(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni toccate dall'elemento corrente
```

[![](../../img/geometria/overlay_/overlay_touches1.png)](../../img/geometria/overlay_/overlay_touches1.png)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

---

## overlay_within

Restituisce se l'elemento corrente è spazialmente all'interno di almeno un elemento da layer destinazione, o un array di risultati basati su espressione per gli elementi nel layer destinazione che contengono l'elemento corrente. Ulteriori informazioni sul sottostante predicato GEOS "Within", come descritto nella funzione PostGIS [ST_WITHIN](https://postgis.net/docs/ST_Within.html).

Sintassi:

- overlay_within(_<span style="color:red;">layer</span>_[,_<span style="color:red;">expression</span>_][,_<span style="color:red;">filter</span>_][,_<span style="color:red;">limit</span>_][,_<span style="color:red;">cache=false</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">layer</span>_ l'altro layer;
* _<span style="color:red;">expression</span>_ un'espressione opzionale per valutare gli elementi dell'altro layer (se non impostata, la funzione restituisce semplicemente un booleano che indica se c'è almeno una corrispondenza);
* _<span style="color:red;">filter</span>_ un'espressione opzionale per filtrare gli elementi corrispondenti (se non impostata, verranno restituiti tutti gli elementi);
* _<span style="color:red;">limit</span>_ un numero intero opzionale per limitare il numero di elementi corrispondenti (se non impostato, verranno restituiti tutti gli elementi);
* _<span style="color:red;">cache</span>_ imposta su "vero" per creare un indice spaziale locale (il più delle volte, questo è indesiderato, a meno che tu non stia lavorando con un fornitore di dati particolarmente lento);

[ ] indica componenti opzionali

Esempi:

```
overlay_within('regions') → true se l'elemento corrente è spazialmente all'interno di una regione
overlay_within('regions', filter:= population > 10000) → vero se l'elemento corrente è spazialmente all'interno di una regione con una popolazione maggiore di 10000
overlay_within('regions', name) → un array di nomi, per le regioni contenenti l'elemento corrente
array_to_string(overlay_within('regions', name)) → una stringa come lista di nomi separati da virgole, per le regioni che contengono l'elemento corrente
overlay_within('regions', name)[0] → una stringa con il nome della regione che contengono l'elemento corrente
array_sort(overlay_within(layer:='regions', expression:="name", filter:= population > 10000)) → un array ordinato di nomi, per le regioni contenenti l'elemento corrente e con una popolazione superiore a 10000
overlay_within(layer:='regions', expression:= geom_to_wkt($geometry), limit:=2) → un array di geometrie (in WKT), per un massimo di due regioni contenenti l'elemento corrente
```

[![](../../img/geometria/overlay_/overlay_within1.png)](../../img/geometria/overlay_/overlay_within1.png)

!!! Warning "Nota bene:" 
	**La funzione restituisce un output corretto anche se i due layer hanno EPSG differenti!**

---

## perimeter

Calcola il perimetro di un oggetto a geometria poligonale. I calcoli sono sempre planimetrici nel Sistema di Riferimento Spaziale (SR) di detta geometria, e l'unità di misura della lunghezza restituita è conforme all'unità di misura del SR. Ciò differisce dal calcolo eseguito dalla funzione [$perimeter](#perimeter), la quale esegue calcoli ellissoidali basati sull'ellissoide del progetto e sulle impostazioni delle unità di misura della distanza.

Sintassi:

- perimeter(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria poligono

Esempi:

```
perimeter(geom_from_wkt('POLYGON((0 0, 4 0, 4 2, 0 2, 0 0))')) → 12.0
```

[![](../../img/geometria/perimeter/perimeter1.png)](../../img/geometria/perimeter/perimeter1.png)

---

## point_n

Restituisce un nodo specifico da una geometria.

Sintassi:

- point_n(_<span style="color:red;">geometry</span>_, _<span style="color:red;">index</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria
* _<span style="color:red;">index</span>_ indice del nodo da restituire, dove 1 è il primo nodo; se il valore è negativo, l'indice del vertice selezionato sarà il suo conteggio totale meno il valore assoluto

Esempi:

```
geom_to_wkt(point_n(geom_from_wkt('POLYGON((0 0, 4 0, 4 2, 0 2, 0 0))'),2)) → 'Point (4 0)'
```

[![](../../img/geometria/point_n/point_n1.png)](../../img/geometria/point_n/point_n1.png)

--

[![](../../img/geometria/point_n/point_n2.png)](../../img/geometria/point_n/point_n2.png)

---

Esempi correlati:

[esempio nro 4](/esempi/add_col_z.md) - Come aggiungere la quota Z alla tabella attributi

---

## point_on_surface

Restituisce un punto garantendo che sia giacente sulla superficie della geometria.

Sintassi:

- point_on_surface(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
point_on_surface($geometry) → una geometria punto
```

[![](../../img/geometria/point_on_surface/point_on_surface1.png)](../../img/geometria/point_on_surface/point_on_surface1.png)

--

[![](../../img/geometria/point_on_surface/point_on_surface2.png)](../../img/geometria/point_on_surface/point_on_surface2.png)

---

## pole_of_inaccessibility

Calcola il polo dell'inaccessibilità approssimato per una superficie, che è il punto interno più distante dal contorno della superficie. Questa funzione usa l'algoritmo 'polylabel' (Vladimir Agafonkin, 2016), che è un approccio iterativo garantito per trovare il vero polo dell'inaccessibilità all'interno di una tolleranza specificata. Tolleranze più precise richiedono più iterazioni e sarà necessario più tempo per il calcolo.

Sintassi:

- pole_of_inaccessibility(_<span style="color:red;">geometry</span>_, _<span style="color:red;">tolerance</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">tolerance</span>_ distanza massima tra il punto restituito e la vera posizione del polo

Esempi:

```
geom_to_wkt(pole_of_inaccessibility( geom_from_wkt('POLYGON((0 1,0 9,3 10,3 3, 10 3, 10 1, 0 1))'), 0.1)) → 'Point(1.55, 1.55)'
```

[![](../../img/geometria/pole_of_inaccessibility/pole_of_inaccessibility1.png)](../../img/geometria/pole_of_inaccessibility/pole_of_inaccessibility1.png)

--

[![](../../img/geometria/pole_of_inaccessibility/pole_of_inaccessibility2.png)](../../img/geometria/pole_of_inaccessibility/pole_of_inaccessibility2.png)

---

## project

Restituisce un punto proiettato da un punto di partenza usando una distanza e una direzione di immersione (azimut) in radianti.

Sintassi:

- project(_<span style="color:red;">point</span>_, _<span style="color:red;">distance</span>_, _<span style="color:red;">azimuth</span>_[,_<span style="color:red;">elevation</span>_])

[ ] indica componenti opzionali

Argomenti:

* _<span style="color:red;">point</span>_ punto di partenza
* _<span style="color:red;">point</span>_ distanza da proiettare
* _<span style="color:red;">azimuth</span>_ azimuth in radianti in senso orario, dove 0 corrisponde a nord
* _<span style="color:red;">elevation</span>_ angolo di inclinazione in radianti

Esempi:

```
project(make_point(1, 2), 3, radians(270)) → Point(-2, 2)
```

[![](../../img/geometria/project/project1.png)](../../img/geometria/project/project1.png)

--

[![](../../img/geometria/project/project1.gif)](../../img/geometria/project/project1.gif)

---

## relate

Testa la rappresentazione Dimensional Extended 9 Intersection [Model (DE-9IM)](https://en.wikipedia.org/wiki/DE-9IM) della relazione tra due geometrie.

### Variabile di relazione

Restituisce la rappresentazione Dimensional Extended 9 Intersection Model (DE-9IM) della relazione tra due geometrie.

Sintassi:

* relate(_<span style="color:red;">geometry</span>_, _<span style="color:red;">geometry</span>_)
)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
relate( geom_from_wkt( 'LINESTRING(40 40,120 120)' ), geom_from_wkt( 'LINESTRING(40 40,60 120)' ) ) → 'FF1F00102'
```

[![](../../img/geometria/relate/relate1.png)](../../img/geometria/relate/relate1.png)

### Variabile di corrispondenza del modello

Testa se la relazione DE-9IM tra due geometrie corrisponde a un pattern specificato: restituisc true Vero, false Falso.

Sintassi:

- relate( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">geometry</span>_,  _<span style="color:red;">pattern</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">pattern</span>_ Tratteggio DE-9IM da far corrispondere

Esempi:

```
relate( geom_from_wkt( 'LINESTRING(40 40,120 120)' ), geom_from_wkt( 'LINESTRING(40 40,60 120)' ), '**1F001**' ) → Vero
```

[![](../../img/geometria/relate/relate2.png)](../../img/geometria/relate/relate2.png)

Link utili:

* [Wikipedia](https://en.wikipedia.org/wiki/DE-9IM)
* [OpenGeo](https://connect.boundlessgeo.com/docs/suite/4.6/dataadmin/pgAdvanced/de9im.html)

---

## reverse

Inverte il verso di una linestring invertendo l'ordine dei sui vertici.

Sintassi:

- reverse(_<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
geom_to_wkt(reverse(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2)'))) → 'LINESTRING(2 2, 1 1, 0 0)'
```

[![](../../img/geometria/reverse/reverse1.png)](../../img/geometria/reverse/reverse1.png)

--

[![](../../img/geometria/reverse/reverse2.png)](../../img/geometria/reverse/reverse2.png)

---

## rotate

Restituisce una versione ruotata di una geometria. I calcoli si trovano nel sistema di riferimento spaziale di questa geometria.

Sintassi:

- rotate( _<span style="color:red;">geometry</span>_, _<span style="color:red;">rotation</span>_[, _<span style="color:red;">center</span>_][,_<span style="color:red;">per_part=false</span>_])

[ ] indica componenti opzionali

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">rotation</span>_ rotazione oraria in gradi
*  _<span style="color:red;">center</span>_ punto centrale di rotazione. Se non specificato, viene utilizzato il centro del perimetro di delimitazione della geometria.
*  _<span style="color:red;">per_part</span>_ applica la rotazione per parte. Se true, la rotazione verrà applicata attorno al centro del riquadro di delimitazione di ciascuna parte quando la geometria di input è multiparte e non è specificato un punto centrale di rotazione esplicito.


Esempi:

```
rotate($geometry, 45, make_point(4, 5)) → la geometria ruotava di 45 gradi in senso orario attorno al punto (4, 5)
rotate($geometry, 45) → la geometria ruotava di 45 gradi in senso orario attorno al centro del riquadro di delimitazione
```

[![](../../img/geometria/rotate/rotate1.png)](../../img/geometria/rotate/rotate1.png)

[![screen](../../img/novita_312/Image03.png)](../../img/novita_312/Image03.png)

**>=QGIS 3.24**

[![](../../img/geometria/rotate/per_part.gif)](../../img/geometria/rotate/per_part.gif)

---

## roundness

Calcola quanto una forma di poligono è quasi un cerchio. La funzione restituisce 1 quando la forma del poligono è un cerchio perfetto e 0 quando è completamente piatta.

La definizione usata: `Roundness = (4 * pi * Area) / Perimeter^2`

Sintassi:

- roundness( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ un poligono

Esempi:

```
round(roundness(geom_from_wkt('POLYGON(( 0 0, 0 1, 1 1, 1 0, 0 0))')), 3) → 0.785
round(roundness(geom_from_wkt('POLYGON(( 0 0, 0 0.1, 1 0.1, 1 0, 0 0))')), 3) → 0.260
```

[![](../../img/geometria/roundness/img_01.png)](../../img/geometria/roundness/img_01.png)

---

## scale

Restituisce una versione scalata di una geometria. I calcoli sono nel sistema di riferimento spaziale di questa geometria.

Sintassi:

- scale( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">x_scale</span>_,  _<span style="color:red;">y_scale</span>_,  _[,<span style="color:red;">center</span>]_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria 
*  _<span style="color:red;">x_scale</span>_ Fattore di scala asse-x 
*  _<span style="color:red;">y_scale</span>_ Fattore di scala asse-y 
*  _<span style="color:red;">center</span>_ punto centrale della scalatura. Se non specificato, viene utilizzato il centro del rettangolo di delimitazione della geometria.

Esempi:

```
scale($geometry, 2, 0.5, make_point(4, 5)) → geometria scalata di due volte in orizzontale e dimezzata in verticale, intorno al punto (4, 5)
scale($geometry, 2, 0.5) → geometria scalata di due volte in orizzontale e dimezzata in verticale, intorno al centro del suo riquadro di delimitazione
```

[![](../../img/geometria/scale/img_01.png)](../../img/geometria/scale/img_01.png)

geometria scalata del 75% (in x e y) rispetto il centroide della stessa geometria di partenza:

```
scale($geometry,.75,.75, centroid($geometry))
```
[![](../../img/geometria/scale/img_02.png)](../../img/geometria/scale/img_02.png)

---

## segments_to_lines

Restituisce una geometria multi linea consistente in una linea per ogni segmento nella geometria in ingresso.

Sintassi:

- segments_to_lines( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ oggetto geometria

Esempi:

```
geom_to_wkt(segments_to_lines(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2)'))) → 'MultiLineString ((0 0, 1 1),(1 1, 2 2))'
```

[![](../../img/geometria/segments_to_lines/segments_to_lines1.png)](../../img/geometria/segments_to_lines/segments_to_lines1.png)

---

## shared_paths

Restituisce un insieme contenente i percorsi condivisi dalle due geometrie in ingresso. Quelli che vanno nella stessa direzione sono nel primo elemento della collezione, quelli che vanno nella direzione opposta sono nel secondo elemento. I percorsi di per se stessi sono dati nella direzione della prima geometria.

Sintassi:

- shared_paths( _<span style="color:red;">geometry1</span>_,_<span style="color:red;">geometry2</span>_)

Argomenti:

*  _<span style="color:red;">geometry1</span>_ una geometria di tipo LineString/MultiLineString
*  _<span style="color:red;">geometry2</span>_ una geometria di tipo LineString/MultiLineString

Esempi:

```
- geom_to_wkt(shared_paths(geom_from_wkt('MULTILINESTRING((26 125,26 200,126 200,126 125,26 125),(51 150,101 150,76 175,51 150)))'),geom_from_wkt('LINESTRING(151 100,126 156.25,126 125,90 161, 76 175)'))) → 'GeometryCollection (MultiLineString ((126 156.25, 126 125),(101 150, 90 161),(90 161, 76 175)),MultiLineString EMPTY)'
- geom_to_wkt(shared_paths(geom_from_wkt('LINESTRING(76 175,90 161,126 125,126 156.25,151 100)'),geom_from_wkt('MULTILINESTRING((26 125,26 200,126 200,126 125,26 125),(51 150,101 150,76 175,51 150))'))) → 'GeometryCollection (MultiLineString EMPTY,MultiLineString ((76 175, 90 161),(90 161, 101 150),(126 125, 126 156.25)))'
```

[![](../../img/geometria/shared_paths/shared_paths.png)](../../img/geometria/shared_paths/shared_paths.png)

---

## shortest_line

Restituisce la linea più corta che unisce la geometria 1 alla geometria 2. La linea risultante partirà dalla geometria 1 e finirà nella geometria 2.

Sintassi:

- shortest_line( _<span style="color:red;">geometry1</span>_,  _<span style="color:red;">geometry2</span>_)

Argomenti:

* _<span style="color:red;">geometry1</span>_ geometria _dalla_ quale cercare la linea più corta
* _<span style="color:red;">geometry2</span>_ geometria _verso_ la quale cercare la linea più corta

Esempi:

```
geom_to_wkt(shortest_line(geom_from_wkt('LINESTRING (20 80, 98 190, 110 180, 50 75 )'),geom_from_wkt('POINT(100 100)'))) → LineString(73.0769 115.384, 100 100)
```

[![](../../img/geometria/shortest_line/shortest_line1.png)](../../img/geometria/shortest_line/shortest_line1.png)

--

[![](../../img/geometria/shortest_line/shortest_line2.png)](../../img/geometria/shortest_line/shortest_line2.png)

[![shortestline](https://img.youtube.com/vi/m2AqZjMZVvQ/0.jpg)](https://www.youtube.com/watch?v=m2AqZjMZVvQ&list=PLqDFjeQq7NBjz5PWb66PNUqMgN1fce4cu "shortest_line")

---

## simplify

Semplifica una geometria rimuovendo nodi usando una soglia basata sulla distanza (cioè, l'algoritmo Douglas Peucker). L'algoritmo mantiene grandi deviazioni nelle geometrie e riduce il numero di vertici in segmenti quasi rettilinei.

Sintassi:

- simplify(simplify_vw(_<span style="color:red;">geometry</span>, <span style="color:red;">tolerance</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">tolerance</span>_ deviazione massima dai segmenti rettilinei per i punti da rimuovere

Esempi:

```
geom_to_wkt(simplify(geometry:=geom_from_wkt('LineString(0 0, 5 0.1, 10 0)'),tolerance:=5)) → 'LineString(0 0, 10 0)'
```

[![](../../img/geometria/simplify/simplify1.png)](../../img/geometria/simplify/simplify1.png)

---

## simplify_vw

Semplifica una geometria rimuovendo nodi usando una soglia basata sull'area (cioè, l'algoritmo Visvalingam-Whyatt ). L'algoritmo rimuove i vertici che creano piccole aree nelle geometrie, ad esempio picchi stretti o segmenti quasi rettilinei.

Sintassi:

- simplify_vw(_<span style="color:red;">geometry</span>, <span style="color:red;">tolerance</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">tolerance</span>_ una misura dell'area massima creata da un nodo per il nodo da rimuovere

Esempi:

```
geom_from_wkt('LineString(0 0, 5 0, 5.01 10, 5.02 0, 10 0)'),tolerance:=5)) → 'LineString(0 0, 10 0)'
```

[![](../../img/geometria/simplify_vw/simplify_vw1.png)](../../img/geometria/simplify_vw/simplify_vw1.png)

--

[![](../../img/geometria/simplify_vw/simplify_vw2.png)](../../img/geometria/simplify_vw/simplify_vw2.png)

---

## single_sided_buffer

Restituisce una geometria formata facendo un buffer solo da un lato di una geometria di tipo linestring. Le distanze sono espresse nel SR di tale geometria.

Sintassi:

- single_sided_buffer( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">distance</span>_[,  _<span style="color:red;">segments=8</span>_][,  _<span style="color:red;">join=1</span>_][,  _<span style="color:red;">miter_limit=2.0</span>_])

[ ] indica componenti opzionali

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria (multi)linestring
*  _<span style="color:red;">distance</span>_ distanza di buffer. Valori positivi saranno bufferizzati a sinistra delle linee, valori negativi a destra
*  _<span style="color:red;">segments</span>_ numero di segmenti da usare per rappresentare un quarto di cerchio quando è utilizzato uno stile di unione arrotondato. Un numero grande risulta in un buffer più morbido, con più nodi.
*  _<span style="color:red;">join</span>_ stile di unione per gli angoli, dove 1 = arrotondato, 2 = seghettato e 3 = smussato
*  _<span style="color:red;">miter_limit</span>_ limite sul rapporto di seghettatura usato per angoli molto appuntiti (solamente quando si usano le unioni seghettate)

Esempi:

```
single_sided_buffer($geometry, 10.5) → linea bufferizzata a sinistra di 10.5 unità
single_sided_buffer($geometry, -10.5) → linea bufferizzata a destra di 10.5 unità
single_sided_buffer($geometry, 10.5, segments:=16, join:=1) → linea bufferizzata a sinistra di 10.5 unità, usando più segmenti per risultare in un buffer più morbido
single_sided_buffer($geometry, 10.5, join:=3) → linea bufferizzata a sinistra di 10.5 unità, usando un'unione smussata
```

[![](../../img/geometria/single_sided_buffer/single_sided_buffer1.png)](../../img/geometria/single_sided_buffer/single_sided_buffer1.png)

--

[![](../../img/geometria/single_sided_buffer/single_sided_buffer2.png)](../../img/geometria/single_sided_buffer/single_sided_buffer2.png)

---

## sinuosity

Restituisce la sinuosità di una curva che è il rapporto tra la lunghezza della curva e la distanza diretta (2D) tra i suoi punti iniziali e finali.

Sintassi

- sinuosity(_<span style="color:red;">geometry</span>_)

Argomenti

- _<span style="color:red;">geometry</span>_ Curva in ingresso (circularstring, linestring)

Esempi

```
round(sinuosity(geom_from_wkt('LINESTRING(2 0, 2 2, 3 2, 3 3)')), 3) → 1.265
sinuosity(geom_from_wkt('LINESTRING( 3 1, 5 1)')) → 1.0
```
[![](../../img/geometria/sinuosity/sinuosity1.png)](../../img/geometria/sinuosity/sinuosity1.png)

---

## smooth

Smussa una geometria con l'aggiunta di ulteriori nodi che arrotondano gli angoli nella geometria.

Sintassi:

- smooth( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">iterations=1</span>_,  _<span style="color:red;">offset=0.25</span>_,  _<span style="color:red;">min_length=1</span>_,  _<span style="color:red;">max_angle=180</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">iterations</span>_ Numero di iterazioni di smussatura da applicare. Valori più alti fanno risultare geometria più morbide, ma più complesse.
*  _<span style="color:red;">offset</span>_ valore tra 0 e 0.5 che controlla quanto la geometria smussata segua strettamente la geometria originale. Valori più piccoli risultano in una lisciatura più stretta, valori più grandi risultano in una lisciatura più larga.
*  _<span style="color:red;">min_length</span>_ lunghezza minima dei segmenti ai quali applicare la smussatura. Questo parametro può essere usato per evitare di posizionare nodi aggiuntivi eccessivi nei segmenti più corti della geometria.
*  _<span style="color:red;">max_angle</span>_ angolo massimo (0-180) da applicare al nodo per la smussatura. Abbassando intenzionalmente l'angolo massimo si abbassa l'arrotondamento sugli angoli della geometria. Per esempio, un valore di 80 gradi preserverà l'angolo nella geometria.

Esempi:

```
geom_to_wkt(smooth(geometry:=geom_from_wkt('LineString(0 0, 5 0, 5 5)'),iterations:=1,offset:=0.2,min_length:=-1,max_angle:=180)) → 'LineString (0 0, 4 0, 5 1, 5 5)'
```

[![](../../img/geometria/smooth/smooth1.png)](../../img/geometria/smooth/smooth1.png)

---

## square_wave

Costruisce onde quadrate/rettangolari lungo il confine di una geometria.

Sintassi:

- square_wave( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">wavelength</span>_,  _<span style="color:red;">amplitude</span>_,  _[,<span style="color:red;">strict</span>]_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria 
* _<span style="color:red;">wavelength</span>_ lunghezza d'onda di un'onda di forma quadra 
* _<span style="color:red;">amplitude</span>_ ampiezza di un'onda di forma triangolare 
* _<span style="color:red;">strict</span>_ Per valore predefinito l'argomento lunghezza d'onda è trattato come una "lunghezza d'onda massima", dove la lunghezza d'onda effettiva sarà regolata dinamicamente in modo che un numero esatto di onde quadrate sia creato lungo i confini della geometria. Se l'argomento strict è impostato a true allora la lunghezza d'onda sarà usata esattamente e una forma incompleta potrebbe essere usata per la forma d'onda finale.

Esempi:

```
square_wave(geom_from_wkt('LineString(0 0, 10 0)'), 3, 1) → Onde quadrate con lunghezza d'onda 3 e ampiezza 1 lungo la linea
```

[![](../../img/geometria/wave/square_wave_01.png)](../../img/geometria/wave/square_wave_01.png)

[![](../../img/geometria/wave/square_wave_02.png)](../../img/geometria/wave/square_wave_02.png)

---

## square_wave_randomized

Costruisce onde quadrate/rettangolari casuali lungo il confine di una geometria.

Sintassi:

- square_wave_randomized( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">min_wavelength</span>_,  _<span style="color:red;">max_wavelength</span>_,  _<span style="color:red;">min_amplitude</span>_,  _<span style="color:red;">max_amplitude</span>_  _[,<span style="color:red;">seed=0</span>]_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria 
* _<span style="color:red;">min_wavelength</span>_  lunghezza d'onda minima delle onde
* _<span style="color:red;">max_wavelength</span>_ lunghezza d'onda massima delle onde 
* _<span style="color:red;">min_amplitude</span>_ ampiezza minima delle onde 
* _<span style="color:red;">max_amplitude</span>_ ampiezza massima delle onde
* _<span style="color:red;">seed</span>_ specifica un seme casuale per la generazione delle onde. Se il seme è 0, allora verrà generato un insieme completamente casuale di onde.


Esempi:

```
square_wave_randomized(geom_from_wkt('LineString(0 0, 10 0)'), 2, 3, 0.1, 0.2) → Onde quadrate di dimensioni casuali con lunghezze d'onda tra 2 e 3 e ampiezze tra 0,1 e 0,2 lungo la linea
```

[![](../../img/geometria/wave/square_wave_randomized_01.png)](../../img/geometria/wave/square_wave_randomized_01.png)

[![](../../img/geometria/wave/square_wave_randomized_02.png)](../../img/geometria/wave/square_wave_randomized_02.png)

---

## start_point

Restituisce il primo nodo di una geometria.

Sintassi:

- start_point( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ oggetto geometria

Esempi:

```
geom_to_wkt(start_point(geom_from_wkt('LINESTRING(4 0, 4 2, 0 2)'))) → 'Point (4 0)'
```

[![](../../img/geometria/start_point/start_point1.png)](../../img/geometria/start_point/start_point1.png)

Start_point di geometria poligonale:

[![](../../img/geometria/start_point/start_point2.png)](../../img/geometria/start_point/start_point2.png)

Start_point di geometria lineare:

[![](../../img/geometria/end_point/end_point3.png)](../../img/geometria/end_point/end_point3.png)

---

## straight_distance_2d

Restituisce la distanza diretta/euclidea tra il primo e l'ultimo vertice di una geometria. La geometria deve essere una curva (circularstring, linestring).

Sintassi

- straight_distance_2d(_<span style="color:red;">geometry</span>_)

Argomenti

- _<span style="color:red;">geometry</span>_ una geometria (circularstring, linestring)

Esempi

```
straight_distance_2d(geom_from_wkt('LINESTRING(1 0, 1 1)')) → 1
round(straight_distance_2d(geom_from_wkt('LINESTRING(1 4, 3 5, 5 0)')), 3) → 5.657
```

[![](../../img/geometria/straight_distance_2d/straight_distance_2d1.png)](../../img/geometria/straight_distance_2d/straight_distance_2d1.png)

---
## sym_difference

Restituisce una geometria che rappresenta la porzione di due geometrie che non si interseca.

Sintassi:

- sym_difference( _<span style="color:red;">geometry1</span>_,  _<span style="color:red;">geometry2</span>_)

Argomenti:

*  _<span style="color:red;">geometry1</span>_ una geometria
*  _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
geom_to_wkt( sym_difference( geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ), geom_from_wkt( 'LINESTRING(3 3, 8 8)' ) ) ) → LINESTRING(5 5, 8 8)
```

[![](../../img/geometria/sym_difference/sym_difference1.png)](../../img/geometria/sym_difference/sym_difference1.png)

[![](../../img/geometria/sym_difference/sym_difference3.png)](../../img/geometria/sym_difference/sym_difference3.png)

!!! Tip "Espressione"
```
	-- differenza simmetrica tra le due linee
	sym_difference( 
	make_line(  -- linea a
		start_point(geometry(get_feature_by_id('linea_a',0))), 
		start_point($geometry),
		end_point(geometry(get_feature_by_id('linea_a',0)))),
	make_line(  -- linea b
		start_point($geometry), 
		end_point(geometry(get_feature_by_id('linea_a',0))),
		end_point($geometry))
					)
	-- NB: -- l' ordine delle geometrie è indifferente
```

!!! Question "Prova tu"
	[Dati e progetto qgz](https://github.com/gbvitrano/HfcQGIS/raw/master/prova_tu/DIFFERENCE.zip)

--

[![](../../img/geometria/sym_difference/sym_difference2.png)](../../img/geometria/sym_difference/sym_difference2.png)

---

## tapered_buffer

Crea un buffer lungo una geometria della linea in cui il diametro del buffer varia in modo uniforme sulla lunghezza della linea.

Sintassi:

- tapered_buffer( _<span style="color:red;">geometry</span>_, _<span style="color:red;">start_width</span>_, _<span style="color:red;">end_width</span>_[,_<span style="color:red;">segments=8</span>_]_)

[ ] contrassegna componenti opzionali

Argomenti:

*  _<span style="color:red;">geometry</span>_ input geometry. Deve essere una (multi) geometria della linea.
*  _<span style="color:red;">start_width</span>_ larghezza del buffer all'inizio della linea,
*  _<span style="color:red;">end_width</span>_ larghezza del buffer alla fine della riga.
*  _<span style="color:red;">segments</span>_ numero di segmenti per approssimare le curve del quarto di cerchio nel buffer

Esempi:

```
tapered_buffer(geometry:=geom_from_wkt('LINESTRING(1 2, 4 2)'),start_width:=1,end_width:=2,segments:=8) → Un buffer rastremato che inizia con un diametro di 1 e termina con un diametro di 2 lungo la geometria della linea.
```

[![](../../img/geometria/tapered_buffer/tapered_buffer1.png)](../../img/geometria/tapered_buffer/tapered_buffer1.png)

--

[![](../../img/geometria/tapered_buffer/tapered_buffer2.png)](../../img/geometria/tapered_buffer/tapered_buffer2.png)


[QGIS - feature](https://github.com/qgis/QGIS/pull/6882)

---

## touches

Verifica se una geometria tocca un'altra. Restituisce vero (1) se le geometrie hanno almeno un punto in comune, ma i loro interni non si intersecano.

Sintassi:

- touches( _<span style="color:red;">geometry1</span>_,  _<span style="color:red;">geometry2</span>_)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
touches( geom_from_wkt( 'LINESTRING(5 3, 4 4)' ), geom_from_wkt( 'LINESTRING(3 3, 4 4, 5 5)' ) ) → 1
touches( geom_from_wkt( 'POINT(4 4)' ), geom_from_wkt( 'POINT(5 5)' ) ) → 0
```

[![](../../img/geometria/touches/touches1.png)](../../img/geometria/touches/touches1.png)

Nota bene:

--

Osservazioni:
	
Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (Ctrl+F3):

```
touches(geometry(get_feature( 'province_rt_rt','pk_uid','46')),$geometry)
```

dove:

* _geometry1_ è `geometry(get_feature( 'province_rt_rt','pk_uid','52'))`
* _geometry2_ è `$geometry`


[![](../../img/geometria/touches/touches2.png)](../../img/geometria/touches/touches2.png)

seleziono tutti i comuni `touches` (toccati) dalla provincia con `pk_uid`46 (Siena)

PS:** potrei anche negare (`NOT`) l'espressione per selezionare il complementare (tutti i comuni tranne quelli toccati dalla provincia di Siena).

`NOT touches(geometry(get_feature( 'province_rt_rt','pk_uid','52')),$geometry)`

[![](../../img/geometria/touches/touches3.png)](../../img/geometria/touches/touches3.png)

---

## transform

Restituisce la geometria trasformata da un SR sorgente ad un SR di destinazione.

Sintassi:

- transform( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">source_auth_id</span>_,  _<span style="color:red;">dest_auth_id</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">source_auth_id</span>_ ID del SR sorgente
*  _<span style="color:red;">dest_auth_id</span>_ ID del SR destinazione

Esempi:

```
geom_to_wkt( transform( $geometry, 'EPSG:2154', 'EPSG:4326' ) ) → POINT(0 51)
```

[![](../../img/geometria/transform/transform1.png)](../../img/geometria/transform/transform1.png)

--

[![](../../img/geometria/transform/transform2.png)](../../img/geometria/transform/transform2.png)

---

## translate

Restituisce una versione traslata di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- translate( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">dx</span>_,  _<span style="color:red;">dy</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria
* _<span style="color:red;">dx</span>_ delta x
* _<span style="color:red;">geomdyetry</span>_ delta y

Esempi:

```
translate($geometry, 5, 10) → una geometria dello stesso tipo come l'originale
```

[![](../../img/geometria/translate/translate1.png)](../../img/geometria/translate/translate1.png)

--

[![](../../img/geometria/translate/translate2.png)](../../img/geometria/translate/translate2.png)

---

## triangular_wave

Costruisce onde triangolari lungo il confine di una geometria.

Sintassi:

- triangular_wave( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">wavelength</span>_,  _<span style="color:red;">amplitude</span>_,  _[,<span style="color:red;">strict</span>]_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria 
* _<span style="color:red;">wavelength</span>_ lunghezza d'onda di un'onda di forma triangolare 
* _<span style="color:red;">amplitude</span>_ ampiezza di un'onda di forma triangolare 
* _<span style="color:red;">strict</span>_ Costruisce onde triangolari lungo i confini di una geometria. Per default l'argomento lunghezza d'onda è trattato come una "lunghezza d'onda massima", dove la lunghezza d'onda effettiva sarà regolata dinamicamente in modo da creare un numero esatto di onde triangolari lungo i confini della geometria. Se l'argomento strict è impostato a true, allora la lunghezza d'onda sarà usata esattamente e una forma incompleta potrebbe essere usato per la forma d'onda finale.

Esempi:

```
triangular_wave(geom_from_wkt('LineString(0 0, 10 0)'), 3, 1) → Onde triangolari con lunghezza d'onda 3 e ampiezza 1 lungo la linea
```

[![](../../img/geometria/wave/triangular_wave_01.png)](../../img/geometria/wave/triangular_wave_01.png)

[![](../../img/geometria/wave/triangular_wave_02.png)](../../img/geometria/wave/triangular_wave_02.png)

---

## triangular_wave_randomized

Costruisce onde triangolari casuali lungo il confine di una geometria.

Sintassi:

- triangular_wave_randomized( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">min_wavelength</span>_,  _<span style="color:red;">max_wavelength</span>_,  _<span style="color:red;">min_amplitude</span>_,  _<span style="color:red;">max_amplitude</span>_  _[,<span style="color:red;">seed=0</span>]_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria 
* _<span style="color:red;">min_wavelength</span>_  lunghezza d'onda minima delle onde
* _<span style="color:red;">max_wavelength</span>_ lunghezza d'onda massima delle onde 
* _<span style="color:red;">min_amplitude</span>_ ampiezza minima delle onde 
* _<span style="color:red;">max_amplitude</span>_ ampiezza massima delle onde
* _<span style="color:red;">seed</span>_ specifica un seme casuale per la generazione delle onde. Se il seme è 0, allora verrà generato un insieme completamente casuale di onde.


Esempi:

```
triangular_wave_randomized(geom_from_wkt('LineString(0 0, 10 0)'), 2, 3, 0.1, 0.2) → Onde triangolari di dimensioni casuali con lunghezze d'onda tra 2 e 3 e ampiezze tra 0,1 e 0,2 lungo la linea
```

[![](../../img/geometria/wave/triangular_wave_randomized_01.png)](../../img/geometria/wave/triangular_wave_randomized_01.png)

[![](../../img/geometria/wave/triangular_wave_randomized_02.png)](../../img/geometria/wave/triangular_wave_randomized_02.png)

---

## union

Restituisce una geometria che rappresenta l'insieme dei punti dell'unione delle geometrie.

Sintassi:

- union( _<span style="color:red;">geometry1</span>_,  _<span style="color:red;">geometry2</span>_)

Argomenti:

*  _<span style="color:red;">geometry1</span>_ una geometria
*  _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
geom_to_wkt( union( geom_from_wkt( 'POINT(4 4)' ), geom_from_wkt( 'POINT(5 5)' ) ) ) → MULTIPOINT(4 4, 5 5)
```

[![](../../img/geometria/union/union1.png)](../../img/geometria/union/union1.png)

[![](../../img/geometria/union/union3.png)](../../img/geometria/union/union3.png)

!!! Tip "Espressione"
```
	-- unione delle due linee
	union( 
	make_line(  -- linea a
		start_point(geometry(get_feature_by_id('linea_a',0))), 
		start_point($geometry),
		end_point(geometry(get_feature_by_id('linea_a',0)))),
	make_line(  -- linea b
		start_point($geometry), 
		end_point(geometry(get_feature_by_id('linea_a',0))),
		end_point($geometry))
					)
	-- NB: -- l' ordine delle geometrie è indifferente
```

!!! Question "Prova tu"
	[Dati e progetto qgz](https://github.com/gbvitrano/HfcQGIS/raw/master/prova_tu/DIFFERENCE.zip)

--

[![](../../img/geometria/union/union2.png)](../../img/geometria/union/union2.png)

---

## wave

Costruisce onde arrotondate (sinusoidali) lungo il confine di una geometria.

Sintassi:

- wave( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">wavelength</span>_,  _<span style="color:red;">amplitude</span>_,  _[,<span style="color:red;">strict</span>]_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria 
* _<span style="color:red;">wavelength</span>_ lunghezza d'onda di un'onda di forma sinusoidale 
* _<span style="color:red;">amplitude</span>_ ampiezza di un'onda di forma sinusoidale 
* _<span style="color:red;">strict</span>_ Per valore predefinito l'argomento lunghezza d'onda è trattato come una "lunghezza d'onda massima", dove la lunghezza d'onda effettiva sarà regolata dinamicamente in modo che un numero esatto di onde quadrate sia creato lungo i confini della geometria. Se l'argomento strict è impostato a true allora la lunghezza d'onda sarà usata esattamente e una forma incompleta potrebbe essere usata per la forma d'onda finale.

Esempi:

```
wave(geom_from_wkt('LineString(0 0, 10 0)'), 3, 1) → Onde sinusoidali con lunghezza d'onda 3 e ampiezza 1 lungo la linea
```

[![](../../img/geometria/wave/wave_01.png)](../../img/geometria/wave/wave_01.png)

[![](../../img/geometria/wave/wave_02.png)](../../img/geometria/wave/wave_02.png)

---

## wave_randomized

Costruisce onde curve casuali (sinusoidali) lungo il confine di una geometria.

Sintassi:

- wave_randomized( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">min_wavelength</span>_,  _<span style="color:red;">max_wavelength</span>_,  _<span style="color:red;">min_amplitude</span>_,  _<span style="color:red;">max_amplitude</span>_  _[,<span style="color:red;">seed=0</span>]_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria 
* _<span style="color:red;">min_wavelength</span>_  lunghezza d'onda minima delle onde
* _<span style="color:red;">max_wavelength</span>_ lunghezza d'onda massima delle onde 
* _<span style="color:red;">min_amplitude</span>_ ampiezza minima delle onde 
* _<span style="color:red;">max_amplitude</span>_ ampiezza massima delle onde
* _<span style="color:red;">seed</span>_ specifica un seme casuale per la generazione delle onde. Se il seme è 0, allora verrà generato un insieme completamente casuale di onde.


Esempi:

```
wave_randomized(geom_from_wkt('LineString(0 0, 10 0)'), 2, 3, 0.1, 0.2) → Onde curve di dimensioni casuali con lunghezze d'onda tra 2 e 3 e ampiezze tra 0,1 e 0,2 lungo la stringa
```

[![](../../img/geometria/wave/wave_randomized_01.png)](../../img/geometria/wave/wave_randomized_01.png)

[![](../../img/geometria/wave/wave_randomized_02.png)](../../img/geometria/wave/wave_randomized_02.png)

---

## wedge_buffer

Restituisce un buffer a forma di cuneo che origina da una geometria del punto.

Sintassi:

- wedge_buffer( _<span style="color:red;">geometry</span>_, _<span style="color:red;">azimuth</span>_, _<span style="color:red;">width</span>_, _<span style="color:red;">outer_radius</span>_[,_<span style="color:red;">inner_radius=0.0</span>_])

[ ] contrassegna componenti opzionali

Argomenti:

*  _<span style="color:red;">geometry</span>_ punto centrale (origine) del buffer. Deve essere una geometria puntuale.
*  _<span style="color:red;">azimuth</span>_  (in gradi) per il centro del cuneo da puntare.
*  _<span style="color:red;">width</span>_ buffer w larghezza (in gradi). Si noti che il cuneo si estenderà fino a metà della larghezza angolare su entrambi i lati della direzione dell'azimut.
*  _<span style="color:red;">outer_radius</span>_ raggio esterno per i buffers
*  _<span style="color:red;">inner_radius</span>_ raggio interno opzionale per i buffers

Esempi:

```
wedge_buffer(center:=geom_from_wkt('POINT(1 2)'),azimuth:=90,width:=180,outer_radius:=1) → Un buffer a forma di cuneo centrato sul punto (1,2), rivolto verso est, con una larghezza di 180 gradi e raggio esterno di 1.
```

[![](../../img/geometria/wedge_buffer/wedge_buffer1.png)](../../img/geometria/wedge_buffer/wedge_buffer1.png)

--

[![](../../img/geometria/wedge_buffer/wedge_buffer2.png)](../../img/geometria/wedge_buffer/wedge_buffer2.png)

---

## within

Controlla qualora una geometria sia interna ad un'altra. Restituisce  1 (vero) se la _geometria1_ è completamente contenuta nella_ geometria2_.

Sintassi:

- within( _<span style="color:red;">geometry1</span>_,  _<span style="color:red;">geometry2</span>_)

Argomenti:

* _<span style="color:red;">geometry1</span>_ una geometria
* _<span style="color:red;">geometry2</span>_ una geometria

Esempi:

```
within( geom_from_wkt( 'POINT( 0.5 0.5)' ), geom_from_wkt( 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))' ) ) → 1
within( geom_from_wkt( 'POINT( 5 5 )' ), geom_from_wkt( 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0 ))' ) ) → 0
```

[![](../../img/geometria/within/within1.png)](../../img/geometria/within/within1.png)

Osservazioni:

	Usando algoritmo `Seleziona per espressione` presente in strumenti di processing oppure ![icona](https://docs.qgis.org/2.18/en/_images/mIconExpressionSelect.png) (Ctrl+F3):
```
	- within($geometry,geometry(get_feature( 'province_rt_rt','pk_uid','53')))
```
dove:

* _geometry1_ è `$geometry`
* _geometry2_ è `geometry(get_feature( 'province_rt_rt','pk_uid','53'))`


[![](../../img/geometria/within/within3.png)](../../img/geometria/within/within3.png)

seleziono tutti i comuni `within` (contenuti) nella provincia con `pk_uid`53 (Grosseto)

PS:** potrei anche negare (`NOT`) l'espressione per selezionare il complementare (tutti i comuni tranne quelli contenuti nella provincia di Grosseto).

`NOT within($geometry,geometry(get_feature( 'province_rt_rt','pk_uid','53')))`

Altro esempio con condizione sulle etichette

!!! Tip "Espressione"
```
	CASE WHEN within( $geometry,
	geometry(get_feature('poligono','id',1))) = 1
	THEN 'INTERNO'
	ELSE 'NON INTERNO'
	END
```

[![](../../img/geometria/within/within2.png)](../../img/geometria/within/within2.png)

---

## x

Restituisce la minima coordinata x di una geometria punto, o la coordinata x del centroide di una geometria non puntuale.

Sintassi:

- x( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
x( geom_from_wkt( 'POINT(2 5)' ) ) → 2
x( $geometry ) → coordinata x del centroide dell'elemento corrente
```

[![](../../img/geometria/x/x1.png)](../../img/geometria/x/x1.png)

--

[![](../../img/geometria/x/x2.png)](../../img/geometria/x/x2.png)

---

## x_max

Restituisce la coordinata x massima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- x_max( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
x_max( geom_from_wkt( 'LINESTRING(2 5, 3 6, 4 8)') ) → 4
```

[![](../../img/geometria/x_max/x_max1.png)](../../img/geometria/x_max/x_max1.png)

--

[![](../../img/geometria/x_max/x_max2.png)](../../img/geometria/x_max/x_max2.png)

---

## x_min

Restituisce la coordinata x minima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- x_min( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
x_min( geom_from_wkt( 'LINESTRING(2 5, 3 6, 4 8)') ) → 2
```

[![](../../img/geometria/x_min/x_min1.png)](../../img/geometria/x_min/x_min1.png)

--

[![](../../img/geometria/x_min/x_min2.png)](../../img/geometria/x_min/x_min2.png)

---

## y

Restituisce la coordinata y minima di una geometria puntuale, o la coordinata y del centroide di una geometria non puntuale.

Sintassi:

- y( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
y( geom_from_wkt( 'POINT(2 5)' ) ) → 5
y( $geometry ) → coordinata y del centroide dell'elemento corrente
```

[![](../../img/geometria/y/y1.png)](../../img/geometria/y/y1.png)

--

[![](../../img/geometria/y/y2.png)](../../img/geometria/y/y2.png)

---

## y_max

Restituisce la coordinata y massima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- y_max( _<span style="color:red;">geometry</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
y_max( geom_from_wkt( 'LINESTRING(2 5, 3 6, 4 8)') ) → 8
```

[![](../../img/geometria/y_max/y_max1.png)](../../img/geometria/y_max/y_max1.png)

--

[![](../../img/geometria/y_max/y_max2.png)](../../img/geometria/y_max/y_max2.png)

---

## y_min

Restituisce la coordinata y minima di una geometria. I calcoli sono effettuati nel sistema di riferimento spaziale di tale geometria.

Sintassi:

- y_min( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria

Esempi:

```
y_min( geom_from_wkt( 'LINESTRING(2 5, 3 6, 4 8)') ) → 5
```

[![](../../img/geometria/y_min/y_min1.png)](../../img/geometria/y_min/y_min1.png)

--

[![](../../img/geometria/y_min/y_min2.png)](../../img/geometria/y_min/y_min2.png)

---

## z

Restituisce la coordinata z di una geometria puntuale.

Sintassi:

- z( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria punto

Esempi:

```
z( geom_from_wkt( 'POINTZ(2 5 7)' ) ) → 7
```

[![](../../img/geometria/z/z1.png)](../../img/geometria/z/z1.png)

## z_at

(>= QGIS 3.30)

Recupera una coordinata z della geometria, o un NULL se la geometria non ha valore z.

Sintassi:

- z_at(_<span style="color:red;">geometry</span>_,_<span style="color:red;">vertex</span>_)

Argomenti:

* _<span style="color:red;">geometry</span>_ oggetto geometria
* _<span style="color:red;">vertex</span>_ indice del vertice della geometria (gli indici partono da 0; i valori negativi si applicano a partire dall'ultimo indice, a partire da -1)

Esempi:

```
z_at(geom_from_wkt('LineStringZ(0 0 0, 10 10 5, 10 10 0)'), 1) → 5
```

[![](../../img/geometria/z_at/z_at330.png)](../../img/geometria/z_at/z_at330.png)

---

## $z

Restituisce il valore z del punto corrente se è 3D. Se la feature è una feature multipunto, verrà restituito il valore z del primo punto.

Sintassi

- $z

Esempi

```
$z → 123
```

[![](../../img/geometria/_z/z1.png)](../../img/geometria/_z/z1.png)

---

## z_max

Restituisce la coordinata z massima di una geometria.

Sintassi:

* z_max( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria con z coordinata

Esempi:

```
z_max( geom_from_wkt( 'POINT ( 0 0 1 )' ) ) → 1
z_max( geom_from_wkt( 'MULTIPOINT ( 0 0 1 , 1 1 3 )' ) ) → 3
z_max( make_line( make_point( 0,0,0 ), make_point( -1,-1,-2 ) ) ) → 0
z_max( geom_from_wkt( 'LINESTRING( 0 0 0, 1 0 2, 1 1 -1 )' ) ) → 2
z_max( geom_from_wkt( 'POINT ( 0 0 )' ) ) → NULL
```

[![](../../img/geometria/z_max/z_max1.png)](../../img/geometria/z_max/z_max1.png)

---

## z_min

Restituisce la coordinata z minima di una geometria.

Sintassi:

* z_min( _<span style="color:red;">geometry</span>_)

Argomenti:

*  _<span style="color:red;">geometry</span>_ una geometria con z coordinata

Esempi:

```
z_min( geom_from_wkt( 'POINT ( 0 0 1 )' ) ) → 1
z_min( geom_from_wkt( 'MULTIPOINT ( 0 0 1 , 1 1 3 )' ) ) → 1
z_min( make_line( make_point( 0,0,0 ), make_point( -1,-1,-2 ) ) ) → -2
z_min( geom_from_wkt( 'LINESTRING( 0 0 0, 1 0 2, 1 1 -1 )' ) ) → -1
z_min( geom_from_wkt( 'POINT ( 0 0 )' ) ) → NULL
```

[![](../../img/geometria/z_min/z_min1.png)](../../img/geometria/z_min/z_min1.png)

---
