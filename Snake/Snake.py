import pygame, time, random
def Create_screen(width, height): #creates the screen
    screen = pygame.display.set_mode((width,height))
    return screen

def Grid(screen, vel, vel_celice, vel_ekrana):
    for i in range(1, vel):
        pygame.draw.rect(screen, white, [(vel_celice+1)*i, 0, 1, vel_ekrana])
    for i in range(1, vel):
        pygame.draw.rect(screen, white, [0, (vel_celice+1)*i, vel_ekrana, 1])

white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

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

class snake():
    def __init__(self, x):
        self.x = x
        self.y = x
        self.score = 1
    def move(self, key):
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.y -= 1
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            self.y += 1
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.x -= 1
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.x += 1

class fruit():
    def __init__(self, vel, table):
        self.x = random.randint(0, vel-1)
        self.y = random.randint(0, vel-1)
        if table[self.y][self.x].mode == "Snake":
            sort = False
            while sort == False:
                for i in range(0, vel):
                    for j in range(0, vel):
                        if table[i][j].HP == 0:
                            self.x = j
                            self.y = i
                            sort = True
                            break
                    if sort == True:
                        break
        table[self.y][self.x].mode = "Fruit"

def main():
    random.seed()
    running = True 
    vel = int(input("Vnesi velikost tabele(5 = 5x5, 6 = 6x6...): "))
    vel_celice = 16
    vel_ekrana = vel_celice*vel+vel-2
    screen = Create_screen(vel_ekrana,vel_ekrana)
    Snake = snake(int(vel/2))
    Table = []
    for i in range(0, vel):
        Table.append([])
    for i in range(0, vel):
        for j in range(0, vel):
            x = (vel_celice*j)+j
            y = (vel_celice*i)+i
            Table[i].append(celica(x, y, vel_celice))
    Table[Snake.y][Snake.x].HP = Snake.score
    key_buffer = False
    key_buffer_k = False
    Fruit = fruit(vel, Table)
    Grid(screen, vel, vel_celice, vel_ekrana)
    for i in range(0, vel):
        for j in range(0, vel):
            Table[i][j].show(screen)
    pygame.display.update()
    t0 = time.clock()
    while running == True:
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_s] or key[pygame.K_a] or key[pygame.K_d] or key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
            if key_buffer == False or time.clock() - t0 > 0.175:
                print(Fruit.x, " ", Fruit.y)
                t0 = time.clock()
                screen.fill(black)
                Grid(screen, vel, vel_celice, vel_ekrana)
                Snake.move(key)
                Table[Snake.y][Snake.x].HP += Snake.score
                if Table[Snake.y][Snake.x].mode == "Fruit":
                    Table[Snake.y][Snake.x].mode = "Snake"
                    Snake.score += 1
                    del Fruit
                    Fruit = fruit(vel, Table)
                if Table[Snake.y][Snake.x].HP > Snake.score:
                    return 0
                for i in range(0, vel):
                    for j in range(0, vel):
                        Table[i][j].show(screen)
                pygame.display.update()
                key_buffer = True
        else:
            key_buffer = False
        if key[pygame.K_k]:
            if key_buffer_k == False:
                key_buffer_k = True
                print(Table[Fruit.y][Fruit.x].mode)
                Table[Fruit.y][Fruit.x].mode = "Nada"
                print(Table[Fruit.y][Fruit.x].mode)
                del Fruit
                Fruit = fruit(vel, Table)
        else:
            key_buffer_k = False
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #For ending the loop
                pygame.quit()
                running = False

main()