#TP34
def caracter_entre_cada_letra(cadena):
    print("Caracter entre cada letra")
    p=""
    for x in range(len(cadena)):
         p=p+cadena[x]+","
    print(p[:-1])
         
def espacios(cadena):
    ca=""
    carac="_"
    for x in range(len(cadena)):
        if cadena[x]==" ":
            ca=ca+carac
        else:
            ca=ca+cadena[x]
    print("Espacios por '_' ")
    print(ca)
def digitos_por_el_caracter(cadena):
    ca=""
    carac="X"
    for x in range(len(cadena)):
        ca=ca+carac
    print("Su clave es:",ca)
def caracter_cada_tres(cadena):
    carac="."
    ca=""
    w=0
    for x in range(len(cadena)):
        w=w+1
        ca=ca+cadena[x]
        if w==3:
            ca=ca+carac
            w=0
    print("Caracter cada 3 digitos")
    print(ca)
    
#Bloque principal
print("*********************")
caracter_entre_cada_letra("separar")
print("*********************")
espacios("mi archivo de texto.txt")
print("*********************")
digitos_por_el_caracter("1540")
print("*********************")
caracter_cada_tres("2552552550")



