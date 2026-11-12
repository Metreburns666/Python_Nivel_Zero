# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.

# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

# 6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] y almacÃ©nalo en una variable. Imprime la variable y la lista.

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).

print("Resolucion")
print("-------------------")
print("Ejercicio 1")

lista = [1,2,3,4,5]

print("Lista del 1 al 5: " + str(lista))

print("-------------------")
print("Ejercicio 2")

lista2 = [10, 20, 30, 40, 50]
print("Lista 2: " + str(lista2))
print("El tercer elemento de la lista2 es: "+str(lista2[2]))

print("-------------------")
print("Ejercicio 3")

lista.append(6)
print("Lista del 1 al 6: " + str(lista))

print("-------------------")
print("Ejercicio 4")

lista2.insert(2, 15)

print("Lista 2 con el nro 15: " + str(lista2))

print("-------------------")
print("Ejercicio 5")

lista2.remove(30)

print("Lista 2 sin nro 30: " + str(lista2))

print("-------------------")
print("Ejercicio 6")

nro_eliminado = lista.pop()

print("Se elimino de la lista 1 el siguiente nro: " + str(nro_eliminado))
print("Asi quedo la lista 1: " + str(lista))

print("-------------------")
print("Ejercicio 7")

lista3 = [100, 200, 300, 400, 500]
print("La lista 3: " + str(lista3))
lista3.reverse()
print("La lista 3 a la inversa: " + str(lista3))

print("-------------------")
print("Ejercicio 8")

lista4=[3, 1, 4, 2, 5]
print("Lista 4: "  + str(lista4))
lista4.sort() 
print("Lista 4 ordenada: " + str(lista4))

print("-------------------")
print("Ejercicio 9")

lista5 = [1,2,3]
print("La lista 5 es: " + str(lista5))
lista6 = [4,5,6]
print("La lista 6 es: " + str(lista6))
lista7 = lista5 + lista6
print("La lista 7 es:" + str(lista7))

print("-------------------")
print("Ejercicio 10")

lista8 = [10, 20, 30, 40, 50]
print("Lista 8: " + str(lista8))

sublista8 = lista8[1:3]

print("Sublista del elemento 1 al 3 de la lista 8: " + str(sublista8))
print(type(sublista8))