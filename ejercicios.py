

# EJERCICIO Nº 2 CADENAS 

cadena = 'nevada'
cont = 0

for i in cadena:
    if 'a' in i:
        cont += 1
print(cont)


# EJERCICIO Nº 6 CADENAS


cadena = input('Escribe una palabra: ')


for i in range(len(cadena)):
    print(f'Texto: {cadena} - {i+1}')




# EJERCICIO Nº 12

cadena_2 = input('Introduce que quieres comparar: ')
cadena_1 = 'el rio es azul'


if cadena_2 in cadena_1:
    print(f'La cadena "{cadena_2}" SI esta en "{cadena_1}"')
else:
    print(f'La cadena "{cadena_2}" NO esta en "{cadena_1}"')





#EXERCICIS DE SUBCADENES
 # EJERCICIO Nº 1



cadena = 'arbol'
cont = 0

for i in range(len(cadena)):
    print(cadena[:i+1])






