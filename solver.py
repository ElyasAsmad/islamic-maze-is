from queue import PriorityQueue
from pygame import *
from singleton import GameSingleton

# Player init position is 32, 32

class Solver:
    
    def __init__(self) -> None:
        # self.goal = goal
        pass
    
    def check_wall(self, pos: str):
        return pos == 'W'
        
    def parse_level(self):
        # Noted by E, W, N, S
        level = GameSingleton.level
        
        maze_map = {}
        
        # Playable area
        for i in range(1, len(level) - 1):
            for j in range(1, len(level[i]) - 1):
                # 2. If not walls around the game, check possible movement for EWNS
                
                # Consider all movement is possible, then we check collision
                temp = {
                    'E': 1,
                    'W': 1,
                    'N': 1,
                    'S': 1
                }
                
                ## Check top (N) [row index - 1]
                if self.check_wall(level[i - 1][j]):
                    temp['N'] = 0
                
                ## Check bottom (S) [row index + 1]
                if self.check_wall(level[i + 1][j]):
                    temp['S'] = 0
                    
                ## Check left (W) [col index - 1]
                if self.check_wall(level[i][j - 1]):
                    temp['W'] = 0
                
                ## Check right (E) [col index + 1]
                if self.check_wall(level[i][j + 1]):
                    temp['E'] = 0
                    
                maze_map[(i, j)] = temp
            
        # print('maze_map')
        # print(maze_map)

        return maze_map
        
    def h(self, cell1, cell2):
        x1, y1 = cell1
        x2, y2 = cell2    
        
        return (abs(x1-x2) + abs(y1-y2))
    
    def a_star(self, start=None):
        
        goal = (13, 18)
        
        # Start pos
        if start is None:
            start = (2, 2) # Default starting position
        
        maze_map = self.parse_level()
        
        grids = []
        for i, value_i in enumerate(GameSingleton.level):
            for j, value_j in enumerate(value_i):
                grids.append((i, j))
        
        open = PriorityQueue()
        open.put((self.h(start, goal), self.h(start, goal), start))
        a_path = {}
        g_score = {row: float('inf') for row in grids}
        g_score[start] = 0
        f_score = {row: float('inf') for row in grids}
        f_score[start] = self.h(start, goal)
        search_path=[start]
        while not open.empty():
            curr_cell = open.get()[2]
            search_path.append(curr_cell)
            if curr_cell == goal:
                break
            for d in 'ESNW':
                if maze_map[curr_cell][d] == True:
                    if d == 'E':
                        child_cell = (curr_cell[0], curr_cell[1] + 1)
                    if d == 'W':
                        child_cell = (curr_cell[0], curr_cell[1] - 1)
                    if d == 'N':
                        child_cell = (curr_cell[0] - 1, curr_cell[1])
                    if d == 'S':
                        child_cell = (curr_cell[0] + 1, curr_cell[1])
                        
                    temp_g_score = g_score[curr_cell]+1
                    temp_f_score = temp_g_score + self.h(child_cell,goal)
                    
                    if temp_f_score < f_score[child_cell]:
                        a_path[child_cell] = curr_cell
                        g_score[child_cell] = temp_g_score
                        f_score[child_cell] = temp_g_score + self.h(child_cell, goal)
                        open.put((f_score[child_cell], self.h(child_cell, goal), child_cell))
                        # a_path[child_cell] = curr_cell
        
        fwd_path = {}
        xy_path = {}
        cell = goal
        
        while cell!=start:
            
            fwd_path[a_path[cell]] = cell
            
            key = (a_path[cell][1] * 16, a_path[cell][0] * 16)
            xy_path[key] = (cell[1] * 16, cell[0] * 16)
            
            cell = a_path[cell]
        
        return search_path, a_path, fwd_path, xy_path
            