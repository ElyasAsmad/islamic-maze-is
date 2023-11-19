import pygame

from wall import Wall
from question_block import QuestionBlock
from game_question import GameQuestion

class Player(object):
    
    def __init__(self):
        self.is_stopped = True
        self.rect = pygame.Rect(32, 32, 16, 16)
        self.clock = pygame.time.Clock()

    def move(self, dx, dy):
        
        # A method for Player instance movement 
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
    def move_totm(self, dx, dy):
        
        # Set move loop
        self.is_stopped = False
        
        while not (self.is_stopped):
            
            self.rect.x += dx
            self.rect.y += dy
            
            # If you collide with a wall, move out based on velocity
            for wall in Wall.walls:
                if self.rect.colliderect(wall.rect):   
                    self.is_stopped = True                 
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                
                # if player.rect.colliderect(q_block):
                # question = GameQuestion()
    
    def move_single_axis(self, dx, dy):
        
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in Wall.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
        for q_block in QuestionBlock.q_block_list:
                
            if self.rect.colliderect(q_block.rect):       
                
                question = GameQuestion(q_block.rect)
                question.ask_player()
                      
                if dx > 0:
                    self.rect.right = q_block.rect.left
                if dx < 0:
                    self.rect.left = q_block.rect.right
                if dy > 0:
                    self.rect.bottom = q_block.rect.top
                if dy < 0:
                    self.rect.top = q_block.rect.bottom