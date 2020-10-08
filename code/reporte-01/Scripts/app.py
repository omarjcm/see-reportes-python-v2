from funciones import *
from reporte_excel import *
from reporte_datos import *

nombre_archivo = obtener_nombre_archivo()

archivo = cargar_archivo( nombre_archivo )
hoja = obtener_hoja( archivo, 'Reporte SEE' )

agregar_imagen( hoja )

hoja_activa = archivo.active
agregar_titulo( hoja_activa )

cabecera = [ 'País', 'Año', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12' ]
agregar_filtro( hoja_activa, hoja, cabecera )
agregar_datos( hoja_activa, hoja, cabecera )

archivo.save( nombre_archivo )