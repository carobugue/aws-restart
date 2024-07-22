"""
tipo de datos primitivo
## booleamos bools
 valor de verdad: True o false
 
 """
#### lista

"""
es una coleccio ordenada de valores
se define con [] y se separa sus elemetos con , 
los elementos puedens ser cualquier tipo de dato 


"""
# con las lista los indices siempre empiezan en 0
personas = ["anahi", "david," "ariel" ]
numeros = [100,98,86]
 

myFruitList = ["manzana","banana","pera","uva"]

print(f"La lista de frutas es {myFruitList}")
print(f"El tipo de dato es {type(myFruitList)}")

# si quiero imprimir un elemento debo hacerlo por su indice

print(f"el segundo elemento es {myFruitList[1]}")

# error tipo tipico es intentar acceder a un indice que no existe 

# puedo cambiar el valor en los elementos
# quiero cambiar banana por coco(indice 1 )

myFruitList[1] = "coco"

print(f"la nueva lista es {myFruitList}")

""""
tupla
muy similar a la lista
se define con corchetes redondos () y se separa con las ,
no es  mutable ( no se le puede agregar, quitar nada )

"""
myFinalTuple = ("manzana","banana","pera","uva")
print(f"la lista de tupla {myFinalTuple}")
print(type(myFinalTuple))

# para acceder a aun alemento lo hago igual que lista
# () para iniciar una funcion
#{} para agregar una variable con un f para hacer una diccionario
# , da espacio automatico
# 

print(myFinalTuple[1])

"""
diccionario
coleccion de valores guardados con un modelos llave valor
el diccionario se define con{} y elemento separados por,
cada elemento se ve llave : valor 


"""
persona = {"nombre": "carolina bugueño ", "ciudad":"santiago","edad":"32"}

print(persona)
print(type(persona))

# la manera de acceder a un valor es por su llave 

print(persona["ciudad"])
# son mutables
#puedo cambiar un valor

persona["ciudad"] = "viña del mar"

print(persona["ciudad"])

##input te ayuda a preguntar por ese valor

persona["ciudad"] = input ("cual es tu ciudad")

### lista de canciones

lista5canciones = ["on my live","ojitos bonitos","alone","smells like","contigo"]
print(f"mi musica {lista5canciones}")
print( f"mi top1 {lista5canciones[0]}")
print(f"mi top5 {lista5canciones[4]}")

## diccionario de ropa


ropa = { "polera": "beige","pantalon":"azul","zapatos":"blancos"}
print(f" mi ropa {ropa}")
print(ropa["polera"])




























 