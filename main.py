import os
import sys
import random
import pygame
import tkinter as tk
from tkinter import messagebox

walls = []

class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        
        # A method for Player instance movement 
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

class Wall:
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
class IslamicQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Islamic Codes Quiz")

        self.label = tk.Label(master, text="Islamic Codes Quiz", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.question_number = 0
        self.score = 0

        self.question_text = tk.StringVar()
        self.question_text.set(question[self.question_number])

        self.question_label = tk.Label(master, textvariable=self.question_text, font=("Helvetica", 12))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = answers[self.question_number]

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "Your answer is correct!")
            self.score += 1
        else:
            messagebox.showerror("Incorrect!", "Sorry, that's incorrect.")

        self.question_number += 1

        if self.question_number < len(question):
            self.question_text.set(question[self.question_number])
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Completed", f"Quiz finished! Your final score: {self.score}/{len(question)}")
            sys.exit()

def game(lmaze, level):
    global walls  # Use the global walls list
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Islamic Maze Quiz - Intelligent System")
    screen = pygame.display.set_mode((320, 240))
    clock = pygame.time.Clock()
    player = Player()
    if level == 4:
        pygame.quit()
        sys.exit()

    x = y = 0
    end_rect = None
    for row in lmaze[level]:
        for col in row:
            if col == "W":
                walls.append(Wall((x, y)))  # Append walls to the list
            if col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 0

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move(-16, 0)
                if event.key == pygame.K_RIGHT:
                    player.move(16, 0)
                if event.key == pygame.K_UP:
                    player.move(0, -16)
                if event.key == pygame.K_DOWN:
                    player.move(0, 16)

        if player.rect.colliderect(end_rect):
            if level + 1 < len(lmaze):
                if quiz(level):
                    game(lmaze, level + 1)  # Call next level
            else:
                messagebox.showinfo("Game Completed", "You've completed all levels!")
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
        clock.tick(60)

          # Exit the while loop to show the quiz interface

def quiz(level):
    root = tk.Tk()
    app = IslamicQuizApp(root)
    root.mainloop()

    ans = app.answer_entry.get()
    if ans.lower() == answers[level].lower():
        return True
    else:
        return False

lmaze = [
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W                  W",
        "W         WWWWWW   W",
        "W   WWWW       W   W",
        "W   W        WWWW  W",
        "W WWW  WWWW        W",
        "W   W     W W      W",
        "W   W     W   WWW WW",
        "W   WWW WWW   W W  W",
        "W     W   W   W W  W",
        "WWW   W   WWWWW W  W",
        "W W      WW        W",
        "W W   WWWW   WWW   W",
        "W     W    E   W   W",
        "WWWWWWWWWWWWWWWWWWWW",
    ],
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W                  W",
        "W         WWWWWW   W",
        "W   WWWW       W   W",
        "W   W        WWWW  W",
        "W WWW  WWWW        W",
        "W   W     W W      W",
        "W   W     W   WWW WW",
        "W   WWW WWW   W W  W",
        "W     W   W   W W  W",
        "WWW   W   WWWWW W  W",
        "W W      WW        W",
        "W W   WWWW   WWW   W",
        "W     W  E     W   W",
        "WWWWWWWWWWWWWWWWWWWW",
    ],
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W                  W",
        "W         WWWWWW   W",
        "W   WWWW       W   W",
        "W   W        WWWW  W",
        "W WWW  WWWW        W",
        "W   W     W W      W",
        "W   W     W   WWW WW",
        "W   WWW WWW   W W  W",
        "W     W   W   W W  W",
        "WWW   W   WWWWW W  W",
        "W W      WW        W",
        "W W   WWWW   WWW   W",
        "W  E  W    E   W   W",
        "WWWWWWWWWWWWWWWWWWWW",
    ],
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W                  W",
        "W         WWWWWW   W",
        "W   WWWW       W   W",
        "W   W        WWWW  W",
        "W WWW  WWWW        W",
        "W   W     W W      W",
        "W   W     W   WWW WW",
        "W   WWW WWW   W W  W",
        "W     W   W   W W  W",
        "WWW   W   WWWWW W  W",
        "W W      WW        W",
        "W W   WWWW   WWW   W",
        "W   E  W    E  W   W",
        "WWWWWWWWWWWWWWWWWWWW",
    ]
]

question = [
    "What is the first pillar of Islam?",
    "Who is the final prophet in Islam?",
    "What is the holy book of Islam?",
    "In which month do Muslims fast?",
]
answers = [
    "Shahada",
    "Muhammad",
    "Quran",
    "Ramadan"
]



if __name__ == "__main__":
    walls = []  # Initialize walls globally
    game(lmaze, 0)  # Start the game with maze_data and level 0
