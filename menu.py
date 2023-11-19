import tkinter as tk
from game import Game
from singleton import GameSingleton

color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'

class Menu:
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.geometry('350x500')
        self.root.resizable(width=False, height=False)
        
        main_frame = tk.Frame(self.root, bg=color1, pady=40)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        self.main_frame = main_frame
        
    def create_button(self, text: str, callback): 
        return tk.Button(
            self.main_frame,
            background=color2,
            foreground=color4,
            activebackground=color3,
            activeforeground=color4,
            highlightthickness=2,
            highlightbackground=color2,
            width=13,
            height=2,
            highlightcolor='WHITE',
            border=0,
            cursor='hand1',
            font=('Arial', 16, 'bold'),
            text=text,
            bd = '5', 
            command=callback,
        ) 
        
    def init_game(self):
        self.root.destroy()
        GameSingleton.game = Game(self.root)
            
    def create(self):
        title = tk.Label(self.main_frame, text = 'ISlamic Maze Game', fg='WHITE', bg=color1)
        title.config(font =("Inter", 24))
        title.grid(column=0, row=0)
        
        # Create a Button
        btn1 = self.create_button('Play', callback=self.init_game)
        btn1.grid(column=0, row=1)
        
        btn2 = self.create_button('Quit', callback=self.root.destroy)
        btn2.grid(column=0, row=2)
    