from blocks.Block import Brick
from levels.Levels import Levels
from Constants import *

class Test(Levels):
    def __init__(self, game):
        self.game = game
        self.width = 1600
        self.height = HEIGHT
    
    def gen_block(self):
        for i in range(int(self.width / 40)+1):
            for k in range(int(self.height / 40)+1):
                self.game.screen.blit(self.game.assets['BLOCKS'][1][1], (40*i, 40*k))
                self.game.blocks.add(Brick(self.game, (40*i, 40*k), (1,1), (0,0,0,0)))
                
            self.game.blocks.add(Brick(self.game, (40*i, 0), (0,0), (1,1,1,1)))
            self.game.blocks.add(Brick(self.game, (40*i, 40), (0,1), (0,0,0,0)))
            
    def spawn_npc(self):
        self.game.add_monster(400.0, 350.0)
        self.game.entities.add(self.game.player)        

    def update(self):
        Levels.update(self)