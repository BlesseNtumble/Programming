import pygame

# image, u (width), v (height), size
ENTITIES = [
        #ENTITIES
        ('PLAYER', ('resources/actor.png', 6, 4, 48)),
        #BLOCKS
        ('BLOCKS', ('resources/blocks.png', 2, 2, 40))
        ]
PROJECTILES = [
        ('ARROW', ('resources/arrow.png', 4, 48))
        ]
GUI = [
        ('HP_MP_FRAME', 'resources/bar.png')
    ] 

class Resources():
    def __init__(self, entities_data, projectile_data, images):
        self.pack = {}
        self.entities_data = entities_data
        self.projectile_data = projectile_data
        self.images = images
        self.generate_pack()
    
    def generate_pack(self):        
        for i in self.entities_data:
            img = list()
            temp = pygame.image.load(i[1][0]).convert_alpha()
            size = i[1][3]
            u = i[1][1]
            v = i[1][2]
            for m in range(u):
                l = list()
                for k in range(v):                                      
                    l.append(temp.subsurface(size * m, size * k, size, size))
                img.append(l)                
            self.pack[i[0]] = img
            
        for i in self.projectile_data:
            img = list()
            temp = pygame.image.load(i[1][0]).convert_alpha()
            u = i[1][1]
            size = i[1][2]
            for m in range(u):
                img.append(temp.subsurface(0, size * m, size, size))
            self.pack[i[0]] = img
            
        for i in self.images:
            self.pack[i[0]] = pygame.image.load(i[1])
            
        print(self.pack)