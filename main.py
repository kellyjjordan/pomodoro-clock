import time
import threading 
import tkinter as tk
from tkinter import ttk, PhotoImage

#UI class
class PomodoroTimer:
    def __init__(self):
        #UI
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
        #grid layout
        self.grid_layout = ttk.Frame(self.root) #adds the  grid layout to the root (main UI)
        self.grid_layout.pack(pady=10) #grid layout is packed into the root frame
        #adding in the buttons 

        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread) #adds into the grid layout and the command is tied to the self.start_timer thread
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_clock) #adds into the grid layout and the command is tied to the self.start_timer thread
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_timer) #adds into the grid layout and the command is tied to the self.start_timer thread
        self.reset_button.grid(row=0, column=2)

        #adding the label count for the pormodo
        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoro: 0", font=("Ubuntu",16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3) #columnspan adjusted the position of the column?




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