# 1. Crea un set con los numeros del 1 al 5 e impri­melo.

# 2. Añade el numero 6 al set {1, 2, 3, 4, 5} e impri­melo.

# 3. Intenta añadir el numero 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Que sucede?

# 4. Verifica si el numero 3 esta en el set {1, 2, 3, 4, 5} e imprime el resultado.

# 5. Elimina el numero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

# 6. Usa el metodo clear() para vaciar un set y luego imprime su longitud.

# 7. Convierte el set {"manzana", "naranja", "platano"} en una lista e imprime el primer elemento de la lista.

# 8. Realiza la union de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.



print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")
set = {1,2,3,4,5}
print(set)
print("---------------------------------------------------------")
print("---------------------Ejercicio #2------------------------")
set.add(6)
print(set)
print(type(set))
print("---------------------------------------------------------")
print("---------------------Ejercicio #3------------------------")
set.add(5)
print(set) # No pasa nada ya que es un numero que se encuentra dentro del set y los sets no admiten repetidos
print("---------------------------------------------------------")
print("---------------------Ejercicio #4------------------------")
print("El numero 3 se encuentra dentro de set: " + str(3 in set))
print("---------------------------------------------------------")
print("---------------------Ejercicio #5------------------------")
set.remove(4)
print(set)
print("---------------------------------------------------------")
print("---------------------Ejercicio #6------------------------")
print("Cantidad de elementos que tiene antes de eliminar todo: "+ str(len(set)))
set.clear()
print("Cantidad de elementos despues de borrar todo: "+ str(len(set)))
print("---------------------------------------------------------")
print("---------------------Ejercicio #7------------------------")
set2 = {"manzana", "naranja", "platano"}
set2 = list(set2)
print("El primer elemento de la lista es: "+ set2[0])
print("---------------------------------------------------------")
print("---------------------Ejercicio #8------------------------")
set3= {1,2,3}
set4= {4,5,6}
set_unidos = set3.union(set4)
print(set_unidos)
print("---------------------------------------------------------")
print("---------------------Ejercicio #9------------------------")
set5= {1, 2, 3, 4}
set6= {3, 4, 5, 6}
set_diferencia = set5.difference(set6)
print(set_diferencia)
print("---------------------------------------------------------")
print("---------------------Ejercicio #10-----------------------")
my_set = {}
print(my_set)
del my_set
# print(my_set) NameError: name 'my_set' is not defined