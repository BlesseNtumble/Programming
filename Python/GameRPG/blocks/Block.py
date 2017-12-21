from pygame import *
import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, uv, image_id, block_sides):
        pygame.sprite.Sprite.__init__(self)
        
        self.game = game
        
        self.image_id = image_id
        self.block_sides = block_sides
        self.image = self.game.assets[self.image_id][uv[0]][uv[1]]
        
        self.rect = self.image.get_rect()        
        self.rect.x = x
        self.rect.y = y       
        self.size = self.rect.size[0]    
        
    def tick(self):
        self.action()        
    
    def move(self):
        pass
        
    def action(self):
        pass
    
class Brick(Block):
    def __init__(self, game, pos, uv, blocked):
        Block.__init__(self, game, pos[0], pos[1], uv, 'BLOCKS', blocked)
        
class ChangeLevelBlock(Block):
    def __init__(self, game, pos, uv, blocked, level):
        self.level = level
        Block.__init__(self, game, pos[0], pos[1], uv, 'BLOCKS', blocked)
    
    def action(self):
        if(self.game.player.rect.x >= self.rect.x - 20 and self.game.player.rect.x <= self.rect.x + 20and self.game.player.rect.y >= self.rect.y - 40 and self.game.player.rect.y <= self.rect.y):
            
            self.game.gen_world(self.level)        
            print(self.game.player.rect.x, self.rect.x)