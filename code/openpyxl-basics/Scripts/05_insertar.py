from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Habitos' )

hoja.insert_rows(1, 2)

cabecera = ('Número de Serie', 'Hábitos')

for indice_col, valor in enumerate( cabecera, start=1 ):
    hoja.cell( row=1, column=indice_col, value=valor )

archivo_excel.save( ruta )