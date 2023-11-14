import os
import sys
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# TODO: Implement A* algorithm to automatically move player
# TODO: Use tkinter as game starting GUI

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

class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


# List of Islamic codes/questions
islamic_codes = [
    "What is the first pillar of Islam?",
    "Who is the final prophet in Islam?",
    "What is the holy book of Islam?",
    "In which month do Muslims fast?",
    "What is the pilgrimage to Mecca called?",
    "What is the significance of Laylat al-Qadr?",
    "How many times a day do Muslims pray?",
    "What is the meaning of 'Sadaqah'?",
    "What is the Islamic concept of monotheism?",
    "What is the meaning of 'Jihad' in Islam?"
]

# Corresponding list of answers
islamic_answers = [
    "Shahada",
    "Muhammad",
    "Quran",
    "Ramadan",
    "Hajj",
    "Night of Power",
    "Five",
    "Voluntary charity",
    "Tawhid",
    "Striving or struggling"
]

class IslamicQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Islamic Codes Quiz")

        self.label = tk.Label(master, text="Islamic Codes Quiz", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.question_number = 0
        self.score = 0

        self.question_text = tk.StringVar()
        self.question_text.set(islamic_codes[self.question_number])

        self.question_label = tk.Label(master, textvariable=self.question_text, font=("Helvetica", 12))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = islamic_answers[self.question_number].lower()

        if user_answer == correct_answer:
            messagebox.showinfo("Correct!", "Your answer is correct!")
            self.score += 1
        else:
            correct_answer_message = f"The correct answer is: {correct_answer}"
            messagebox.showinfo("Incorrect!", correct_answer_message)

        self.question_number += 1

        if self.question_number < len(islamic_codes):
            self.question_text.set(islamic_codes[self.question_number])
            self.answer_entry.delete(0, tk.END)
        else:
            self.show_final_score()

    def show_final_score(self):
        final_score_message = f"You got {self.score} out of {len(islamic_codes)} questions correct."
        messagebox.showinfo("Quiz Completed", final_score_message)
        self.master.destroy()

def switch_to_quiz():
    root = tk.Tk()
    app = IslamicQuizApp(root)
    root.mainloop()

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("ISlamic Maze Quiz - Intelligent System")
screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
walls = []
player = Player() # Instantiate the player

# Game layout
level = [
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
]

# Translate the level string above into a real game map. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True

while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
            
        # Player movement when keyboard key is pressed
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player.move(-16, 0)
            if e.key == pygame.K_RIGHT:
                player.move(16, 0)
            if e.key == pygame.K_UP:
                player.move(0, -16)
            if e.key == pygame.K_DOWN:
                player.move(0, 16)


    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        switch_to_quiz()
        pygame.quit()
        sys.exit()

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
    pygame.display.flip()
    clock.tick(360)

pygame.quit()
