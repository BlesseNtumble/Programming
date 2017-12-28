# -*- coding: utf-8 -*-
import random

from blocks.Block import Blocks
from levels.Levels import Levels


class Start(Levels):
    def __init__(self, game):
        Levels.__init__(self, game)
    
        self.width = len(self.file[0])*32
        self.height = len(self.file)*32
        
        self.layer_1 = open('resources/levels/' + self.getLevelFile() + '_1.txt', 'r')
        self.layer_1 = [line.strip() for line in self.layer_1]
    
    def getLevelFile(self):
        return 'start/layer_0' 
    
    def init_blocks(self, x, y, file):
        if(file[y][x] == '-'):
            j = random.randint(0, 100)
            if j > 2: 
                self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (random.randint(0, 3),0), 'GRASS', (0,0,0,0)))
            else:
                self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (random.randint(4, 6),0), 'GRASS', (0,0,0,0)))
        
        if(file[y][x] == '1'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,0), 'WATER', (1,1,1,1))) # верх реки
        if(file[y][x] == '2'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,1), 'WATER', (1,1,1,1))) # центр реки
        if(file[y][x] == '3'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,2), 'WATER', (0,0,0,0))) # низ реки
     
        if(file[y][x] == 'z'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,1), 'WATER', (0,0,0,0))) # центр реки без коллизии
        
        if(file[y][x] == '8'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,1), 'WATER', (0,0,0,0))) # лево реки
        if(file[y][x] == '9'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,1), 'WATER', (0,0,0,0))) # право реки
        
        if(file[y][x] == '4'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,0), 'WATER', (0,0,0,0))) # угол (справа-вниз) реки
        if(file[y][x] == '5'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,0), 'WATER', (0,0,0,0))) # угол (слева-вниз) реки
        if(file[y][x] == '6'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,2), 'WATER', (0,0,0,0))) # угол (справа-вверх) реки
        if(file[y][x] == '7'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,2), 'WATER', (0,0,0,0))) # угол (слева-вверх) реки
        
        if(file[y][x] == 'a'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (4,0), 'WATER', (0,0,0,0))) # наруж угол (слева-вверх) реки
        if(file[y][x] == 'b'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (5,0), 'WATER', (0,0,0,0))) # наруж угол (справа-вверх) реки
        if(file[y][x] == 'c'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (4,1), 'WATER', (0,0,0,0))) # наруж угол (слева-вниз) реки
        if(file[y][x] == 'd'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (5,1), 'WATER', (0,0,0,0))) # наруж угол (справа-вниз) реки


    def add_gen_block(self):  
        for y in range(len(self.layer_1)):
            for x in range(len(self.layer_1[y])):
                if(self.layer_1[y][x] == '1'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,0), 'BRIDGE_2', (0,0,0,0)))

    def spawn_npc(self):
        self.game.entities.add(self.game.player) 