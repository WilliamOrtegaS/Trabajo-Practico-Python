def poker(cartas):
    c=0
    for x in range(len(cartas)):
        c=cartas[x]
        cant=0
        for w in range(len(cartas)):
            if cartas[w]==c:
                cant=cant+1
    if cant==4: 
            print("POKER")
    else:
        print("No es un Poker")
#B_P
cartas=(4,4,3,4,4)
poker(cartas)
