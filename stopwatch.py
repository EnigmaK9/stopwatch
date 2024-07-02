import tkinter as tk
from tkinter import ttk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = ttk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

        self.update_clock()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.elapsed_time = 0
        self.start_time = time.time()
        self.update_label()

    def update_clock(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.update_label()
        self.root.after(1000, self.update_clock)

    def update_label(self):
        hours, rem = divmod(self.elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        self.label.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()

