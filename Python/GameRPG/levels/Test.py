from blocks.Block import ChangeLevelBlock
from levels.Levels import Levels
from Constants import *

class Test(Levels):
    def __init__(self, game):
        Levels.__init__(self, game)
        
        self.game = game
        self.width = len(self.file[0])*40
        self.height = len(self.file)*40
    
    """
    def gen_block(self):
        Levels.gen_block(self)
        for i in range(int(self.width / 40)+1):
            #for k in range(int(self.height / 40)+1):
               
            self.game.blocks.add(Brick(self.game, (40*i, 0), (0,0), (1,1,1,1)))
            self.game.blocks.add(Brick(self.game, (40*i, 40), (0,1), (0,0,0,0)))
    """  
    def getLevelFile(self):
        return 'test.txt' 
     
    def init_blocks(self, x, y, file):
        #if(file[y][x] == '0'):self.game.blocks.add(Brick(self.game, (40*x, 40*y), (1,1), (0,0,0,0)))
        #if(file[y][x] == '1'): self.game.blocks.add(Brick(self.game, (40*x, 40*y), (0,0), (1,1,1,1)))
        #if(file[y][x] == '2'):  self.game.blocks.add(Brick(self.game, (40*x, 40*y), (0,1), (0,0,0,0)))
        #if(file[y][x] == 'T'):  self.game.blocks.add(ChangeLevelBlock(self.game, (40*x, 40*y), (0,1), (0,0,0,0), 'non'))
        pass
        
    def spawn_npc(self):
        self.game.add_monster(400.0, 350.0)
        self.game.add_monster(850.0, 350.0)
        self.game.add_monster(850.0, 650.0)
        self.game.add_monster(150.0, 950.0)
        self.game.add_monster(850.0, 30.0)
        self.game.entities.add(self.game.player)  
   
