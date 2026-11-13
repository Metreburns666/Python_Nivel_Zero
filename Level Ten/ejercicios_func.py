# 1. Crea una funcion llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningun nombre, debe saludar diciendo "Hola, desconocido".

# 2. Escribe una funcion llamada "multiply" que reciba dos numeros como argumentos y retorne el resultado de multiplicarlos.

# 3. Crea una funcion llamada "is_even" que reciba un numero entero como argumento y retorne True si es par y False si es impar.

# 4. Escribe una funcion llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayusculas.

# 5. Crea una funcion llamada "arbitrary_sum" que reciba un numero arbitrario de numeros como argumentos y retorne la suma de todos ellos.

# 6. Escribe una funcion llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

# 7. Crea una funcion llamada "power" que reciba dos numeros: base y exponente, y retorne el resultado de elevar la base al exponente.

# 8. Escribe una funcion llamada "calculate_average" que reciba tres numeros y retorne su promedio.

# 9. Crea una funcion llamada "count_characters" que reciba una cadena de texto y retorne el numero de caracteres que contiene.

# 10. Escribe una funcion llamada "display_messages" que reciba un numero indefinido de cadenas y las imprima en mayusculas, una por una, tal como se hizo en el archivo proporcionado.


print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")

def personalized_greeting(nombre="desconocido"):
    print(f"Hola, {nombre}")

personalized_greeting()
personalized_greeting("Yirumita Yirumon")

print("---------------------------------------------------------")
print("---------------------Ejercicio #2------------------------")

def multiply(numero1,numero2):
    return numero1*numero2

multiplicacion = multiply(29,32)
print(multiplicacion)

print("---------------------------------------------------------")
print("---------------------Ejercicio #3------------------------")

def is_even(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

par_impar = is_even(27)
print(par_impar)
par_impar = is_even(30)
print(par_impar)

print("---------------------------------------------------------")
print("---------------------Ejercicio #4------------------------")

def convert_to_uppercase(texto):
    return texto.upper()

mayus = convert_to_uppercase("un perrito")
print(mayus)

print("---------------------------------------------------------")
print("---------------------Ejercicio #5------------------------")

def arbitrary_sum(*numeros):
    suma = 0

    for numero in numeros:
        suma += numero
    return suma

sum_numeros = arbitrary_sum(28,37,50,100)
print(sum_numeros)

print("---------------------------------------------------------")
print("---------------------Ejercicio #6------------------------")

def generate_full_greeting(nombre, apellido):
    return f"Hola, {nombre} {apellido}"

hola = generate_full_greeting("Lucas", "Manson")
print(hola)

print("---------------------------------------------------------")
print("---------------------Ejercicio #7------------------------")

def power(base, exponente):
    return base**exponente

potencia = power(30,5)
print(potencia)

print("---------------------------------------------------------")
print("---------------------Ejercicio #8------------------------")

def calculate_average(numero1,numero2,numero3):
    cant_numeros = [numero1,numero2,numero3]
    suma = numero1+numero2+numero3
    promedio = suma/len(cant_numeros)
    return promedio

calcular_prom = calculate_average(10,2,5)
print(calcular_prom)

print("---------------------------------------------------------")
print("---------------------Ejercicio #9------------------------")

def count_characters(palabra):
    cant_letras= 0
    for letra in palabra:
        cant_letras +=1
    return cant_letras

cant_caracteres = count_characters("Hipopotamo")
print(cant_caracteres)

print("---------------------------------------------------------")
print("---------------------Ejercicio #10-----------------------")

def display_messages(*textos):
    for texto in textos:
        print(texto.upper())

display_messages("Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon","Yirumita","Yirumon")