import openpyxl

ruta = 'C:\\Data\\test.xlsx'

archivo_excel = openpyxl.load_workbook( ruta )
hoja = archivo_excel['Habitos']
#hoja.title = 'Habitos'

archivo_excel.save( ruta )