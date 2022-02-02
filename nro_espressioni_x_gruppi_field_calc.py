# Korto19 2022
# Calcola il numero di espressioni per ogni gruppo del Field Calc
# lanciarlo da console python in QGIS
from qgis.core import QgsExpression
#numero totale espressioni
nro_tot = len(QgsExpression.Functions())
#creo due dizionari
gruppi_funzioni = {}
gruppi = {}
#popolo il primo con le coppie funzione, gruppo
#ed il secondo con gruppo e contatore
for i in range(0, nro_tot):
    gruppi[QgsExpression.Functions()[i].group()] = 1
    gruppi_funzioni[QgsExpression.Functions()[i].name()] = QgsExpression.Functions()[i].group()
#uso il secondo gruppo per classificare il primo e conto 
for key, value in gruppi_funzioni.items():
    #print(key, ' : ', value)
    gruppi[value] = gruppi[value] + 1
#stampo il risultato
print(gruppi)
print ('nro totale espressioni: ',nro_tot)