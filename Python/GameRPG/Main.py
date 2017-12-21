# -*- coding: utf-8 -*-
from os import path, makedirs

import pygame

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
        
        print('%.5f' % (0.1-0.9))
        
        if(path.isfile('resources/saves/save.txt')):
            file = open('resources/saves/save.txt', 'r+')
            file = [line.strip() for line in file]
            self.player.level = int(file[0])
            self.player.experience = int(file[1])
            self.player.hp = float(file[2])
            self.player.mp = float(file[3])
            self.player.rect.x = int(file[4])
            self.player.rect.y = int(file[5])
            self.current_level = file[6]
        
        
        self.levels = {}     
        ############## LEVELS ###############
        self.levels['DEFAULT'] = Test(self)
        self.levels['non'] = Default(self)   
        #####################################
        self.total_level_width  = self.levels[self.current_level].width   
        self.total_level_height = self.levels[self.current_level].height
        self.screen = pygame.Surface((WIDTH, self.total_level_height))
        
        self.gen_world(self.current_level)      

        self.timer = pygame.time.Clock()
        
       
                
        
        self.draw_screen()
    
    def __window__(self):
        pygame.init()
        pygame.display.set_caption('Test')
        
        self.window = pygame.display.set_mode(SIZE)
        
        
        self.isRun = True

    
    # Обработка событий
    def event_handler(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.savegame()
                self.isRun = False    
            elif event.type == pygame.USEREVENT+1:
                [i.tick() for i in self.entities]
                [i.tick() for i in self.blocks]
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
                        self.player.attack()
                       
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
        self.window.blit(self.screen, ((WIDTH - self.levels[self.current_level].width) * (-1), 0))
        
        self.blocks.update()    
        #self.blocks.draw(self.screen)  
        self.projectiles.update()
        #self.projectiles.draw(self.screen)        
        self.entities.update()
        #self.entities.draw(self.screen)   
        
        self.camera = Camera(self.camera_configure, self.total_level_width, self.total_level_height)       
        self.camera.update(self.player)
        [self.screen.blit(e.image, self.camera.apply(e)) for e in self.blocks]
        [self.screen.blit(e.image, self.camera.apply(e)) for e in self.entities]
        [self.screen.blit(e.image, self.camera.apply(e)) for e in self.projectiles]
                      
        [i.render_ui(self.screen, self.camera, self.window) for i in self.entities]
        
        pygame.display.update() #or .flip()?
    
    def move(self):
        
        [i.move() for i in self.projectiles]
        [i.move() for i in self.entities]
            
    def gen_world(self, level):
        
        self.current_level = level 
        
        for i in self.entities: self.entities.remove(i)
        for i in self.blocks: self.blocks.remove(i)
        
        self.total_level_width  = self.levels[self.current_level].width   
        self.total_level_height = self.levels[self.current_level].height
        
        self.levels[self.current_level].gen()
        
    # Отрисовка экрана
    def draw_screen(self):
        pygame.time.set_timer(pygame.USEREVENT+1, 100)
        
        while self.isRun == True:
            self.render()
            self.timer.tick(100) 
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
        t = max(-(camera.height-HEIGHT + 120), t) # Не движемся дальше нижней границы
        t = min(0, t)                           # Не движемся дальше верхней границы
    
        return pygame.Rect(l, t, w, h)      

    def savegame(self):
        if not path.isdir('resources/saves/'): makedirs('resources/saves/')
        file = open('resources/saves/save.txt', 'w+')        
        file.write(str(self.player.level) + '\n')
        file.write(str(self.player.experience) + '\n')
        file.write(str(self.player.hp) + '\n')
        file.write(str(self.player.mp) + '\n')
        file.write(str(self.player.rect.x) + '\n')
        file.write(str(self.player.rect.y) + '\n')        
        file.write(str(self.current_level))
        file.close()
        
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
    
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
        
Main()
