# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).
print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")

def division(dividendo,divisor):
    try:
        resultado = dividendo/divisor
        return print(f"El numero resultante de la division entre {dividendo} y {divisor} es de {resultado}")
    except:
        divisor = 0
        print("Error: No se puede dividir por cero")

operacion = division(23,0)
segunda_operacion = division(25,5)

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.

def convertir_entero(valor):
    try:
        return int(valor)
    except ValueError as error:
        print(f"Se ha generador un error del tipo {ValueError} explicacion: {error}")

texto = convertir_entero("Texto")
print(texto)
texto2 = convertir_entero("25")
print(texto2)
texto3 = convertir_entero(5.2)
print(texto3)

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

def leer_archivo(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")

"""
bueno no segui mas con los ejercicios por que me dio fiaca, 
pero ya habia entendido la logica xD
"""

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el caso donde el índice esté fuera de rango.

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.