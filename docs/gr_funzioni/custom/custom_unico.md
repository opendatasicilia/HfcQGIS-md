---
social_image: img/card_social/hfc_gr_custom.png
---

# Gruppo Custom

!!! Abstract
    **Questo gruppo contiene funzioni Python create dall'utente. <br> Le funzioni vanno salvate in file *.py nella cartella `espression` presente nel profilo utente QGIS `(C:\Users\nomeUtente\AppData\Roaming\QGIS\QGIS3\profiles\default\python\expressions)`**

---

## fattoriale

Calcola il fattoriale di un numero definito come il prodotto di tutti i numeri tra 1 e n.
Per convenzione il fattoriale di 0 = 1 la notazione matematica per fattoriale è n!
La funzione è compresa nel modulo math
**NB:** valore massimo memorizzabile in un campo numerico è 20! (2432902008176640000)

Esempio:

```
fact(10)→ 3628800`
```

![](../../img/custom/fact1.png)

Codice Python:

```py
from qgis.core import *
from qgis.gui import *
import math

@qgsfunction(args='auto', group='Custom')
def fact(n, feature, parent):
    """
    Calcola il fattoriale di un numero
    definito come il prodotto di tutti
    i numeri tra 1 e n.<ul> </ul>
    Per convenzione il fattoriale di 0 = 1
    la notazione matematica per fattoriale è n!
    La funzione è compresa nel modulo math
    NB: valore massimo memorizzabile 20!
    <ul> </ul>
    <h2>Example usage:</h2>
    <ul>
      <li>Fattoriale(5) -> 120</li>
      <li>in simboli 5! = 120</li>
    </ul>
    """
    return math.factorial(n)
```

Lo script Python è stato realizzato da [Giulio Fattori](https://github.com/Korto19)

---

## my_sum

Calcola la somma dei due parametri valore1 e valore2. 

Esempio:

```
my_sum(5, 8) -> 13
my_sum("fiel1", "field2") -> 42
```

![](../../img/custom/my_sum1.png)

Codice Python:

```py
from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def my_sum(value1, value2, feature, parent):
    """
    Calcola la somma dei due parametri valore1 e valore2.
    <h2>Esempio di utilizzo:</h2>
    <ul>
      <li>my_sum(5, 8) -> 13</li>
      <li>my_sum("fiel1", "field2") -> 42</li>
    </ul>
    """
    return value1 + value2
```

---

## perimetro_km

Questa funzione ritorna il valore del perimetro della geometria in km 

Esempio:

```
perimetro_km() - > 25
```

![](../../img/custom/perimetro_km().png)

Codice Python:

```py
from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def perimetro_km( feature, parent):
    """ 
	Questa funzione ritorna il valore del perimetro della geometria in km
	<ul>
      <li>perimetro_km() - > 25</li>
    </ul>
	"""
    geom_perimetro_km = feature.geometry().length()/1000
    return geom_perimetro_km
