# -*- coding: utf-8 -*-
import pygame

from Constants import *
from Resources import *
from blocks.Block import Brick
from entities.EntityMonster import *
from entities.EntityPlayer import *


class Main():
    def __init__(self, screen):
        self.assets = Resources(ENTITIES, PROJECTILES, GUI).pack
        self.screen = screen 
        self.isRun = True
        self.isPressed = False
       
        self.entities = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()   
        
        self.player = EntityPlayer(self)
        self.entities.add(self.player)   

        self.add_monster(400, 350)
        
        for i in range(int(WIDTH / 40)):
            self.blocks.add(Brick(self, (40*i, 40), (0,1), (0,0,0,0)))            
            self.blocks.add(Brick(self, (40*i, 0), (0,0), (1,1,1,1)))

        self.timer = pygame.time.Clock()        
        
        self.draw_screen()
    
    # Обработка событий
    def event_handler(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.isRun = False    
            elif event.type == pygame.USEREVENT+1:
                [i.tick() for i in self.entities]
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
                        self.player.attack()
                        
                    if event.key == pygame.K_z:
                        self.player.useSkill()
                        
                if event.key == pygame.K_q:
                    if self.player.animation != DEAD:
                        self.player.kill()
                    else: self.player.ressurection()
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN: 
                    self.player.movedir[DOWN] = 0                       
                        
                if event.key == pygame.K_LEFT: 
                    self.player.movedir[LEFT] = 0                        
                    
                if event.key == pygame.K_RIGHT: 
                    self.player.movedir[RIGHT] = 0                        
                        
                if event.key == pygame.K_UP: 
                    self.player.movedir[UP] = 0                      

          

    # Тело рендера
    def render(self):
        self.screen.fill((0, 65, 0))
        
        self.projectiles.update()
        self.projectiles.draw(self.screen)
        self.entities.update()
        self.entities.draw(self.screen)
        self.blocks.update()
        self.blocks.draw(self.screen)  
              
        [i.render_ui(self.screen) for i in self.entities]

        pygame.display.update() #or .flip()?
    
    def move(self):
       
        for i in self.projectiles: i.move()  
        for i in self.entities: i.move()     
            
    # Отрисовка экрана
    def draw_screen(self):
        pygame.time.set_timer(pygame.USEREVENT+1, 100)        
        while self.isRun == True:
            
            self.timer.tick(60) 
            self.event_handler()           
            self.move()                
            self.render()
            
    def add_monster(self, x, y):
        self.entities.add(EntityMonster(self, [x, y]))
        
pygame.init()
pygame.display.set_caption('Test')
screen = pygame.display.set_mode(SIZE)  
game = Main(screen)
pygame.quit()