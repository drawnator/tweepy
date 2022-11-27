#Guilherme Silva Toledo
#26/03/2022
#this code is a basic implementation of john conway's game of life
#using python, in wich the script can both generate the terminal version
#or the image version of the game

import math
import random
import time
from PIL import Image, ImageDraw

import cProfile
import pstats

# Matrix generation-------------------------------------------------------------
from c3510_matrixGenerator import*
# Matrix calculations ----------------------------------------------------------
from c3510_matrixCalculator import*
# Render -----------------------------------------------------------------------
def createBanner(geracao,x,y,map):
    im = Image.new('1', (x,y),color=1)
    px = im.load()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                px[j,i] = 0
    number = 0#f"{249+250-geracao:0>3}"
    im.save(f'gif/{number}.png')

def formatNPrint(map):
    lineTxt = ''
    for lineNum in map:
        for num in lineNum:
            if num == 1:
                lineTxt += '# '
            elif num == 0:
                lineTxt += '. '
            else:
                lineTxt += f'{numero} '
        lineTxt +='\n'
    return lineTxt

# Post -------------------------------------------------------------------------
def conectar_instancia(instancia_nome):
    import tweepy as tw
    with open(instancia_nome, 'r') as instancia:
                consumer_key = instancia.readline().strip('\n')
                consumer_secret = instancia.readline().strip('\n')
                access_token = instancia.readline().strip('\n')
                access_secret = instancia.readline().strip('\n')
                auth = tw.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_secret)
                api = tw.API(auth)
    return api

# User settings ----------------------------------------------------------------
def start(x,y):
    #settings
    starting_map = createIMap(x,y)#createMap(x,y)
    Methuselah = Acorn()
    R_test = [[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]]
    #add:
    add_Methuselahs(x//2,y//2,Methuselah,starting_map)

    #rodar:
    return starting_map

def pregen(map,geracao):
    for i in range(geracao):
        print(f'pregeracao {i}')
        map = next_gen(map)
    return map

def main(x,y,map,geracao):
    for _ in range(10):
        createBanner(geracao,x,y,map)
        geracao += 1
    while geracao < 250:
        print(f'geracao {geracao}')
        createBanner(geracao,x,y,map)
        map = next_gen(map)
        geracao += 1

if __name__ == '__main__':
    #rate_limit = api.rate_limit_status()
    #api = conectar_instancia('instancias/key_staging.txt')
    #print(rate_limit['resources']['users']['/users/profile_banner'])
    option = 3
    x = (1500,900,450,200,99)[option]
    y = (500,500,250,100,47)[option]
    real_map = start(x,y)
    geracao = 0
    real_map = pregen(real_map,geracao)
    with cProfile.Profile() as pr:
        main(x,y,real_map,geracao)
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
        #api.update_profile_banner('game_of_life_banner.png')
        #time.sleep(30.01)
        #input()
        # i+= 1
        # if i%130 == 0:
        #     add_Methuselahs(x//2,y//2,Diehard(),real_map)
