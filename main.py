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

        self.short_break_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu", 48))
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
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10) #columnspan adjusted the position of the column?

        self.pomodoro = 0
        self.skipped = False
        self.stopped = False





        self.root.mainloop()

    #Functions for the timer

    #start timer threads 
    def start_timer_thread(self):
        t = threading.Thread(target=self.start_timer)
        t.start()
        

    #start timer function
    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        #time loop
        if timer_id == 1:
            full_seconds = 60 * 25
            full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes,seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skip_button: #if the looped is not stopped but skipped 
                self.pomodoro += 1
                self.pomodoro_counter_label.config(text=f"Pomodoros: {self.pomodoro}")
                #checks for break time
                if self.pomodoro % 4 ==0:  #after 4 pomodoros, it moves to the  long breaks 
                    self.tabs.select(2)
                else:
                    self.tabs.select(1) # long break
                self.start_timer()
            #break interval loop
        elif timer_id == 2:
            full_seconds=60 * 5
            full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -=1
            if not self.stopped or self.skip_button:
                self.tabs.select(0) #after the break it goes back to the pomdoro label
                self.start_timer()
        elif timer_id == 3:
            full_seconds = 60 * 15
            full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes,seconds = divmod(full_seconds, 60)
                self.long_break_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -=1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
            else:
                print("invalid timer_id") #error 


    #reset timer
    def reset_timer(self): #resets the pomodoro 
        self.stopped = True
        self.skipped = False
        self.pomodoro = 0
        self.pomodoro_timer_label.config(text="25:00")
        self.short_break_label.config(text="05:00")
        self.long_break_label.config(text="15:00")
        self.pomodoro_counter_label.config(text="Pomodoros: 0")
        
    #skip clock
    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoro_timer_label.config(text="25:00")
        elif current_tab ==1:
            self.short_break_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_label.config(text="15:00")
    #pause clock
    def pasue_timer(self):
        pass

    

PomodoroTimer()