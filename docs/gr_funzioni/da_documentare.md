# Vuoi documentare una variabile? Ecco quelle ancora non pronte


Al momento sono circa **130**


Variable|Description
--------|-----------
[algorithm_id](./variabili/algorithm_id.md)|The unique ID of an algorithm
[animation_end_time](./variabili/animation_end_time.md)|End of the animation’s overall temporal time range (as a datetime value)
[animation_interval](./variabili/animation_interval.md)|Duration of the animation’s overall temporal time range (as an interval value)
[animation_start_time](./variabili/animation_start_time.md)|Start of the animation’s overall temporal time range (as a datetime value)
[atlas_feature](./variabili/atlas_feature.md)|The current atlas feature (as feature object)
[atlas_featureid](./variabili/atlas_featureid.md)|The current atlas feature ID
[atlas_featurenumber](./variabili/atlas_featurenumber.md)|The current atlas feature number in the layout
[atlas_filename](./variabili/atlas_filename.md)|The current atlas file name
[atlas_geometry](./variabili/atlas_geometry.md)|The current atlas feature geometry
[atlas_layerid](./variabili/atlas_layerid.md)|The current atlas coverage layer ID
[atlas_layername](./variabili/atlas_layername.md)|The current atlas coverage layer name
[atlas_pagename](./variabili/atlas_pagename.md)|The current atlas page name
[atlas_totalfeatures](./variabili/atlas_totalfeatures.md)|The total number of features in atlas
[canvas_cursor_point](./variabili/canvas_cursor_point.md)|The last cursor position on the canvas in the project’s geographical coordinates
[cluster_color](./variabili/cluster_color.md)|The color of symbols within a cluster, or NULL if symbols have mixed colors
[cluster_size](./variabili/cluster_size.md)|The number of symbols contained within a cluster
[current_feature](./variabili/current_feature.md)|The feature currently being edited in the attribute form or table row
[current_geometry](./variabili/current_geometry.md)|The geometry of the feature currently being edited in the form or the table row
[current_parent_feature](./variabili/current_parent_feature.md)|represents the feature currently being edited in the parent form. Only usable in an embedded form context.
[current_parent_geometry](./variabili/current_parent_geometry.md)|represents the geometry of the feature currently being edited in the parent form. Only usable in an embedded form context.
[form_mode](./variabili/form_mode.md)|What the form is used for, like AddFeatureMode, SingleEditMode, MultiEditMode, SearchMode, AggregateSearchMode or IdentifyMode as string.
[frame_duration](./variabili/frame_duration.md)|Temporal duration of each animation frame (as an interval value)
[frame_number](./variabili/frame_number.md)|Current frame number during animation playback
[frame_rate](./variabili/frame_rate.md)|Number of frames per second during animation playback
[fullextent_maxx](./variabili/fullextent_maxx.md)|Maximum x value from full canvas extent (including all layers)
[fullextent_maxy](./variabili/fullextent_maxy.md)|Maximum y value from full canvas extent (including all layers)
[fullextent_minx](./variabili/fullextent_minx.md)|Minimum x value from full canvas extent (including all layers)
[fullextent_miny](./variabili/fullextent_miny.md)|Minimum y value from full canvas extent (including all layers)
[geometry_part_count](./variabili/geometry_part_count.md)|The number of parts in rendered feature’s geometry
[geometry_part_num](./variabili/geometry_part_num.md)|The current geometry part number for feature being rendered
[geometry_point_count](./variabili/geometry_point_count.md)|The number of points in the rendered geometry’s part
[geometry_point_num](./variabili/geometry_point_num.md)|The current point number in the rendered geometry’s part
[geometry_ring_num](./variabili/geometry_ring_num.md)|Current geometry ring number for feature being rendered (for polygon features only). The exterior ring has a value of 0.
[grid_axis](./variabili/grid_axis.md)|The current grid annotation axis (eg, ‘x’ for longitude, ‘y’ for latitude)
[grid_number](./variabili/grid_number.md)|The current grid annotation value
[item_id](./variabili/item_id.md)|The layout item user ID (not necessarily unique)
[item_uuid](./variabili/item_uuid.md)|The layout item unique ID
[layer](./variabili/layer.md)|The current layer
[layer_crs](./variabili/layer_crs.md)|The Coordinate Reference System Authority ID of the current layer
[layer_id](./variabili/layer_id.md)|The ID of current layer
[layer_ids](./variabili/layer_ids.md)|The IDs of all the map layers in the current project as a list
[layer_name](./variabili/layer_name.md)|The name of current layer
[layers](./variabili/layers.md)|All the map layers in the current project as a list
[layout_dpi](./variabili/layout_dpi.md)|The composition resolution (DPI)
[layout_name](./variabili/layout_name.md)|The layout name
[layout_numpages](./variabili/layout_numpages.md)|The number of pages in the layout
[layout_page](./variabili/layout_page.md)|The page number of the current item in the layout
[layout_pageheight](./variabili/layout_pageheight.md)|The active page height in the layout (in mm for standard paper sizes, or whatever unit was used for custom paper size)
[layout_pageoffsets](./variabili/layout_pageoffsets.md)|Array of Y coordinate of the top of each page. Allows to dynamically position items on pages in a context where page sizes may change
[layout_pagewidth](./variabili/layout_pagewidth.md)|The active page width in the layout (in mm for standard paper sizes, or whatever unit was used for custom paper size)
[legend_column_count](./variabili/legend_column_count.md)|The number of columns in the legend
[legend_filter_by_map](./variabili/legend_filter_by_map.md)|Indicates if the content of the legend is filtered by the map
[legend_filter_out_atlas](./variabili/legend_filter_out_atlas.md)|Indicates if the atlas is filtered out of the legend
[legend_split_layers](./variabili/legend_split_layers.md)|Indicates if layers can be split in the legend
[legend_title](./variabili/legend_title.md)|The title of the legend
[legend_wrap_string](./variabili/legend_wrap_string.md)|The character(s) used to wrap the legend text
[map_crs](./variabili/map_crs.md)|The Coordinate reference system of the current map
[map_crs_acronym](./variabili/map_crs_acronym.md)|The acronym of the Coordinate reference system of the current map
[map_crs_definition](./variabili/map_crs_definition.md)|The full definition of the Coordinate reference system of the current map
[map_crs_description](./variabili/map_crs_description.md)|The name of the Coordinate reference system of the current map
[map_crs_ellipsoid](./variabili/map_crs_ellipsoid.md)|The acronym of the ellipsoid of the Coordinate reference system of the current map
[map_crs_proj4](./variabili/map_crs_proj4.md)|The Proj4 definition of the Coordinate reference system of the current map
[map_crs_projection](./variabili/map_crs_projection.md)|The descriptive name of the projection method used by the Coordinate reference system of the map (e.g. ‘Albers Equal Area’)
[map_crs_wkt](./variabili/map_crs_wkt.md)|The WKT definition of the Coordinate reference system of the current map
[map_end_time](./variabili/map_end_time.md)|The end of the map’s temporal time range (as a datetime value)
[map_extent](./variabili/map_extent.md)|The geometry representing the current extent of the map
[map_extent_center](./variabili/map_extent_center.md)|The point feature at the center of the map
[map_extent_height](./variabili/map_extent_height.md)|The current height of the map
[map_extent_width](./variabili/map_extent_width.md)|The current width of the map
[map_id](./variabili/map_id.md)|The ID of current map destination. This will be ‘canvas’ for canvas renders, and the item ID for layout map renders
[map_interval](./variabili/map_interval.md)|The duration of the map’s temporal time range (as an interval value)
[map_layer_ids](./variabili/map_layer_ids.md)|The list of map layer IDs visible in the map
[map_layers](./variabili/map_layers.md)|The list of map layers visible in the map
[map_rotation](./variabili/map_rotation.md)|The current rotation of the map
[map_scale](./variabili/map_scale.md)|The current scale of the map
[map_start_time](./variabili/map_start_time.md)|The start of the map’s temporal time range (as a datetime value)
[map_units](./variabili/map_units.md)|The units of map measurements
[model_path](./variabili/model_path.md)|Full path (including file name) of current model (or project path if model is embedded in a project).
[model_folder](./variabili/model_folder.md)|Folder containing current model (or project folder if model is embedded in a project).
[model_name](./variabili/model_name.md)|Name of current model
[model_group](./variabili/model_group.md)|Group for current model
[notification_message](./variabili/notification_message.md)|Content of the notification message sent by the provider (available only for actions triggered by provider notifications).
[parent](./variabili/parent.md)|Refers to the current feature in the parent layer, providing access to its attributes and geometry when filtering an aggregate function
[project_abstract](./variabili/project_abstract.md)|The project abstract, taken from project metadata
[project_area_units](./variabili/project_area_units.md)|The area unit for the current project, used when calculating areas of geometries
[project_author](./variabili/project_author.md)|The project author, taken from project metadata
[project_basename](./variabili/project_basename.md)|The basename of current project’s filename (without path and extension)
[project_creation_date](./variabili/project_creation_date.md)|The project creation date, taken from project metadata
[project_crs](./variabili/project_crs.md)|The Coordinate reference system of the project
[project_crs_arconym](./variabili/project_crs_arconym.md)|The acronym of the Coordinate reference system of the project
[project_crs_definition](./variabili/project_crs_definition.md)|The full definition of the Coordinate reference system of the project
[project_crs_description](./variabili/project_crs_description.md)|The description of the Coordinate reference system of the project
[project_crs_ellipsoid](./variabili/project_crs_ellipsoid.md)|The ellipsoid of the Coordinate reference system of the project
[project_crs_proj4](./variabili/project_crs_proj4.md)|The Proj4 representation of the Coordinate reference system of the project
[project_crs_wkt](./variabili/project_crs_wkt.md)|The WKT (well known text) representation of the coordinate reference system of the project
[project_distance_units](./variabili/project_distance_units.md)|The distance unit for the current project, used when calculating lengths of geometries and distances
[project_ellipsoid](./variabili/project_ellipsoid.md)|The name of the ellipsoid of the current project, used when calculating geodetic areas or lengths of geometries
[project_filename](./variabili/project_filename.md)|The filename of the current project
[project_folder](./variabili/project_folder.md)|The folder of the current project
[project_home](./variabili/project_home.md)|The home path of the current project
[project_identifier](./variabili/project_identifier.md)|The project identifier, taken from the project’s metadata
[project_keywords](./variabili/project_keywords.md)|The project keywords, taken from the project’s metadata
[project_last_saved](./variabili/project_last_saved.md)|Date/time when project was last saved.
[project_path](./variabili/project_path.md)|The full path (including file name) of the current project
[project_title](./variabili/project_title.md)|The title of current project
[project_units](./variabili/project_units.md)|The units of the project’s CRS
[qgis_locale](./variabili/qgis_locale.md)|The current language of QGIS
[qgis_os_name](./variabili/qgis_os_name.md)|The current Operating system name, eg ‘windows’, ‘linux’ or ‘osx’
[qgis_platform](./variabili/qgis_platform.md)|The QGIS platform, eg ‘desktop’ or ‘server’
[qgis_release_name](./variabili/qgis_release_name.md)|The current QGIS release name
[qgis_short_version](./variabili/qgis_short_version.md)|The current QGIS version short string
[qgis_version](./variabili/qgis_version.md)|The current QGIS version string
[qgis_version_no](./variabili/qgis_version_no.md)|The current QGIS version number
[row_number](./variabili/row_number.md)|Stores the number of the current row
[snapping_results](./variabili/snapping_results.md)|Gives access to snapping results while digitizing a feature (only available in add feature)
[scale_value](./variabili/scale_value.md)|The current scale bar distance value
[symbol_angle](./variabili/symbol_angle.md)|The angle of the symbol used to render the feature (valid for marker symbols only)
[symbol_color](./variabili/symbol_color.md)|The color of the symbol used to render the feature
[symbol_count](./variabili/symbol_count.md)|The number of features represented by the symbol (in the layout legend)
[symbol_id](./variabili/symbol_id.md)|The Internal ID of the symbol (in the layout legend)
[symbol_label](./variabili/symbol_label.md)|The label for the symbol (either a user defined label or the default autogenerated label - in the layout legend)
[symbol_layer_count](./variabili/symbol_layer_count.md)|Total number of symbol layers in the symbol
[symbol_layer_index](./variabili/symbol_layer_index.md)|Current symbol layer index
[symbol_marker_column](./variabili/symbol_marker_column.md)|Column number for marker (valid for point pattern fills only).
[symbol_marker_row](./variabili/symbol_marker_row.md)|Row number for marker (valid for point pattern fills only).
[user_account_name](./variabili/user_account_name.md)|The current user’s operating system account name
[user_full_name](./variabili/user_full_name.md)|The current user’s operating system user name
[value](./variabili/value.md)|The current value
[with_variable](./variabili/with_variable.md)|Allows setting a variable for usage within an expression and avoid recalculating the same value repeatedly
[zoom_level](./variabili/zoom_level.md)|Zoom level of the tile that is being rendered (derived from the current map scale). Normally in interval [0, 20].



<a href="https://www.paypal.me/pigrecoinfinito" target="_blank"><img width="400"  class="immagonobox" 
src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/sviluppo_funzioni.png" 
Title="La documentazione di queste funzioni non è stata ancora sviluppata. Se vuoi sostenerle fai una donazione con PayPal, scrivendo ..." 
alt="Donazione HfcQgis" style="margin: 0 auto; display: block;" /></a>

