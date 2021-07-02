Variabili
===================================

`Funzionalità`_ introdotta da Nyall Dawson nella QGIS 2.12

Questo gruppo contiene variabili dinamiche relative all'applicazione, al
file di progetto e ad altre impostazioni. Significa che alcune funzioni
potrebbero non essere disponibili in base al contesto:

\* seleziona per espressione |exp| 

\* calcolatore di campi |calc| 

\* geometry generator |epsilos|

\* proprietà del layer |mod|

\* compositore di stampe |print|

In QGIS, puoi utilizzare le variabili per memorizzare dati utili con valori ricorrenti (ad esempio il titolo del progetto o il nome completo dell’utente) che possono essere utilizzati nelle espressioni. Le variabili possono essere definite a livello globale dell’applicazione, a livello di progetto, a livello di layer, a livello di composizione e a livello di elemento del compositore. Proprio come le regole CSS a cascata, le variabili possono essere sovrascritte, ad esempio una variabile a livello di progetto sovrascrive le variabili di livello globale di qualsiasi applicazione impostate con lo stesso nome.

Puoi utilizzare queste variabili per creare stringhe di testo o altre espressioni personalizzate utilizzando il carattere @ prima del nome della variabile.

Riguardano:

+---------------------+-----------------------+-----------------------+
| Funzione            | Descrizione           | applicazione          |
+=====================+=======================+=======================+
| `atlas_feature`_    | Ritorna la geometria  | proprietà del layer,  |
|                     | attuale dell'atlante  | geometry generator    |
|                     | (come oggetto         |                       |
|                     | geometria)            |                       |
+---------------------+-----------------------+-----------------------+
| `atlas_featureid`_  | Ritorna ID della      | proprietà del layer,  |
|                     | geometria attuale     | geometry generator    |
|                     | dell'atlante          |                       |
+---------------------+-----------------------+-----------------------+
| `atlas_featurenumbe | Returns the current   |
| r`_                 | atlas feature number  |
|                     | in the layout         |
+---------------------+-----------------------+-----------------------+
| `atlas_filename`_   | Returns the current   |
|                     | atlas file name       |
+---------------------+-----------------------+-----------------------+
| `atlas_geometry`_   | Returns the current   | proprietà del layer,  |
|                     | atlas feature         | geometry generator    |
|                     | geometry              |                       |
+---------------------+-----------------------+-----------------------+
| `atlas_layerid`_    | Returns the current   |
|                     | atlas coverage layer  |
|                     | ID                    |
+---------------------+-----------------------+-----------------------+
| `atlas_layername`_  | Returns the current   |
|                     | atlas coverage layer  |
|                     | name                  |
+---------------------+-----------------------+-----------------------+
| `atlas_pagename`_   | Returns the current   | proprietà del layer,  |
|                     | atlas page name       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `atlas_totalfeature | Returns the total     |
| s`_                 | number of features in |
|                     | atlas                 |
+---------------------+-----------------------+-----------------------+
| `cluster_color`_    | Returns the color of  |
|                     | symbols within a      |
|                     | cluster, or NULL if   |
|                     | symbols have mixed    |
|                     | colors                |
+---------------------+-----------------------+-----------------------+
| `cluster_size`_     | Returns the number of |
|                     | symbols contained     |
|                     | within a cluster      |
+---------------------+-----------------------+-----------------------+
| `geometry_part_coun | Returns the number of | proprietà del layer,  |
| t`_                 | parts in rendered     | geometry generator    |
|                     | feature’s geometry    |                       |
+---------------------+-----------------------+-----------------------+
| `geometry_part_num` | Returns the current   | proprietà del layer,  |
| _                   | geometry part number  | geometry generator    |
|                     | for feature being     |                       |
|                     | rendered              |                       |
+---------------------+-----------------------+-----------------------+
| `geometry_point_cou | Returns the number of | proprietà del layer,  |
| nt`_                | points in the         | geometry generator    |
|                     | rendered geometry’s   |                       |
|                     | part                  |                       |
+---------------------+-----------------------+-----------------------+
| `geometry_point_num | Returns the current   | proprietà del layer,  |
| `_                  | point number in the   | geometry generator    |
|                     | rendered geometry’s   |                       |
|                     | part                  |                       |
+---------------------+-----------------------+-----------------------+
| `grid_axis`_        | Returns the current   |
|                     | grid annotation axis  |
|                     | (eg, ‘x’ for          |
|                     | longitude, ‘y’ for    |
|                     | latitude)             |
+---------------------+-----------------------+-----------------------+
| `grid_number`_      | Returns the current   |
|                     | grid annotation value |
+---------------------+-----------------------+-----------------------+
| `item_id`_          | Returns the layout    |
|                     | item user ID (not     |
|                     | necessarily unique)   |
+---------------------+-----------------------+-----------------------+
| `item_uuid`_        | Returns the layout    |
|                     | item unique ID        |
+---------------------+-----------------------+-----------------------+
| `layer`_            | Returns the current   | Calcolatore di        |
|                     | layer                 | campi,Seleziona per   |
|                     |                       | espressione,proprietà |
|                     |                       | del layer, geometry   |
|                     |                       | generator             |
+---------------------+-----------------------+-----------------------+
| `layer_id`_         | Returns the ID of     | Calcolatore di        |
|                     | current layer         | campi,Seleziona per   |
|                     |                       | espressione,proprietà |
|                     |                       | del layer, geometry   |
|                     |                       | generator             |
+---------------------+-----------------------+-----------------------+
| `layer_name`_       | Returns the name of   |
|                     | current               |
|                     | layer,proprietà del   |
|                     | layer, geometry       |
|                     | generator             |
+---------------------+-----------------------+-----------------------+
| `layout_dpi`_       | Returns the           |
|                     | composition           |
|                     | resolution (DPI)      |
+---------------------+-----------------------+-----------------------+
| `layout_name`_      | Returns the layout    | Calcolatore di        |
|                     | name                  | campi,Seleziona per   |
|                     |                       | espressione           |
+---------------------+-----------------------+-----------------------+
| `layout_numpages`_  | Returns the number of |
|                     | pages in the layout   |
+---------------------+-----------------------+-----------------------+
| `layout_page`_      | Returns the page      |
|                     | number of the current |
|                     | item in the layout    |
+---------------------+-----------------------+-----------------------+
| `layout_pageheight` | Returns the active    |
| _                   | page height in the    |
|                     | layout (in mm)        |
+---------------------+-----------------------+-----------------------+
| `layout_pagewidth`_ | Returns the active    |
|                     | page width in the     |
|                     | layout (in mm)        |
+---------------------+-----------------------+-----------------------+
| `map_crs`_          | Returns the           | proprietà del layer,  |
|                     | Coordinate reference  | geometry generator    |
|                     | system of the current |                       |
|                     | map                   |                       |
+---------------------+-----------------------+-----------------------+
| `map_crs_definition | Returns the full      | proprietà del layer,  |
| `_                  | definition of the     | geometry generator    |
|                     | Coordinate reference  |                       |
|                     | system of the current |                       |
|                     | map                   |                       |
+---------------------+-----------------------+-----------------------+
| `map_extent`_       | Returns the geometry  | proprietà del layer,  |
|                     | representing the      | geometry generator    |
|                     | current extent of the |                       |
|                     | map                   |                       |
+---------------------+-----------------------+-----------------------+
| `map_extent_center` | Returns the point     | proprietà del layer,  |
| _                   | feature at the center | geometry generator    |
|                     | of the map            |                       |
+---------------------+-----------------------+-----------------------+
| `map_extent_height` | Returns the current   | proprietà del layer,  |
| _                   | height of the map     | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `map_extent_width`_ | Returns the current   | proprietà del layer,  |
|                     | width of the map      | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `map_id`_           | Returns the ID of     | proprietà del layer,  |
|                     | current map           | geometry generator    |
|                     | destination. This     |                       |
|                     | will be ‘canvas’ for  |                       |
|                     | canvas renders, and   |                       |
|                     | the item ID for       |                       |
|                     | layout map renders    |                       |
+---------------------+-----------------------+-----------------------+
| `map_rotation`_     | Returns the current   | proprietà del layer,  |
|                     | rotation of the map   | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `map_scale`_        | Returns the current   | proprietà del layer,  |
|                     | scale of the map      | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `map_units`_        | Returns the units of  | proprietà del layer,  |
|                     | map measurements      | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `parent`_           | Returns attributes    |
|                     | and geometry from the |
|                     | parent feature when   |
|                     | in the filter of the  |
|                     | “aggregate”           |
|                     | expression function   |
+---------------------+-----------------------+-----------------------+
| `project_abstract`_ | Returns the project   |
|                     | abstract, taken from  |
|                     | project metadata      |
+---------------------+-----------------------+-----------------------+
| `project_author`_   | Returns the project   |
|                     | author, taken from    |
|                     | project metadata      |
+---------------------+-----------------------+-----------------------+
| `project_creation_d | Returns the project   |
| ate`_               | creation date, taken  |
|                     | from project metadata |
+---------------------+-----------------------+-----------------------+
| `project_identifier | Returns the project   |
| `_                  | identifier, taken     |
|                     | from project metadata |
+---------------------+-----------------------+-----------------------+
| `project_keywords`_ | Returns the project   |
|                     | keywords, taken from  |
|                     | project metadata      |
+---------------------+-----------------------+-----------------------+
| `project_crs`_      | Returns the           | Calcolatore di        |
|                     | Coordinate reference  | campi,Seleziona per   |
|                     | system of the project | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `project_crs_defini | Returns the full      | Calcolatore di        |
| tion`_              | definition of the     | campi,Seleziona per   |
|                     | Coordinate reference  | espressione           |
|                     | system of the project |                       |
+---------------------+-----------------------+-----------------------+
| `project_filename`_ | Returns the filename  | Calcolatore di        |
|                     | of current project    | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `project_folder`_   | Returns the folder    | Calcolatore di        |
|                     | for current project   | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `project_path`_     | Returns the full path | Calcolatore di        |
|                     | (including file name) | campi,Seleziona per   |
|                     | of current project    | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `project_title`_    | Returns the title of  | Calcolatore di        |
|                     | current project       | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `qgis_locale`_      | Returns the current   | Calcolatore di        |
|                     | language of QGIS      | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `qgis_os_name`_     | Returns the current   | Calcolatore di        |
|                     | Operating system      | campi,Seleziona per   |
|                     | name, eg ‘windows’,   | espressione,          |
|                     | ‘linux’ or ‘osx’      | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `qgis_platform`_    | Returns QGIS          | Calcolatore di        |
|                     | platform, eg          | campi,Seleziona per   |
|                     | ‘desktop’ or ‘server’ | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `qgis_release_name` | Returns current QGIS  | Calcolatore di        |
| _                   | release name          | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `qgis_short_version | Returns current QGIS  | Calcolatore di        |
| `_                  | version short string  | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `qgis_version`_     | Returns current QGIS  | Calcolatore di        |
|                     | version string        | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `qgis_version_no`_  | Returns current QGIS  | Calcolatore di        |
|                     | version number        | campi,Seleziona per   |
|                     |                       | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `snapping_results`_ | Gives access to       |
|                     | snapping results      |
|                     | while digitizing a    |
|                     | feature (only         |
|                     | available in add      |
|                     | feature)              |
+---------------------+-----------------------+-----------------------+
| `symbol_angle`_     | Returns the angle of  | proprietà del layer,  |
|                     | the symbol used to    | geometry generator    |
|                     | render the feature    |                       |
|                     | (valid for marker     |                       |
|                     | symbols only)         |                       |
+---------------------+-----------------------+-----------------------+
| `symbol_color`_     | Returns the color of  | proprietà del layer,  |
|                     | the symbol used to    | geometry generator    |
|                     | render the feature    |                       |
+---------------------+-----------------------+-----------------------+
| `user_account_name` | Returns the current   | Calcolatore di        |
| _                   | user’s operating      | campi,Seleziona per   |
|                     | system account name   | espressione           |
+---------------------+-----------------------+-----------------------+
| `user_full_name`_   | Returns the current   | Calcolatore di        |
|                     | user’s operating      | campi,Seleziona per   |
|                     | system user name      | espressione,          |
|                     |                       | proprietà del layer,  |
|                     |                       | geometry generator    |
+---------------------+-----------------------+-----------------------+
| `row_number`_       | Memorizza il numero   | calcolatore campi     |
|                     | della riga corrente   |                       |
+---------------------+-----------------------+-----------------------+
| `value`_            | Returns the current   |
|                     | value                 |
+---------------------+-----------------------+-----------------------+
| `with_variable`_    | Allows setting a      |
|                     | variable for usage    |
|                     | within an expression  |
|                     | and avoid             |
|                     | recalculating the     |
|                     | same value repeatedly |
+---------------------+-----------------------+-----------------------+


