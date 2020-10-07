import pandas as pd

def obtener_transacciones_x_pais():
    transacciones = pd.read_excel('../Data/transacciones_202008.xlsx', sheet_name='Sheet1')
    #transacciones['InvoiceDate'] = 

