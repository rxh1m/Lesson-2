import pygame

WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))

run = True

class Rect():
    def __init__(self,x,y,w,h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def display(self):
        pygame.draw.rect(screen,self.color,(self.x, self.y, self.w, self.h))
    def grow(self):
        self.w = self.w + 10
        self.h = self.h + 10
        self.display()

r1 = Rect(0,0,50,50,"white")
screen.fill("sky blue")
pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
        if event.type == pygame.MOUSEBUTTONDOWN:
                r1.display()
                pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
                r1.grow()
                pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                print(pos)
                r2 = Rect(pos[0],pos[1],10,10,"yellow")
                r2.display()
                pygame.display.update()