# -*- coding: utf-8 -*-
import random

from blocks.Block import Blocks
from levels.Levels import Levels


class Start(Levels):
    def __init__(self, game):
        Levels.__init__(self, game)
    
        self.width = len(self.file[0])*32
        self.height = len(self.file)*32
        
        self.layer_blocks = open('resources/levels/' + self.getLevelFile() + '_blocks.txt', 'r')
        self.layer_blocks = [line.strip() for line in self.layer_blocks]
        
        self.layer_1 = open('resources/levels/' + self.getLevelFile() + '_decors.txt', 'r')
        self.layer_1 = [line.strip() for line in self.layer_1]
    
    def getLevelFile(self):
        return 'start/layer' 
    
    def init_blocks(self, x, y, file):
        if(file[y][x] == '-'):
            j = random.randint(0, 100)
            if j > 2: 
                self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (random.randint(0, 3),0), 'GRASS', (0,0,0,0)))
            else:
                self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (random.randint(4, 6),0), 'GRASS', (0,0,0,0)))
        
        if(file[y][x] == '+'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,1), 'DIRT_CLIFFS', (0,0,0,0)))
        
        if(file[y][x] == '1'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,0), 'WATER', (0,0,0,0))) # верх реки
        if(file[y][x] == '2'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,1), 'WATER', (0,0,0,0))) # центр реки
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
        for y in range(len(self.layer_blocks)):
            for x in range(len(self.layer_blocks[y])):
                if(self.layer_blocks[y][x] == '#'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,0), 'NULL', (1,1,1,1)))
               
        for y in range(len(self.layer_1)):
            for x in range(len(self.layer_1[y])):                
                if(self.layer_1[y][x] == '1'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (0,0), 'BRIDGE_1_UP', (0,0,0,0)))
                if(self.layer_1[y][x] == '2'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (0,1), 'BRIDGE_1_UP', (0,0,0,0)))
                if(self.layer_1[y][x] == '3'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (0,2), 'BRIDGE_1_UP', (0,0,0,0)))
                
                if(self.layer_1[y][x] == '4'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (1,0), 'BRIDGE_1_UP', (0,0,0,0)))
                if(self.layer_1[y][x] == '5'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (1,1), 'BRIDGE_1_UP', (0,0,0,0)))
                if(self.layer_1[y][x] == '6'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (1,2), 'BRIDGE_1_UP', (0,0,0,0)))
                
                if(self.layer_1[y][x] == '7'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (2,0), 'BRIDGE_1_UP', (0,0,0,0)))
                if(self.layer_1[y][x] == '8'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (2,1), 'BRIDGE_1_UP', (0,0,0,0)))
                if(self.layer_1[y][x] == '9'): self.game.blocks.add(Blocks(self.game, (32*x - 16, 32*y), (2,2), 'BRIDGE_1_UP', (0,0,0,0)))
               
                if(self.layer_1[y][x] == 'c'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,4), 'DIRT_CLIFFS', (0,0,0,0)))
                if(self.layer_1[y][x] == 'b'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,3), 'DIRT_CLIFFS', (0,0,0,0)))
                if(self.layer_1[y][x] == 'a'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,2), 'DIRT_CLIFFS', (0,0,0,0)))
                if(self.layer_1[y][x] == 'd'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,1), 'DIRT_CLIFFS', (0,0,0,0)))
                
                if(self.layer_1[y][x] == 'e'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,1), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'f'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,2), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'g'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,3), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'h'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,0), 'DIRT_CLIFFS_1', (0,0,0,0), 1))
                
                if(self.layer_1[y][x] == 'i'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,1), 'DIRT_CLIFFS_1', (0,0,0,0), 1))
                if(self.layer_1[y][x] == 'j'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,2), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'k'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,3), 'DIRT_CLIFFS_1', (0,0,0,0)))
                
                if(self.layer_1[y][x] == 's'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (3,0), 'DIRT_CLIFFS_1', (0,0,0,0), 1))
               
                if(self.layer_1[y][x] == 'p'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (3,1), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'q'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (3,2), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'r'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (3,3), 'DIRT_CLIFFS_1', (0,0,0,0)))
                
                if(self.layer_1[y][x] == 'l'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (1,2), 'GRASS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'm'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,2), 'GRASS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'n'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (2,1), 'GRASS_1', (0,0,0,0)))
                
                if(self.layer_1[y][x] == 'o'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (3,0), 'GRASS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 't'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,2), 'GRASS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'x'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (4,0), 'GRASS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'y'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,1), 'GRASS_1', (0,0,0,0)))

                if(self.layer_1[y][x] == 'u'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,1), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'v'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,2), 'DIRT_CLIFFS_1', (0,0,0,0)))
                if(self.layer_1[y][x] == 'w'): self.game.blocks.add(Blocks(self.game, (32*x, 32*y), (0,3), 'DIRT_CLIFFS_1', (0,0,0,0)))
                
    def spawn_npc(self):
        self.game.entities.add(self.game.player) 
        
        self.game.add_monster(400.0, 350.0, 4)
        self.game.add_monster(850.0, 350.0, 3)
        self.game.add_monster(450.0, 650.0, 8)
