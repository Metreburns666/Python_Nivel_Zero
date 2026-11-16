# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un metodo "make_sound" que imprima un sonido generico.

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacenala en una propiedad publica. AÃ±ade el metodo "make_sound" que imprima un sonido dependiendo de la especie.

# 3. Crea una clase llamada "Car" con las propiedades publicas "brand" y "model". Ademas, debe tener una propiedad privada "_speed" que inicialmente sera 0.

# 4. Añade a la clase "Car" un metodo llamado "accelerate" que aumente la velocidad en 10 unidades. Añade tambien un metodo "brake" que reduzca la velocidad en 10 unidades. Asegurate de que la velocidad no sea negativa.

# 5. Crea una clase "Book" que tenga propiedades como "title" (publico) y "author" (privado). Añade un metodo para obtener el autor y otro para cambiar el titulo del libro.

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade metodos para depositar y retirar dinero, asegurandote de que no se pueda retirar mas de lo que hay en la cuenta.

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un metodo que calcule la distancia entre dos puntos.

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un metodo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

print("---------------------------------------------------------")
print("----------------------Respuestas-------------------------")
print("---------------------------------------------------------")
print("---------------------Ejercicio #1------------------------")

class Animal:

    def __init__(self,species):
        self.species = species

    def make_sound(self):
        print("Sonido Generico")

Yaguarete = Animal("Yaguarete")
Yaguarete.make_sound()
print("---------------------------------------------------------")
print("---------------------Ejercicio #2------------------------")

class Animal:
    def __init__(self,species):
        self.species = species

    def make_sounds(self):
        if self.species == "Gato":
            print("Miauuu")
        elif self.species == "Perro":
            print("Guaw Guaw")
        else:
            print("Sonido Generico")

Yiruma = Animal("Gato")
Yiruma.make_sounds()

print("---------------------------------------------------------")
print("-------------------Ejercicio #3 y #4---------------------")

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed +=10         

    def brake(self):
        self.__speed -=10
    
    def get_speed(self):
        return f" La velocidad actual es de {self.__speed}"
        

sututu = Car("Subaru","Impreza STI WRX")
print(sututu.brand)
print(sututu.model)
print(sututu.get_speed())
sututu.accelerate()
sututu.accelerate()
sututu.accelerate()
sututu.accelerate()
print(sututu.get_speed())
sututu.brake()
print(sututu.get_speed())

print("---------------------------------------------------------")
print("---------------------Ejercicio #5------------------------")

# 5. Crea una clase "Book" que tenga propiedades como "title" (publico) y "author" (privado). Añade un metodo para obtener el autor y otro para cambiar el titulo del libro.


class Book:
    def __init__(self,titulo,author):
        self.title = titulo
        self.__author = author

    def get_author(self):
        return f"El nombre del autor es: {self.__author}"    

    def cambiar_titulo(self,nvo_titulo):
        self.title = nvo_titulo


libro = Book("Parque Jurasico", "Michael Crichton")
print(libro.title)
print(libro.get_author())
libro.cambiar_titulo("Jurassic Park")
print(libro.title)

print("---------------------------------------------------------")
print("---------------------Ejercicio #6------------------------")
# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self,nombre,apellido,lista_notas):
        self.nombre = nombre
        self.apellido = apellido
        self.fullname = f"{nombre} {apellido}"
        self.notas = lista_notas

    def promedio(self):
        sum_notas = 0
        cant_notas = len(self.notas)
        for nota in self.notas:
            sum_notas += nota
        promedio = sum_notas / cant_notas
        return f"Las calificaciones del alumno {self.fullname} tienen un promedio de {promedio}"

lista_notas = [10,10,7,8,8,10]

lucas = Estudiante("Lucas","Metrebian",lista_notas)

print(lucas.fullname)
print(lucas.promedio())

print("---------------------------------------------------------")
print("---------------------Ejercicio #7------------------------")
# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade metodos para depositar y retirar dinero, asegurandote de que no se pueda retirar mas de lo que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposito(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
        else:
            print("Saldo insuficiente")

print("---------------------------------------------------------")
print("---------------------Ejercicio #8------------------------")

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un metodo que calcule la distancia entre dos puntos.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y ** 2) ** 0.5

print("---------------------------------------------------------")
print("---------------------Ejercicio #9------------------------")
# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee:

    def __init__(self, nombre, paga_hora, horas_trabajo):

        self.name = nombre
        self.hourly_wage = paga_hora
        self.hours_worked = horas_trabajo

    def generar_pago(self):
        return self.hourly_wage * self.hours_worked
        

lucas = Employee("Lucas",25,10)


print(lucas.generar_pago())

print("---------------------------------------------------------")
print("---------------------Ejercicio #10-----------------------")

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un metodo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:
    def __init__(self,lista_productos):
        self.inventory = lista_productos

    def agregar_producto(self,producto):
        self.inventory.append(producto)

    def mostrar_productos(self):
        for producto in self.inventory:
            print(f"Producto: {producto}")
        

despensa = Store(["Manzana","Pera","Banana"])

despensa.mostrar_productos()
despensa.agregar_producto("Kiwi")
despensa.mostrar_productos()