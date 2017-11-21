# -*- coding: utf-8 -*-
from pygame import *

from Constants import *
from entities.EntityArrow import EntityArrow
from entities.EntityMonster import EntityMonster
from entities.EntityPlayer import *
from entities.base.EntityLiving import *
from skills.Arrow import Arrow


class Main():
    def __init__(self, screen):
        self.screen = screen 
        self.isRun = True

        self.players = [EntityPlayer(self)]  
        self.player = self.players[0]             
        self.projectiles = []
        self.monsters = []
        
        self.add_monster(400, 150)
       
        self.draw_screen()
    
    # Обработка событий
    def event_handler(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.isRun = False            
                       
            elif event.type == pygame.USEREVENT+1:
                self.player.tick()
               
                for i in self.monsters:
                    i.tick()
                
            # Нажатие клавиш
            elif event.type == pygame.KEYDOWN:  
                   
                if self.player.animation != DEAD:
                    
                    if event.key == pygame.K_DOWN:                    
                        self.player.movedir = [1, 0, 0, 0] #[D, L, R, U]

                    if event.key == pygame.K_LEFT:                    
                        self.player.movedir = [0, 1, 0, 0] #[D, L, R, U]
                        
                    if event.key == pygame.K_RIGHT:                    
                        self.player.movedir = [0, 0, 1, 0] #[D, L, R, U]
                        
                    if event.key == pygame.K_UP:                    
                        self.player.movedir = [0, 0, 0, 1] #[D, L, R, U]
                        
                    if event.key == pygame.K_SPACE:
                        Arrow(self, self.player).useSkill()
                            
                if event.key == pygame.K_z: 
                    if self.player.animation != DEAD:
                        self.player.kill()
                    else: self.player.ressurection()
                        
                    
            # Отжатие клавиш
            elif event.type == pygame.KEYUP:               
                
                if self.player.animation != DEAD:
                    if event.key == pygame.K_DOWN: 
                        self.player.movedir[DOWN] = 0
                        self.player.animation = 1
                        
                    if event.key == pygame.K_LEFT: 
                        self.player.movedir[LEFT] = 0
                        self.player.animation = 1
                        
                    if event.key == pygame.K_RIGHT: 
                        self.player.movedir[RIGHT] = 0
                        self.player.animation = 1

                        
                    if event.key == pygame.K_UP: 
                        self.player.movedir[UP] = 0
                        self.player.animation = 1

    # Тело рендера
    def render(self):
        self.screen.fill((0, 65, 0))

        # mosnter
        for i in self.monsters: 
            i.render(self.screen) 
            i.render_gui(self.screen)
                
        # player
        self.player.render(self.screen)
        self.player.render_gui(self.screen)           
        
        # other
        for i in self.projectiles: i.render(self.screen)       
        
        pygame.display.flip()
    
    def move(self):
        self.player.move()
        
        for i in self.projectiles: 
            i.move()
            i.remove_projetile()
            
        for i in self.monsters:
            #pygame.time.wait(round(3 + i.speed))
            i.move()            
            
    # Отрисовка экрана
    def draw_screen(self):
        pygame.time.set_timer(pygame.USEREVENT+1, 100)        
        while self.isRun == True:

                       
            self.move()                
            self.render()
            self.event_handler()
           
        
    def add_monster(self, x, y):
        self.monsters.append(EntityMonster(self, [x, y]))
        
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Test')
game = Main(screen)