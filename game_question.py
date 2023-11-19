
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror
import random
import sys
import os
import pygame
import random
from singleton import GameSingleton
from question import questions
from question_block import QuestionBlock

class GameQuestion:
    
    def __init__(self, q_block: pygame.Rect):
        self.q_block = q_block
    
    def ask_player(self):
        q = random.choice(questions)
        
        answer = askstring('ISlamic Maze Quiz', q.question)
        
        if answer in q.answer:
            QuestionBlock.q_block_list.remove(self.q_block)    
            print('betul')
        else:
            self.wrong_answer()
    
    def wrong_answer(self):

        GameSingleton.health -= 1
        
        if GameSingleton.health != 0:
            showerror('ISlamic Maze Quiz', 'Sorry, you have entered a wrong answer. Please try again. Health remaining: {}'.format(GameSingleton.health))
        else:
            showerror('ISlamic Maze Quiz', 'Sorry, your health is already 0 :( but... NEVER BACK DOWN NEVER WHAT??')
            pygame.quit()
            sys.exit()
    
    def check_answer():
        pass