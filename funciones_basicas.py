# Ejercicio 1
# Crea una función llamada mostrar_mensaje() que reciba un texto como argumento
# y lo imprima por pantalla.
def mostrar_mensaje(texto):
    return f'Este {texto} es para ti'

print(mostrar_mensaje('mensaje personalizado'))






# Ejercicio 2
# Crea una función llamada suma_dos_numeros() que reciba dos números
# y devuelva la suma de ambos.
def suma_dos_numeros(num1, num2):
    
    return num1 + num2

print(suma_dos_numeros(3, 6))


# Ejercicio 3
# Crea una función llamada contar_pares() que reciba una lista de números
# y devuelva cuántos de esos números son pares.
def contar_pares(lista):
    pares = []

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares
        
print(contar_pares([2, 3, 4, 6, 7, 8, 9]))


# Ejercicio 4
# Crea una función llamada es_mayor_de_edad() que reciba una edad
# y devuelva True si es mayor o igual a 18, y False si es menor.
def es_mayor_de_edad(edad):
    
    if edad >= 18:
        return f'Es mayor de edad'
    else:
        return f'No es mayor de edad'

print(es_mayor_de_edad(int(input('Introducir edad:   '))))




# Ejercicio 5
# Crea una función llamada repetir_caracter() que reciba un carácter y un número n,
# y devuelva el carácter repetido n veces como una sola cadena.

def repetir_caracter(caracter, n):
    pass



#EJERCICO FUNCIONES

