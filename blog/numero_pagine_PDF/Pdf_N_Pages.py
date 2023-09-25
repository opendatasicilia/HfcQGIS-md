# Korto19 2023
from qgis.core import *
from qgis.gui import *
from PyPDF2 import PdfReader

@qgsfunction(group='HfcQGIS',referenced_columns=[])
def Get_Pdf_N_Pages(pdfpath, *args, **kwargs):
    """
    Restituisce il numero di pagine di un pdf dando il percorso
    <h2>Example usage:</h2>
    <ul>
      <li>Get_Pdf_N_Pages(pdfpath)-> 3</li>
    </ul>
    """

    reader = PdfReader(str(pdfpath))
    number_of_pages = len(reader.pages)

    return number_of_pages