Gruppo sul calcolatore di campi,Seleziona per espressione 

|image0|

Geometry generator - stile  |epsilos| 

|image2|

Selezione per espressione  |exp|

|image4|

Calcolatore di campi,Seleziona per espressione  |calc| 

|image6|

Compositore di stampe  |print|

|image8|

.. _atlas_feature: atlas_feature.html
.. _atlas_featureid: atlas_featureid.html
.. _atlas_featurenumber: atlas_featurenumber.html
.. _atlas_filename: atlas_filename.html
.. _atlas_geometry: atlas_geometry.html
.. _atlas_layerid: atlas_layerid.html
.. _atlas_layername: atlas_layername.html
.. _atlas_pagename: atlas_pagename.html
.. _atlas_totalfeatures: atlas_totalfeatures.html
.. _cluster_color: cluster_color.html
.. _cluster_size: cluster_size.html
.. _geometry_part_count: geometry_part_count.html
.. _geometry_part_num: geometry_part_num.html
.. _geometry_point_count: geometry_point_count.html
.. _geometry_point_num: geometry_point_num.html
.. _grid_axis: grid_axis.html
.. _grid_number: grid_number.html
.. _item_id: item_id.html
.. _item_uuid: item_uuid.html
.. _layer: layer.html
.. _layer_id: layer_id.html
.. _layer_name: layer_name.html
.. _layout_dpi: layout_dpi.html
.. _layout_name: layout_name.html
.. _layout_numpages: layout_numpages.html
.. _layout_page: layout_page.html
.. _layout_pageheight: layout_pageheight.html
.. _layout_pagewidth: layout_pagewidth.html
.. _map_crs: map_crs.html
.. _map_crs_definition: map_crs_definition.html
.. _map_extent: map_extent.html
.. _map_extent_center: map_extent_center.html
.. _map_extent_height: map_extent_height.html
.. _map_extent_width: map_extent_width.html
.. _map_id: map_id.html
.. _map_rotation: map_rotation.html
.. _map_scale: map_scale.html
.. _map_units: map_units.html
.. _parent: parent.html
.. _project_abstract: project_abstract.html
.. _project_author: project_author.html
.. _project_creation_date: project_creation_datemd
.. _project_identifier: project_identifier.html
.. _project_keywords: project_keywords.html
.. _project_crs: project_crs.html
.. _project_crs_definition: project_crs_definition.html
.. _project_filename: project_filename.html
.. _project_folder: project_folder.html
.. _project_path: project_path.html
.. _project_title: project_title.html
.. _qgis_locale: qgis_locale.html
.. _qgis_os_name: qgis_os_name.html
.. _qgis_platform: qgis_platform.html
.. _qgis_release_name: qgis_release_name.html
.. _qgis_short_version: qgis_short_version.html
.. _qgis_version: qgis_version.html
.. _qgis_version_no: qgis_version_no.html
.. _snapping_results: snapping_results.html
.. _symbol_angle: symbol_angle.html
.. _symbol_color: symbol_color.html
.. _user_account_name: user_account_name.html
.. _user_full_name: user_full_name.html
.. _row_number: row_number.html
.. _value: value.html
.. _with_variable: with_variable.html

