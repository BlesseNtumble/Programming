# -*- coding: utf-8 -*-
import pygame

from Constants import *
from blocks.Block import Brick


class Level():
   
    def __init__(self, game):
        self.game = game
        self.width = 1500
        self.height = 500       

    def gen(self):
        self.gen_block() 
        self.spawn_npc()          
                
    def gen_block(self):
        for i in range(int(WIDTH / 40)):
            for k in range(int(HEIGHT / 40)):
                self.game.blocks.add(Brick(self.game, (40*i, 40), (0,1), (0,0,0,0)))            
                self.game.blocks.add(Brick(self.game, (40*i, 0), (0,0), (1,1,1,1)))
            
    def spawn_npc(self):
        self.game.add_monster(400, 350)
        self.game.entities.add(self.game.player)        

    def update(self):
        self.game.screen.fill((0, 60, 0))