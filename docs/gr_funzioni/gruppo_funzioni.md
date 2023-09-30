# Gruppi funzioni

Nell'Interfaccia del **Field Calc** (e nel costruttore di espressione) è presente, nella parte centrale, una sezione che raccoglie i Gruppi delle Funzioni elencate sotto:

Gruppo funzioni|nro funzioni*|Descrizione   | info
---------------|:-----------:|--------------|-----
[**Aggrega**](./aggrega/aggrega_unico.md) |(23/23)|Contiene funzioni che aggregano valori nei livelli e campi.| aggiornate a<br> **QGIS 3.0**
[**Array**](./array/array_unico.md)| (36/36) |Questo gruppo contiene funzioni espressione per la creazione e la manipolazione di array (noti anche come strutture dati ad elenco). L'ordine dei valori all'interno dell'array è importante, al contrario della struttura dati 'a mappa', in cui l'ordine delle coppie chiave-valore è irrilevante e i valori vengono identificati dalle loro chiavi.|aggiornate a<br> **QGIS 3.28**
[**Campi e valori**](./campi_e_valori/campi_e_valori_unico.md)| (1/1)|Contiene un elenco di campi del layer. Si possono ottenere valori campione con il click del tasto destro del mouse. Seleziona il nome del campo dall'elenco e fai click con il tasto destro per aprire il menù con le opzioni per caricare un campione di valori dal campo selezionato. | Elenco dei campi del layer selezionato <br> **QGIS 3.28**
[**Colore**](./colore/colore_unico.md)| (17/17)|Questo gruppo contiene funzioni per manipolare i colori| Per manipolare i colori
[**Condizioni**](./condizioni/condizioni_unico.md)| (6/6)|Questo gruppo contiene funzioni per gestire controlli condizionali nelle espressioni.|aggiornate a<br> **QGIS 3.6**
[**Conversioni**](./conversioni/conversioni_unico.md)| (15/15)|Questo gruppo contiene funzioni per convertire i dati da un tipo ad un altro, es. da stringa a intero, da intero a stringa.|aggiornate a<br> **QGIS 3.16**
[**Corrispondenza Fuzzy**](./corrispondenza_fuzzy/corrispondenza_fuzzy_unico.md)| (4/4)| Questo gruppo contiene funzioni per confronti fuzzy fra valori.|funzioni per confronti fuzzy fra valori
[**Custom**](./custom/custom_unico.md)| (16/16)| Questo gruppo contiene funzioni Python create in modo personalizzato dall'utente.|funzioni personalizzate
[**Data ora**](./data_ora/data_ora_unico.md) |(21/21)|Questo gruppo contiene funzioni per gestire dati con date e ore.|aggiornate a<br> **QGIS 3.14**
[**Espressioni utente**](./espressione_utente/espressione_utente_unico.md)| (?)|Questo gruppo contiene espressioni memorizzate nel profilo utente.|aggiornate a<br> **QGIS 3.12**
[**File e percorsi**](./file_e_percorsi/file_e_percorsi_unico.md)| (9/9)|Contiene funzioni che manipolano nomi di file e di percorsi. manipolano nomi di file e di percorsi | aggiornate a<br> **QGIS 3.22**
[**Form**](./form/form_unico.md)| (0/2)|Questo gruppo contiene funzioni che sono disponibili nel contesto modulo attributi. Per esempio, in impostazioni campo widget. Gruppo visibile solo nei widget. | aggiornate a<br> **QGIS 3.14**
[**Generale**](./generale/generale_unico.md)| (7/7)|Questo gruppo contiene funzioni generali assortite.| assortimento di funzioni generiche
[**Geometria**](./geometria/geometria_unico.md) |(151/151)|Questo gruppo contiene funzioni che operano sugli oggetti geometrici es. lunghezza, area.| aggiornate a<br> **QGIS 3.34**
[**Layer mappa**](./layer_mappa/layer_mappa_unico.md)| (3/3)|Contiene due funzioni e la lista dei layer della mappa che sono disponibili nel progetto corrente con possibilità di leggere[^1] i nomi e valori degli attributi.| aggiornate a<br> **QGIS 3.30**
[**Layout**](./layout/layout_unico.md)| (2/2)|  Visibile solo nel layout di stampa
[**Maps**](./maps/maps_unico.md)| (14/14) |Questo gruppo contiene funzioni per la creazione e la manipolazione di strutture di dati 'a mappa' (noti anche come oggetti dizionario, coppie chiave-valore o array associative). Si possono assegnare valori a determinate chiavi. L'ordine delle coppie chiave-valore nell'oggetto mappa non è rilevante.|>= **QGIS 3.0** aggiornate a<br> **QGIS 3.24**
[**Matematica**](./matematica/matematica_unico.md)| (28/28)|Questo gruppo contiene funzioni matematiche es. radice quadrata, seno e coseno|aggiornate a<br> **QGIS 3.12**
[**Operatori**](./operatori/operatori_unico.md)| (23/23)|Questo gruppo contiene operatori es. + - *|aggiornate a<br> **QGIS 3.20**
[**Raster**](./rasters/rasters_unico.md)|(2/2)|Contiene funzioni che calcolano statistiche e valori raster.|>= **QGIS 3.4** 
[**Recente**](./recente/recente.md) |(1/1)| Elenca le ultime 20 espressioni utilizzate
[**Record e attributi**](./record_e_attributi/record_e_attributi_unico.md)| (17/17)|Questo gruppo contiene funzioni che operano sugli identificativi dei record.|aggiornate a<br> **QGIS 3.30**
[**Sensors**]()|Questo gruppo contiene le funzioni per interagire con i sensori| a<br> **QGIS 3.30**
[**Relazioni**](./relazioni/relazioni_unico.md)| (?)| Visibile solo se ci sono relazioni di progetto
[**Stringhe di testo**](./stringhe_di_testo/stringhe_di_testo_unico.md)|(25/25)| Questo gruppo contiene le funzioni che operano sulle stringhe es. sostituzione, conversione in maiuscolo.|aggiornate a<br> **QGIS 3.32**
[**Variabili**](./variabili/variabili.md) |(4/65+) |Questo gruppo contiene variabili dinamiche che possono essere inserite nelle tue espressioni.|>= **QGIS 2.12** - variano in funzione del contesto

![](../img/gruppi_funzioni.png)

conteggio: <https://gist.github.com/pigreco/2b2ad2eb12d17c4370b09635ae1470b4>

\* i numeri tra parentesi rappresentano: `(numero funzioni documentate/numero funzioni nel gruppo)`

## espressione e tag

I tag sono utili per la ricerca delle espressioni:

