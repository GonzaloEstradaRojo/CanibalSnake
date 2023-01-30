import pygame, random, math


width, height = 800, 800
FPS = 30
run, gameOver = True, False
cols,rows = 30,30
rectW, rectH = width/cols, height/rows

screen = pygame.display.set_mode((width, height))
board = [[0 for _ in range(cols)] for _ in range(rows)]

pygame.init()


def ResetBoard():
    global board
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    
def DrawBoard():
    for i in range(len(board)):
        for j in range(len(board)[i]):
            pygame.draw.rect
def GameLoop():
    global running, gameOver
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_r]:
            GameLoop()
     

if __name__ == "__main__":
    GameLoop()