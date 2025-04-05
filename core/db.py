

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "elderly_care_system"

class DBConnector:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        print("[DB] Connected to MongoDB")

    def insert_reminder(self, user_id, reminder_data):
        return self.db.reminders.insert_one({
            "user_id": user_id,
            **reminder_data
        })

    def get_user_reminders(self, user_id):
        return list(self.db.reminders.find({"user_id": user_id}))

    def insert_health_record(self, user_id, vitals_data):
        return self.db.health.insert_one({
            "user_id": user_id,
            **vitals_data
        })

    def get_latest_health_record(self, user_id):
        return self.db.health.find_one(
            {"user_id": user_id},
            sort=[("timestamp", -1)]
        )

    def insert_user(self, user_data):
        return self.db.users.insert_one(user_data)

    def get_user(self, username):
        return self.db.users.find_one({"username": username})


# Sample usage
if __name__ == "__main__":
    db = DBConnector()
    print(db.get_user_reminders("user123"))
