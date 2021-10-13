# Estrarre un campo da un attributo HStore

Il formato HStore è molto usato nel database OpenStreetMap, leggi [qui](https://pigrecoinfinito.com/2021/10/12/qgis-e-il-formato-hstore/).

In questo esempio estrarremo dall'attributo `other_tags` il valore della chiave `population`, il dataset è [qui](https://download.geofabrik.de/europe/italy/isole.html)

[![](https://pigrecoinfinito.files.wordpress.com/2021/10/image-14.png)](https://pigrecoinfinito.files.wordpress.com/2021/10/image-14.png)

espressione utilizzata:

```
to_int(
    map_get(
        hstore_to_map("other_tags"),'population')
)
```

## provaci tu

[download isole](https://download.geofabrik.de/europe/italy/isole.html)