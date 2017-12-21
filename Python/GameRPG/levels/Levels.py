# -*- coding: utf-8 -*-
from Constants import *
from blocks.Block import Brick


class Levels():
   
    def __init__(self, game):
        self.game = game
        
        self.file = open('resources/levels/' + self.getLevelFile(), 'r')
        self.file = [line.strip() for line in self.file]
        

    def gen(self):
        self.gen_block() 
        self.spawn_npc()          
            
    def getLevelFile(self):
        pass    
    
    def gen_block(self):
        self.game.screen.fill((0,0,0))
        
        for y in range(len(self.file)):
            for x in range(len(self.file[y])):                
                self.init_blocks(x, y, self.file)
                #self.game.blocks.add(Brick(self.game, (40*x, 40*y), (1,1), (0,0,0,0)))
        '''
        for i in range(int(self.width / 40)+1):
            for k in range(int(self.height / 40)+1):
                self.game.blocks.add(Brick(self.game, (40*i, 40*k), (1,1), (0,0,0,0)))
        '''
    def init_blocks(self, x, y, file):
        pass
    
    def spawn_npc(self):
        pass      

    def update(self):
        self.game.window.fill((0,60,0))
        
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
        