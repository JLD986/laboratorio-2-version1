print('***************************************************************************************\n')
print('                              Tiendita\n                                                 ')
print('***************************************************************************************\n')

articulo = float(input('Escriba el precio del articulo vendido\n  '))
cash = float(input("Ingrese la cantidad de dinero que entrega el cliente\n"))

if cash > articulo:
    vuelto = (cash-articulo)
    print('El cambio para el cliente es ', vuelto)
elif cash == articulo:
    print('El cliente ha dado la cantidad exacta de dinero ')
    
elif cash < articulo:
    debe = (articulo - cash)
    print(' El cliente  debe ', debe, 'PAGUEMEEEEEEEEEE')
    
else: print('No se debe cambio ')

print('******************************************************************************************')
print('Fin')