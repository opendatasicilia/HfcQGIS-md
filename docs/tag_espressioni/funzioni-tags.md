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
