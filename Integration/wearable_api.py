# agents/wearable_api.py

import random
import time
from datetime import datetime

class WearableDeviceAPI:
    def __init__(self, user_id):
        self.user_id = user_id
        print(f"[WearableAPI] Initialized for user: {self.user_id}")

    def get_vital_signs(self):
        """
        Simulate the fetching of real-time health vitals from a wearable device.
        """
        vitals = {
            "user_id": self.user_id,
            "heart_rate": random.randint(60, 120),       # bpm
            "blood_pressure": f"{random.randint(100, 160)}/{random.randint(60, 100)}",  # systolic/diastolic
            "glucose_level": round(random.uniform(80, 200), 1),  # mg/dL
            "timestamp": datetime.utcnow().isoformat()
        }
        print(f"[WearableAPI] Fetched vitals: {vitals}")
        return vitals

    def detect_fall(self):
        """
        Simulate fall detection using motion sensors in the wearable.
        """
        fall_detected = random.choice([True, False, False, False])  # Low probability
        if fall_detected:
            print(f"[WearableAPI] 🚨 Fall detected for user {self.user_id}")
            return {
                "user_id": self.user_id,
                "event": "fall",
                "timestamp": datetime.utcnow().isoformat()
            }
        return None


# Sample usage
if __name__ == "__main__":
    device = WearableDeviceAPI("user123")
    
    while True:
        vitals = device.get_vital_signs()
        fall_event = device.detect_fall()

        # This would normally be sent to the HealthAgent or SafetyAgent
        time.sleep(5)
