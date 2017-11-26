from entities.EntityArrow import EntityArrow

class Skills():
        
    def __init__(self, name, mp, time, caster):
        self.name = name
        self.cost = mp
        self.caster = caster
        self.reload_time = time
        self.cooldown = 0
           
    def useSkill(self):    
        if self.cooldown == 0 and self.caster.mp >= self.cost:
            self.caster.mp -= self.cost
            self.cooldown = self.reload_time
            self.action()
            
    def tick(self):                
        if self.cooldown > 0 and self.caster.tick_living % 10 == 0:
            self.cooldown -= 1
    
    def action(self):
        pass
        

class Arrow(Skills):
    
    def __init__(self, caster):
        Skills.__init__(self, 'Arrow', 10, 1, caster)
        
    def action(self):
        self.caster.game.projectiles.add(EntityArrow(self.caster.game, self.caster, self.caster.rect.x, self.caster.rect.y, self.caster.direction))

            
            