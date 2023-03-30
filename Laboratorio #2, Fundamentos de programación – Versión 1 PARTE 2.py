print('**************************************************************************\n')
print("                         De algo sirve \n                                     ")
print('**************************************************************************\n')

num1=int(input('Ingrese un numero cualquiera\n'))
num2= int(input('ingrese un segundo numero\n'))
num3= int(input('Ingrese un tercer numero\n'))

if num1<num3 and num2< num3:
    print(num3, ' Es el numero mayor' )
    if num1<num2:
        print(num2, 'es el segundo numero mas alto')
        print("el numero mas pequeño es ", num1)
    else: print(num1, "Es el segundo numero mas alto \n", num2 , "Es el numero menor")
elif num1>num2 and num1 > num3:
    print(num1, ' Es el numero mayor')
    if num3<num2:
        print(num2, 'es el segundo numero mas alto')
        print("el numero mas pequeño es ", num3)
    else: print(num2, "Es el segundo numero mas alto \n", num1 , "Es el numero menor")
elif num2>num1 and num2 > num3:
    print(num2,"es el numero mayor")
    if num1<num3:
        print(num3, 'es el segundo numero mas alto')
        print("el numero mas pequeño es ", num1)
    else: print(num1, "Es el segundo numero mas alto \n", num3 , "Es el numero menor")
print("FIN")
