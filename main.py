import tkinter

# from singleton import GameSingleton

from menu import Menu

root = tkinter.Tk()
Menu(root).create()
root.mainloop()

# from solver import Solver

# searchPath, a_path, fwd_path, xy_path = Solver().a_star()

# print(a_path)