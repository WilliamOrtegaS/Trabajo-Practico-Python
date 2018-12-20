def primera_letra(palabra):
  p=palabra.upper()
  cadena=p.split(" ")
  for x in range(len(cadena)):
      print(cadena[x][0],end="")
  print("")
  
  oracion=palabra.title()
  print(oracion)
  for x in range(len(cadena)):
      if cadena[x][0]=="A" or cadena[x][0]=="a":
          print(cadena[x])

  
    
primera_letra("Republica Argentina")
        
    
