import tkinter as tk
from tkinter import messagebox
import time

class PomodoroApp:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        self.work_minutes = 25
        self.break_minutes = 5
        self.seconds = 0
        self.is_running = False
        self.is_break = False

        self.label = tk.Label(master, text="25:00", font=("Helvetica", 48))
        self.label.pack()

        #start button
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        #stop button
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED) #prevents the user from starting another time
        self.stop_button.config(state=tk.NORMAL)

        while self.minutes > 0 or self.seconds > 0:
            if not self.is_running:
                break
            #checks if its time for break
            if self.work_minutes == 24 and self.seconds == 30 and not self.is_break:
                self.is_break = True
                messagebox.showinfo("TIME FOR BREAK!")
                self.break_timer()
                break

            if self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.seconds -= 1

            self.label.config(text=f"{self.minutes:02d}:{self.seconds:02d}")
            self.master.update()
            time.sleep(1)

        if self.work_minutes == 0 and self.seconds == 0:
            self.stop_timer()

        messagebox.showinfo("Pomodoro Timer", "Time's up!")

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.minutes = 25
        self.seconds = 0
        self.label.config(text="25:00")

    #function or if where it adds in 5 min break at the halfway  mark (10 mins)
    def break_timer(self):
        while self.break_minutes > 0 or self.seconds > 0:
            if not self.is_break:
                break
            if self.seconds ==0:
                self.break_minutes -=1 #decrements the mins by 1
                self.seconds = 59
            else:
                self.seconds -=1
                
            self.label.config(text=f"{self.break_minutes:02d}:{self.seconds:02d}")
            self.master.update()
            time.sleep(1)

            if self.break_minutes == 0 and self.seconds == 0:
                messagebox.showinfo("break times over! back to work!")
                self.is_break = False
                self.start_timer()

    #function to add different time intervals (30 mins, 1 hour (60mins), 2 hours (120 mins))

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
