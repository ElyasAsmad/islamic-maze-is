import pygame

class Wall(object):
    
    walls = []
    
    def __init__(self, pos):
        self.walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)