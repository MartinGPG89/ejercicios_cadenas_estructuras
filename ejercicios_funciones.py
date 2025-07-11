'''#funciones

#Nº1

def orden(lista):
    lista_temp = lista.copy()

    lista_temp.sort()
    return lista_temp

lista = [4, 7, 2, 9]

print(orden(lista))




  cadena = e1.get()

    lista = cadena.split(',')
    resultado = []

    for n in lista:
        resultado.append(int(n))
        suma = 0

        for i in resultado:
            suma += i ** 3

        Llabel.config(text = f'{suma}') 

#nº2

 def sumar(lista):
    
   lista_temp = lista.copy()

   suma = 0

   for elemento  in lista_temp:

        suma = suma + elemento 

   return suma

lista = [2, 2, 6]

print(sumar(lista))
 

#nº3

 def cuadradolista(lista):
    lista_temp = lista.copy()

    suma = 0

    for element in lista_temp:
        suma = suma + element * element

    return suma

lista = [2, 2, 6]
print(cuadradolista(lista))

 
#nº4

 def cubolista(lista):
    lista_temp = lista.copy()

    suma = 0

    for element in lista_temp:
        suma = suma + element *element*element

    return suma

lista = [2, 2, 6]
print(cubolista(lista))
 



#nº5

 def minlista(lista):
    lista_temp = lista.copy()

    return min(lista_temp)

lista = [2, 6, 8]

print(minlista(lista))

 

#nº6

 def maxlista(lista):
    lista_temp = lista.copy()

    return max(lista_temp)

lista = [2, 6, 8, 76]

print(maxlista(lista)) 


#nº7

 def orden(lista):
    lista_temp = lista.copy()

    lista_temp.reverse()
    return lista_temp

lista = [2, 6, 8, 76]
print(orden(lista))
 

#nº8

 def parallel (lista):

    lista_temp = lista.copy()

    rea = []

    for pos in range(len(lista_temp)):
          if pos % 2 == 0:
                 rea.append(lista_temp[pos])
    return rea

lista = [1, 3, 5, 7,9, 12, 29, 56, 73]
print(parallel(lista))


 




#nº9

 def impar (lista):

    lista_temp = lista.copy()

    rea = []

    for pos in range(len(lista_temp)):
          if pos % 2 != 0:
                 rea.append(lista_temp[pos])
    return rea

lista = [1, 3, 5, 7,9, 12, 29, 56, 73]
print(impar(lista))

 
#nº10

 def digitos(lista):
    lista_temp = lista.copy()

    nueva_lista = [] 
 
    for pos in nueva_lista:
        nueva_lista.append(len(lista_temp.count()))
     

     for pos in range(len(lista_temp)):
         cadena = str( lista_temp[pos])
         longitud_cadena = len(cadena)
         nueva_lista.append(longitud_cadena) 
     #nueva_lista.append( len(str(lista_temp[pos])))    
    for numero in lista_temp:
         cadena = str(numero)
         longitud_cadena  = len(cadena)
         nueva_lista.append(longitud_cadena)
         #nueva_lista.append( len(str(numero)))      
    
    return nueva_lista

lista = [1, 3, 5, 7, 56, 73]
print(digitos(lista))
     

#nº11

 def cadenas(lista):

    lista_temp = lista.copy()
    nueva_lista = []

    for pos in range(len(lista_temp)):
        nueva_lista.append(len(lista_temp[pos]))
    return nueva_lista
    

    
lista = ['agua', 'montaña', 'arbol']

print(cadenas(lista)) 



#nº12

 def minusculas(lista):
    lista_temp = lista.copy()

    lista_min = []

    for pos in lista_temp:
        lista_min.append(pos.lower())


    return lista_min


lista = ['AGUA', 'MONTAÑA', 'ARBOL']
print(minusculas(lista))
 

#nº13
 def mayusculas(lista):
    lista_temp = lista.copy()

    lista_mayus = []

    for pos in lista_temp:
        lista_mayus.append(pos.upper())


    return lista_mayus


lista = ['agua', 'montaña', 'arbol']
print(mayusculas(lista)) 




#nº14

 def concat(lista):
    lista_temp = lista.copy()

    nueva_cadena = ''

    for pos in lista_temp:
        nueva_cadena = ''.join(lista_temp)

    return nueva_cadena


lista = ['el', 'rio', 'es', 'azul']
print(concat(lista))
 


#nº15

 
def alfabetic(lista):

    lista_alfabetic = lista.copy()
   
      va_lista = []

    for pos in lista_alfabetic:
        nueva_lista.append(sorted(pos))   
    
    lista_alfabetic .sort()

    return lista_alfabetic 


lista = ["rojo", "azul", "verde"]
print (alfabetic(lista))


 

#ºn16

 def paralelo(lista):
    lista_temp = lista.copy()

    lista_paralel = []

    for pos in range(len(lista_temp)):
        if pos % 2 == 0:
            lista_paralel.append(lista_temp[pos])
    return lista_paralel
    

lista = [ 'agua', 'montaña', 'arbol']

print(paralelo(lista))


 

#nº17

 def impar(lista):
    lista_temp = lista.copy()

    lista_impar = []

    for pos in range(len(lista_temp)):
        if pos % 2 != 0:
            lista_impar.append(lista_temp[pos])
    return lista_impar
    

lista = [ 'agua', 'montaña', 'arbol']

print(impar(lista))
 


#nº18

 def ultimo(lista):
    list_temp =lista.copy()
    lista_ultimo =[]

    for pos in range (len(list_temp)):
        lista_ultimo.append(list_temp[pos].rstrip())
    
    for pos in list_temp:
        lista_ultimo.append(pos[:-1])

    return lista_ultimo

lista = ['rojo', 'azul', 'verde']

print (ultimo(lista)) 



#nº19

 def primero(lista):
    list_temp =lista.copy()
    lista_primera =[]

    
    for pos in list_temp:
        lista_primera.append(pos[1:])

    return lista_primera

lista = ['rojo', 'azul', 'verde']

print (primero(lista))
 '''

#nº20

def invert(lista):
    list_temp = lista.copy()
    lista_invert=[]

    for pos in list_temp:
        lista_invert.append(pos[::-1])

    return lista_invert

lista= ['rojo','verde','azul']

print (invert(lista))


