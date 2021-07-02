Colore
===================================

Questo gruppo contiene le funzioni per manipolare i colori

+---------------------------------+------------------------------------+
| Funzione                        | Descrizione                        |
+=================================+====================================+
| `color_cmyk`_                   | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi componenti ciano, magenta,    |
|                                 | giallo e nero                      |
+---------------------------------+------------------------------------+
| `color_cmyka`_                  | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi componenti ciano, magenta,    |
|                                 | giallo, nero e alfa (trasparenza)  |
+---------------------------------+------------------------------------+
| `color_grayscale_average`_      | Applica un filtro in scala di      |
|                                 | grigio e restituisce una           |
|                                 | rappresentazione di stringa da un  |
|                                 | colore fornito QGIS >= 3.2         |
+---------------------------------+------------------------------------+
| `color_hsl`_                    | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi attributi tonalità,           |
|                                 | saturazione e luminosità.          |
+---------------------------------+------------------------------------+
| `color_hsla`_                   | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi attributi tonalità,           |
|                                 | saturazione, luminosità e alfa     |
|                                 | (trasparenza)                      |
+---------------------------------+------------------------------------+
| `color_hsv`_                    | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi attributi tonalità,           |
|                                 | saturazione e valore               |
+---------------------------------+------------------------------------+
| `color_hsva`_                   | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi attributi tonalità,           |
|                                 | saturazione, valore e alfa         |
|                                 | (trasparenza)                      |
+---------------------------------+------------------------------------+
| `color_mix_rgb`_                | Restituisce una stringa che        |
|                                 | rappresenta un colore che mescola  |
|                                 | i valori rosso, verde, blu e alfa  |
|                                 | di due colori forniti in base a un |
|                                 | determinato rapporto QGIS >= 3.2   |
+---------------------------------+------------------------------------+
| `color_part`_                   | Restituisce uno specifico          |
|                                 | componente colore da una stringa   |
|                                 | colore, es. la componente rosso o  |
|                                 | alfa                               |
+---------------------------------+------------------------------------+
| `color_rgb`_                    | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi componenti rosso, verde e blu |
+---------------------------------+------------------------------------+
| `color_rgba`_                   | Restituisce una rappresentazione   |
|                                 | stringa di un colore basato sui    |
|                                 | suoi componenti rosso, verde, blue |
|                                 | ed alpha (trasparenza)             |
+---------------------------------+------------------------------------+
| `create_ramp`_                  | Restituisce una scala di colori a  |
|                                 | gradiente per una mappa di colori  |
|                                 | e passi                            |
+---------------------------------+------------------------------------+
| `darker`_                       | Restituisce una stringa di colore  |
|                                 | più scuro (o più chiaro)           |
+---------------------------------+------------------------------------+
| `lighter`_                      | Restituisce una stringa di colore  |
|                                 | più chiaro (o più scuro)           |
+---------------------------------+------------------------------------+
| `project_color`_                | Restituisce un colore dallo schema |
|                                 | colore del progetto.               |
+---------------------------------+------------------------------------+
| `ramp_color`_                   | Restituisce una stringa            |
|                                 | rappresentante un colore ottenuto  |
|                                 | da una scala colore                |
+---------------------------------+------------------------------------+
| `set_color_part`_               | Imposta uno specifico componente   |
|                                 | colore per un stringa colore       |
+---------------------------------+------------------------------------+

|image0|

.. _color_cmyk: color_cmyk.html
.. _color_cmyka: color_cmyka.html
.. _color_grayscale_average: color_grayscale_average.html
.. _color_hsl: color_hsl.html
.. _color_hsla: color_hsla.html
.. _color_hsv: color_hsv.html
.. _color_hsva: color_hsva.html
.. _color_mix_rgb: color_mix_rgb.html
.. _color_part: color_part.html
.. _color_rgb: color_rgb.html
.. _color_rgba: color_rgba.html
.. _create_ramp: create_ramp.html
.. _darker: darker.html
.. _lighter: lighter.html
.. _project_color: project_color.html
.. _ramp_color: ramp_color.html
.. _set_color_part: set_color_part.html

.. |image0| image:: /img/colore/gruppo_colore1.png

**Elenco funzioni Colore**

.. toctree::
   :maxdepth: 3
   
   color_cmyk
   color_cmyka
   color_grayscale_average
   color_hsl
   color_hsla
   color_hsv
   color_hsva
   color_mix_rgb
   color_part
   color_rgb
   color_rgba
   create_ramp
   darker
   lighter
   project_color
   ramp_color
   set_color_part
   
