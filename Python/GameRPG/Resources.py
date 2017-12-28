import pygame

# image, u (width), v (height), size
ENTITIES = [
        #ENTITIES
        ('PLAYER', ('resources/actor.png', 6, 4, 48)),
        #BLOCKS
        ('GRASS', ('resources/levels/grass_blocks.png', 7, 1, 32)),
        ('WATER', ('resources/levels/water_blocks.png', 6, 3, 32)),
        ('BRIDGE_1', ('resources/levels/bridge_1.png', 1, 1, 96)),
        ('BRIDGE_2', ('resources/levels/bridge_2.png', 1, 1, 96)),
        ('STUMP_1', ('resources/levels/stump_1.png', 1, 1, 64)),
        ('LEAVES_1', ('resources/levels/leaves_1.png', 1, 1, 96)),
        ]
PROJECTILES = [
        ('ARROW', ('resources/arrow.png', 4, 48))
        ]
GUI = [
        
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