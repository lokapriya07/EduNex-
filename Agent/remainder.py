

import time
from datetime import datetime
from core.db_connector import fetch_upcoming_reminders, log_reminder_event
from integrations.voice_interface import speak_text

def check_and_trigger_reminders():
    """
    Fetch reminders from the database and trigger them if it's time
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    reminders = fetch_upcoming_reminders(now)

    for reminder in reminders:
        message = f"Hi, this is your reminder to {reminder['task']} at {reminder['time']}."
        print(f" Triggering reminder: {message}")
        speak_text(message)
        log_reminder_event(reminder['id'], "triggered")

def reminder_loop():
    """
    Runs continuously to check for due reminders every minute
    """
    print(" Reminder Agent started.")
    while True:
        check_and_trigger_reminders()
        time.sleep(60)  

# For testing
if __name__ == "__main__":
    reminder_loop()
