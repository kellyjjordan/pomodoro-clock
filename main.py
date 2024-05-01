import time
import threading 
import tkinter as tk
from tkinter import ttk, PhotoImage

#UI class
class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro Timer")
        #load the image file
        icon_image = tk.PhotoImage(file='info1.png')
        
        self.root.tk.call('wm','iconphoto',self.root._w, icon_image)

        self.root.mainloop()

PomodoroTimer()