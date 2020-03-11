import pygame, time, random

def Create_screen(width): #creates the screen
    if width % vel_celice != 0:
        width = vel_celice * count
    screen = pygame.display.set_mode((width,width))
    return screen

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

path = pygame.image.load("Photos/Tiles/Rocky.png").convert_alpha()

def Draw_Map(screen):
    f = open("Map.txt","r")
    for i in range(0, count):
        fl = f.readline()
        for j in range(0, count):
            if fl[j] == "O":
                pygame.draw.rect(screen, green, [(vel_celice * j)-(j - 8), (vel_celice * i)-(i - 8), vel_celice, vel_celice])
            elif fl[j] == "X":
                screen.blit(pygame.transform.scale(path,(vel_celice+1,vel_celice+1)), ((vel_celice * j)-(j - 8), (vel_celice * i)-(i - 8))) 
            elif fl[j] == "N":
                pygame.draw.rect(screen, blue, [(vel_celice * j)-(j - 8), (vel_celice * i)-(i - 8), vel_celice, vel_celice])
def main():
    running = True
    while running == True:
        screen.fill(red)
        Draw_Map(screen)
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                f.close()
                running = False
main()
