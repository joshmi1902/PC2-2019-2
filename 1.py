import os
os.system("cls")

def contarletra (texto,letra):
    #letra dentro del txt
    for letra in texto:
        if letra.count(texto) == 0:
            print(letra)
    return contarletra

#ejemplos:

x = contarletra("dificilisimo", "i")
print(x)
