from Constants import *
from blocks.Block import Brick
from levels.Levels import Levels


class Default(Levels):
    def __init__(self, game):
        self.game = game
        self.width = 1000
        self.height = HEIGHT
    
    def gen_block(self):
        Levels.gen_block(self)
        for i in range(int(self.width / 40)):
            self.game.blocks.add(Brick(self.game, (40*i, 0), (0,0), (1,1,1,1)))
            
    def spawn_npc(self):
        self.game.entities.add(self.game.player)
                
    def update(self):
        Levels.update(self)