```

---

## reverse_string

Questa funzione ritorna il valore rovesciato di un testo

Esempio:

``` 
reverse_string('Pigrecoinfinito) - > 'otinifniocergiP' `
```

![](../../img/custom/reverse_string1.png)

Codice Python:

```py
from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def reverse_string(string_to_reverse, feature, parent):
   """ 
   Questa funzione ritorna il valore rovesciato di un testo
	<ul>
      <li>reverse_string('Pigrecoinfinito) - > 'otinifniocergiP'</li>
    </ul>
	"""
   return string_to_reverse[::-1]
```

---

## get_parcel_info

[WMS Catasto Agenzia delle Entrate CC BY 4.0](https://www.agenziaentrate.gov.it/portale/it/web/guest/schede/fabbricatiterreni/consultazione-cartografia-catastale/servizio-consultazione-cartografia):

La funzione, tramite una richiesta [GetFeatureInfo](https://gdal.org/drivers/raster/wms.html?highlight=getfeatureinfo), restituisce le informazioni utili sulla particella che ricade sotto il pixel di mio interesse:

Sintassi:

- get_parcel_info(_<span style="color:red;">x</span>_,_<span style="color:red;">y</span>_)

Argomenti:

- _<span style="color:red;">x</span>_ coordinata x di un punto
- _<span style="color:red;">y</span>_ coordinata x di un punto

Esempio:

```
get_parcel_info(355461.5,4222490.7) → 'IT.AGE.PLA.G273_0033A0.673'
```

codice Python:

```py
# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WMS Catasto Agenzia delle Entrate CC BY 4.0
                              -------------------
        copyright            : (C) 2020 by Giulio Fattori
        email                : giulio.fattori@tin.it
 ***************************************************************************/
"""

from qgis.core import *
from qgis.gui import *
import requests



@qgsfunction(args='auto', group='Custom')
def get_parcel_info(xx, yy, feature, parent):
    """
    <h1>WMS Catasto Agenzia delle Entrate CC BY 4.0:</h1><br>    
    La funzione, tramite una richiesta GetFeatureInfo, restituisce le informazioni utili sulla particella che ricade sotto il pixel di mio interesse:
    <h2>Esempio:</h2>
    <ul>
      <li>get_parcel_info(355461.5,4222490.7) -> 'IT.AGE.PLA.G273_0033A0.673'</li>
      <li>get_parcel_info("fieldX", "fieldY") -> 'IT.AGE.PLA.G273_0033A0.673'</li>
    </ul>
    <h2>NB: le coordinate X e Y devono essere in EPSG 3045</h2>
    """
    req = "https://wms.cartografia.agenziaentrate.gov.it/inspire/wms/ows01.php?REQUEST=GetFeatureInfo&SERVICE=WMS&SRS=EPSG:3045&STYLES=&VERSION=1.1&FORMAT=image/png&BBOX="+str(xx-1)+","+str(yy-1)+","+str(xx+1)+","+str(yy+1)+"&HEIGHT=9&WIDTH=9&LAYERS=CP.CadastralParcel&QUERY_LAYERS=CP.CadastralParcel&INFO_FORMAT=text/html&X=5&Y=5"

    r = requests.get(req, auth=('user', 'pass'))
    a = r.text.partition("InspireId localId</th><td>")[2]
    b = a.partition("</td>")[0]
    return b
```

![](../../img/custom/get_parcel_info1.png)

Lo script Python è stato realizzato da [Giulio Fattori](https://github.com/Korto19)

---

## get_catastal_info

[Catasto Agenzia delle Entrate CC BY 4.0](https://www.agenziaentrate.gov.it/portale/it/web/guest/schede/fabbricatiterreni/consultazione-cartografia-catastale/servizio-consultazione-cartografia):

La funzione, tramite una richiesta ajax.php, restituisce le informazioni disponibili su quel che ricade sotto il punto selezionato.

Sintassi:

- get_catastal_info(_<span style="color:red;">longitudine</span>_, _<span style="color:red;">latitudine</span>_, _<span style="color:red;">chiave</span>_)

Argomenti:

- _<span style="color:red;">longitudine</span>_ coordinata  x del punto
- _<span style="color:red;">latitudine</span>_ coordinata  y del punto
- _<span style="color:red;">chiave</span>_ per le Particelle: 

    * SIGLA_PROV 
    * COD_COMUNE 
    * DENOM 
    * SEZIONE 
    * FOGLIO 
    * ALLEGATO 
    * SVILUPPO 
    * NUM_PART 
    * TIPOLOGIA
  <br>Per Acque e Strade:
    * TIPOLOGIA 
    * COMUNI 

Esempio:

```
get_catastal_info(12.567315,37.914197, 'TIPOLOGIA') -> 'ACQUA'
```

codice Python:

```py
# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WMS Catasto Agenzia delle Entrate CC BY 4.0
                              -------------------
        copyright            : (C) 2020 by Giulio Fattori
        email                : giulio.fattori@tin.it
 ***************************************************************************/
"""

from qgis.core import *
from qgis.gui import *
import requests, json

@qgsfunction(args='auto', group='Custom')
def get_catastal_info(xx, yy, chiave, feature, parent):
    """
    <h1>Catasto Agenzia delle Entrate CC BY 4.0:</h1>    
    La funzione, tramite una richiesta ajax.php, restituisce le informazioni disponibili su quel che ricade sotto il punto selezionato.
    
    <p style="color:Olive"><b>Sintassi</b></p>
    <p style="color:blue"><b>get_catastal_info</b><mark style="color:black">(</mark>
    <mark style="color:red">x</mark>
    <mark style="color:black">,</mark>
    <mark style="color:red">y</mark>
    <mark style="color:black">,</mark>
    <mark style="color:red">chiave</mark>
    <mark style="color:black">)</mark><br>
    
    <br><mark style="color:black"><b>Le possibili chiavi sono:
    <ul>
        Per le particelle:
        <li>SIGLA_PROV</li>
        <li>COD_COMUNE</li>
        <li>DENOM</li>
        <li>SEZIONE</li>
        <li>FOGLIO</li>
        <li>ALLEGATO</li>
        <li>SVILUPPO</li>
        <li>NUM_PART</li>
        <li>TIPOLOGIA</li>
    </ul>    
    <ul>Per Acque e Strade:
        <li>TIPOLOGIA</li>
        <li>COMUNI</li>
    </ul></b>
    
    <h2>Esempio:</h2>
    <ul>
      <li>get_catastal_info(12.567315,37.914197, 'TIPOLOGIA') -> 'ACQUA'</li>
    </ul>
    
    <h2><b>Le coordinate X e Y devono essere espresse nel sistema WGS84 (EPSG:4326)</h2>
    <h2><b>Il campo risultante deve essere di tipo string di adeguata lunghezza</h2>
    <h2><b>Se la chiave non è presente risulterà ND</h2>
    """
    
    req = "https://wms.cartografia.agenziaentrate.gov.it/inspire/ajax/ajax.php?op=getDatiOggetto&lon=" + str(xx) + "&lat=" + str(yy)
    r = requests.get(req, auth=('user', 'pass'))
    res = json.loads(r.text)
    try:
        b = str(res[chiave])
    except:
        b = 'ND'
    
    return b
```

![](../../img/custom/get_catastal_info1.png)

Lo script Python è stato realizzato da [Giulio Fattori](https://github.com/Korto19)

---

## fill-down

Restituisce un valore dal campo specificato, dove il valore del campo della riga precedente viene propagato ai campi con valori `NULL` successivi. Opera in base all'id dei record.

Sintassi:

- fill_down(_<span style="color:red;">attibuto</span>_) -> popola le celle sottostanti

Argomenti:

- _<span style="color:red;">attributo</span>_ un campo

Esempio:

```
fill-down("attributo")
```

```py
from qgis.core import *
from qgis.gui import *
mem = 'NULL'

@qgsfunction(args='auto', group='Custom', handlesnull=True)
def fill_down(value1, feature, parent):
    """
    Restituisce un valore dal campo specificato,
    dove il valore del campo della riga precedente
    viene propagato ai campi con valori Null successivi
    <p>    
    Returns a value from the specified field,
    where the value of the field of the previous row
    it is propagated to subsequent null fields
    <h2>Example usage:</h2>
    <ul>
      <li>fill_down("Dato") -> Fill_Data</li>
      <table>
        <thead>
        <tr>
        <th>Dato</th>
        <th>Fill_Data</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td style="text-align:right">a</td>
        <td style="text-align:right">a</td>
        </tr>
        <tr>
        <td>&nbsp;</td>
        <td style="text-align:right">a</td>
        </tr>
        <tr>
        <td>&nbsp;</td>
        <td style="text-align:right">a</td>
        </tr>
        <tr>
        <td style="text-align:right">b</td>
        <td style="text-align:right">b</td>
        </tr>
        <tr>
        <td></td>
        <td style="text-align:right">b</td>
        </tr>
        </tbody>
        </table>
            </ul>
        
        Opera in base all'id dei record
        <p>
        Operate based on the ID of the records
    """
    global mem
    res = str(value1)
    if res in ('NULL',''):
        res = mem
    else:
        mem = str(value1)
    return res
```

![](../../img/custom/fill-down1.png)

Lo script Python è stato realizzato da [Giulio Fattori](https://github.com/Korto19)

---

## random_points_in_polygon

Genera 'n' di punti all'interno della geometria del poligono corrente.

Sintassi:

- random_points_in_polygon(_<span style="color:red;">numero</span>_)

Argomenti:

- _<span style="color:red;">numero</span>_ numero di punti da tracciare

```py
from qgis.core import *
from qgis.gui import *

import random   # Needed for generating pseudo random numbers

@qgsfunction(args='auto', group='Custom')
def random_points_in_polygon(number_of_points, feature, parent):
    """
    <i>random_points_in_polygon( n )</i><br><br>
    Generates 'n' number of points inside the current polygon geometry.<br><br>
    <b>Requires</b><br>
    <i>n</i> (Integer)<br><br>
    <b>Example</b><br>
    <i>random_points_in_polygon( 25 )</i><br>
    <br>
    &lt;geometry: MultiPoint&gt; with 25 points
    """
    points = list() # Create an empty list for the points
    
    
    # Until there's the required points in the list, loop (not the best way probably)
    while len(points) < number_of_points:
        # Create random x and y coordinates inside feature geometry bounding box
        rnd_x = random.uniform(feature.geometry().boundingBox().xMinimum(), feature.geometry().boundingBox().xMaximum())
        rnd_y = random.uniform(feature.geometry().boundingBox().yMinimum(), feature.geometry().boundingBox().yMaximum())
        # Use the coordinates to create a point
        rnd_point = QgsPointXY(rnd_x, rnd_y)
        
        # Test if the point is inside the feature geometry
        if QgsGeometry.fromPointXY(rnd_point).within(feature.geometry()):
            # If it is inside, add it to the list (increasing the length of the list)
            points.append(rnd_point)
    
    # Return a multipoint geometry
    return QgsGeometry.fromMultiPointXY(points)
```

![](../../img/custom/random_points_in_polygon1.png)

Lo script Python è stato realizzato da [Giulio Fattori](https://github.com/Korto19)

---

