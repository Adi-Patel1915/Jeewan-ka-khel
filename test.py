import pygame as game
import numpy
import random as rndm
#--------------------
game.init()
Width = 1920
Height = 1200

CellSize = 20
StateColor = ((0, 0, 0), (255, 255, 255))
Canvas = game.display.set_mode((Width, Height))
game.display.set_caption("Game of Life X Game Theory")
Switch = True
Clock = game.time.Clock()
FPS = 60 #FPS here
#--------------------
class CELL():
    def __init__(self, x, y): # will add a future parameter state
        self.x = x
        self.y = y
        self.Rect = game.rect.Rect(self.x, self.y, CellSize, CellSize)
        self.state = rndm.randint(0, 1)

    def Draw(self):
        game.draw.rect(Canvas, StateColor[self.state], self.Rect)





#--------------------
celllist = []
for i in range(0, (Width - CellSize) + 1, CellSize):
    temp = []
    for j in range(0, (Height - CellSize) + 1, CellSize):
        temp.append(CELL(i, j))
    
    celllist.append(temp)
#-------------------------------------------
def NextState(Celllist):
    CurrentState = Celllist.copy()
    for i in range(len(CurrentState)):
        for j in range(len(CurrentState[0])):
            neighbor = 0
            for xoffset in range(-1,2):
                for yoffset in range(-1,2):
                    if (i + xoffset < 0) or (i + xoffset > len(CurrentState) - 1) or (j + yoffset < 0) or (j + yoffset > len(CurrentState[0]) - 1) or (xoffset == 0 and yoffset == 0):
                        continue
                    elif CurrentState[i + xoffset][j + yoffset].state == 1:
                        neighbor += 1
            
            if neighbor <= 1 and Celllist[i][j].state == 1:
                Celllist[i][j].state = 0
            elif neighbor >= 4 and Celllist[i][j].state == 1:
                Celllist[i][j].state = 0
            elif (neighbor == 2 or neighbor == 3) and Celllist[i][j].state == 1:
                Celllist[i][j].state = 1
            elif neighbor == 3 and Celllist[i][j].state == 0:
                Celllist[i][j].state = 1


    return None

#-------------------------------------------
while Switch:
    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            Switch = False

    for i in celllist:
        for j in i:
            j.Draw()

    NextState(celllist)
    game.display.update()
    Clock.tick(FPS)