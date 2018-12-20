def separaciones_por_miles(num):
    punto="."
    ca=""
    m=0
    pos=-1
    for x in range(len(num)):
        ca=ca+num[pos]
        m=x+1
        if m==3:
            ca=ca+"."
        else:
            if m==6:
                ca=ca+"." 
            else:
                if m==9:
                     ca=ca+"."               
        pos=pos-1      
    print(ca[::-1])
#Bloque principal
separaciones_por_miles("1234567890")
