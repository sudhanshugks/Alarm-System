import tkinter as tk
from datetime import datetime, timedelta
import winsound
import time

# Create a basic window
root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("400x400")

# Display the clock
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), bg='purple', fg='white')
clock_label.pack(fill='both', expand=1)

# Function to update the clock display
def update_clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    check_alarm(current_time)
    clock_label.after(1000, update_clock)

# Function to set an alarm
def set_alarm(event=None):
    alarm_time = alarm_entry.get()
    alarms.append(alarm_time)
    alarm_label.config(text=f"Alarm is set for {alarm_time}")

# Function to check the alarm time
def check_alarm(current_time):
    for alarm in alarms:
        if current_time == alarm:
            alarm_label.config(text="ALARM!!!")
            play_alarm_sound()

# Function to play the alarm sound
def play_alarm_sound():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000  # Set duration to 1000 milliseconds (1 second)
    winsound.Beep(frequency, duration)

# Function to set a countdown timer
def set_countdown_timer(event=None):
    try:
        duration = int(countdown_entry.get())
        end_time = datetime.now() + timedelta(minutes=duration)
        while datetime.now() < end_time:
            remaining_time = end_time - datetime.now()
            minutes, seconds = divmod(remaining_time.seconds, 60)
            countdown_label.config(text=f"{minutes:02d}:{seconds:02d}")
            root.update()
            time.sleep(1)  # add a small delay to avoid high CPU usage
        countdown_label.config(text="Countdown Complete!")
        play_alarm_sound()
    except ValueError:
        countdown_label.config(text="Please enter a valid number!")

# Function to set an interval timer
def set_interval_timer(event=None):
    try:
        work_duration = int(work_entry.get())
        rest_duration = int(rest_entry.get())
        while True:
            play_alarm_sound()
            time.sleep(work_duration * 60)  # convert minutes to seconds
            play_alarm_sound()
            time.sleep(rest_duration * 60)  # convert minutes to seconds
    except ValueError:
        interval_label.config(text="Please enter valid durations!")

# Entry for setting the alarm
alarm_entry = tk.Entry(root, font=('calibri', 16, 'bold'), width=30)
alarm_entry.insert(0, 'Alarm time (e.g. 13:30:00)')
alarm_entry.bind("<FocusIn>", lambda args: alarm_entry.delete('0', 'end'))
alarm_entry.bind("<Return>", set_alarm)
alarm_entry.pack(pady=20)

# Button to set the alarm
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=10)

# Label for displaying the set alarm
alarm_label = tk.Label(root, font=('calibri', 16), fg='red')
alarm_label.pack(pady=20)

# Entry for setting the countdown timer
countdown_entry = tk.Entry(root, font=('calibri', 16, 'bold'), width=30)
countdown_entry.insert(0, 'Countdown(minutes)(e.g., 5)')
countdown_entry.bind("<FocusIn>", lambda args: countdown_entry.delete('0', 'end'))
countdown_entry.bind("<Return>", set_countdown_timer)
countdown_entry.pack(pady=20)

# Button to set the countdown timer
set_countdown_timer_button = tk.Button(root, text="Set Countdown Timer", command=set_countdown_timer)
set_countdown_timer_button.pack(pady=10)

# Label for displaying the countdown
countdown_label = tk.Label(root, font=('calibri', 16), fg='blue')
countdown_label.pack(pady=20)

# Entry for setting the work duration for the interval timer
work_entry = tk.Entry(root, font=('calibri', 16, 'bold'), width=30)
work_entry.insert(0, 'Work duration(minutes)(e.g., 25)')
work_entry.bind("<FocusIn>", lambda args: work_entry.delete('0', 'end'))
work_entry.pack(pady=20)

# Entry for setting the rest duration for the interval timer
rest_entry = tk.Entry(root, font=('calibri', 16, 'bold'), width=30)
rest_entry.insert(0, 'Rest duration(minutes)(e.g., 5)')
rest_entry.bind("<FocusIn>", lambda args: rest_entry.delete('0', 'end'))
rest_entry.pack(pady=20)

# Button to set the interval timer
set_interval_timer_button = tk.Button(root, text="Set Interval Timer", command=set_interval_timer)
set_interval_timer_button.pack(pady=10)

# Label for displaying the interval timer
interval_label = tk.Label(root, font=('calibri', 16), fg='green')
interval_label.pack(pady=20)

# List to store alarms
alarms = []

# Update the clock display
update_clock()

# Start the Tkinter main loop
root.mainloop()