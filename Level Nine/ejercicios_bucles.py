# 1. Usa un bucle while para imprimir los numeros del 1 al 10.

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada numero.

# 3. Escribe un programa que use un bucle while para sumar los numeros del 1 al 100 e imprime el resultado.

# 4. Escribe un bucle for que imprima cada caracter de la cadena "Python".

# 5. Usa un bucle while para encontrar el primer numero divisible por 7 entre 1 y 50.

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

# 7. Escribe un programa que use un bucle while para imprimir los numeros pares entre 1 y 20.

# 8. Usa un bucle for con la funcion range() para imprimir los numeros del 1 al 10 en orden inverso.

# 9. Escribe un programa que use un bucle for para contar cuantas veces aparece el numero 30 en la lista[30, 10, 30, 20, 30, 40].

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")
numero = 0

while numero < 10:
    numero += 1
    print(numero)

print("---------------------------------------------------------")
print("---------------------Ejercicio #2------------------------")

lista = [10, 20, 30, 40, 50]

for numero in lista:
    print(numero)

print("---------------------------------------------------------")
print("---------------------Ejercicio #3------------------------")

suma= 0
numero = 0

while numero <100:
    numero +=1
    suma += numero
else:
    print("La suma de todos los numeros del 1 al 100 es: " + str(suma))

print("---------------------------------------------------------")
print("---------------------Ejercicio #4------------------------")

caracter = "Python"

for letra in caracter:
    print(letra)

print("---------------------------------------------------------")
print("---------------------Ejercicio #5------------------------")

numero = 0

while numero <50:
    numero +=1
    if numero %7 == 0:
        print(f"El numero {numero} es divisible por 7")
        break

print("---------------------------------------------------------")
print("---------------------Ejercicio #6------------------------")

dict = {"name": "Brais", "age": 37, "country": "Galicia"}

for clave in dict:
    print(clave)

print("---------------------------------------------------------")
print("---------------------Ejercicio #7------------------------")

numero = 0
while numero <20 :
    numero += 1
    if numero %2 == 0:
        print(f"Este numero {numero}, es un numero par")

print("---------------------------------------------------------")
print("---------------------Ejercicio #8------------------------")
numero = 10
con = 0
for con in range(0,10):
    print(numero)
    numero -=1
    con +=1

print("---------------------------------------------------------")
print("---------------------Ejercicio #9------------------------")

lista =[30, 10, 30, 20, 30, 40]
cant = 0
for numero in lista:
    if numero == 30:
        cant +=1 
print(f"El numero 30 aparece en esta lista {lista} es de: {cant} veces")


print("---------------------------------------------------------")
print("---------------------Ejercicio #10-----------------------")
lista_nombres = ["Lucas","Gaston","Valentin","Daiana","Pablo","Christian","Carlo","Claudio","Brais","Guillermina","Pedro","Batman"]
for nombre in lista_nombres:
    print(nombre)
    if nombre == "Brais":
        print(f"Hemos encontrado al señor {nombre}, y con el esta lleno el barco")
        break