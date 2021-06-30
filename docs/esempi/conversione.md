# Etichettare punti EPSG 4326 sessadecimali in sessagesimali GMS

La conversione tra i due sistemi è abbastanza semplice e quindi vado direttamente alla espressione da usare nel calcolatore di campi:

```
'lon :' || floor($x)
|| '° ' || 
floor( ($x - floor($x))*60) 
||''' '|| 
format_number( 
to_real((($x - floor($x))*60) -floor((($x - floor($x))*60 )))*60 ,2)||'" E'
|| '_' || 
'lat :' || floor($y)
|| '° ' || 
floor( ($y - floor($y))*60) 
||''' '|| 
format_number( 
to_real((($y - floor($y))*60) -floor((($y - floor($y))*60 )))*60 ,2) ||'" N'
```
Funzione [floor](../gr_funzioni/matematica/floor.html)

![](../img/esempi/conversione/conversione1.png)

![](../img/esempi/conversione/conversione2.png)


Geopackage è [qui](https://github.com/gbvitrano/HfcQGIS/blob/master/esempi/dati_esempi.zip?raw=true)

## Nota bene

Dalla versione QGIS 3.4 è possibile usare le funzioni [to_dm](../gr_funzioni/conversioni/to_dm.html) o [to_dms](../gr_funzioni/conversioni/to_dms.html)
