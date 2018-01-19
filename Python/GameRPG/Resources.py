import pygame

# image, u (width), v (height), size
ENTITIES = [
        #ENTITIES
        ('PLAYER', ('resources/actor.png', 6, 4, 36, 48)),
        #BLOCKS
        ('NULL', ('resources/null_block.png', 1, 1, 32, 32)),
        ('GRASS', ('resources/levels/grass_blocks.png', 7, 1, 32, 32)),
        ('GRASS_1', ('resources/levels/grass_blocks_1.png', 5, 3, 32, 32)),
        ('WATER', ('resources/levels/water_blocks.png', 6, 3, 32, 32)),
        ('BRIDGE_1', ('resources/levels/bridge_1.png', 1, 1, 96, 96)),
        ('BRIDGE_2', ('resources/levels/bridge_2.png', 1, 1, 96, 96)),
        ('BRIDGE_1_UP', ('resources/levels/bridge_up.png', 3, 3, 32, 32)),        
        ('DIRT_CLIFFS', ('resources/levels/dirt_cliffs.png', 3, 5, 32, 32)),
        ('DIRT_CLIFFS_1', ('resources/levels/dirt_cliffs_1.png', 4, 4, 32, 32))
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
            xsize = i[1][3]
            ysize = i[1][4]
            u = i[1][1]
            v = i[1][2]
            for m in range(u):
                l = list()
                for k in range(v):                                      
                    l.append(temp.subsurface(xsize * m, ysize * k, xsize, ysize))
                img.append(l)                
            self.pack[i[0]] = img
            
        for i in self.projectile_data:
            img = list()
            temp = pygame.image.load(i[1][0]).convert_alpha()
            u = i[1][1]
            xsize = i[1][2]
            for m in range(u):
                img.append(temp.subsurface(0, xsize * m, xsize, xsize))
            self.pack[i[0]] = img
            
        for i in self.images:
            self.pack[i[0]] = pygame.image.load(i[1]).convert_alpha()
            
        print(self.pack)