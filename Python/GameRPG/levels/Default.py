from Constants import *
from blocks.Block import *
from levels.Levels import Levels


class Default(Levels):
    def __init__(self, game):
        Levels.__init__(self, game)
        self.game = game
        
        self.width = len(self.file[0])*40
        self.height = len(self.file)*40
    
    def spawn_npc(self):
        self.game.entities.add(self.game.player)
        self.game.player.rect.x = 80
        self.game.player.rect.y = 80
        
    def getLevelFile(self):
        return 'test1.txt' 
    
    def init_blocks(self, x, y, file):
        if(file[y][x] == '0'):self.game.blocks.add(Brick(self.game, (40*x, 40*y), (1,1), (0,0,0,0)))
        if(file[y][x] == '1'): self.game.blocks.add(Brick(self.game, (40*x, 40*y), (0,0), (1,1,1,1)))
        if(file[y][x] == '2'):  self.game.blocks.add(Brick(self.game, (40*x, 40*y), (0,1), (0,0,0,0)))
        if(file[y][x] == 'T'):  self.game.blocks.add(ChangeLevelBlock(self.game, (40*x, 40*y), (1,1), (0,0,0,0), 'DEFAULT'))
        