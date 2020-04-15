def convert_txt_to_array():
    game_map = []
    f = open("Map.txt","r")
    for i in range(count):
        game_map.append([])
    for i in range(count):
        for j in range(count):
            vel = 'P'
            game_map[i].append(vel)
    f.seek(0)
    for i in range(0, count):
        fl = f.readline()
        for j in range(0, count):
            game_map[i][j] = fl[j]
    return game_map

f = open("Map.txt","r")
open("GPS.txt", "w")
count = len(f.readline()) - 1
print("Mapa je velika: ", count)
Start_Point = 0
End_Point = 0
Path = []

def Locate_Start_End(Game_Map):
    for i in range(0, count):
        if(Game_Map[0][i] == 'X'):
            if(i == 0):
                if(Game_Map[0][1] == 'N'):
                    Start_Point = i
            elif(i == count-1):
                if(Game_Map[0][i-1] == 'N'):
                    Start_Point = i
            else:
                if(Game_Map[0][i-1] == 'N' and Game_Map[0][i+1] == 'N'):
                    Start_Point = i
    for i in range(0, count):
        if(Game_Map[count-1][i] == 'X'):
            if(i == 0):
                if(Game_Map[count-1][1] == 'N'):
                    End_Point = i
            elif(i == count-1):
                if(Game_Map[count-1][i-1] == 'N'):
                    End_Point = i
            else:
                if(Game_Map[count -1][i-1] == 'N' and Game_Map[count -1][i+1] == 'N'):
                    End_Point = i
    return Start_Point, End_Point

def Pathing(Game_Map, Start_Point, End_Point):
    Path.append(Start_Point)
    x = Start_Point
    y = 0
    From = 'W'
    while(y != count - 1):
        if Game_Map[y + 1][x] == 'X' and From != 'S' and y != count -1:
            Path.append('S')
            From = 'W'
            y = y + 1
            continue
        elif Game_Map[y - 1][x] == 'X' and From != 'W' and y != 0:
            Path.append('W')
            From = 'S'
            y = y - 1
            continue
        elif Game_Map[y][x-1] == 'X' and From != 'A' and x != 0:
            Path.append('A')
            From = 'D'
            x = x - 1
            continue
        elif Game_Map[y][x+1] == 'X' and From != 'D' and x != count - 1:
            Path.append('D')
            From = 'A'
            x = x + 1
            continue
        print("Searching... x =", x, "y =", y, "From =", From)
    f = open("GPS.txt", "w") 
    for i in range(0, len(Path)):
        f.write(str(Path[i]))

def main():
    Game_Map = convert_txt_to_array()
    Start_Point, End_Point = Locate_Start_End(Game_Map)
    for i in range(0, count):
        for j in range(0, count):
            print(Game_Map[i][j], end = "")
        print("")
    Pathing(Game_Map, Start_Point, End_Point)

main()