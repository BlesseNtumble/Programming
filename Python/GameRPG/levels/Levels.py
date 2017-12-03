# -*- coding: utf-8 -*-
from Constants import *
from blocks.Block import Brick


class Levels():
   
    def __init__(self, game):
        self.game = game
        self.width = WIDTH
        self.height = HEIGHT - 50

    def gen(self):
        self.gen_block() 
        self.spawn_npc()          
                
    def gen_block(self):
        self.game.screen.fill((0,0,0))
       
        for i in range(int(self.width / 40)+1):
            for k in range(int(self.height / 40)+1):
                self.game.blocks.add(Brick(self.game, (40*i, 40*k), (1,1), (0,0,0,0)))
            
    def spawn_npc(self):
        pass      

    def update(self):
        self.game.window.fill((0,60,0))
        