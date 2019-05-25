import pygame, random, math, os, random

white = [255, 255, 255]
black = [0, 0, 0]

running = True
width = 1080
height = 840

screen = pygame.display.set_mode((width,height))

rounded_speed = 10 #if you put the sensitivity higher than rounded_speed it has the chance to go backwards
sensitivity = 10

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
           self.speed = random.uniform(rounded_speed-sensitivity, rounded_speed+sensitivity)
           if self.speed == 0:
               self.speed = random.uniform(rounded_speed-sensitivity, rounded_speed+sensitivity)
           st = 0
           self.x = 0
       print(self.speed)
    def moveleft(self):
        self.x -= self.speed
    def Check_boundry(self):
        if self.x < -1910:
            self.x = 1910
        elif self.x > 1910:
            self.x = -1910
    def display(self, screen):
        screen.blit(self.picture, (self.x,self.y))
        if self.x > 0:
            screen.blit(self.picture, (self.x-1920,self.y))
        if self.x <= 0:
            screen.blit(self.picture, (self.x+1920,self.y))

Background =[]
Back = Background_Parallax(1, Pictures[0])
Background.append(Back)
Clouds = Background_Parallax(1, Pictures[1])
Background.append(Clouds)
Trees = Background_Parallax(1, Pictures[2], 500)
Background.append(Trees)


while running == True:
    screen.fill(white)
    for layer in Background:
        layer.moveleft()
        layer.display(screen)
        layer.Check_boundry()
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == pygame.QUIT: #For ending the loop
            pygame.quit()
