from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
from funciones import *

ruta = '../Data/datos.xlsx'

archivo_excel = cargar_archivo( ruta )
hoja = obtener_hoja(archivo_excel, 'registros' )

datos = []

for fila_valor in hoja.values:
    cedula, apellidos, nombres, genero, nota_anterior, nota_actual, tipo_rectificacion, motivo, periodo, interciclo, materia, grupo, docente, ciudad, fecha_elaboracion, titulo_director, director_carrera, cargo, carrera, firma, nota_firma, imagen = fila_valor
    plantilla = '../Data/datos_formato.docx'
    dato = {
        'cedula':cedula,
        'apellidos':apellidos,
        'nombres':nombres,
        'genero':genero,
        'nota_anterior':str(nota_anterior),
        'nota_actual':str(nota_actual),
        'tipo_rectificacion':tipo_rectificacion,
        'motivo':motivo,
        'periodo':periodo, 
        'interciclo':interciclo, 
        'materia':materia, 
        'grupo':grupo, 
        'docente':docente, 
        'ciudad':ciudad, 
        'fecha_elaboracion':fecha_elaboracion, 
        'titulo_director':titulo_director, 
        'director_carrera':director_carrera, 
        'cargo':cargo, 
        'carrera':carrera, 
        'firma':firma, 
        'nota_firma':nota_firma, 
        'IMAGE:imagen':imagen
    }
    datos.append( dato )

documento = MailMerge( plantilla )
documento.merge_templates( datos, separator='page_break' )
documento.write('../Data/documentos.docx')