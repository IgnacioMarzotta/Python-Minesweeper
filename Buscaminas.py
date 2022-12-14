#                   Grupo 5
#   Ignacio Agustin Marzotta Díaz (23.601.779-6) / NRC 17337
#   Diego Angel Díaz Muñoz (20.552.571-8) / NRC 17337

characters = ["a", "b", "c", "d", "e", "f"]
numbers = ["1", "2", "3", "4", "5", "6"]
mainMatrix = [ ["N","N","N","N","N","N"],
               ["N","N","N","N","N","N"],
               ["N","N","N","N","N","N"],
               ["N","N","N","N","N","N"],
               ["N","N","N","N","N","N"],
               ["N","N","N","N","N","N"] ]

bombsPosition = str(input("Ingresa las posiciones de las minas: ").lower())

while((len(bombsPosition) != 6) or (bombsPosition[0] not in characters) or (bombsPosition[1] not in numbers) or (bombsPosition[2] not in characters) or (bombsPosition[3] not in numbers) or (bombsPosition[4] not in characters) or (bombsPosition[5] not in numbers)):
    print("Error, recuerda usar el formato correcto.")
    bombsPosition = str(input("Ingresa las posiciones de las minas: ").lower())
else:
    mainMatrix[characters.index(bombsPosition[0])][numbers.index(bombsPosition[1])] = "B"
    mainMatrix[characters.index(bombsPosition[2])][numbers.index(bombsPosition[3])] = "B"
    mainMatrix[characters.index(bombsPosition[4])][numbers.index(bombsPosition[5])] = "B"

    #Primer print de tabla despues de ingresar posicion de bombas
    y = 0
    print("  ", end="")
    for i in numbers:
        print(numbers[y], end="  ")
        y += 1
    print( )

    x = 0
    for i in mainMatrix:
        print(characters[x].upper(), end="")
        for j in i:
            print(" . ", end="")
        x += 1
        print( )

    emptyCellCounter = 2

    while(emptyCellCounter >= 1):
        guessPosition = str(input("Ingresa la posición a descubrir: ").lower())

        bombsNearCounter = 0

        if((len(guessPosition)) == 2 and (guessPosition[0] in characters) and (guessPosition[1] in numbers)):
            #Revisar las posiciones alrededor de guessPosition
            if(mainMatrix[characters.index(guessPosition[0])][numbers.index(guessPosition[1])] != "B"):
                try:
                    #Arriba
                    if(mainMatrix[characters.index(guessPosition[0])+1][numbers.index(guessPosition[1])] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0

                try:
                    #Esq. Arriba Derecha
                    if(mainMatrix[characters.index(guessPosition[0])+1][numbers.index(guessPosition[1])+1] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0

                try:
                    #Esq. Arriba Izquierda
                    if(mainMatrix[characters.index(guessPosition[0])+1][numbers.index(guessPosition[1])-1] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0

                try:
                    #Derecha
                    if(mainMatrix[characters.index(guessPosition[0])][numbers.index(guessPosition[1])+1] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0

                try:
                    #Izquierda
                    if(mainMatrix[characters.index(guessPosition[0])][numbers.index(guessPosition[1])-1] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0
                
                try:
                    #Abajo
                    if(mainMatrix[characters.index(guessPosition[0])-1][numbers.index(guessPosition[1])] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0

                try:
                    #Esq. Abajo Derecha
                    if(mainMatrix[characters.index(guessPosition[0])-1][numbers.index(guessPosition[1])+1] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0
                
                try:
                    #Esq. Abajo Izquierda
                    if(mainMatrix[characters.index(guessPosition[0])-1][numbers.index(guessPosition[1])-1] == "B"):
                        bombsNearCounter += 1
                except IndexError:
                    bombsNearCounter += 0
            else:
                y = 0
                print("  ", end="")
                for i in numbers:
                    print(numbers[y], end="  ")
                    y += 1
                print( )
                
                x = 0
                for i in mainMatrix:
                    print(characters[x].upper(), end="")
                    for j in i:
                        if(j == 1):
                            print(" 1 ", end="")
                        elif(j == 2):
                            print(" 2 ", end="")
                        elif(j == 3):
                            print(" 3 ", end="")
                        elif(j == 0):
                            print(" 0 ", end="")
                        elif(j == "B"):
                            print(" * ", end="")
                        else:
                            print(" . ", end="")
                    x += 1 
                    print( )
                    
                print("PERDISTE")
                break

            #Reemplazar por la cantidad de minas cerca
            mainMatrix[characters.index(guessPosition[0])][numbers.index(guessPosition[1])] = bombsNearCounter

            emptyCellCounter -= 1

            if(emptyCellCounter != 0):
                emptyCellCounter = 0
                y = 0
                print("  ", end="")
                for i in numbers:
                    print(numbers[y], end="  ")
                    y += 1
                print( )

                x = 0
                for i in mainMatrix:
                    print(characters[x].upper(), end="")
                    for j in i:
                        if(j == 1):
                            print(" 1 ", end="")
                        elif(j == 2):
                            print(" 2 ", end="")
                        elif(j == 3):
                            print(" 3 ", end="")
                        elif(j == 0):
                            print(" 0 ", end="")
                        elif(j == "B"):
                            print(" . ", end="")
                        else:
                            print(" . ", end="")
                            emptyCellCounter += 1
                    x += 1
                    print( )
            else:
                y = 0
                print("  ", end="")
                for i in numbers:
                    print(numbers[y], end="  ")
                    y += 1
                print( )

                x = 0
                for i in mainMatrix:
                    print(characters[x].upper(), end="")
                    for j in i:
                        if(j == 1):
                            print(" 1 ", end="")
                        elif(j == 2):
                            print(" 2 ", end="")
                        elif(j == 3):
                            print(" 3 ", end="")
                        elif(j == 0):
                            print(" 0 ", end="")
                        elif(j == "B"):
                            print(" * ", end="")
                    x += 1
                    print( )
                print("GANASTE")
                break
        else:
            print("Por favor, recuerda usar el formato correcto.")