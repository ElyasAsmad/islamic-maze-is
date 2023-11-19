import os
import pygame
import sys
from tkinter import Tk

from player import Player
from wall import Wall
from question_block import QuestionBlock
from singleton import GameSingleton
from solver import Solver

import tkinter.messagebox as mb

class Game:
    
    running = True
    is_solving = False
    question_blocks = []
    highlight_blocks: list[pygame.Rect] = []
    path_blocks: list[pygame.Rect] = []
    
    def __init__(self, root: Tk) -> None:
        
        self.root = root
        
        # Initialise pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        # Set up the display
        pygame.display.set_caption("ISlamic Maze Quiz - Intelligent System")
        self.screen = pygame.display.set_mode((320, 240))

        self.clock = pygame.time.Clock()
        self.player = Player() # Instantiate the player

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
            
        # print(self.end_rect.x / 16, self.end_rect.y / 16)

        while self.running:
            
            self.clock.tick(60)
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.running = False
                    
                # Player movement when keyboard key is pressed
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        # player.move(-16, 0)
                        self.player.move(-16, 0)
                    if e.key == pygame.K_RIGHT:
                        self.player.move(16, 0)
                    if e.key == pygame.K_UP:
                        self.player.move(0, -16)
                    if e.key == pygame.K_DOWN:
                        self.player.move(0, 16)
                    if e.key == pygame.K_p:
                        res = mb.askokcancel('ISlamic Maze Game', 'Do you want to solve this maze?')
                        
                        if res:
                            self.is_solving = True
                        else:
                            print('User cancelled')
                            
                    end_rect_in_unit = (self.end_rect.x, self.end_rect.y)
                    
                    print('End rect: {}'.format(end_rect_in_unit))

            if self.player.rect.colliderect(self.end_rect):
                mb.showinfo('ISlamic Maze Game', 'Alhamdulillah, you win!')
                pygame.quit()
                sys.exit()
                
            if self.is_solving:
                player_pos = self.player.get_position()
                player_pos = (player_pos[1] / 16, player_pos[0] / 16)
                
                search_path, a_path, fwd_path, xy_path = Solver().a_star(start=player_pos)
                
                # Renders A* algorithm search area first!
                for highlight in search_path:
                    self.clock.tick(12)
                    tile = pygame.Rect(highlight[1] * 16, highlight[0] * 16, 16, 16)
                    self.highlight_blocks.append(tile)
                    self.render()
                
                for k, v in a_path.items():
                    
                    self.clock.tick(24)
                    
                    path_tile = pygame.Rect(v[1] * 16 + 6, v[0] * 16 + 6, 4, 4)
                    self.path_blocks.append(path_tile)
                    self.render()
                
                # for a in self.highlight_blocks:
                #     self.clock.tick(12)
                    
                #     path_tile = pygame.Rect(a.x + 6, a.y + 6, 4, 4)
                #     self.path_blocks.append(path_tile)
                #     self.render()
                
                current_pos = (-1, -1)
                
                # Swap sebab terbalik
                end_rect_in_unit = (self.end_rect.x, self.end_rect.y)
                
                while current_pos != end_rect_in_unit:
                    
                    self.clock.tick(6)
                    
                    # Get current position to check with A* algorithm's advice
                    current_pos = self.player.get_position()
                    
                    next_move = xy_path[current_pos]
                    
                    # print('Current pos: {}'.format(current_pos))
                    # print('Next move: {}'.format(next_move))
                    
                    self.player.move_to_position(next_move[0], next_move[1])
                    
                    # Re-renders screen to show user's player position update
                    self.render()
                    
                    # Check if we already reached the flag
                    if self.player.get_position() == end_rect_in_unit:
                        break
                    
            self.render()

        pygame.quit()
        
    def render(self):
        
        # Draw the scene
        self.screen.fill((0, 0, 0))
        for wall in Wall.walls:
            pygame.draw.rect(self.screen, (255, 255, 255), wall.rect)
                
        for q_block in QuestionBlock.q_block_list:
            pygame.draw.rect(self.screen, (0, 255, 0), q_block)

        # Render player health
        heart_img = pygame.image.load('assets/images/heart.png')
        heart_img = pygame.transform.scale(heart_img, (16, 16)).convert_alpha()
        for i in range(0, GameSingleton.health):
            self.screen.blit(heart_img, ((i * 16) + 16 + (i * 3), 0))
            
        for h_block in self.highlight_blocks:
            pygame.draw.rect(self.screen, (0, 0, 128), h_block)
            
        for t_block in self.path_blocks:
            pygame.draw.rect(self.screen, (238, 210, 2), t_block)
            
        pygame.draw.rect(self.screen, (255, 0, 0), self.end_rect)
        
        pygame.draw.rect(self.screen, (255, 200, 0), self.player.rect)
        # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
        pygame.display.flip()
        self.clock.tick(360)