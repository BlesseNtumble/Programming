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
        pass
            
    def spawn_npc(self):
        pass      

    def update(self):
        self.game.window.fill((0,60,0))
        