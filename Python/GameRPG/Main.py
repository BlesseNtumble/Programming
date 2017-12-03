# -*- coding: utf-8 -*-
import pygame
import threading

from Constants import *
from Resources import *
from blocks.Block import Brick
from entities.EntityMonster import *
from entities.EntityPlayer import *
from levels.Default import Default
from levels.Test import Test




class Main():
    def __init__(self):
        self.__window__()
        
        self.assets = Resources(ENTITIES, PROJECTILES, GUI).pack
        
        self.isPressed = False
       
        self.entities = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group() 
        self.player = EntityPlayer(self)
        
        self.current_level = 'DEFAULT'        
        self.levels = {}
        ############## LEVELS ###############
        self.levels['DEFAULT'] = Test(self)
        self.levels['non'] = Default(self)   
        #####################################
        self.gen_world(self.current_level)      

        self.timer = pygame.time.Clock()
        
        total_level_width  = self.levels[self.current_level].width   
        total_level_height = self.levels[self.current_level].height
        self.camera = Camera(self.camera_configure, total_level_width, total_level_height)
        
        self.draw_screen()
    
    def __window__(self):
        pygame.init()
        pygame.display.set_caption('Test')
        
        self.window = pygame.display.set_mode(SIZE)
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        
        self.isRun = True

    
    # Обработка событий
    def event_handler(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.isRun = False    
            elif event.type == pygame.USEREVENT+1:
                [i.tick() for i in self.entities]
            elif event.type == pygame.KEYDOWN:
                if self.player.animation != DEAD:
                    
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:                    
                        self.player.movedir = [1, 0, 0, 0] #[D, L, R, U]

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:                    
                        self.player.movedir = [0, 1, 0, 0] #[D, L, R, U]
                        
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:                    
                        self.player.movedir = [0, 0, 1, 0] #[D, L, R, U]
                        
                    if event.key == pygame.K_UP or event.key == pygame.K_w:                    
                        self.player.movedir = [0, 0, 0, 1] #[D, L, R, U]
                        
                    if event.key == pygame.K_SPACE:
                        #self.player.attack()
                        if self.current_level != 'non':
                            self.gen_world('non')
                        else: self.gen_world('DEFAULT')
                        
                    if event.key == pygame.K_z:
                        self.player.useSkill(0)
                       
                if event.key == pygame.K_q:
                    if self.player.animation != DEAD:
                        self.player.kill()
                    else: self.player.ressurection()
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                    self.player.movedir[DOWN] = 0                       
                        
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                    self.player.movedir[LEFT] = 0                        
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    self.player.movedir[RIGHT] = 0                        
                        
                if event.key == pygame.K_UP or event.key == pygame.K_w: 
                    self.player.movedir[UP] = 0  
                    
    # Тело рендера
    def render(self):   
        self.levels[self.current_level].update()
        self.window.blit(self.screen, (0,0))
               
        self.blocks.update()    
        #self.blocks.draw(self.screen)  
        self.projectiles.update()
        #self.projectiles.draw(self.screen)        
        self.entities.update()
        #self.entities.draw(self.screen)   
        
        self.camera.update(self.player)
        [self.screen.blit(e.image, self.camera.apply(e)) for e in self.blocks]
        [self.screen.blit(e.image, self.camera.apply(e)) for e in self.entities]
        [self.screen.blit(e.image, self.camera.apply(e)) for e in self.projectiles]
                      
        [i.render_ui(self.screen, self.camera) for i in self.entities]
        
        pygame.display.update() #or .flip()?
    
    def move(self):
        
        [i.move() for i in self.projectiles]
        [i.move() for i in self.entities]
            
    def gen_world(self, level):
        
        self.current_level = level 
        
        for i in self.entities: self.entities.remove(i)
        for i in self.blocks: self.blocks.remove(i)
        
        self.levels[self.current_level].gen()
        
    # Отрисовка экрана
    def draw_screen(self):
        pygame.time.set_timer(pygame.USEREVENT+1, 100)
        
        while self.isRun == True:
            self.render()
            self.timer.tick(60) 
            self.event_handler()           
            self.move()           
            
    def add_monster(self, x, y):
        self.entities.add(EntityMonster(self, [x, y]))
        
    def camera_configure(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l+WIDTH / 2, -t+HEIGHT / 2
    
        l = min(0, l)                           # Не движемся дальше левой границы
        l = max(-(camera.width-WIDTH), l)   # Не движемся дальше правой границы
        t = max(-(camera.height-HEIGHT), t) # Не движемся дальше нижней границы
        t = min(0, t)                           # Не движемся дальше верхней границы
    
        return pygame.Rect(l, t, w, h)      

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
    
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
        
Main()
