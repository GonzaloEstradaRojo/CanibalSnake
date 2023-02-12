import pygame, random, math

UP = 0
RIGTH = 1
DOWN = 2
LEFT = 3

class Snake(pygame.sprite.Sprite):

   def __init__(self, surface, pos, width):
      pygame.sprite.Sprite.__init__(self)
      self.pos = pos
      self.width = width
      self.rect = pygame.Rect(0,0, self.width, self.width)
      self.surface = surface
      self.dir = RIGTH   
      self.score = 0
      self.body = []

   
   def MoveSnake(self):
      if self.dir == RIGTH:
         self.pos = (self.pos[0] + self.width, self.pos[1])
      elif self.dir == DOWN:
         self.pos = (self.pos[0], self.pos[1] + self.width)
      elif self.dir == LEFT:
         self.pos = (self.pos[0] - self.width, self.pos[1])
      elif self.dir == UP:
         self.pos = (self.pos[0], self.pos[1] - self.width)
      self.DrawSnake()

   def ChangeDirection(self, event):
      if event.key == pygame.K_UP:
         print("UP")
         self.dir = UP
      elif event.key == pygame.K_RIGHT:
         print("RIGTH")
         self.dir = RIGTH
      elif event.key == pygame.K_DOWN:
         print("DOWN")
         self.dir = DOWN
      elif event.key == pygame.K_LEFT:
         print("LEFT")
         self.dir = LEFT

   def DrawSnake(self):
      # self.surface.fill((100,100,100))
      pygame.draw.rect(self.surface, (0,255,0), pygame.Rect(self.pos[0], self.pos[1], self.width, self.width))

   def CheckBorderCollision(self):
      w, h = self.surface.get_size()
      if self.pos[0] + self.width > w:
         self.pos = (0, self.pos[1])
      
      if self.pos[0] < 0:
         self.pos = (w - self.width, self.pos[1])

      if self.pos[1] + self.width > h:
         self.pos = (self.pos[0], 0)
      
      if self.pos[1] < 0:
         self.pos = (self.pos[0], h - self.width)
      



   def AddPiece(self):
      pass

   def EatFruit():
      pass 

   def update(self):
      self.MoveSnake()
      self.CheckBorderCollision()
      self.DrawSnake()
