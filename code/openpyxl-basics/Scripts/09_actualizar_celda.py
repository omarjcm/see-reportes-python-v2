from funciones import *

ruta = '../Data/data.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'Habitos' )

hoja.cell( row=1, column=1, value='Num. de Serie' )
hoja.cell( row=1, column=1 ).value = 'Serie Núm.'

celda = hoja.cell( row=1, column=1 )
celda.value = 'Número de Serie'
celda.font = openpyxl.styles.Font( bold=True, color='336600' )
celda.fill = openpyxl.styles.PatternFill( 'solid', fgColor='99ff66' )

archivo_excel.save( ruta )