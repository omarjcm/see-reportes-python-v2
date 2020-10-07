from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Habitos' )

archivo_excel.create_sheet( title='Seguidores', index=0 )
archivo_excel.create_sheet( title='Proyectos', index=2 )

print( archivo_excel.worksheets )

seguidores = [
        ('Id', 'Dominio', 'Seguidores'),
        (1, 'Youtube', 3000),
        (2, 'Facebook - SEE', 10000),
        (3, 'Twitter', 8000)
]

hoja = archivo_excel['Seguidores']

for seguidor in seguidores:
    hoja.append( seguidor )

archivo_excel.save( ruta )