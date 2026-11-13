# # # # 1. Escribe un programa que verifique si un numero es positivo, negativo o cero.

# # # # 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.

# # # # 3. Escribe un programa que verifique si una cadena de texto esta vaci­a y muestre un mensaje en consecuencia.

# # # # 4. Crea un programa que solicite dos numeros al usuario y compare cual es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

# # # # 5. Escribe un programa que verifique si un numero es divisible por 3 y por 5 al mismo tiempo.

# # # # 6. Solicita al usuario que ingrese un numero y verifica si es par o impar.

# # # # 7. Escribe un programa que determine si una persona puede votar en funcion de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.

# # # # 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.

# # # # 9. Escribe un programa que determine si un numero esta entre 10 y 20 (ambos incluidos).

# # # # 10. Escribe un programa que simule un semaforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.


print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")

numero = int(input("Ingrese un numero por favor: "))
    
if numero > 0:
    print(f"{numero} : Es un numero positivo")
elif numero < 0:
    print(f"{numero} : Es un numero negativo")
else:
    print(f"{numero} : Es igual a 0")

print("---------------------------------------------------------")
print("---------------------Ejercicio #2------------------------")

edad = int(input("Ingrese su edad por favor: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

print("---------------------------------------------------------")
print("---------------------Ejercicio #3------------------------")

mensaje = "Yirumita Yirumon, Yirumita Yirumon"

if mensaje:
    print("Esta es la cancion de Yirumita: " + mensaje)
else:
    print("La variable esta vacia")

print("---------------------------------------------------------")
print("---------------------Ejercicio #4------------------------")

num_a = int(input("Ingrese un numero para asignarle el valor A por favor: "))
num_b = int(input("Ingrese otro numero para asignarle el valor B por favor: "))
if num_a > num_b:
    print("numero A es mayor que numero B")
elif num_a < num_b:
    print("numero B es mayor que numero A")
else:
    print("Ambos numeros tienen el mismo valor")    


print("---------------------------------------------------------")
print("---------------------Ejercicio #5------------------------")

numeros_divisibles = int(input("Ingrese un numero para verificar si es divisible por 3 y por 5: "))

if numeros_divisibles % 3 == 0 and numeros_divisibles % 5 == 0:
    print("El numero ingresado es divisible por 3 y por 5")
else:
    print("El numero ingresado no es divisible por 3 y por 5")

print("---------------------------------------------------------")
print("---------------------Ejercicio #6------------------------")

nro_par = int(input("Ingrese un numero por favor para verificar si es par o impar: "))

if nro_par %2 == 0:
    print("El numero ingresado es un numero par")
else:
    print("El numero ingresado es un numero impar")

print("---------------------------------------------------------")
print("---------------------Ejercicio #7------------------------")

edad = int(input("Ingrese su edad por favor, para verificar si es apto para poder votar: "))
if edad >= 18:
    print("Usted puede votar")
elif edad >= 16 and edad < 18:
    print("Usted puede votar, pero necesita un permiso especial")
else:
    print("Usted no puede votar")

print("---------------------------------------------------------")
print("---------------------Ejercicio #8------------------------")

password = input("Por favor ingrese una contraseña: ")
ver_password = input("Por favor verifique su contraseña: ")

if password == ver_password:
    print("Se ha guardado exitosamente su contraseña")
else:
    print("Contraseña incorrecta")

print("---------------------------------------------------------")
print("---------------------Ejercicio #9------------------------")

numero = 9
if numero >= 10 and numero <= 20:
    print("numero es mayor o igual a diez y menor o igual a 20")
else:
    print("numero es menor que 10 o es mayor que 20")

print("---------------------------------------------------------")
print("---------------------Ejercicio #10-----------------------")
color = input("Por favor ingrese un color entre Rojo, Amarillo y Verde: ").upper()
if color == "VERDE":
    print("Avance")
elif color == "AMARILLO":
    print("Avance con cuidado")
elif color == "ROJO":
    print("Detengase")
else:
    print("Color no valido")