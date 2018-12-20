def dos_primeros(caracter):
    print("Dos primero caracteres: ")
    print(caracter[0],caracter[1])
def tres_ultimos(caracter):
    cant=len(caracter)
    print("Ultimos tres caracteres:")
    print(caracter[cant-3],caracter[cant-2],caracter[cant-1])
def cada_dos(caracter):
    print("Cadena cada dos caracteres: ")
    print(caracter[::2])
def inverso(caracter):
    print("Cadena en sentido inverso :")
    print(caracter[::-1])
    print()
    
def sentido(caracter):
    ca=""
    print("Cadena en un sentido y en sentido inverso:")
    ca=caracter+caracter[::-1]
    print(ca)
#Bloque Principal
caracter=input("Ingrese palabra: ")
print("----------------------")
dos_primeros(caracter)
print("-----------------------")
tres_ultimos(caracter)
print("-----------------------")
cada_dos(caracter)
print("-----------------------")
caracter=input("Ingrese palabra :")
inverso(caracter)
print("-----------------------")
sentido(caracter)
print("-----------------------")



