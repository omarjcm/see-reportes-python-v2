from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Seguidores' )

imagen = openpyxl.drawing.image.Image( '../Data/images/see.png' )
hoja.add_image( imagen, 'A8' )

archivo_excel.save( ruta )