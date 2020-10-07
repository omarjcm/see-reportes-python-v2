import openpyxl

ruta = '..\\Data\\test.xlsx'

archivo_excel = openpyxl.Workbook()
hoja = archivo_excel['Sheet']
hoja.title = 'Habitos'

archivo_excel.save( ruta )