# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muestralo.

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

# 4. Cuenta cuantas veces aparece el numero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

# 5. Encuentra el I­ndice de la primera aparicion de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

# 7. Crea una subtupla con los elementos desde la posicion 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

# 10. Crea una tupla con un solo elemento (el numero 100) e imprÃ­mela. Asegurate de usar la sintaxis correcta para crear una tupla con un solo elemento.


print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")
tupla = (10,20,30,40,50)
print("Tupla #1 : " + str(tupla))
print("---------------------------------------------------------")
print("---------------------Ejercicio #2------------------------")
tupla2= (100, 200, 300, 400, 500)
print("Tupla #2 elemento nro 2: " + str(tupla2[1]))
print("---------------------------------------------------------")
print("---------------------Ejercicio #3------------------------")
tupla3 = (1, 2, 3)
# tupla3[0] = 10 TypeError: 'tuple' object does not support item assignment
print("---------------------------------------------------------")
print("---------------------Ejercicio #4------------------------")
tupla4 = (1, 2, 3, 3, 4, 5, 3)
print(tupla4.count(3))
print("---------------------------------------------------------")
print("---------------------Ejercicio #5------------------------")
tupla5= ("Java", "Python", "JavaScript", "Python")
print(tupla5.index("Python"))
print("---------------------------------------------------------")
print("---------------------Ejercicio #6------------------------")
# (1, 2, 3) y (4, 5, 6)
tupla6 =(1,2,3)
tupla7 =(4,5,6)
sum_tuplas = (tupla6 + tupla7)
print(sum_tuplas)
print("---------------------------------------------------------")
print("---------------------Ejercicio #7------------------------")
tupla8 = (10, 20, 30, 40, 50)
subtupla = tupla8[2:4]
print(subtupla)
print("---------------------------------------------------------")
print("---------------------Ejercicio #8------------------------")
tupla9= ("rojo", "verde", "azul")
print("Tupla 9 sin modificaciones: " + str(tupla9))
tupla9 = list(tupla9)
print("tupla 9 convertida a lista: " + str(tupla9))
tupla9[2]= "Amarillo"
tupla9 = tuple(tupla9)
print("Tupla 9 nuevamente tupla con modificaciones: " + str(tupla9))
print("---------------------------------------------------------")
print("---------------------Ejercicio #9------------------------")
my_tuple = ("Hola","como","estan")
print(my_tuple)
del(my_tuple)
#print(my_tuple) NameError: name 'my_tuple' is not defined

print("---------------------------------------------------------")
print("---------------------Ejercicio #10-----------------------")
tupla10 = (100,)
print(tupla10)
print(type(tupla10))