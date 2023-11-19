import os
import pygame
import sys
from tkinter import Tk

from player import Player
from wall import Wall
from question_block import QuestionBlock
from singleton import GameSingleton

class Game:
    
    running = True
    question_blocks = []
    
    def __init__(self, root: Tk) -> None:
        # Initialise pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        # Set up the display
        pygame.display.set_caption("ISlamic Maze Quiz - Intelligent System")
        screen = pygame.display.set_mode((320, 240))

        clock = pygame.time.Clock()
        player = Player() # Instantiate the player

        # Translate the level string above into a real game map. W = wall, E = exit
        x = y = 0
        for row in GameSingleton.level:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    self.end_rect = pygame.Rect(x, y, 16, 16)
                if col == "Q":
                    QuestionBlock((x, y))
                x += 16
            y += 16
            x = 0

        while self.running:
            
            clock.tick(60)
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.running = False
                # if event.type == pygame.QUIT:
                #     pygame.quit()
                #     sys.exit()
                    
                # Player movement when keyboard key is pressed
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        # player.move(-16, 0)
                        player.move(-16, 0)
                    if e.key == pygame.K_RIGHT:
                        player.move(16, 0)
                    if e.key == pygame.K_UP:
                        player.move(0, -16)
                    if e.key == pygame.K_DOWN:
                        player.move(0, 16)

            if player.rect.colliderect(self.end_rect):
                pygame.quit()
                sys.exit()

            # Draw the scene
            screen.fill((0, 0, 0))
            for wall in Wall.walls:
                pygame.draw.rect(screen, (255, 255, 255), wall.rect)
            
            pygame.draw.rect(screen, (255, 0, 0), self.end_rect)
            
            for q_block in QuestionBlock.q_block_list:
                pygame.draw.rect(screen, (0, 255, 0), q_block)

            heart_img = pygame.image.load('assets/images/heart.png')
            heart_img = pygame.transform.scale(heart_img, (16, 16)).convert_alpha()
            for i in range(0, GameSingleton.health):
                screen.blit(heart_img, ((i * 16) + 16 + (i * 3), 0))
            
            pygame.draw.rect(screen, (255, 200, 0), player.rect)
            # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
            pygame.display.flip()
            clock.tick(360)

        pygame.quit()