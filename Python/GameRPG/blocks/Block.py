import pygame

class Block():
    def __init__(self, game, x, y, image_pack, block_sides):
        self.game = game
        self.posX = x
        self.posY = y
        self.block_sides = block_sides
        self.image = image_pack[0]
        self.u = image_pack[1]
        self.v = image_pack[2]
        self.size = image_pack[3]
        self.images = []
        
        temp = pygame.image.load(self.image).convert_alpha()
        
        for m in range(self.u):
            i = []
            for k in range(self.v):                                      
                i.append(temp.subsurface(self.size * m, self.size * k, self.size, self.size))
            self.images.append(i)
            
    def render(self, screen):       
        screen.blit(self.images[self.u - 1][self.v - 1], (self.posX, self.posY))
        
    def tick(self):
        pass
    
    def move(self):
        pass
        
class Brick(Block):
    def __init__(self, game, pos, uv, blocked):
        self.image = ['resources/blocks.png', uv[0], uv[1], 40]
        Block.__init__(self, game, pos[0], pos[1], self.image, blocked)