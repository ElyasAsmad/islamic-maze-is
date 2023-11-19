from queue import PriorityQueue
from pygame import *
from singleton import GameSingleton
import pygame

# Player init position is 32, 32

class Solver:
    
    def __init__(self, goal: Rect) -> None:
        self.goal = goal
        
    def h(cell1, cell2):
        x1, y1 = cell1
        x2, y2 = cell2       
    
    def a_star(self):
        # Starting position for player
        start = (32, 32)
        
        grids = []
        for i, value_i in enumerate(GameSingleton.level):
            for j, value_j in enumerate(value_i):
                grids.append((i * 16, j * 16))
        
        g_score = {cell: float('inf') for cell in grids}
        g_score[start] = 0
        
        f_score = {cell: float('inf') for cell in grids}
        f_score[start] = self.h(start,(32,32))
        
        open = PriorityQueue()
        open.put((self.h(start,(32,32)),self.h(start,(32,32)),start))
        a_path = {}
        while not open.empty():
            curr_cell = open.get()[2]
            if curr_cell == (32,32):
                break
            for d in 'ESNW':
                pass
        