# -*- coding: utf-8 -*-
from Constants import *
from entities.base.EntityLiving import *
from skills.Skills import Skills, Arrow


position = [150, 50]

class EntityPlayer(EntityLiving):
    
    def __init__(self, game):
        self.name = 'Little Boy'
        self.game = game
        self.chars = [100, 100, SPEED] #HP, MP, SPEED
        self.base = [self.chars[0], self.chars[1], position[0], position[1], HP_REG, MP_REG, SPEED]       
        EntityLiving.__init__(self, self.game, self.name, self.chars, self.base, DOWN, ALIVE, position, 'PLAYER')    
    
        self.skill_list.append(Arrow(self))
    
    def useSkill(self, skillid):        
        self.skill_list[skillid].useSkill()
        
    def tick(self):
        EntityLiving.tick(self)
        [i.tick() for i in self.skill_list]
        
        if self.experience >= EXP[self.level - 1]:
            self.level += 1
            self.experience = 0

    def render_ui(self, screen, camera): 
        #EntityLiving.render_ui(self, screen, camera, True)
        color_bg      = (30, 30, 30) 
        color_font    = (255, 255, 255)
        fontObj = pygame.font.Font('freesansbold.ttf', 13)
        
        textSurfaceObj = fontObj.render('FPS: ' + str(int(self.game.timer.get_fps())), False, color_font, color_bg)
        textRectObj = textSurfaceObj.get_rect()        
        textRectObj.center = (WIDTH - 43, 25)
        screen.blit(textSurfaceObj, textRectObj)
        
        pygame.draw.rect(screen, (20,20,20), (WIDTH / 2 - 500, HEIGHT - 20, 1000, 17))        
        exp = int((1000 * self.experience) / EXP[self.level - 1])
        pygame.draw.rect(screen, (100,100,100), (WIDTH / 2 - 498, HEIGHT - 18, exp, 13))
        
        
        textSurfaceObj = fontObj.render(str(self.experience) + "/" + str(EXP[self.level - 1]) + " XP", False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WIDTH / 2, HEIGHT - 11)
        screen.blit(textSurfaceObj, textRectObj)
        
        pygame.draw.rect(screen, (0,0,0), (2, 15, 180, 60))
        
        textSurfaceObj = fontObj.render(str(self.level), False, color_font, color_bg)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (15 + len(str(self.level)), 24)
        screen.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = fontObj.render(str(self.name), False, color_font, color_bg)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (55, 24)
        screen.blit(textSurfaceObj, textRectObj)
        
        pygame.draw.rect(screen, (120,0,0), (27, 35, 150, 13))
        hp = int((self.hp/self.start_parameters[0]) * 150)
        pygame.draw.rect(screen, (220,0,0), (27, 35, hp, 13))
        
        pygame.draw.rect(screen, (0,120,120), (27, 50, 150, 13))
        mp = int((self.mp/self.start_parameters[1]) * 150)
        pygame.draw.rect(screen, (0,220,220), (27, 50, mp, 13))
        
        textSurfaceObj = fontObj.render("HP", False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (15, 41)
        screen.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = fontObj.render(str(int(self.hp)) + "/" + str(self.base[0]), False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (105, 42)
        screen.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = fontObj.render("MP", False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (15, 56)
        screen.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = fontObj.render(str(int(self.mp)) + "/" + str(self.base[1]), False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (105, 57)
        screen.blit(textSurfaceObj, textRectObj)
        
        