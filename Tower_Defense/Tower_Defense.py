import pygame, time, random, datetime

def Create_screen(width): #creates the screen
    if width % vel_celice != 0:
        width = vel_celice * count
    screen = pygame.display.set_mode((width,width))
    return screen

class Enemy():
    def __init__(self):
        self.path = path
        self.x = int(path[0])
        self.destx = self.x
        self.y = 0
        self.desty = self.y
        self.i = 1
        self.dir = 'X'
        self.timestep = time.clock()
        self.speed = 5
        self.moving = False
    def draw(self, screen):
        pygame.draw.rect(screen, purple, [vel_celice * self.x + (vel_celice/10)/2, vel_celice * self.y + (vel_celice/10)/2, vel_celice - vel_celice/10, vel_celice - vel_celice/10])

    def move(self, fps):
        if self.moving == False:
           self.dir = self.get_direction()
        self.moving = True
        if self.dir == 'S':
            self.y += self.speed/fps
            if self.y > self.desty:
                self.y = self.desty
        elif self.dir == 'W':
            self.y -= self.speed/fps
            if self.y < self.desty:
                self.y = self.desty
        elif self.dir == 'A':
            self.x -= self.speed/fps
            if self.x < self.destx:
                self.x = self.destx
        elif self.dir == 'D':
            self.x += self.speed/fps
            if self.x > self.destx:
                self.x = self.destx
        if self.x == self.destx and self.y == self.desty:
            self.moving = False
        print("Speed:", self.speed/fps, " Direction:", self.dir, " Desired x:", self.destx, " Desired y:", self.desty, " Moving:", self.moving, " i:", self.i)

    def get_direction(self):
        if(self.i == len(self.path)):
            self.i = 0
            self.x = int(self.path[0])
            self.destx = self.x
            self.y = 0
            self.desty = self.y
            return 'X'
        elif path[self.i] == 'S':
            self.i += 1
            self.desty += 1
            return 'S'
        elif path[self.i] == 'A':
            self.i += 1
            self.destx -= 1
            return 'A'
        elif path[self.i] == 'D':
            self.i += 1
            self.destx += 1
            return 'D'
        elif path[self.i] == 'W':
            self.i += 1
            self.desty -= 1
            return 'W'

class celica():
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.HP = 0
        self.mode = "Nada"
    def show(self, screen):
        if self.HP > 0 and self.mode != "Fruit":
            self.HP -= 1
            self.mode = "Snake"
            pygame.draw.rect(screen, red, [self.x, self.y, self.vel, self.vel])
        elif self.HP == 0 and self.mode != "Fruit":
            self.mode = "Nada"
        elif self.mode == "Fruit":
            pygame.draw.rect(screen, green, [self.x, self.y, self.vel, self.vel])

vel_ekrana = 840
f = open("Map.txt","r")
count = len(f.readline()) - 1
f.seek(0)
vel_celice = int(vel_ekrana / count)
screen = Create_screen(vel_ekrana) 

white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]
purple = [128, 0 ,128]

path_texture = pygame.image.load("Photos/Tiles/Rocky.png").convert_alpha()

def getfps(fps, frame, time1, time1old):
    if(time1 == 0):
        time1 = time.clock()
    time2 =  time.clock()
    frame += 1
    if(time2 - time1 >= 1):
        fps = frame
        frame = 0
        time1old = time1
        time1 = time.clock()
    print("Frame:",frame,"FPS:", fps, "Time diff:", time2 - time1old)
    return fps, frame, time1, time1old


def convert_txt_to_array(name):
    game_map = []
    f = open(name,"r")
    f.seek(0)
    countf = len(f.readline())
    f.seek(0)
    fl = f.readline()
    for i in range(0, countf):
        game_map.append(fl[i])
    return game_map

def convert_txt_to_2Darray(name):
    game_map = []
    f = open(name,"r")
    f.seek(0)
    countf = len(f.readline()) - 1
    for i in range(countf):
        game_map.append([])
    for i in range(countf):
        for j in range(countf):
            vel = 'P'
            game_map[i].append(vel)
    f = open(name,"r")
    f.seek(0)
    for i in range(0, countf):
        fl = f.readline()
        for j in range(0, countf):
            game_map[i][j] = fl[j]
    return game_map

gmap = convert_txt_to_2Darray("Map.txt")
path = convert_txt_to_array("GPS.txt")
def get_path():
    f = open("Map.txt","r")
    fl = f.readline()
    f.seek(0)
    pathx = ""
    start = "UP"
    if start == "UP":
        for i in range(count):
            if fl[i] == 'X':
                start = i
                break
    path += i
    return pathx

#path = get_path() 

def Draw_Map(screen):
    f = open("Map.txt","r")
    for i in range(0, count):
        fl = f.readline()
        for j in range(0, count):
            if fl[j] == "O":
                pygame.draw.rect(screen, green, [(vel_celice * j), (vel_celice * i), vel_celice, vel_celice])
            elif fl[j] == "X":
                pygame.draw.rect(screen, red, [(vel_celice * j), (vel_celice * i), vel_celice, vel_celice])
                #screen.blit(pygame.transform.scale(path_texture,(vel_celice+1,vel_celice+1)), ((vel_celice * j)-(j - 8), (vel_celice * i)-(i - 8))) 
            elif fl[j] == "N":
                pygame.draw.rect(screen, blue, [(vel_celice * j), (vel_celice * i), vel_celice, vel_celice])
def main():
    running = True
    cycle = 0
    frame = 0
    Enemy_1 = Enemy()
    fps = 60
    time1 = 0
    time1old = 1
    fps_lock = False
    fps_val = 120
    fps_int = 1/fps_val
    timefps = time.clock()
    while running == True:
        if(time.clock() - timefps >= fps_int or fps_lock == False):
            timefps = time.clock()
            fps, frame, time1, time1old = getfps(fps, frame, time1, time1old)
            print("Cycle:", cycle, " Max cycles:", 12 * (fps/60))
            Enemy_1.move(fps)
            cycle = 0
            screen.fill(red)
            Draw_Map(screen)
            Enemy_1.draw(screen)
            pygame.display.update()
            cycle += 1
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: #For ending the loop
                    pygame.quit()
                    f.close()
                    running = False
main()
