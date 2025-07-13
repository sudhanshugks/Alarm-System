# Alarm-System
🕒 Python Alarm Clock GUI
A simple and interactive Python GUI application built with Tkinter that includes:

⏰ Alarm Clock

⏳ Countdown Timer

🔁 Interval (Pomodoro-style) Timer

This app allows users to set alarms, run countdowns, and alternate between work/rest intervals—perfect for productivity or daily scheduling.

💡 Features
Live Clock Display (updates every second)

Set Alarm: Get notified at a specific time.

Countdown Timer: Input time in minutes; alarm plays on completion.

Interval Timer: Alternate between work and rest durations repeatedly (Pomodoro style).

Audio Alert: Uses winsound.Beep to play a simple alarm sound on Windows.

🖼️ GUI Preview
Add a screenshot here (e.g. screenshots/app_ui.png)

bash
Copy
Edit
# Example placeholder until image is added
![Alarm Clock GUI Preview](screenshots/app_ui.png)
🛠️ Requirements
Python 3.x

Windows OS (uses winsound, which is Windows-specific)

📦 How to Run
Clone this repository

bash
Copy
Edit
git clone https://github.com/your-username/python-alarm-clock.git
cd python-alarm-clock
Run the script

bash
Copy
Edit
python "Code File.py"
📋 Usage Instructions
Set Alarm: Enter time in HH:MM:SS format (24-hour clock).

Countdown Timer: Enter duration in minutes.

Interval Timer: Enter both work and rest durations in minutes.

Alarms and timers will trigger a system beep when time is up.

🚫 Limitations
Runs only on Windows (due to winsound)

No persistence — alarms reset on restart

The Interval Timer runs infinitely (press Ctrl+C in terminal to stop)

📌 TODO
Add stop/pause functionality

Add cross-platform sound support (e.g., playsound)

Improve GUI styling with themes or icons

🧑‍💻 Author
Sudhanshu Kumar