![](https://user-images.githubusercontent.com/12854129/147858304-eba8754b-70b5-4883-9d8d-09a905fe2c4d.png)

funzioni|tags
--------|-----
$geometry|current, processing, functions
$id|row, current
$length|distance, planimetric, length, perimeter, current, linestring, project, settings, ellipsoid, border, setting, calculated
$map|layout, item, drawn, current, main, print, map, window, overview, canvas
$page|layout, print, page, current
$perimeter|distance, planimetric, length, perimeter, current, polygon, project, settings, ellipsoid, setting, calculated
$rownum|row, number, current
$scale|denominator, contexts, current, scale, canvas, map
$vertex_as_point|point, mesh, vertex, current
$vertex_index|index, mesh, vertex, current
$vertex_x|coordinate, mesh, vertex, current
$vertex_y|coordinate, mesh, vertex, current
$vertex_z|mesh, vertex, current
$x|first, point, coordinate, current, multipoint
$x_at|current, retrieves, feature, coordinate
$y|first, point, coordinate, current, multipoint
$y_at|current, retrieves, feature, coordinate
$z|first, point, current, multipoint, altitude, 3D
%|division, remainder
*|multiplication, values
+|addition, null, result, values
-|subtraction, null, result, values
/|division, values
<|left, evaluates, compares, less, values, right
<=|compares, equal, less, values, left, evaluates, right
<>|compares, evaluates, values, equal
=|compares, evaluates, values, equal
AND|condition
CASE|casewhen, clause, series, met, first, corresponding, end, none, evaluated, components, conditions, optional, marks, return, evaluation, else, case, evaluate, result, stops, condition, set
ILIKE|compare, numbers, insensitive, first, match, sensitive, supplied, parameter, case, matches, pattern
IN|list, contained, found
IS|compare, same, equal, identical
IS NOT|compare, same, different
LIKE|compare, sensitive, numbers, first, works, supplied, parameter, matches, pattern
Meshes|calculate, functions, return, mesh, related, contains
NOT|negates, condition
NULL|equates, null
OR|condition
[]|array, operator, element, map, index
\>|greater, compares, evaluates, left, values, right
\>=|compares, equal, values, greater, left, evaluates, right
^|power, values
abs|absolute
acos|angle, cosine, inverse, radians
affine_transform|affine, coordinate, operations, spatial, transformation, reference, offset, system, calculations, translation, rotation, order, added, present, scale
age|difference, needs, datetimes, order, extract, information, following, interval, dates, functions, yearmonthweekdayhourminutesecond
aggregate|aggregate, combine, features, calculated, merge, concatenate, sum, mean, median, count, quartile, minimum, maximum, minority, majority, standard, deviation, length, unique
angle_at_vertex|angles, specified, clockwise, angle, linestring, degrees, bisector, north, average, vertex
apply_dash_pattern|dash, stroked, multilinestring, input, ring, specified, applies, line, pattern, returning
area|planimetric, polygon, spatial, reference, system, calculations, area, project, settings, surface, ellipsoid, units
array|list, array, parameter, containing
array_agg|array, field, aggregated
array_all|array, contains, compare, search
array_append|array, added, end
array_cat|concatenated, arrays, containing
array_distinct|array, containing, distinct
array_filter|array, items, limit, evaluates
array_find|array, found, first, lowest, index
array_first|array, first
array_foreach|evaluated, array, iterate, item
array_get|array, position, index, last, nth, one, first
array_insert|array, added, position
array_intersect|array, element, exists, intersection, overlap
array_last|array, last
array_length|elements, array, count
array_majority|common, array, median
array_max|array, maximum
array_mean|array, ignored, mean, numeric, arithmetic
array_median|array, arithmetic, median, ignored
array_min|array, minimum
array_minority|common, array, median
array_prepend|array, added, beginning
array_prioritize|sorted, array, first, specified, missing, second, ordering, added, present, result, end
array_remove_all|array, entries, removed
array_remove_at|array, removed, index
array_replace|array, map, replaced, supplied
array_reverse|array, reversed, order
array_slice|array, defined, arguments, start, position, slice, portion, end, index
array_sort|sorted, array, elements, provided
array_sum|array, ignored, numeric, arithmetic, sum
array_to_string|concatenates, delimiter, join, aggregate
ascii|code, first, associated, character, unicode
asin|sine, inverse, angle, radians
atan|tangent, inverse, angle, radians
atan2|tangent, arguments, signs, angle, inverse, quadrant
attribute|attribute
attributes|attributes, names, field, keys, containing, map
azimuth|measured, clockwise, points, angle, vertical, north, azimuth, radians
base_file_name|suffix, base, directory, name, file, folder, path
boundary|polygon, linestrings, instance, combinatorial, topological, points, collections, types, ring, boundary, closure
bounds|box, input, spatial, reference, calculations, system, represents, bounding
bounds_height|box, spatial, reference, calculations, system, height, bounding
bounds_width|width, box, spatial, reference, calculations, system, bounding
buffer|distance, equal, spatial, reference, calculations, system, points, segments, miter, join, cap, round
buffer_by_m|line, according, values, varies, vertices, buffer, diameter
ceil|rounds, number
centroid|geometric, center
char|associated, character, unicode, code
clamp|specified, restricts, input, range
close_line|first, point, closed, end, input, appending, result, line, multi
closest_point|closest, point, nearest
coalesce|list, first, arguments, null
collect|aggregated, multipart
collect_geometries|part, set, collects, object, multi
color_cmyk|cyan, color, black, yellow, representation, components
color_cmyka|cyan, alpha, color, black, yellow, representation, components
color_grayscale_average|filter, color, provided, applies, grayscale, representation
color_hsl|attributes, lightness, color, hue, representation, saturation
color_hsla|attributes, alpha, lightness, color, transparency, hue, representation, saturation
color_hsv|attributes, color, hue, representation, saturation
color_hsva|attributes, alpha, color, transparency, hue, representation, saturation
color_mix_rgb|green, blue, red, alpha, mixing, color, colors, provided, ratio
color_part|red, specific, color, component, alpha
color_rgb|green, blue, red, color, representation, components
color_rgba|green, blue, red, alpha, color, representation, components
combine|combination, union
concat|empty, converted, numbers, concatenates, null, strings, several, other, values
concatenate|aggregated, field, joined, delimiter, strings
concatenate_unique|aggregated, unique, field, joined, delimiter, strings
contains|lie, point, lies, tests, interior, exterior, within, points, contains
convex_hull|hull, convex, minimum, represents, encloses, set
cos|angle, cosine
count|aggregate, features, matching, count
count_distinct|aggregate, distinct, count
count_missing|aggregate, missing, count
create_ramp|map, gradient, steps, strings, ramp, color
crosses|common, supplied, crosses, tests, interior, points
current_parent_value|field, actual, unsaved, wrapped, retrieve, widget, current, relation, differ, edited, embedded, coalesce, attribute, form, filter, added, features, parent, context, usable
current_value|table, field, actual, unsaved, current, differ, edited, row, attribute, form, added, features
darker|darker, color, lighter
datetime_from_epoch|passed, datetime, localtime, msecs, date, coordinated, converted, universal, milliseconds, time
day|date, extracts, interval, days, number, day
day_of_week|week, day, specified, datetime, corresponds, ranges, date, saturday
decode_uri|depends, layer, data, dataprovider, provider, uri, underlying, decodes, available
degrees|converts, degrees, radians
densify_by_count|generates, layer, line, number, one, new, polygon, vertices, larger, original
densify_by_distance|maximum, edges, additional, generates, line, densified, adding, new, polygon, interval, layer, one, distance, vertices, specified
difference|part, represents, intersect, clip
disjoint|share, intersect, tests, space
display_expression|evaluated, arguments, details, display, default
distance|projected, reference, spatial, minimum, units
distance_to_vertex|distance, specified, vertex
end_point|last, node, vertex
env|operating, content, prefixes, gets, definition, found, drive, check, system, environment, path, variables, letters, inject, specific, configuration, depends, administrator, variable, documentation, handy, set
epoch|interval, date, milliseconds, epoch
eval|dynamic, fields, parameters, expression, expand, context, passed, variables, evaluates
eval_template|dynamic, fields, parameters, template, expand, context, passed, variables, evaluates
exif|exif, retrieves, tag, file, image, values
exif_geotag|geotags, exif, point, file, image
exp|exponential
extend|start, distances, line, last, linestring, amount, parts, bearing, lines, extends, reference, spatial, extended, first, segment, system, multilinestring, specified, end
exterior_ring|polygon, line, ring, exterior, result, representing
extrude|curve, version, extension, input, specified, extruded, linestring, multi
file_exists|path, exists, file
file_name|extension, name, directory, file, path
file_path|path, directory, name, folder, file
file_size|size, file, bytes
file_suffix|extension, path, suffix, file
flip_coordinates|latitude, longitude, reversed, swapped, coordinates, repairing, copy
floor|downwards, rounds, number
force_polygon_ccw|exterior, clockwise, respect, convention, rings, counter, interior, forces
force_polygon_cw|exterior, clockwise, respect, convention, rings, interior, counter, forces
force_rhr|contexts, clockwise, boundary, interior, rings, bounded, force_polygon_cw, explicit, polygon, area, exterior, inconsistency, right, use, hand, particular, respect, counter, forces, ring, recommended, oriented, direction, rule, definition
format|format, supplied, arguments
format_date|custom, type, uses, format, strings, time, date, formats, see, qdatetime, tostring
format_number|formatted, truncates, places, separator, decimal, default, thousands, locale, language
from_base64|encoding, base, binary, decodes
from_json|json, loads, formatted
generate_series|sequence, containing, numbers, array
geom_from_gml|representation, conversion
geom_from_wkb|created, wkb, binary, known, representation, conversion
geom_from_wkt|text, known, wkt, representation, conversion
geom_to_wkb|wkb, binary, representation, known, conversion
geom_to_wkt|text, wkt, srid, representation, known, conversion
geometry|
geometry_n|part, input, multipart, collection, specific
geometry_type|describing, type, point, polygon, line
get_feature|attribute, first, matching, search, find
get_feature_by_id|
hamming_distance|distance, length, input, sensitive, different, strings, corresponding, hamming, equates, characters, case, same, comparison, positions
hash|hex, bytes, byte, digits, hash, method, given, represented, character, long, bits, produces
hausdorff_distance|distance, segment, dissimilar, densify, linestrings, parallel, other, matching, total, close, executed, specifying, occurs, equal, fraction, testing, method, discrete, linear, default, approximate, sets, length, large, lower, similar, similarity, parameter, measure, split, make, approach, closest, examples, provided, performs, insufficient, networks, specify, optional, decreasing, approximation, cases, densification, specified, computing, argument, subsegments, hausdorff, exact, indicating, subset, standard
hour|extracts, number, time, part, interval, hours, hour, datetime
hstore_to_map|formatted, hstore, map
if|tests, different, check, result, conditional, depending, condition
inclination|zenith, nadir, inclination, measured, points
interior_ring_n|interior, polygon, hole, ring
intersection|shared, represents, portion, overlap
intersects|share, space, intersects, tests, intersect, portion, overlaps
intersects_bbox|box, tests, overlaps, defined, intersect, bounding
iqr|field, quartile, range, inter, calculated, statistics, aggregates
is_closed|points, start, closed, end, coincident, result, false, line
is_directory|path, directory, folder
is_empty|empty, is_empty_or_null, see, coordinates, false
is_empty_or_null|empty, is_empty, coordinates, false
is_file|path, file
is_layer_visible|specified, visible
is_multipart|type, multi
is_selected|selected, arguments, details
is_valid|rules, valid, ogc, according, formed
item_variables|layout, item, variables, print, map
layer_property|property, matching, metadata
left|first, substring, leftmost, characters, contains, extracts
length|distance, linestring, length, count, characters, planimetric
length3D|planimetric, distance, length, spatial, reference, system, calculations, calculates, line, project, differs, object, match, settings, ellipsoid, units
levenshtein|distance, required, edit, indicate, sensitive, similarity, insertions, similar, mean, measure, different, character, change, substitutions, strings, edits, distances, larger, deletions, equates, case, minimum, levenshtein, smaller
lighter|darker, color, lighter
line_interpolate_angle|distance, angles, parallel, specified, clockwise, angle, linestring, degrees, north
line_interpolate_point|distance, interpolated, linestring, point, specified, along
line_locate_point|distance, point, specified, closest, linestring, position, corresponding, along
line_merge|passed, single, return, input, linestrings, merged, connected, linestring, multilinestring
line_substring|curve, start, specified, measured, falls, existing, interpolated, beginning, distances, line, end, portion
ln|natural, logarithm
log|base, logarithm
log10|base, logarithm
longest_common_substring|longest, common, input, sensitive, case, substring, strings
lower|converts, letters, lower, case
lpad|length, padded, width, truncated, specified, target, fill, left, character, smaller
m|point, measure
m_max|maximum, measure
m_min|minimum, measure
main_angle|oriented, minimal, covers, clockwise, angle, long, north, degrees, rectangle, axis, bounding
majority|occurring, field, majority, aggregate
make_circle|circular, polygon
make_date|year, date, month, numbers, day
make_datetime|minute, month, numbers, day, year, second, hour, datetime
make_ellipse|polygon, elliptical
make_interval|minute, seconds, month, year, weeks, values, interval, hours, days
make_line|point, line, series
make_point|optional, point
make_point_m|point, coordinate
make_polygon|outer, ring, series, inner, optional, polygon
make_rectangle_3points|rectangle, points
make_regular_polygon|polygon, regular
make_square|square, diagonal
make_time|minute, hour, second, numbers, time
make_triangle|triangle, polygon
map|passed, keys, pair, containing, parameters, map
map_akeys|array, map, keys
map_avals|array, map
map_concat|containing, key, concatenate, contain, entries, maps, map
map_credits|list, rights, layers, layout, item, usage, credit, strings, map
map_delete|deleted, corresponding, map, key
map_exist|map, exists, key
map_get|map, exists, key
map_insert|map, added, exists, key, overridden
map_prefix_keys|prefixed, keys, map
map_to_hstore|formatted, hstore, elements, map, merge
maptip|evaluated, arguments, maptip, details, default, see
max|longest, biggest, most, largest, maximum
max_length|length, maximum, strings, characters, count, aggregate
maximum|maximum, aggregate
md5|hash
mean|average, aggregate, mean
median|median, aggregate
mime_type|type, data, binary
min|least, smallest, minimum
min_length|length, characters, count, minimum, strings
minimal_circle|enclosing, minimal, minimum, represents, encloses, circle, smallest
minimum|minimum, aggregate
minority|least, occurring, field, minority, aggregate
minute|minutes, extracts, part, interval, number, time, datetime
month|date, extracts, months, part, interval, month, number
nodes_to_points|vertex, multipoint, node, input
now|static, evaluating, current, date, time
nullif|substitute, equals, condition, compare
num_geometries|collection, multipart, parts, count
num_interior_rings|rings, holes, count, polygon, collection, interior
num_points|vertices
num_rings|rings, holes, polygon, collection, exterior, including
num_selected|evaluated, selected, works, default, features
offset_curve|spatial, offsetting, reference, system, linestring, formed, distances, side
order_parts|criteria, multigeometry, orders, parts, given
oriented_bbox|oriented, box, minimal, represents, bounding
overlaps|share, tests, contained, overlaps, same, dimension, space
overlay_contains|least, predicate, current, contained, target, contains, array, geos, st_contains, postgis, described, underlying, features
overlay_crosses|predicate, st_crosses, crosses, current, target, array, geos, described, underlying, features, crossed
overlay_disjoint|predicate, st_disjoint, disjoint, current, target, array, geos, described, underlying, features
overlay_equals|predicate, current, equals, equal, target, array, geos, st_equals, described, underlying, features
overlay_intersects|intersected, least, predicate, current, target, array, geos, postgis, described, st_intersects, intersects, underlying, features
overlay_nearest|distance, layers, large, slow, current, target, array, lot, features
overlay_touches|least, predicate, touches, current, target, array, geos, described, underlying, touched, st_touches, features
overlay_within|predicate, current, contain, target, array, geos, described, underlying, features
parameter|algorithm, parameter, processing
perimeter|planimetric, distance, polygon, perimeter, spatial, reference, system, calculations, project, differs, object, match, settings, ellipsoid, units
pi|calculations, pi
point_n|specific, node, vertex
point_on_surface|point, surface, lie, centroid, overlay
pole_of_inaccessibility|inaccessibility, precise, tolerances, calculates, guaranteed, boundary, require, point, true, iterations, internal, uses, approximate, approach, polylabel, find, distant, calculate, pole, take, surface, specified, tolerance, iterative
project|distance, elevation, projected, start, point, azimuth, radians, bearing
project_color|scheme, project, color
q1|field, quartile, first, calculated
q3|third, field, quartile, calculated
radians|converts, degrees, radians
ramp_color|ramp, color, representing
rand|random, inclusive, specified, range, argument, seed, same, provided, minimum, maximum, integer, depending
randf|random, specified, range, argument, seed, same, provided, float, minimum, maximum, inclusive, depending
range|field, range, aggregate, minimum, maximum
raster_statistic|raster, statistics
raster_value|provided, point, raster, found
regexp_match|return, found, matching, unicode, regular, position, substring, first
regexp_matches|array, groups, capturing, captured, order, appear, supplied, regular, strings
regexp_replace|regular, supplied, replaced
regexp_substr|regular, matches, supplied, portion
relate|dimensional, relationship, extended, intersection, representation, model, tests
relation_aggregate|child, matching, aggregate, features, relation
replace|array, map, strings, supplied, replaced
represent_attributes|attributes, keys, arguments, representation, map, see, attribute, configured, names, type, details, depends, widget
represent_value|depends, configured, field, type, widgets, map, representation, widget
reverse|direction, order, vertices, reverses, line, reversing
right|last, substring, rightmost, characters, contains
rotate|version, spatial, reference, calculations, rotated, system
round|rounds, places, decimal, number
roundness|polygon, perfect, flat, close, shape, calculates, circle
rpad|length, right, padded, width, specified, truncated, target, fill, character, smaller
scale|version, scaled, spatial, reference, calculations, system
scale_exp|exponential, curve, ease, transforms, output, given, input, domain, range, specified, values
scale_linear|transforms, linear, output, given, input, domain, range, interpolation
second|extracts, part, seconds, interval, number, time, datetime
segments_to_lines|consisting, segment, input, multi, line
set_color_part|alpha, component, specific, red, color, sets
sha256|hash
shortest_line|start, resultant, joining, end, shortest, line
simplify|straight, large, deviations, nodes, algorithm, reduces, simplifies, segments, number, threshold, distance, removing, vertices, based, preserves
simplify_vw|spikes, areas, straight, nodes, algorithm, area, simplifies, removes, narrow, segments, visvalingam, threshold, create, vertices, removing, based, small
sin|sine, angle
single_sided_buffer|buffering, spatial, reference, system, linestring, formed, distances, side
sinuosity|curve, distance, length, endpoints, sinuosity, ratio, straight
smooth|adding, corners, smoothed, dimensionality, round, output, contain, input, retain, extra, smooths, nodes, values, same
soundex|code, represented, similar, matching, algorithm, soundex, same, phonetic, representation, strings, sounds
sqlite_fetch_and_increment|attributes, children, applied, uncommitted, works, relations, prefetched, intended, creating, several, auto_increment, form, databases, transaction, parents, filter_value, mode, open, primary, evaluate, sidenote, add, require, impossible, default_values, table, insert, nice, formats, current, adding, get, target, work, specified, usage, columns, retrieved, autoincrementing, new, limitation, gpkg, parallel, database, additional, makes, postgres, modifies, sequence, cached, manage, key, same, id_field, acquire, filtered, default, filter_attribute, parent, option, unsafe, sqlite, separate, parameter, map, row, configurations, lifetime, processes, incremented, able, features, purpose
sqrt|root, square
square_wave|waves, rectangular, constructs, square, boundary
square_wave_randomized|waves, rectangular, constructs, square, boundary, randomized
start_point|first, node
stdev|deviation, field, standard, aggregate
straight_distance_2d|distance, curve, circularstring, first, last, direct, euclidean, linestring, vertex
string_to_array|split, convert, separate, delimiter, divides
strpos|substring, position, return, found, first, matching
substr|part
sum|field, summed, aggregate
sym_difference|portions, represents, intersect
tan|angle, tangent
tapered_buffer|varies, buffer, line, diameter, length
title|letter, words, lower, converts, leading, capital, title, case
to_base64|encoding, base, binary, encodes
to_date|provided, additional, user, format_date, parse, qdate, converts, default, current, format, object, fromstring, date, optional, documentation, see
to_datetime|provided, additional, user, format_date, parse, qdate, converts, default, datetime, current, format, object, fromstring, optional, documentation, qtime, see
to_decimal|converts, minute, degree, equivalent, second, coordinate, decimal
to_dm|converts, minute, degree, coordinate
to_dms|converts, minute, degree, second, coordinate
to_int|converts, invalid, converted, integer
to_interval|type, month, converts, date, interval, take, hours, days
to_json|formatted, json, array, create, other, map
to_real|converts, precision, invalid, rounded, numbers, changes, real, result, converted, saving, conversion, smaller
to_string|converts, number
to_time|provided, additional, format, object, parse, time, converts, fromstring, optional, documentation, qtime, see
touches|point, common, touches, interiors, tests, intersect
transform|crs, source, transformed, destination, reprojection
translate|spatial, reference, calculations, system, translated, displace, move
triangular_wave|waves, boundary, constructs, triangular
triangular_wave_randomized|waves, boundary, constructs, randomized, triangular
trim|removes, leading, whitespace, spaces, tabs, trailing
try|return, tries, error, alternative, provided, exception
union|union, dissolve, point, represents, set
upper|converts, upper, letters, case
url_encode|encoded, producing, form, characters, query, plus, url, compliant, converted, map, sign, transforms
uuid|createuuid, generates, method, unique, quuid, identifier, row
var|stored, variable, specified
wave|waves, rounded, sine, boundary, constructs
wave_randomized|waves, sine, boundary, curved, constructs, randomized
wedge_buffer|buffer, wedge, point, originating, shaped
week|weeks, week, date, extracts, interval, number
with_variable|variable, argument, value, evaluation
within|tests, contains, completely
wordwrap|maximum, minimum, wrapped, characters, multiline
x|centroid, point, coordinate
x_max|coordinate, spatial, reference, calculations, system, maximum
x_min|coordinate, spatial, reference, calculations, system, minimum
y|centroid, point, coordinate
y_max|coordinate, spatial, reference, calculations, system, maximum
y_min|coordinate, spatial, reference, calculations, system, minimum
year|year, years, date, extracts, part, interval, number
z|point, coordinate
z_max|coordinate, maximum
z_min|coordinate, minimum
\|\||behavior, different, see, concat, null, joins, result, values
~|white, space, regular, performs, backslash, characters, escaped, character, expression, match

## tag e espressioni

tag | espressioni
----|----
|geometry, get_feature_by_id
absolute|abs
adding|smooth, sqlite_fetch_and_increment, densify_by_distance
corners|smooth
smoothed|smooth
dimensionality|smooth
round|smooth, buffer
output|smooth, scale_exp, scale_linear
contain|smooth, map_concat, overlay_within
input|smooth, bounds, segments_to_lines, extrude, apply_dash_pattern, hamming_distance, scale_exp, close_line, longest_common_substring, geometry_n, line_merge, clamp, scale_linear, nodes_to_points
retain|smooth
extra|smooth
smooths|smooth
nodes|smooth, simplify_vw, simplify
values|smooth, +, ||, <=, >=, =, <>, /, concat, exif, scale_exp, >, <, buffer_by_m, make_interval, *, ^, -
same|smooth, sqlite_fetch_and_increment, soundex, IS NOT, IS, hamming_distance, rand, randf, overlaps
addition|+
null|+, ||, concat, NULL, coalesce, -
result|+, ||, CASE, to_real, close_line, is_closed, exterior_ring, array_prioritize, -, if
affine|affine_transform
coordinate|affine_transform, x, y, to_dm, to_decimal, to_dms, z_max, $vertex_x, $vertex_y, z_min, x_max, y_max, x_min, y_min, $x_at, $y_at, $x, $y, make_point_m, z
operations|affine_transform
spatial|affine_transform, bounds, bounds_height, single_sided_buffer, x_max, y_max, x_min, y_min, buffer, length3D, perimeter, area, distance, offset_curve, translate, extend, scale, rotate, bounds_width
transformation|affine_transform
reference|affine_transform, bounds, bounds_height, single_sided_buffer, x_max, y_max, x_min, y_min, buffer, length3D, perimeter, area, distance, offset_curve, translate, extend, scale, rotate, bounds_width
offset|affine_transform
system|affine_transform, bounds, bounds_height, single_sided_buffer, x_max, y_max, x_min, y_min, buffer, env, length3D, perimeter, area, offset_curve, translate, extend, scale, rotate, bounds_width
calculations|affine_transform, bounds, bounds_height, pi, x_max, y_max, x_min, y_min, buffer, length3D, perimeter, area, translate, scale, rotate, bounds_width
translation|affine_transform
rotation|affine_transform
order|affine_transform, regexp_matches, array_reverse, age, reverse
added|affine_transform, array_prepend, array_append, array_insert, current_parent_value, map_insert, array_prioritize, current_value
present|affine_transform, array_prioritize
scale|affine_transform, $scale
aggregate|aggregate, count_distinct, count, count_missing, mean, relation_aggregate, array_to_string, stdev, range, sum, minority, max_length, maximum, median, minimum, majority
combine|aggregate
features|aggregate, count, sqlite_fetch_and_increment, relation_aggregate, overlay_nearest, num_selected, current_parent_value, overlay_intersects, overlay_contains, overlay_touches, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint, current_value
calculated|aggregate, $length, $perimeter, q1, iqr, q3
merge|aggregate, map_to_hstore
concatenate|aggregate, map_concat
sum|aggregate, array_sum
mean|aggregate, array_mean, mean, levenshtein
median|aggregate, array_median, array_majority, array_minority, median
count|aggregate, count_distinct, count, count_missing, num_geometries, length, array_length, min_length, max_length, num_interior_rings
quartile|aggregate, q1, iqr, q3
minimum|aggregate, array_min, z_min, x_min, y_min, levenshtein, minimal_circle, range, convex_hull, min, min_length, wordwrap, minimum, m_min, distance, rand, randf
maximum|aggregate, array_max, z_max, x_max, y_max, range, max_length, max, maximum, densify_by_distance, m_max, wordwrap, rand, randf
minority|aggregate, minority
majority|aggregate, majority
standard|aggregate, stdev, hausdorff_distance
deviation|aggregate, stdev
length|aggregate, sinuosity, hamming_distance, length, $length, $perimeter, hausdorff_distance, min_length, max_length, lpad, rpad, length3D, tapered_buffer
unique|aggregate, concatenate_unique, uuid
distinct|count_distinct, array_distinct
matching|count, get_feature, relation_aggregate, soundex, hausdorff_distance, layer_property, regexp_match, strpos
missing|count_missing, array_prioritize
aggregated|concatenate, collect, concatenate_unique, array_agg
field|concatenate, concatenate_unique, array_agg, attributes, represent_value, stdev, current_parent_value, q1, iqr, range, sum, minority, majority, current_value, q3
joined|concatenate, concatenate_unique
delimiter|concatenate, concatenate_unique, array_to_string, string_to_array
strings|concatenate, concatenate_unique, regexp_matches, replace, soundex, format_date, hamming_distance, levenshtein, concat, min_length, max_length, map_credits, longest_common_substring, create_ramp
multipart|collect, num_geometries, geometry_n
algorithm|parameter, soundex, simplify_vw, simplify
parameter|parameter, sqlite_fetch_and_increment, ILIKE, LIKE, hausdorff_distance, array
processing|parameter, $geometry
alpha|set_color_part, color_hsva, color_hsla, color_cmyka, color_rgba, color_mix_rgb, color_part
component|set_color_part, color_part
specific|set_color_part, env, geometry_n, color_part, point_n
red|set_color_part, color_rgba, color_mix_rgb, color_rgb, color_part
color|set_color_part, color_hsva, color_hsla, color_hsv, color_hsl, color_cmyka, color_cmyk, darker, lighter, color_grayscale_average, color_rgba, color_mix_rgb, color_rgb, create_ramp, ramp_color, color_part, project_color
sets|set_color_part, hausdorff_distance
angle|cos, acos, tan, angle_at_vertex, line_interpolate_angle, azimuth, main_angle, sin, asin, atan2, atan
cosine|cos, acos
inverse|acos, asin, atan2, atan
radians|acos, degrees, radians, project, azimuth, asin, atan
tangent|tan, atan2, atan
angles|angle_at_vertex, line_interpolate_angle
specified|angle_at_vertex, sqlite_fetch_and_increment, line_substring, extrude, apply_dash_pattern, line_interpolate_angle, line_interpolate_point, line_locate_point, hausdorff_distance, distance_to_vertex, scale_exp, pole_of_inaccessibility, lpad, rpad, densify_by_distance, rand, randf, array_prioritize, clamp, is_layer_visible, extend, var, day_of_week
clockwise|angle_at_vertex, force_rhr, line_interpolate_angle, force_polygon_ccw, force_polygon_cw, azimuth, main_angle
linestring|angle_at_vertex, single_sided_buffer, extrude, line_interpolate_angle, straight_distance_2d, line_interpolate_point, length, $length, line_locate_point, line_merge, offset_curve, extend
degrees|angle_at_vertex, degrees, radians, line_interpolate_angle, main_angle
bisector|angle_at_vertex
north|angle_at_vertex, line_interpolate_angle, azimuth, main_angle
average|angle_at_vertex, mean
vertex|angle_at_vertex, $vertex_x, $vertex_y, straight_distance_2d, distance_to_vertex, $vertex_index, end_point, $vertex_z, $vertex_as_point, point_n, nodes_to_points
array|array_prepend, array_append, array_insert, array_median, array_distinct, array_all, array_slice, array_intersect, array_remove_all, array_agg, array_first, array_find, regexp_matches, array_mean, array_sum, array_filter, array_last, map_avals, map_akeys, array_replace, replace, array_max, array_min, [], array_get, array_remove_at, array_reverse, array_majority, array_minority, overlay_nearest, array_length, array_foreach, to_json, overlay_intersects, overlay_contains, overlay_touches, array, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint, generate_series, array_sort, array_prioritize
beginning|array_prepend, line_substring
end|array_append, array_slice, CASE, line_substring, close_line, is_closed, array_prioritize, extend, shortest_line
position|array_insert, array_slice, array_get, line_locate_point, regexp_match, strpos
arithmetic|array_median, array_mean, array_sum
ignored|array_median, array_mean, array_sum
containing|array_distinct, attributes, array_cat, map_concat, array, map, generate_series
contains|array_all, Meshes, left, right, overlay_contains, contains, within
compare|array_all, ILIKE, IS NOT, IS, LIKE, nullif
search|array_all, get_feature
defined|array_slice, intersects_bbox
arguments|array_slice, represent_attributes, display_expression, maptip, format, coalesce, is_selected, atan2
start|array_slice, line_substring, project, is_closed, extend, shortest_line
slice|array_slice
portion|array_slice, line_substring, regexp_substr, intersects, intersection
index|array_slice, array_find, [], array_get, array_remove_at, $vertex_index
element|array_intersect, []
exists|array_intersect, map_insert, map_exist, map_get, file_exists
intersection|array_intersect, relate
overlap|array_intersect, intersection
entries|array_remove_all, map_concat
removed|array_remove_all, array_remove_at
first|array_first, array_find, array_get, get_feature, CASE, ascii, ILIKE, LIKE, straight_distance_2d, q1, start_point, close_line, $x, $y, $z, left, coalesce, regexp_match, array_prioritize, extend, strpos
found|array_find, IN, env, raster_value, regexp_match, strpos
lowest|array_find
groups|regexp_matches
capturing|regexp_matches
captured|regexp_matches
appear|regexp_matches
supplied|regexp_matches, array_replace, replace, crosses, ILIKE, LIKE, format, regexp_substr, regexp_replace
regular|regexp_matches, make_regular_polygon, regexp_substr, regexp_replace, regexp_match, ~
numeric|array_mean, array_sum
items|array_filter
limit|array_filter
evaluates|array_filter, <=, >=, =, <>, eval, eval_template, >, <
last|array_last, array_get, straight_distance_2d, end_point, right, extend
map|map_avals, map_akeys, array_replace, replace, [], sqlite_fetch_and_increment, represent_attributes, attributes, map_concat, map_delete, $scale, represent_value, url_encode, map_to_hstore, hstore_to_map, to_json, $map, item_variables, map_credits, map_insert, map_exist, map_get, create_ramp, map, map_prefix_keys
keys|map_akeys, represent_attributes, attributes, map, map_prefix_keys
replaced|array_replace, replace, regexp_replace
operator|[]
nth|array_get
one|array_get, densify_by_count, densify_by_distance
reversed|array_reverse, flip_coordinates
associated|char, ascii
character|char, ascii, levenshtein, hash, lpad, rpad, ~
unicode|char, ascii, regexp_match
code|char, ascii, soundex
attribute|attribute, get_feature, represent_attributes, current_parent_value, current_value
find|get_feature, pole_of_inaccessibility
attributes|color_hsva, color_hsla, sqlite_fetch_and_increment, color_hsv, represent_attributes, color_hsl, attributes
transparency|color_hsva, color_hsla
hue|color_hsva, color_hsla, color_hsv, color_hsl
representation|color_hsva, color_hsla, color_hsv, represent_attributes, color_hsl, soundex, geom_from_wkb, color_cmyka, color_cmyk, represent_value, relate, color_grayscale_average, color_rgba, color_rgb, geom_from_gml, geom_from_wkt, geom_to_wkt, geom_to_wkb
saturation|color_hsva, color_hsla, color_hsv, color_hsl
lightness|color_hsla, color_hsl
children|sqlite_fetch_and_increment
applied|sqlite_fetch_and_increment
uncommitted|sqlite_fetch_and_increment
works|sqlite_fetch_and_increment, LIKE, num_selected
relations|sqlite_fetch_and_increment
prefetched|sqlite_fetch_and_increment
intended|sqlite_fetch_and_increment
creating|sqlite_fetch_and_increment
several|sqlite_fetch_and_increment, concat
auto_increment|sqlite_fetch_and_increment
form|sqlite_fetch_and_increment, url_encode, current_parent_value, current_value
databases|sqlite_fetch_and_increment
transaction|sqlite_fetch_and_increment
parents|sqlite_fetch_and_increment
filter_value|sqlite_fetch_and_increment
mode|sqlite_fetch_and_increment
open|sqlite_fetch_and_increment
primary|sqlite_fetch_and_increment
evaluate|sqlite_fetch_and_increment, CASE
sidenote|sqlite_fetch_and_increment
add|sqlite_fetch_and_increment
require|sqlite_fetch_and_increment, pole_of_inaccessibility
impossible|sqlite_fetch_and_increment
default_values|sqlite_fetch_and_increment
table|sqlite_fetch_and_increment, current_value
insert|sqlite_fetch_and_increment
nice|sqlite_fetch_and_increment
formats|sqlite_fetch_and_increment, format_date
current|sqlite_fetch_and_increment, $vertex_x, $vertex_y, $geometry, $x_at, $y_at, $scale, overlay_nearest, $length, $perimeter, current_parent_value, $x, $y, $z, $vertex_index, overlay_intersects, $map, $page, overlay_contains, overlay_touches, $vertex_z, $vertex_as_point, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint, to_date, to_datetime, $id, $rownum, now, current_value
get|sqlite_fetch_and_increment
target|sqlite_fetch_and_increment, overlay_nearest, overlay_intersects, overlay_contains, overlay_touches, lpad, rpad, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint
work|sqlite_fetch_and_increment
usage|sqlite_fetch_and_increment, map_credits
columns|sqlite_fetch_and_increment
retrieved|sqlite_fetch_and_increment
autoincrementing|sqlite_fetch_and_increment
new|sqlite_fetch_and_increment, densify_by_count, densify_by_distance
limitation|sqlite_fetch_and_increment
gpkg|sqlite_fetch_and_increment
parallel|sqlite_fetch_and_increment, line_interpolate_angle, hausdorff_distance
database|sqlite_fetch_and_increment
additional|sqlite_fetch_and_increment, densify_by_distance, to_time, to_date, to_datetime
makes|sqlite_fetch_and_increment
postgres|sqlite_fetch_and_increment
modifies|sqlite_fetch_and_increment
sequence|sqlite_fetch_and_increment, generate_series
cached|sqlite_fetch_and_increment
manage|sqlite_fetch_and_increment
key|sqlite_fetch_and_increment, map_concat, map_delete, map_insert, map_exist, map_get
id_field|sqlite_fetch_and_increment
acquire|sqlite_fetch_and_increment
filtered|sqlite_fetch_and_increment
default|sqlite_fetch_and_increment, hausdorff_distance, display_expression, maptip, num_selected, format_number, to_date, to_datetime
filter_attribute|sqlite_fetch_and_increment
parent|sqlite_fetch_and_increment, current_parent_value
option|sqlite_fetch_and_increment
unsafe|sqlite_fetch_and_increment
sqlite|sqlite_fetch_and_increment
separate|sqlite_fetch_and_increment, string_to_array
row|sqlite_fetch_and_increment, uuid, $id, $rownum, current_value
configurations|sqlite_fetch_and_increment
lifetime|sqlite_fetch_and_increment
processes|sqlite_fetch_and_increment
incremented|sqlite_fetch_and_increment
able|sqlite_fetch_and_increment
purpose|sqlite_fetch_and_increment
see|represent_attributes, ||, format_date, is_empty, maptip, to_time, to_date, to_datetime
configured|represent_attributes, represent_value
names|represent_attributes, attributes
type|represent_attributes, format_date, represent_value, geometry_type, mime_type, to_interval, is_multipart
details|represent_attributes, display_expression, maptip, is_selected
depends|represent_attributes, represent_value, decode_uri, env
widget|represent_attributes, represent_value, current_parent_value
base|log, log10, from_base64, to_base64, base_file_name
logarithm|log, log10, ln
behavior|||
different|||, IS NOT, hamming_distance, levenshtein, if
concat|||
joins|||
box|bounds, bounds_height, intersects_bbox, oriented_bbox, bounds_width
represents|bounds, minimal_circle, convex_hull, oriented_bbox, difference, sym_difference, intersection, union
bounding|bounds, bounds_height, intersects_bbox, oriented_bbox, main_angle, bounds_width
height|bounds_height
tests|intersects_bbox, crosses, relate, contains, touches, disjoint, intersects, overlaps, within, if
overlaps|intersects_bbox, intersects, overlaps
intersect|intersects_bbox, difference, touches, sym_difference, disjoint, intersects
buffer|wedge_buffer, buffer_by_m, tapered_buffer
wedge|wedge_buffer
point|wedge_buffer, x, y, closest_point, geometry_type, project, line_interpolate_point, line_locate_point, close_line, $x, $y, $z, exif_geotag, pole_of_inaccessibility, contains, make_point, touches, make_point_m, z, make_line, m, $vertex_as_point, point_on_surface, raster_value, union
originating|wedge_buffer
shaped|wedge_buffer
buffering|single_sided_buffer
formed|single_sided_buffer, is_valid, offset_curve
distances|single_sided_buffer, line_substring, levenshtein, offset_curve, extend
side|single_sided_buffer, offset_curve
calculate|Meshes, pole_of_inaccessibility
functions|Meshes, $geometry, age
return|Meshes, CASE, line_merge, regexp_match, try, strpos
mesh|Meshes, $vertex_x, $vertex_y, $vertex_index, $vertex_z, $vertex_as_point
related|Meshes
pi|pi
casewhen|CASE
clause|CASE
series|CASE, make_polygon, make_line
met|CASE
corresponding|CASE, map_delete, hamming_distance, line_locate_point
none|CASE
evaluated|CASE, display_expression, maptip, array_foreach, num_selected
components|CASE, color_cmyka, color_cmyk, color_rgba, color_rgb
conditions|CASE
optional|CASE, hausdorff_distance, make_point, make_polygon, to_time, to_date, to_datetime
marks|CASE
evaluation|CASE, with_variable
else|CASE
case|CASE, ILIKE, lower, upper, hamming_distance, levenshtein, title, longest_common_substring
stops|CASE
condition|CASE, AND, OR, NOT, nullif, if
set|CASE, convex_hull, env, collect_geometries, union
centroid|x, y, point_on_surface
child|relation_aggregate
relation|relation_aggregate, current_parent_value
circular|make_circle
polygon|make_circle, force_rhr, geometry_type, $perimeter, densify_by_count, interior_ring_n, densify_by_distance, make_polygon, perimeter, area, make_ellipse, exterior_ring, boundary, roundness, make_regular_polygon, num_interior_rings, num_rings, make_triangle
closest|closest_point, line_locate_point, hausdorff_distance
nearest|closest_point
represented|soundex, hash
similar|soundex, levenshtein, hausdorff_distance
soundex|soundex
phonetic|soundex
sounds|soundex
collection|num_geometries, geometry_n, num_interior_rings, num_rings
parts|num_geometries, order_parts, extend
combination|combine
union|combine, union
common|array_majority, array_minority, crosses, longest_common_substring, touches
crosses|crosses, overlay_crosses
interior|crosses, force_rhr, force_polygon_ccw, force_polygon_cw, interior_ring_n, contains, num_interior_rings
points|crosses, buffer, contains, azimuth, is_closed, boundary, make_rectangle_3points, inclination
numbers|ILIKE, LIKE, to_real, concat, make_time, make_datetime, generate_series, make_date
insensitive|ILIKE
match|ILIKE, length3D, perimeter, ~
sensitive|ILIKE, LIKE, hamming_distance, levenshtein, longest_common_substring
matches|ILIKE, LIKE, regexp_substr
pattern|ILIKE, LIKE, apply_dash_pattern
equal|IS, <=, >=, =, <>, buffer, hausdorff_distance, overlay_equals
identical|IS
compares|<=, >=, =, <>, >, <
less|<=, <
left|<=, >=, >, <, lpad
right|<=, >=, force_rhr, >, <, rpad
greater|>=, >
concatenated|array_cat
arrays|array_cat
concatenates|array_to_string, concat
join|array_to_string, buffer
consisting|segments_to_lines
segment|segments_to_lines, hausdorff_distance, extend
multi|segments_to_lines, extrude, close_line, collect_geometries, is_multipart
line|segments_to_lines, line_substring, apply_dash_pattern, geometry_type, reverse, close_line, densify_by_count, buffer_by_m, densify_by_distance, length3D, make_line, is_closed, exterior_ring, extend, shortest_line, tapered_buffer
maps|map_concat
contexts|force_rhr, $scale
boundary|force_rhr, pole_of_inaccessibility, boundary, triangular_wave_randomized, triangular_wave, square_wave, square_wave_randomized, wave, wave_randomized
rings|force_rhr, force_polygon_ccw, force_polygon_cw, num_interior_rings, num_rings
bounded|force_rhr
force_polygon_cw|force_rhr
explicit|force_rhr
area|force_rhr, area, simplify_vw
exterior|force_rhr, force_polygon_ccw, force_polygon_cw, contains, exterior_ring, num_rings
inconsistency|force_rhr
use|force_rhr
hand|force_rhr
particular|force_rhr
respect|force_rhr, force_polygon_ccw, force_polygon_cw
counter|force_rhr, force_polygon_ccw, force_polygon_cw
forces|force_rhr, force_polygon_ccw, force_polygon_cw
ring|force_rhr, apply_dash_pattern, interior_ring_n, make_polygon, exterior_ring, boundary
recommended|force_rhr
oriented|force_rhr, oriented_bbox, main_angle
direction|force_rhr, reverse
rule|force_rhr
definition|force_rhr, env
converts|degrees, radians, to_int, lower, to_dm, to_decimal, to_dms, to_string, to_real, upper, title, to_time, to_date, to_datetime, to_interval
invalid|to_int, to_real
converted|to_int, to_real, concat, url_encode, datetime_from_epoch
integer|to_int, rand
letters|lower, upper, env
lower|lower, hausdorff_distance, title
minute|to_dm, to_decimal, to_dms, make_time, make_datetime, make_interval
degree|to_dm, to_decimal, to_dms
equivalent|to_decimal
second|to_decimal, to_dms, make_time, make_datetime, array_prioritize
decimal|to_decimal, format_number, round
number|to_string, day, month, floor, hour, second, densify_by_count, minute, ceil, round, $rownum, simplify, week, year
precision|to_real
rounded|to_real, wave
changes|to_real
real|to_real
saving|to_real
conversion|to_real, geom_from_wkb, geom_from_gml, geom_from_wkt, geom_to_wkt, geom_to_wkb
smaller|to_real, levenshtein, lpad, rpad
upper|upper
created|geom_from_wkb
wkb|geom_from_wkb, geom_to_wkb
binary|geom_from_wkb, from_base64, to_base64, mime_type, geom_to_wkb
known|geom_from_wkb, geom_from_wkt, geom_to_wkt, geom_to_wkb
createuuid|uuid
generates|uuid, densify_by_count, densify_by_distance
method|uuid, hausdorff_distance, hash
quuid|uuid
identifier|uuid
criteria|order_parts
multigeometry|order_parts
orders|order_parts
given|order_parts, scale_exp, hash, scale_linear
crs|transform
source|transform
transformed|transform
destination|transform
reprojection|transform
retrieves|$x_at, $y_at, exif
feature|$x_at, $y_at
curve|sinuosity, line_substring, extrude, straight_distance_2d, scale_exp
distance|sinuosity, line_interpolate_angle, straight_distance_2d, project, buffer, line_interpolate_point, overlay_nearest, hamming_distance, length, $length, $perimeter, line_locate_point, levenshtein, hausdorff_distance, distance_to_vertex, densify_by_distance, length3D, perimeter, simplify
endpoints|sinuosity
sinuosity|sinuosity
ratio|sinuosity, color_mix_rgb
straight|sinuosity, simplify_vw, simplify
measured|line_substring, azimuth, inclination
falls|line_substring
existing|line_substring
interpolated|line_substring, line_interpolate_point
version|extrude, scale, rotate
extension|extrude, file_name, file_suffix
extruded|extrude
custom|format_date
uses|format_date, pole_of_inaccessibility
format|format_date, format, to_time, to_date, to_datetime
time|format_date, hour, second, make_time, minute, datetime_from_epoch, to_time, now
date|format_date, day, month, epoch, datetime_from_epoch, to_date, now, to_interval, day_of_week, week, make_date, year
qdatetime|format_date
tostring|format_date
cyan|color_cmyka, color_cmyk
black|color_cmyka, color_cmyk
yellow|color_cmyka, color_cmyk
darker|darker, lighter
lighter|darker, lighter
dash|apply_dash_pattern
stroked|apply_dash_pattern
multilinestring|apply_dash_pattern, line_merge, extend
applies|apply_dash_pattern, color_grayscale_average
returning|apply_dash_pattern
extracts|day, month, hour, second, left, minute, week, year
interval|day, month, age, hour, second, epoch, densify_by_distance, make_interval, minute, to_interval, week, year
days|day, make_interval, to_interval
day|day, make_datetime, day_of_week, make_date
months|month
part|month, hour, second, minute, substr, geometry_n, difference, collect_geometries, year
month|month, make_datetime, make_interval, to_interval, make_date
deleted|map_delete
denominator|$scale
canvas|$scale, $map
widgets|represent_value
layer|decode_uri, densify_by_count, densify_by_distance
data|decode_uri, mime_type
dataprovider|decode_uri
provider|decode_uri
uri|decode_uri
underlying|decode_uri, overlay_intersects, overlay_contains, overlay_touches, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint
decodes|decode_uri, from_base64
available|decode_uri
describing|geometry_type
difference|age
needs|age
datetimes|age
extract|age
information|age
following|age
dates|age
yearmonthweekdayhourminutesecond|age
dimensional|relate
relationship|relate
extended|relate, extend
model|relate
vertices|reverse, densify_by_count, buffer_by_m, densify_by_distance, simplify_vw, simplify, num_points
reverses|reverse
reversing|reverse
circularstring|straight_distance_2d
direct|straight_distance_2d
euclidean|straight_distance_2d
elevation|project
projected|project, distance
azimuth|project, azimuth
bearing|project, extend
segments|buffer, simplify_vw, simplify
miter|buffer
cap|buffer
along|line_interpolate_point, line_locate_point
layers|overlay_nearest, map_credits
large|overlay_nearest, hausdorff_distance, simplify
slow|overlay_nearest
lot|overlay_nearest
hamming|hamming_distance
equates|hamming_distance, levenshtein, NULL
characters|hamming_distance, length, url_encode, left, right, min_length, max_length, wordwrap, ~
comparison|hamming_distance
positions|hamming_distance
planimetric|length, $length, $perimeter, length3D, perimeter, area
perimeter|$length, $perimeter, perimeter
project|$length, $perimeter, length3D, perimeter, area, project_color
settings|$length, $perimeter, length3D, perimeter, area
ellipsoid|$length, $perimeter, length3D, perimeter, area
border|$length
setting|$length, $perimeter
required|levenshtein
edit|levenshtein
indicate|levenshtein
similarity|levenshtein, hausdorff_distance
insertions|levenshtein
measure|levenshtein, hausdorff_distance, m_max, m_min, m
change|levenshtein
substitutions|levenshtein
edits|levenshtein
larger|levenshtein, densify_by_count
deletions|levenshtein
levenshtein|levenshtein
dissimilar|hausdorff_distance
densify|hausdorff_distance
linestrings|hausdorff_distance, line_merge, boundary
other|hausdorff_distance, concat, to_json
total|hausdorff_distance
close|hausdorff_distance, roundness
executed|hausdorff_distance
specifying|hausdorff_distance
occurs|hausdorff_distance
fraction|hausdorff_distance
testing|hausdorff_distance
discrete|hausdorff_distance
linear|hausdorff_distance, scale_linear
approximate|hausdorff_distance, pole_of_inaccessibility
split|hausdorff_distance, string_to_array
make|hausdorff_distance
approach|hausdorff_distance, pole_of_inaccessibility
examples|hausdorff_distance
provided|hausdorff_distance, color_grayscale_average, color_mix_rgb, to_time, to_date, to_datetime, raster_value, rand, randf, try, array_sort
performs|hausdorff_distance, ~
insufficient|hausdorff_distance
networks|hausdorff_distance
specify|hausdorff_distance
decreasing|hausdorff_distance
approximation|hausdorff_distance
cases|hausdorff_distance
densification|hausdorff_distance
computing|hausdorff_distance
argument|hausdorff_distance, rand, randf, with_variable
subsegments|hausdorff_distance
hausdorff|hausdorff_distance
exact|hausdorff_distance
indicating|hausdorff_distance
subset|hausdorff_distance
division|%, /
remainder|%
downwards|floor
rounds|floor, ceil, round
dynamic|eval, eval_template
fields|eval, eval_template
parameters|eval, eval_template, map
expression|eval, ~
expand|eval, eval_template
context|eval, eval_template, current_parent_value
passed|eval, eval_template, datetime_from_epoch, map, line_merge
variables|eval, eval_template, item_variables, env
template|eval_template
elements|array_length, map_to_hstore, array_sort
empty|concat, is_empty_or_null, is_empty
is_empty|is_empty_or_null
coordinates|is_empty_or_null, is_empty, flip_coordinates
false|is_empty_or_null, is_empty, is_closed
is_empty_or_null|is_empty
enclosing|minimal_circle
minimal|minimal_circle, oriented_bbox, main_angle
encloses|minimal_circle, convex_hull
circle|minimal_circle, roundness
smallest|minimal_circle, min
encoded|url_encode
producing|url_encode
query|url_encode
plus|url_encode
url|url_encode
compliant|url_encode
sign|url_encode
transforms|url_encode, scale_exp, scale_linear
encoding|from_base64, to_base64
encodes|to_base64
display|display_expression
maptip|maptip
iterate|array_foreach
item|array_foreach, $map, item_variables, map_credits
selected|num_selected, is_selected
exif|exif, exif_geotag
tag|exif
file|exif, file_name, file_suffix, exif_geotag, file_path, file_exists, is_file, file_size, base_file_name
image|exif, exif_geotag
exponential|exp, scale_exp
ease|scale_exp
domain|scale_exp, scale_linear
range|scale_exp, iqr, range, rand, randf, clamp, scale_linear
name|file_name, file_path, base_file_name
directory|file_name, is_directory, file_path, base_file_name
path|file_name, file_suffix, env, is_directory, file_path, file_exists, is_file, base_file_name
suffix|file_suffix, base_file_name
convention|force_polygon_ccw, force_polygon_cw
hours|hour, make_interval, to_interval
hour|hour, make_time, make_datetime
datetime|hour, second, make_datetime, minute, datetime_from_epoch, to_datetime, day_of_week
seconds|second, make_interval
actual|current_parent_value, current_value
unsaved|current_parent_value, current_value
wrapped|current_parent_value, wordwrap
retrieve|current_parent_value
differ|current_parent_value, current_value
edited|current_parent_value, current_value
embedded|current_parent_value
coalesce|current_parent_value
filter|current_parent_value, color_grayscale_average
usable|current_parent_value
inter|iqr
statistics|iqr, raster_statistic
aggregates|iqr
summed|sum
grayscale|color_grayscale_average
node|start_point, end_point, point_n, nodes_to_points
closed|close_line, is_closed
appending|close_line
multipoint|$x, $y, $z, nodes_to_points
altitude|$z
3D|$z
substring|left, right, longest_common_substring, regexp_match, strpos
leftmost|left
formatted|map_to_hstore, hstore_to_map, to_json, format_number, from_json
hstore|map_to_hstore, hstore_to_map
json|to_json, from_json
create|to_json, simplify_vw
truncates|format_number
places|format_number, round
separator|format_number
thousands|format_number
locale|format_number
language|format_number
original|densify_by_count
geometric|centroid
center|centroid
geotags|exif_geotag
green|color_rgba, color_mix_rgb, color_rgb
blue|color_rgba, color_mix_rgb, color_rgb
mixing|color_mix_rgb
colors|color_mix_rgb
hash|md5, sha256, hash
hex|hash
bytes|hash, file_size
byte|hash
digits|hash
long|hash, main_angle
bits|hash
produces|hash
hull|convex_hull
convex|convex_hull
inaccessibility|pole_of_inaccessibility
precise|pole_of_inaccessibility
tolerances|pole_of_inaccessibility
calculates|pole_of_inaccessibility, length3D, roundness
guaranteed|pole_of_inaccessibility
true|pole_of_inaccessibility
iterations|pole_of_inaccessibility
internal|pole_of_inaccessibility
polylabel|pole_of_inaccessibility
distant|pole_of_inaccessibility
pole|pole_of_inaccessibility
take|pole_of_inaccessibility, to_interval
surface|pole_of_inaccessibility, area, point_on_surface
tolerance|pole_of_inaccessibility
iterative|pole_of_inaccessibility
hole|interior_ring_n
intersected|overlay_intersects
least|overlay_intersects, minority, overlay_contains, overlay_touches, min
predicate|overlay_intersects, overlay_contains, overlay_touches, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint
geos|overlay_intersects, overlay_contains, overlay_touches, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint
postgis|overlay_intersects, overlay_contains
described|overlay_intersects, overlay_contains, overlay_touches, overlay_within, overlay_equals, overlay_crosses, overlay_disjoint
st_intersects|overlay_intersects
intersects|overlay_intersects, intersects
milliseconds|epoch, datetime_from_epoch
epoch|epoch
loads|from_json
rightmost|right
latitude|flip_coordinates
longitude|flip_coordinates
swapped|flip_coordinates
repairing|flip_coordinates
copy|flip_coordinates
layout|$map, item_variables, $page, map_credits
drawn|$map
main|$map
print|$map, item_variables, $page
window|$map
overview|$map
page|$page
occurring|minority, majority
contained|overlay_contains, IN, overlaps
st_contains|overlay_contains
touches|overlay_touches, touches
touched|overlay_touches
st_touches|overlay_touches
padded|lpad, rpad
width|lpad, rpad, bounds_width
truncated|lpad, rpad
fill|lpad, rpad
letter|title
words|title
leading|title, trim
capital|title
title|title
lie|contains, point_on_surface
lies|contains
within|contains
according|buffer_by_m, is_valid
varies|buffer_by_m, tapered_buffer
diameter|buffer_by_m, tapered_buffer
list|array, IN, coalesce, map_credits
rights|map_credits
credit|map_credits
longest|max, longest_common_substring
biggest|max
most|max
largest|max
overridden|map_insert
gradient|create_ramp
steps|create_ramp
ramp|create_ramp, ramp_color
edges|densify_by_distance
densified|densify_by_distance
multiline|wordwrap
vertical|azimuth
year|make_datetime, make_interval, make_date, year
weeks|make_interval, week
minutes|minute
multiplication|*
natural|ln
negates|NOT
operating|env
content|env
prefixes|env
gets|env
drive|env
check|env, if
environment|env
inject|env
configuration|env
administrator|env
variable|env, var, with_variable
documentation|env, to_time, to_date, to_datetime
handy|env
covers|main_angle
rectangle|main_angle, make_rectangle_3points
axis|main_angle
outer|make_polygon
inner|make_polygon
clip|difference
collects|collect_geometries
object|collect_geometries, length3D, perimeter, to_time, to_date, to_datetime
localtime|datetime_from_epoch
msecs|datetime_from_epoch
coordinated|datetime_from_epoch
universal|datetime_from_epoch
pair|map
single|line_merge
merged|line_merge
connected|line_merge
folder|is_directory, file_path, base_file_name
differs|length3D, perimeter
units|length3D, perimeter, area, distance
interiors|touches
overlay|point_on_surface
coincident|is_closed
elliptical|make_ellipse
representing|exterior_ring, ramp_color
instance|boundary
combinatorial|boundary
topological|boundary
collections|boundary
types|boundary
closure|boundary
perfect|roundness
flat|roundness
shape|roundness
portions|sym_difference
power|^
equals|overlay_equals, nullif
st_equals|overlay_equals
st_crosses|overlay_crosses
crossed|overlay_crosses
st_disjoint|overlay_disjoint
disjoint|overlay_disjoint
prefixed|map_prefix_keys
property|layer_property
metadata|layer_property
parse|to_time, to_date, to_datetime
fromstring|to_time, to_date, to_datetime
qtime|to_time, to_datetime
user|to_date, to_datetime
format_date|to_date, to_datetime
qdate|to_date, to_datetime
raster|raster_value, raster_statistic
random|rand, randf
inclusive|rand, randf
seed|rand, randf
depending|rand, randf, if
float|randf
removes|trim, simplify_vw
whitespace|trim
spaces|trim
tabs|trim
trailing|trim
tries|try
error|try
alternative|try
exception|try
holes|num_interior_rings, num_rings
including|num_rings
root|sqrt
square|sqrt, make_square, square_wave, square_wave_randomized
rules|is_valid
valid|is_valid
ogc|is_valid
scheme|project_color
share|disjoint, intersects, overlaps
space|disjoint, intersects, overlaps, ~
dimension|overlaps
shared|intersection
sine|sin, asin, wave, wave_randomized
size|file_size
sorted|array_sort, array_prioritize
ordering|array_prioritize
offsetting|offset_curve
translated|translate
displace|translate
move|translate
restricts|clamp
visible|is_layer_visible
spikes|simplify_vw
areas|simplify_vw
simplifies|simplify_vw, simplify
narrow|simplify_vw
visvalingam|simplify_vw
threshold|simplify_vw, simplify
removing|simplify_vw, simplify
based|simplify_vw, simplify
small|simplify_vw
convert|string_to_array
divides|string_to_array
diagonal|make_square
amount|extend
lines|extend
extends|extend
resultant|shortest_line
joining|shortest_line
shortest|shortest_line
static|now
evaluating|now
stored|var
deviations|simplify
reduces|simplify
preserves|simplify
substitute|nullif
subtraction|-
signs|atan2
quadrant|atan2
completely|within
conditional|if
text|geom_from_wkt, geom_to_wkt
wkt|geom_from_wkt, geom_to_wkt
srid|geom_to_wkt
third|q3
interpolation|scale_linear
triangle|make_triangle
dissolve|union
value|with_variable
scaled|scale
rotated|rotate
waves|triangular_wave_randomized, triangular_wave, square_wave, square_wave_randomized, wave, wave_randomized
constructs|triangular_wave_randomized, triangular_wave, square_wave, square_wave_randomized, wave, wave_randomized
randomized|triangular_wave_randomized, square_wave_randomized, wave_randomized
triangular|triangular_wave_randomized, triangular_wave
rectangular|square_wave, square_wave_randomized
curved|wave_randomized
week|day_of_week, week
corresponds|day_of_week
ranges|day_of_week
saturday|day_of_week
white|~
backslash|~
escaped|~
years|year
zenith|inclination
nadir|inclination
inclination|inclination


[^1]: `>= QGIS 3.24`