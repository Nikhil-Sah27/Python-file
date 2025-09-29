import tkinter as tk
import datetime

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")

        self.running = False
        self.start_time = None
        self.elapsed_time = datetime.timedelta(0)  # ✅ FIXED: Store timedelta, not int

        self.time_display = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.time_display.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start, width=10)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, width=10)
        self.stop_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, width=10)
        self.reset_button.pack()

        self.update_display()

    def start(self):
        if not self.running:
            self.start_time = datetime.datetime.now() - self.elapsed_time  # ✅ FIXED
            self.running = True
            self.update_display()

    def stop(self):
        if self.running:
            self.elapsed_time = datetime.datetime.now() - self.start_time  # ✅ FIXED
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = datetime.timedelta(0)  # ✅ FIXED
        self.time_display.config(text="00:00:00")

    def update_display(self):
        if self.running:
            elapsed = datetime.datetime.now() - self.start_time
            self.elapsed_time = elapsed
            time_str = str(elapsed).split(".")[0]  # Remove milliseconds
            self.time_display.config(text=time_str)

        self.root.after(1000, self.update_display)  # Refresh every second

# Run the Stopwatch
if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
