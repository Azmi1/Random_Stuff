import pygame, random, math, os, random

white = [255, 255, 255]
black = [0, 0, 0]

running = True
width = 1080
height = 840

screen = pygame.display.set_mode((width,height))

rounded_speed = 10

Pictures = []
picture = {}
st = 0
entries = os.listdir('Images')
for entry in entries:
    picture[st] = pygame.image.load("Images/"+entry).convert_alpha()
    Pictures.append(picture[st])
    print(entry)

class Background_Parallax(object):
    def __init__(self, id, picture, y = '0'):
       self.picture = picture
       self.y = int(y)
       if id == 1:   
           self.speed = random.uniform(rounded_speed-1, rounded_speed+1)
           st = 0
           self.x = 0
       if id == 2:
           self.speed = Background[len(Background_second)].speed
           st = 0
           self.x = 1910
       print(self.speed)
    def moveleft(self):
        self.x -= self.speed
    def Check_boundry(self):
        if self.x < -1910:
            self.x = 1910
    def display(self, screen):
        screen.blit(self.picture, (self.x,self.y))

Background =[]
Back = Background_Parallax(1, Pictures[0])
Background.append(Back)
Clouds = Background_Parallax(1, Pictures[1])
Background.append(Clouds)
Trees = Background_Parallax(1, Pictures[2], 500)
Background.append(Trees)
Background_second =[]
Back_second = Background_Parallax(2, Pictures[0])
Background_second.append(Back_second)
Clouds_second = Background_Parallax(2, Pictures[1])
Background_second.append(Clouds_second)
Trees_second = Background_Parallax(2, Pictures[2], 500)
Background_second.append(Trees_second)

while running == True:
    screen.fill(white)
    for layer in Background:
        layer.moveleft()
        layer.display(screen)
        layer.Check_boundry()
    for layer in Background_second:
        layer.moveleft()
        layer.display(screen)
        layer.Check_boundry()
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == pygame.QUIT: #For ending the loop
            pygame.quit()
