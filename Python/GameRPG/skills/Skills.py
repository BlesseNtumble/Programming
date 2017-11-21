class Skills():
    
    def __init__(self, game, mp, caster):
        self.game = game
        self.cost = mp
        self.caster = caster
           
    def useSkill(self):
        if self.caster.mp >= self.cost:
            self.caster.mp -= self.cost
            self.action()
        
    def action(self):
        print('Use Skill')