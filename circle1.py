import pygame

WIDTH = 600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))

run = True

class Circle():
    def __init__(self,x,y,r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def display(self):
        pygame.draw.circle(screen,self.color,(self.x, self.y),self.r)
    def grow(self):
        self.r = self.r + 10
        self.display()

c1 = Circle(300,450,50,"white")
screen.fill("sky blue")
pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
        if event.type == pygame.MOUSEBUTTONDOWN:
                c1.display()
                pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
                c1.grow()
                pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                print(pos)
                c2 = Circle(pos[0],pos[1],10,"yellow")
                c2.display()
                pygame.display.update()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    screen.fill("sky blue")
                    c1.y -= 5
                    c1.display()
                    pygame.display.update()
                if event.key == pygame.K_s:
                    screen.fill("sky blue")
                    c1.y += 5
                    c1.display()
                    pygame.display.update()
                if event.key == pygame.K_d:
                    screen.fill("sky blue")
                    c1.x += 5
                    c1.display()
                    pygame.display.update()
                if event.key == pygame.K_a:
                    screen.fill("sky blue")
                    c1.x -= 5
                    c1.display()
                    pygame.display.update()


                    
                    