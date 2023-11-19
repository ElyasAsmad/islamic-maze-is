import pygame

class QuestionBlock(object):
    
    q_block_list = []
    
    def __init__(self, pos):
        self.q_block_list.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)