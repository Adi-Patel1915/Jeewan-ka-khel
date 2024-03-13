import pygame as game
import random as rndm
#--------------------
game.init()
Width = 500
Height = 500

CellSize = 10
StateColor = ((0, 0, 0), (255, 255, 255))
Canvas = game.display.set_mode((Width, Height))
game.display.set_caption("Canvas")
Switch = True
Clock = game.time.Clock()
FPS = 144 #FPS here
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
for i in range(0, Width - 9, CellSize):
    for j in range(0, Height - 9, CellSize):
        celllist.append(CELL(i, j))
while Switch:
    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            Switch = False

    for i in celllist:
        i.Draw()

    
    game.display.update()
    Clock.tick(FPS)