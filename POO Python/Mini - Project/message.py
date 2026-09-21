import time
import threading
import winsound
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class IntervalTimerApp:
    def __init__(self, root):
        self.start_button = None
        self.root = root
        self.root.title("Interval Timer App")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f0f0f0")

        self.background_image = Image.open("background_image.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((1000, 800)))
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.num_sets_var = tk.StringVar()
        self.exercises_per_set_var = tk.StringVar()
        self.work_time_var = tk.StringVar()
        self.rest_time_var = tk.StringVar()
        self.rest_between_sets_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = ttk.Frame(self.root, padding="20", style="Input.TFrame")
        input_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(input_frame, text="Nombre de séries:", style="InputLabel.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.num_sets_var).grid(row=0, column=1)

        ttk.Label(input_frame, text="Nombre d'exercices par série:", style="InputLabel.TLabel").grid(row=1, column=0,
                                                                                                     sticky="w")
        ttk.Entry(input_frame, textvariable=self.exercises_per_set_var).grid(row=1, column=1)

        ttk.Label(input_frame, text="Durée de travail par exercice (en secondes):", style="InputLabel.TLabel").grid(
            row=2, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.work_time_var).grid(row=2, column=1)

        ttk.Label(input_frame, text="Temps de repos entre les exercices (en secondes):",
                  style="InputLabel.TLabel").grid(row=3, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.rest_time_var).grid(row=3, column=1)

        ttk.Label(input_frame, text="Temps de repos entre les séries (en secondes):", style="InputLabel.TLabel").grid(
            row=4, column=0, sticky="w")
        ttk.Entry(input_frame, textvariable=self.rest_between_sets_var).grid(row=4, column=1)

        button_frame = ttk.Frame(self.root, style="Button.TFrame")
        button_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_timer, style="Green.TButton")
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = ttk.Button(button_frame, text="Pause", command=self.pause_timer, style="Orange.TButton")
        self.pause_button.grid(row=0, column=1, padx=5)

        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_timer, style="Red.TButton")
        self.stop_button.grid(row=0, column=2, padx=5)

    def start_timer(self):
        num_sets = int(self.num_sets_var.get())
        exercises_per_set = int(self.exercises_per_set_var.get())
        work_time = int(self.work_time_var.get())
        rest_time = int(self.rest_time_var.get())
        rest_between_sets = int(self.rest_between_sets_var.get())

        self.interval_timer = IntervalTimer(num_sets, exercises_per_set, work_time, rest_time, rest_between_sets)
        self.interval_timer.start()

    def pause_timer(self):
        if hasattr(self, 'interval_timer'):
            self.interval_timer.pause()

    def stop_timer(self):
        if hasattr(self, 'interval_timer'):
            self.interval_timer.stop()

            # Clear the entry fields
            self.num_sets_var.set("")
            self.exercises_per_set_var.set("")
            self.work_time_var.set("")
            self.rest_time_var.set("")
            self.rest_between_sets_var.set("")


class IntervalTimer:
    def __init__(self, num_sets, exercises_per_set, work_time, rest_time, rest_between_sets):
        self.num_sets = num_sets
        self.exercises_per_set = exercises_per_set
        self.work_time = work_time
        self.rest_time = rest_time
        self.rest_between_sets = rest_between_sets
        self.running = False
        self.paused = False

    def start(self):
        self.running = True
        self.paused = False
        thread = threading.Thread(target=self._interval_timer)
        thread.start()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def stop(self):
        self.running = False

    def _interval_timer(self):
        for set_num in range(1, self.num_sets + 1):
            if not self.running:
                break
            print(f'Set {set_num}')
            for exercise_num in range(1, self.exercises_per_set + 1):
                if not self.running:
                    break
                print(f'Exercise {exercise_num}: Work')
                self._timer(self.work_time)
                self._play_notification()
                print('Rest')
                self._timer(self.rest_time)
                self._play_notification()
            if set_num < self.num_sets:
                print(f'Rest between sets: {self.rest_between_sets} seconds')
                self._timer(self.rest_between_sets)
                self._play_notification()

    def _timer(self, seconds):
        while seconds:
            if not self.running:
                break
            if not self.paused:
                mins, secs = divmod(seconds, 60)
                print(f'Time Left: {secs} seconds', end='\r')  # Print remaining time
                time.sleep(1)
                seconds -= 1
        print(' ' * 15, end='\r')  # Clear the remaining time display

    def _play_notification(self):
        winsound.Beep(1000, 1000)  # Notification audio


def main():
    root = tk.Tk()
    root.style = ttk.Style()
    root.style.configure('Green.TButton', foreground='black', background='green', font=('Arial', 12, 'bold'))
    root.style.configure('Orange.TButton', foreground='black', background='orange', font=('Arial', 12, 'bold'))
    root.style.configure('Red.TButton', foreground='black', background='red', font=('Arial', 12, 'bold'))
    root.style.configure('InputLabel.TLabel', foreground='black', font=('Arial', 12))
    root.style.configure('Button.TFrame', background='#f0f0f0')
    app = IntervalTimerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
