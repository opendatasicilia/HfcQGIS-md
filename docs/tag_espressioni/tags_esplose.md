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
