# for se usa  cuando el numero dd iteraciones es concocido o esta iterrando en colecciones
#while cuando las iteraciones dependen de unna condicion dinamica 

import random #generar numeros aleatorios
print("🧙‍ Bienvenidos al programa de adivana🔮🎲")
print("las reglas son simples,pienso en un numero y tu adivinas")

number = random.randint(1,10)#simulara la accion de pienso en un numero

adivinobien = False # varible bool
# mientras que es correcto no sea verdad sigo con el juego
while adivinobien != True:
    adivino = int(input("ingresa un numero "))
    
    if adivino == number:
        adivinobien = True
        print("🎉🎊🥳 adivinaste ")
    else:
        print("no aun no lo adivinas, vuelve a intentar ")
        