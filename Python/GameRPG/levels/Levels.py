# -*- coding: utf-8 -*-
from Constants import *

class Levels():
   
    def __init__(self, game):
        self.game = game
        
        self.file = open('resources/levels/' + self.getLevelFile() + '.txt', 'r')
        self.file = [line.strip() for line in self.file]     

    def gen(self):
        self.gen_block() 
        self.spawn_npc()          
            
    def getLevelFile(self):
        pass    
    
    def gen_block(self):

        for y in range(len(self.file)):
            for x in range(len(self.file[y])):                
                self.init_blocks(x, y, self.file)

        self.add_gen_block()

    def init_blocks(self, x, y, file):
        pass
    
    def add_gen_block(self):
        pass
    def spawn_npc(self):
        pass      

    def update(self):
        #self.game.window.fill((0,60,0))
        pass
        
    def ai_level(self):
        points = set()
        #N = list()
        
        for y in range(len(self.file)):
            for x in range(len(self.file[y])):
                print(x, y)
                #if self.file[y][x] == '2':
                points.add((x,y))
                    
        graf = {}
        for i in points:
            temp = set()
            if(i[0] - 1, i[1]) in points:
                temp.add((i[0] - 1, i[1]))
            if(i[0] + 1, i[1]) in points:
                temp.add((i[0] + 1, i[1]))
            if(i[0], i[1] - 1) in points:
                temp.add((i[0], i[1] - 1))
            if(i[0], i[1] + 1) in points:
                temp.add((i[0], i[1] + 1))
            
            graf[i] = temp
        
        return graf
        