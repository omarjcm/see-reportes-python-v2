
nombre, apellido, correo = ('Guillermo', 'Pizarro', 'gpizarro@ieee.org')

print(nombre)
print(apellido)
print(correo)

print( '{} {}, {}'.format(nombre, apellido, correo) )

dato1 = (1, 'Leer Ciencia Ficcción', 'Activo')
dato2 = (2, 'Salir al Cine', 'Activo')

for indice, valor in enumerate( dato2, start=1 ):
    print( 'Indice: {}, Valor: {}'.format( indice, valor ) )
    
datosLista = [ dato1, dato2 ]

#for dato in datosLista:
#    print(dato)
#
#for dato in datosLista:
#    for indice, valor in enumerate( dato ):
#        print( valor )

for dato in datosLista:
    id_habito, habito, estado = dato
    print(id_habito)
    
    
    
    
    
    