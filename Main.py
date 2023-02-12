import pygame, random, math
import Snake as s

width, height = 800, 800
cols,rows = 25,25
FPS = 10
running, gameOver = True, False
rectW = width/cols

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
# screen.fill((100,100,100))

board = [[0 for _ in range(cols)] for _ in range(rows)]

def ResetBoard():
    global board
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    
def DrawBoard():
    screen.fill((255,255,255))
    for i in range(len(board)):
        for j in range(len(board[i])):

            rect = pygame.Rect(i*rectW, j*rectW, rectW, rectW)
            pygame.draw.rect(screen, (100,100,100), rect,1)
def GameLoop():
    global running, gameOver
    
    s1 = s.Snake(screen, (0,0),rectW)
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                s1.ChangeDirection(event)
            if pygame.key.get_pressed()[pygame.K_r]:
                ResetBoard()
                GameLoop()
        DrawBoard()
        s1.update()
        
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    GameLoop()