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
        pass
    
    def move(self):
        pass
        
class Brick(Block):
    def __init__(self, game, pos, uv, blocked):
        Block.__init__(self, game, pos[0], pos[1], uv, 'BLOCKS', blocked)