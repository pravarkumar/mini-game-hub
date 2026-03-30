import pygame
import sys
import numpy
import pandas
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Game-Hub')
        self.screen = pygame.display.set_mode((1400,900))

        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('cloud_1.jpg')
        self.img.set_colorkey((0,0,0))
        self.img_pos=[0,0]
        self.movementy=[False,False]
        self.movementx=[False,False]
    def run(self):
        while True:
            self.screen.fill((0,0,255))
            self.img_pos[1]+=(self.movementy[1]-self.movementy[0])*10
            self.img_pos[0]+=(self.movementx[1]-self.movementx[0])*10
            self.screen.blit(self.img,self.img_pos)
            for event in pygame.event.get():#mouse keyboard anything is an event
                #event has type attribute 
                if event.type == pygame.QUIT: #click x (the red button) on windoes and it closes 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movementy[0] = True
                    if event.key == pygame.K_s:
                        self.movementy[1]=True
                    if event.key == pygame.K_a:
                        self.movementx[0]=True
                    if event.key == pygame.K_d:
                        self.movementx[1]=True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movementy[0] = False
                    if event.key == pygame.K_s:
                        self.movementy[1]=False
                    if event.key == pygame.K_a:
                        self.movementx[0]=False
                    if event.key == pygame.K_d:
                        self.movementx[1]=False
            pygame.display.update()
            self.clock.tick(60) #60fps
Game().run()

