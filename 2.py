import os
os.system("cls")

n = []
s = []
e = []
hombres = 0
mujeres = 0

#proceso
while len(n) < 5:
    name = input("ingrese nombre: ")
    n.append(name)     
    
while len(s) < 5:
    sexo = input("ingrese sexo: ")
    if sexo == "masculino" or sexo == "femenino":
        s.append(sexo)
        if sexo == "masculino":
            hombres += 1 
        if sexo == "femenino":
            mujeres += 1
   
while len (e) < 5:
    edad = int(input("ingrese edad: "))
    if edad <=17 or edad >= 5:
        e.append(edad)
    else:
        print("ingrese rango valido: ")

promedio = (e[0]+e[1]+e[2]+e[3]+ e[4])/5 
   

print("*********LISTADO*******")
print("nombre de los inscritos son: ", n)
print("sexo de los inscritos: ", s)
print("edad de los inscritos son: ", e)
print("Hay: " ,hombres, "hombres")
print("Hay: ", mujeres, "mujeres")
print("el promedio de edades es: ", promedio)