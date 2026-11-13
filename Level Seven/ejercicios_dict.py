# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

# 2. Accede al valor de la clave name en el diccionario.

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

# 6. Crea un diccionario donde las claves sean numeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

# 7. Verifica si la clave age esta presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

# 8. Imprime solo las claves del diccionario.

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".


print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")
dict1 = {
    "name" : "Lucas",
    "age"  : 34,
    "country" : "Argentina"    
}

print(dict1)

print("---------------------------------------------------------")
print("---------------------Ejercicio #2------------------------")
print(dict1["name"])

print("---------------------------------------------------------")
print("---------------------Ejercicio #3------------------------")
dict1["job"]= "Programador"
print(dict1)

print("---------------------------------------------------------")
print("---------------------Ejercicio #4------------------------")
dict1["age"]= 38
print(dict1)

print("---------------------------------------------------------")
print("---------------------Ejercicio #5------------------------")

del dict1["country"]
print(dict1)

print("---------------------------------------------------------")
print("---------------------Ejercicio #6------------------------")
dict2 = {x: x**2 for x in range(1, 6)}
print(dict2)

print("---------------------------------------------------------")
print("---------------------Ejercicio #7------------------------")
dict3 = {
    "name": "Brais",
    "age": 37, 
    "country": "Galicia"
    }

print("age" in dict3)

print("---------------------------------------------------------")
print("---------------------Ejercicio #8------------------------")
print(dict3.keys())

print("---------------------------------------------------------")
print("---------------------Ejercicio #9------------------------")
lista_keys = list(dict3.keys())
print(lista_keys)

print("---------------------------------------------------------")
print("---------------------Ejercicio #10-----------------------")
new_dict = dict3.fromkeys(lista_keys, "Desconocido")
print(new_dict)