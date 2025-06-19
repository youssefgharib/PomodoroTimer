import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x350")
        self.root.config(bg="#2d2d2d")

        self.work_time = 25 * 60
        self.short_break_time = 5 * 60
        self.long_break_time = 15 * 60
        self.time_left = self.work_time
        self.is_running = False

        self.label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 24, "bold"), bg="#2d2d2d", fg="#ffffff")
        self.label.pack(pady=20)

        self.timer_display = tk.Label(root, text=self.format_time(self.time_left), font=("Helvetica", 48), bg="#2d2d2d", fg="#ffffff")
        self.timer_display.pack(pady=20)

        button_frame = tk.Frame(root, bg="#2d2d2d")
        button_frame.pack(pady=10)

        self.start_work_button = self.create_button(button_frame, "Start Work", lambda: self.start_timer(self.work_time))
        self.start_work_button.pack(side=tk.LEFT, padx=5)

        self.short_break_button = self.create_button(button_frame, "Short Break", lambda: self.start_timer(self.short_break_time))
        self.short_break_button.pack(side=tk.LEFT, padx=5)

        self.long_break_button = self.create_button(button_frame, "Long Break", lambda: self.start_timer(self.long_break_time))
        self.long_break_button.pack(side=tk.LEFT, padx=5)

        control_frame = tk.Frame(root, bg="#2d2d2d")
        control_frame.pack(pady=10)

        self.stop_button = self.create_button(control_frame, "Stop", self.stop_timer, bg="#e74c3c")
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = self.create_button(control_frame, "Reset", self.reset_timer, bg="#3498db")
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def create_button(self, parent, text, command, bg="#4CAF50"):
        button = tk.Button(parent, text=text, command=command, font=("Helvetica", 12), 
                             bg=bg, fg="#ffffff", relief=tk.FLAT, borderwidth=0, padx=10, pady=5)
        button.bind("<Enter>", lambda e: e.widget.config(bg="#5cb85c"))
        button.bind("<Leave>", lambda e: e.widget.config(bg=bg))
        return button

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

    def start_timer(self, duration):
        if not self.is_running:
            self.time_left = duration
            self.is_running = True
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0 and self.is_running:
            self.time_left -= 1
            self.timer_display.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        elif self.is_running:
            self.is_running = False
            messagebox.showinfo("Time's Up!", "The timer has finished!")

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.time_left = self.work_time
        self.timer_display.config(text=self.format_time(self.time_left))

if __name__ == "__main__":
    root = tk.Tk()
    PomodoroTimer(root)
    root.mainloop()
