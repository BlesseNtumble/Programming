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
    
        self.skill_list.append(Arrow(self, 10, 1))

        
        
    def tick(self):
        EntityLiving.tick(self)             

        self.start_parameters[0] = HP[self.level - 1]
        self.start_parameters[1] = MP[self.level - 1]

        if self.experience >= EXP[self.level - 1]:
            self.level += 1
            self.experience = 0
            self.start_parameters[0] = HP[self.level - 1]
            self.start_parameters[1] = MP[self.level - 1]
            self.hp = self.start_parameters[0]      
            self.mp = self.start_parameters[1]      

        #self.regen('hp', 20, 5, 2)
                     
                
        self.getEntityInFace(self)
            
    def move(self):
        EntityLiving.move(self)
        [i.tick() for i in self.game.blocks]  
          
    def render_ui(self, screen, camera, window):
        
        
        color_bg      = (30, 30, 30) 
        color_font    = (255, 255, 255)  
             
        textSurfaceObj = self.font.render("X: " + str(self.rect.x) + " | Y: " + str(self.rect.y), False, color_font)       
        screen.blit(textSurfaceObj, (camera.apply(self).x - 20, camera.apply(self).y + 55))
      
        screen = window      
        
        textSurfaceObj = self.font.render('FPS: ' + str(int(self.game.timer.get_fps())), False, color_font, color_bg)
        textRectObj = textSurfaceObj.get_rect()        
        textRectObj.center = (WIDTH - 43, 25)
        screen.blit(textSurfaceObj, textRectObj)
        
        pygame.draw.rect(screen, (125,125,0), (0, HEIGHT - HUD_PANEL_SIZE, WIDTH, HUD_PANEL_SIZE))
        
        pygame.draw.rect(screen, (20,20,20), (WIDTH / 2 - 500, HEIGHT - 20, 1000, 17))        
        exp = int((1000 * self.experience) / EXP[self.level - 1])
        pygame.draw.rect(screen, (100,100,100), (WIDTH / 2 - 498, HEIGHT - 18, exp, 13))
        
        
        textSurfaceObj = self.font.render(str(self.experience) + "/" + str(EXP[self.level - 1]) + " EXP", False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WIDTH / 2, HEIGHT - 11)
        screen.blit(textSurfaceObj, textRectObj)       
        
        textSurfaceObj = self.font.render(str(self.level), False, color_font, color_bg)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (15 + len(str(self.level)), HEIGHT - 12)
        screen.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = self.font.render(str(self.name), False, color_font, color_bg)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (55, HEIGHT - 12)
        screen.blit(textSurfaceObj, textRectObj)
        
        
        
        #HP BAR
        pygame.draw.rect(screen, (0,0,0), (WIDTH / 2 - 500 - 1, HEIGHT - 73 - 1, 152, 20))
        pygame.draw.rect(screen, (120,0,0), (WIDTH / 2 - 500, HEIGHT - 73, 150, 18)) 
        hp = int((self.hp/self.start_parameters[0]) * 150)
        pygame.draw.rect(screen, (220,0,0), (WIDTH / 2 - 500, HEIGHT - 73, hp, 18))
        #/////////
        
        #MP BAR
        pygame.draw.rect(screen, (0,0,0), (WIDTH / 2 - 500 - 1, HEIGHT - 50 - 1, 152, 20))
        pygame.draw.rect(screen, (0,120,120), (WIDTH / 2 - 500, HEIGHT - 50, 150, 18))        
        mp = int((self.mp/self.start_parameters[1]) * 150)
        pygame.draw.rect(screen, (0,220,220), (WIDTH / 2 - 500, HEIGHT - 50, mp, 18))
        #/////////
        
        textSurfaceObj = self.font.render("HP", False, color_font)
        screen.blit(textSurfaceObj, (WIDTH / 2 - 520, HEIGHT - 70))
        
        textSurfaceObj = self.font.render(str(int(self.hp)) + "/" + str(self.start_parameters[0]), False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WIDTH / 2 - 420, HEIGHT - 63)
        screen.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = self.font.render("MP", False, color_font)
        screen.blit(textSurfaceObj, (WIDTH / 2 - 520, HEIGHT - 48))
        
        textSurfaceObj = self.font.render(str(int(self.mp)) + "/" + str(self.start_parameters[1]), False, color_font)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WIDTH / 2 - 420, HEIGHT - 40)
        screen.blit(textSurfaceObj, textRectObj)