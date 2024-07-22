


# Asignación de variable

# Para denotar que se trata de un string utilizamos
# " "
# o
# ' '
# Con la comilla que abro debo cerrar

myString = "Hola"

print(f"El valor de mi variable es {myString} y su tipo es {type(myString)}")

# Operador
# NO puedo hacer directamente operaciones aritméticas

# Concateción
# Unión de dos o más strings

nombre = "carolina"
apellido = "bugueño"

nombre_completo = nombre + " " +  apellido # Es concatenación

print("El nombre completo es:", nombre_completo)

### funcion de entrada  por teclado

# input()
## frena el programa y espera que el usuario ingrese algo por teclado
# por defecto el nombre que  se recibe es de tipo string
nombre = input("ingresa el nombre:  ")

print(f"tu nombre es : {nombre}")

apellido = input("ingresa el apellido:  ")

nombre_completo + " " + apellido 


print(f"hola, tu nombre es :{nombre}")

print(f"tu nombre_completo es: {nombre_completo}   ")

# coversion de tipe de variables
# casting o casteo
# puedo convertir un string a int o float asi

variable = "2"

numero_convertido = int(variable)

print (f"la variable de tipo {type(variable)} y ahora es {type(numero_convertido)}")
print (f"tu nombre es: { nombre}")


# Voy a sumar dos números
# Si no convierto lo que recibo en input será string
# convierto la entrada de input a int

num = int(input("ingresa un numero: ")) # 5
num2 = int(input("Ingresa otro número: ")) # 2

# al ser strings se concatenarán (unen)
resultado = num + num2
5
print (f"La suma de {num} y {num2} es {resultado}")


print (f"Tu nombre es: {nombre}")



