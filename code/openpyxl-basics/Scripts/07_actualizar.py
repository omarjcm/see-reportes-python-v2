from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Habitos' )

habitos = [
        ('Número de Serie', 'Hábitos'),
        (1, 'Leer Ciencia Ficción'),
        (2, 'Ir al cine'),
        (3, 'Ir a comer a restaurantes diferentes.')
]

columna_indice = 2
hoja.insert_cols( columna_indice )

for indice_fila, valor in enumerate( habitos, start=1 ):
    serie, habito = valor
    hoja.cell( row=indice_fila, column= columna_indice, value=habito )

archivo_excel.save( ruta )



