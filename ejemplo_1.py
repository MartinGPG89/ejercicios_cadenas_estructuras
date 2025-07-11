#2

lista = list(range(0, 101))
pos = 0

while pos < len(lista):
    if lista[pos] % 2 == 0:
        print(lista[pos])
    pos+= 1



#n3

lista = list(range(0, 101))
pos = 0

while pos < len(lista):
    if lista[pos] % 2 == 0 and lista[pos] <= 20:
        print(lista[pos])

    pos+=1 

#n6

lista = list(range(0, 100))
pos = 0
suma = 0

while pos < len(lista):
    if lista[pos] % 2 == 0 and lista[pos] < 100:

        suma += lista[pos]
    pos += 1

print(suma)





#n7. Sumar les potències de 2 menors a 100

lista = list(range(0, 100))
pos = 0
potencia = 1
suma_cont = 0
while pos < len(lista):
    potencia  *= 2 
    if potencia < 100:

             suma_cont += potencia
      
    pos += 1
print(suma_cont)




#nº8. Calcular la mitjana dels números positius llegits

lista = [2, 2, 6, 10]
pos = 0
suma = 0
cont = 0



while pos < len(lista):
    
    cont += 1
    suma += lista[pos]

while pos < len(lista):
    pos += 1

print(cont)

