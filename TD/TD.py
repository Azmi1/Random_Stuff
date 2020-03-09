import pygame, time, random

white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

def Create_screen(width, height): #creates the screen
    screen = pygame.display.set_mode((width,height))
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

def Draw_Map(screen):
    f = open("Map.txt","r")
    vel_celice = vel_ekrana / 16
    for i in range(0, 16):
        fl = f.readline()
        for j in range(0, 16):
            if fl[j] == "O":
                pygame.draw.rect(screen, green, [(vel_celice * j)-j, (vel_celice * i)-i, vel_celice, vel_celice])
            elif fl[j] == "X":
                pygame.draw.rect(screen, red, [(vel_celice * j)-j, (vel_celice * i)-i, vel_celice, vel_celice])
                
vel_ekrana = 840

def main():
    running = True
    screen = Create_screen(vel_ekrana, vel_ekrana) 
    while running == True:
        screen.fill(white)
        Draw_Map(screen)
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                f.close()
                running = False
main()
