from blocks.Block import Brick
from levels.Levels import Level
from Constants import *

class Default():
    def __init__(self, game):
        self.game = game
    
    def gen(self):
        self.gen_block() 
        self.spawn_npc()          
                
    def gen_block(self):
        for i in range(int(WIDTH / 40)):
            self.game.blocks.add(Brick(self.game, (40*i, 0), (0,0), (1,1,1,1)))
            
    def spawn_npc(self):
        self.game.entities.add(self.game.player)
        
    def update(self):
       self.game.screen.fill((0, 60, 0))