
import os

def main(adivinado, error, este, tamaño):

    win = True
    z = 0
    while win and z < tamaño:
        if adivinado[z] == 0:
            win = False
        else:
            z = z + 1
        
    if not win and error != 10:
        letra = input("\nSeleccione una letra : ")
        
        for i in range(0,tamaño):
            if letra == palabra[i]:
                este[i] = 1
                adivinado[i] = 1

        este1 = []
        este1 += este

        for j in range(0, tamaño):
            este1[j] = 0
                       
        if este == este1:
            error = error + 1
            print("\nEsa letra no esta, numero de errores: " + str(error))
                
        for c in range(0,tamaño):
            if adivinado[c] == 1:
                print(palabra[c], end = " ")
            else:
                print("_", end = " ")
        print("\n")
                
        main(adivinado, error, este1, tamaño)
        
    elif error == 10:
        print("\n\n     HAS PERDIDO")
        
    else:
        print("\n\n     HAS GANADO")

def introduccion():
    tamaño = int(input("Escribe longitud de la palabra : "))

    palabra = input("\nEscribe la palabra: ")

    if len(palabra) != tamaño:
        print("\nLa palabra no tiene la longitud correcta\n")
        introduccion()

    return tamaño, palabra
        
print("Ahorcado\n========\n")

tamaño,palabra = introduccion()

os.system("cls")

print("Ahorcado\n========\n")

adivinado = []

print("Tienes 10 errores para acertar esta palabra: ", end = "")
for i in range(0, tamaño):
    print("_", end = " ")
    adivinado.append(0)

main(adivinado, 0, adivinado, tamaño)
input()

    

