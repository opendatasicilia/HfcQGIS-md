# Korto19 2022
from qgis.core import QgsExpression
import csv
# Crea un file CSV e lo popola con le espressioni per ogni gruppo del Field Calc
# lanciare da console python in QGIS

# numero totale espressioni
nro_tot = len(QgsExpression.Functions())
# creo due dizionari
gruppi_funzioni = {}
gruppi = {}
# popolo il primo con le coppie funzione, gruppo
# ed il secondo con gruppo e contatore
for i in range(0, nro_tot):
    gruppi[QgsExpression.Functions()[i].group()] = 1
    gruppi_funzioni[QgsExpression.Functions()[i].name()] = QgsExpression.Functions()[i].group()
#uso il secondo gruppo per classificare il primo e conto 
for key, value in gruppi_funzioni.items():
    #print(key, ' : ', value)
    gruppi[value] = gruppi[value] + 1
# riordino per gruppo
ordered = {k: v for k, v in sorted(gruppi_funzioni.items(), key=lambda item: item[1])}
# print(gruppi)

# scrive un file csv
f = open('C:/Users/pigre/Desktop/gruppi_espressioni.csv', 'w', newline='')
writer = csv.writer(f)
data = ["Gruppo", "Espressione"]
writer.writerow(data)
for keys,values in ordered.items():
    data = [values, keys]
    writer.writerow(data)
# chiudo il file
f.close()