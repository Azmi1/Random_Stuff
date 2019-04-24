import pygame, random, math

white = [255, 255, 255]
black = [0, 0, 0]

running = True
width = 1080
height = 360
Frequency = 3 # How many pixels are apart of points
sensitivity = 5 # How big the diffrence can be from previous height
Fast_Loading = True # It displays faster without slowing downs through time
Make_Connections = False # you can see it above 5 frequency
Show_Cirles = False # puts circles on top of the points

screen = pygame.display.set_mode((width,height))

roadPoints = []
road_display = []
RoadGroup = []

roadPoint = {}
road = {}

WhereStart = 1
st = 1

class First_Point(object):
    def __init__(self):
        self.x = 0
        self.height = random.randint(0,height)

class RoadPoint(object):
    def __init__(self, Cluster, sensitivity,RoadPoints):
        self.i = len(RoadPoints)-1
        self.x = RoadPoints[self.i].x + Cluster
        if RoadPoints[self.i].height > height-10:
            self.height = random.uniform(RoadPoints[self.i].height-sensitivity, RoadPoints[self.i].height)
        else:
            self.height = abs(random.uniform(RoadPoints[self.i].height-sensitivity, RoadPoints[self.i].height+sensitivity))
        self.y = width - self.height 
        self.width = 1
    def Draw(self, screen):
        pygame.draw.rect(screen, black,[self.x, self.height, self.width, self.y])
        if Show_Cirles == True:
            pygame.draw.circle(screen, black,[int(self.x),int(self.height)], 2)

class First_Road(object):
    def Draw(screen):
        l = 1
class Road(object):
    def __init__(self, road, i):
        self.x = road[i-1].x
        self.y = road[i-1].height
        self.width = math.sqrt(Frequency*Frequency + (road[i].height - road[i-1].height) * (road[i].height - road[i-1].height))
        self.height = 2

    def Draw(self, screen):
        pygame.draw.rect(screen, black,[self.x, self.y, self.width, self.height])

screen.fill(white)
pygame.display.update()

First_point = First_Point()
roadPoints.append(First_point)
First_road = First_Road()
RoadGroup.append(First_road)
print("lol")
while running == True:
    screen.fill(white)
    print("lol")
    for i in range(WhereStart, len(roadPoints)):
        roadPoints[i].Draw(screen)
    if Make_Connections == True:
        for i in range(WhereStart, len(RoadGroup)):
            RoadGroup[i].Draw(screen)
    roadPoint[st] = RoadPoint(Frequency, sensitivity, roadPoints)
    roadPoints.append(roadPoint[st])
    if Make_Connections == True:
        road[st] = Road(roadPoints, len(roadPoints)-1)
        RoadGroup.append(road[st])
    if roadPoint[st].x > width:
        for i in range(0,len(roadPoints)):
            roadPoints[i].x -= width
        if Make_Connections == True:
            for i in range(1,len(RoadGroup)):
                RoadGroup[i].x -= width
        if Fast_Loading == True:
            WhereStart = len(roadPoints)-1
    elif roadPoint[st].x < -width:
        for i in range(0,len(roadPoints)):
            roadPoints[i].x += width
        if Make_Connections == True:
            for i in range(0,len(RoadGroup)):
                RoadGroup[i].x += width
        if Fast_Loading == True:
            WhereStart = len(roadPoints)-1
    print("Koliko crt: "+str(len(roadPoints)))
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
