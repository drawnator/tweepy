#Guilherme Silva Toledo
#04/04/2022
#code for formating and outputting the game instance
# FUNCION INDEX
#

from PIL import Image

def createMap(x,y):
    MapArray = [[0 for i in range(x)] for j in range(y)]
    return MapArray

def createRMap(x,y):
    MapArray = [[random.randint(0,10)//10 for i in range(x)] for j in range(y)]
    return MapArray

def createIMap(x,y):
    with Image.open("template.png") as im:
        px = im.load()
    map = createMap(x,y)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if px[j,i] == 0:
                map[i][j] = 1
    return map

def add_Methuselahs(x,y,m,map):
    for i in range(len(m)):
        for j in range(len(m[i])):
            map[i+y][j+x] = m[i][j]

def R_Pentomino():
    return [
    [0,1,1],
    [1,1,0],
    [0,1,0]
    ]

def Diehard():
    return [
    [0,0,0,0,0,0,1,0],
    [1,1,0,0,0,0,0,0],
    [0,1,0,0,0,1,1,1],
    ]

def Acorn():
    return [
    [0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0],
    [1,1,0,0,1,1,1]
    ]
