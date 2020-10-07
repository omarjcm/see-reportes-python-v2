from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Habitos' )

hoja.delete_rows(2)
hoja.delete_cols(2)

archivo_excel.save( ruta )