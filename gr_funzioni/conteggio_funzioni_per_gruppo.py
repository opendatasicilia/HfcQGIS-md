# Korto19 2022
# Script da console
# Lista su un csv dei gruppi e delle funzioni del field calc
# Stampa in console gruppo e n espressioni contenute
# File csv risultante: impostare nome e percorso,con permesso di scrittura, alla riga 31

# Korto19 2022
from qgis.core import QgsExpression
import csv

#creo due dizionari
gruppi_funzioni = {}
gruppi = {}

#popolo il primo con le coppie funzione, gruppo ed il secondo con gruppo e contatore
for i in range(0, len(QgsExpression.Functions())):
    gruppi[QgsExpression.Functions()[i].group()] = 0
    gruppi_funzioni[QgsExpression.Functions()[i].name()] = QgsExpression.Functions()[i].group()
    
#uso il secondo gruppo per classificare il primo e conto 
for key, value in gruppi_funzioni.items():
    gruppi[value] = gruppi[value] + 1
    
#riordino per gruppo
ordered = {k: v for k, v in sorted(gruppi_funzioni.items(), key=lambda item: item[1])}

#riordino nei gruppi
gruppi_ordered = {k: v for k, v in sorted(gruppi.items())}

#apro un file csv, nome file e directory da inserire!!
f = open('C:\\Users\\pigre\\Desktop\\test.csv', 'w', newline='')
writer = csv.writer(f)

#intestazioni parte gruppi / n espressioni
data = ["Gruppo", "n_espressioni"]
writer.writerow(data)

for keys,values in gruppi_ordered.items():
   data = [keys, values]
   writer.writerow(data)
   print(data)

#riga vuota di separazione
data = ["", ""]
writer.writerow(data)

#intestazioni parte gruppo / espressione
data = ["Gruppo", "Espressione"]
writer.writerow(data)
for keys,values in ordered.items():
   data = [values, keys]
   writer.writerow(data)

#chiudo il file
f.close()