.. _Funzionalità: http://nyalldawson.net/2015/12/exploring-variables-in-qgis-2-12-part-1/

.. |exp| image:: https://docs.qgis.org/testing/en/_images/mIconExpressionSelect.png
.. |calc| image:: https://docs.qgis.org/testing/en/_images/mActionCalculateField.png
.. |epsilos| image:: https://docs.qgis.org/testing/en/_images/mIconExpression.png
.. |mod| image:: https://docs.qgis.org/testing/en/_images/mIconDataDefine.png
.. |print| image:: https://docs.qgis.org/testing/en/_images/mActionNewLayout.png
.. |image0| image:: /img/variabili/gruppo_variabili1.png
.. |epsilos| image:: https://docs.qgis.org/testing/en/_images/mIconExpression.png
.. |image2| image:: /img/variabili/gruppo_variabili2.png
.. |exp| image:: https://docs.qgis.org/testing/en/_images/mIconExpressionSelect.png
.. |image4| image:: /img/variabili/gruppo_variabili3.png
.. |calc| image:: https://docs.qgis.org/testing/en/_images/mActionCalculateField.png
.. |image6| image:: /img/variabili/gruppo_variabili4.png
.. |print| image:: https://docs.qgis.org/testing/en/_images/mActionNewLayout.png
.. |image8| image:: /img/variabili/gruppo_variabili5.png

.. toctree::
   :maxdepth: 3
   :hidden:
   
   atlas_feature
   atlas_featureid
   atlas_featurenumber
   atlas_filename
   atlas_geometry
   atlas_layerid
   atlas_layername
   atlas_pagename
   atlas_totalfeatures
   cluster_color
   cluster_size
   geometry_part_count
   geometry_part_num
   geometry_point_count
   geometry_point_num
   grid_axis
   grid_number
   item_id
   item_uuid
   layer
   layer_id
   layer_name
   layout_dpi
   layout_name
   layout_numpages
   layout_page
   layout_pageheight
   layout_pagewidth
   map_crs
   map_crs_definition
   map_extent
   map_extent_center
   map_extent_height
   map_extent_width
   map_id
   map_rotation
   map_scale
   map_units
   parent
   project_abstract
   project_author
   project_creation_date
   project_crs
   project_crs_definition
   project_filename
   project_folder
   project_identifier
   project_keywords
   project_path
   project_title
   qgis_locale
   qgis_os_name
   qgis_platform
   qgis_release_name
   qgis_short_version
   qgis_version
   qgis_version_no
   row_number
   snapping_results
   symbol_angle
   symbol_color
   user_account_name
   user_full_name
   value
   value
   
