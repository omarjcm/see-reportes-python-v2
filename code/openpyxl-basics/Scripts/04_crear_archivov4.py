from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Habitos' )

habitos = [
        (1, 'Leer Ciencia Ficción.'),
        (2, 'Ir al cine.'),
        (3, 'Comer en restaurantes diferentes.')
]

for habito in habitos:
    hoja.append( habito )

archivo_excel.save( ruta )