from c3510_matrixGenerator import*

def countAdj(posx,posy,map):
    sum = 0 - map[posx][posy]
    for i in range(-1,2):
        for j in range(-1,2):
            #print(posx+j,posy+i, map[posx+j][posy+i])
            if map[posx+j][posy+i]:
                sum += 1
    return sum

def stay_alive(posx,posy,map):
    if countAdj(posx,posy,map) in (2,3):
        return 1
    else:
        return 0

def do_revive(posx,posy,map):
    if countAdj(posx,posy,map) == 3:
        return 1
    else:
        return 0

def next_gen(map):
    next_gen = createMap(len(map[0]),len(map))
    for i in range(1,len(map)-1):
        for j in range(1,len(map[0])-1):
            if map[i][j] == 1:
                next_gen[i][j] = stay_alive(i,j,map)
            else:
                next_gen[i][j] = do_revive(i,j,map)
    return next_gen
