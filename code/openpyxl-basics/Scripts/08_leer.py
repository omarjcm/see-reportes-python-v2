from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Habitos' )

for fila_valor in hoja.values:
    serie, habito = fila_valor
    print( '{} - {}'.format(serie, habito) )