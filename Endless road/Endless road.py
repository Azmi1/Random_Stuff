import pygame, random

screen = pygame.display.set_mode((640,240))

white = [255, 255, 255]
black = [0, 0, 0]

running = True
Frequency = 1
sensitivity = 3
height = 240
Fast_Loading = True
Show_Cirles = False

roadPoints = []
road_display = []

roadPoint = {}

WhereStart = 1
st = 1

class First_Point(object):
    def __init__(self):
        self.x = 0
        self.height = random.randint(0,240)

class RoadPoint(object):
    def __init__(self, Cluster, sensitivity,RoadPoints, height):
        self.i = len(RoadPoints)-1
        self.x = RoadPoints[self.i].x + Cluster
        if RoadPoints[self.i].height < 10:
            self.height = random.uniform(RoadPoints[self.i].height, RoadPoints[self.i].height+sensitivity)
        elif RoadPoints[self.i].height > 230:
            self.height = random.uniform(RoadPoints[self.i].height-sensitivity, RoadPoints[self.i].height)
            RoadPoints[self.i].height -= 20
        else:
            self.height = random.uniform(RoadPoints[self.i].height-sensitivity, RoadPoints[self.i].height+sensitivity)
        self.y = height
        self.width = 1
    def Draw(self, screen):
        pygame.draw.rect(screen, black,[self.x, self.height, self.width, self.y])
        if Show_Cirles == True:
            pygame.draw.circle(screen, black,[int(self.x),int(self.height)], 2)

#class Road(object):
#    def __init__(self, road):
screen.fill(white)
pygame.display.update()

First_Road = First_Point()
roadPoints.append(First_Road)
print("lol")
while running == True:
    screen.fill(white)
    print("lol")
    for i in range(WhereStart, len(roadPoints)):
        roadPoints[i].Draw(screen)
    roadPoint[st] = RoadPoint(Frequency, sensitivity, roadPoints, height)
    roadPoints.append(roadPoint[st])
    if roadPoint[st].x > 640:
        for i in range(0,len(roadPoints)):
            roadPoints[i].x -= 640
        if Fast_Loading == True:
            WhereStart = len(roadPoints)-1
    elif roadPoint[st].x < -640:
        for i in range(0,len(roadPoints)):
            roadPoints[i].x += 640
        if Fast_Loading == True:
            WhereStart = len(roadPoints)-1
    print("Koliko crt: "+str(len(roadPoints)))
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
