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

        #styling
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu",16))
        self.s.configure("TButton", font=("Ubuntu",16))

        #tabs 
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        #creating the tabs 
        self.tab1 = ttk.Frame(self.tabs, width=600,height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600,height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600,height=100)

        #customizing the tabs with label (adding in the default timer, fonts and futher styling)
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break_label = ttk.Label(self.tab2, text="5:00", font=("Ubuntu", 48))
        self.short_break_label.pack(pady=20)

        self.long_break_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 48))
        self.long_break_label.pack(pady=20)


        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short break")
        self.tabs.add(self.tab3, text="Long Break")

        #adding in the buttons 




        self.root.mainloop()

    #Functions for the timer

    #start timer threads 
    def start_timer_thread(self):
        pass

    #start timer function
    def start_timer(self):
        pass

    #reset timer
    def reset_timer(self):
        pass
    #skip clock
    def skip_clock(self):
        pass
    #pause clock
    def pasue_timer(self):
        pass

    

PomodoroTimer()