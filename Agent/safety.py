

import time
from integrations.wearables_api import get_motion_data
from integrations.voice_interface import send_alert_voice
from core.db_connector import log_safety_event

ALERT_CONTACTS = ["+91XXXXXXXXXX", "family@example.com"]

def detect_fall(data):
    """
    Basic fall detection logic using motion data (mocked)
    """
    acceleration = data.get("acceleration", 0)
    sudden_drop = data.get("sudden_drop", False)

    if acceleration < 2.0 and sudden_drop:
        return True
    return False

def safety_monitor_loop():
    """
    Continuously monitors motion data and triggers alerts
    """
    print(" Safety Agent running...")

    while True:
        motion_data = get_motion_data()

        if detect_fall(motion_data):
            print(" Fall detected! Notifying caregivers...")
            send_alert_voice("Urgent! Fall detected for Mr. Sharma.", ALERT_CONTACTS)
            log_safety_event("fall", motion_data)
        else:
            print("✅ No fall detected.")

        time.sleep(10)  

# Sample run (only for testing)
if __name__ == "__main__":
    safety_monitor_loop()
