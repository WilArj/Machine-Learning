import pygame
import matplotlib.pyplot as plt
import numpy as np
import time

pygame.init()
#--------------------#

#Ancho y alto de la pantalla
width, height = 1000, 1000

# #Creación de la pantalla
screen = pygame.display.set_mode((width, height))

# Número de celdas en x e y
nxC, nyC = 25, 25

# Dimensiones de cada celda según dimensiones de pantalla y número de celdas fijadas
dimCW = (width)/nxC
dimCH = (height)/nyC

# Color del fondo, gris oscuro
bg = 25, 25, 25

# Rellenamos el fondo con el color elegido
screen.fill(bg)

# Estado de las celdas. Vivas = 1, muertas = 0. Iniciamos matriz con todas muertas
gameState = np.zeros((nxC, nyC))

# Inicializamos autómata con movimientos y palos osciladores
gameState[6,0]=1
gameState[0,1]=1
gameState[1,1]=1
gameState[1,2]=1
gameState[5,2]=1
gameState[6,2]=1
gameState[7,2]=1

# gameState[13,4]=1
# gameState[14,5]=1
# gameState[15,3]=1
# gameState[15,4]=1
# gameState[15,5]=1

gameState[12,17]=1
gameState[12,18]=1
gameState[12,19]=1

gameState[15,20]=1
gameState[15,21]=1
gameState[15,22]=1



# Bucle de ejecución
while True:

    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.01)

    for y in range(0, nxC):
        for x in range(0, nyC):

            # #Calculamos el número de vecinos cercanos usando la técnica toroidal para hacer que lo que desaparezca por un límite de la pantalla aparezca por el otro (muy interesante el uso del módulo % )
            nn =  gameState[(x-1) % nxC, (y-1) % nyC] + \
                  gameState[(x)   % nxC, (y-1) % nyC] + \
                  gameState[(x+1) % nxC, (y-1) % nyC] + \
                  gameState[(x-1) % nxC, (y)   % nyC] + \
                  gameState[(x+1) % nxC, (y)   % nyC] + \
                  gameState[(x-1) % nxC, (y+1) % nyC] + \
                  gameState[(x)   % nxC, (y+1) % nyC] + \
                  gameState[(x+1) % nxC, (y+1) % nyC]
            
            print("total de vecinos", nn)
            print(gameState[x,y])

            # # Regla 1: Una céluna muerta con exactamente 3 vecinas vivas, revive
            if gameState[x, y] == 0 and nn == 3:
                newGameState[x, y] = 1


            # # Regla 2: Una célula viva con menos de 2 o más de 3 vecinas vivas, muere
            elif gameState[x, y] == 1 and (nn < 2 or nn > 3):
                newGameState[x, y] = 0

            # # Creamos el polígono de cada celda
            poly = [((x)    * dimCW, y * dimCH),
                    ((x+1)  * dimCW, y * dimCH),
                    ((x+1)  * dimCW, (y+1) * dimCH),
                    ((x)    * dimCW, (y+1) * dimCH)]
            


            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (240, 240, 240), poly, 0)


    gameState = np.copy(newGameState)
    pygame.display.flip()

