# app.py - Main orchestrator for the Elderly Care AI system

import yaml
import threading
from health_agent import HealthMonitorAgent
from safety_agent import SafetyAgent
from reminder_agent import ReminderAgent
from llm_handler import LLMHandler
from wearable_api import WearableDevice
from voice_interface import VoiceInterface
from db_connector import DBConnector

def load_settings():
    with open('settings.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    print("🔵 Starting Elderly Care AI System...")
    config = load_settings()

    # Initialize DB
    db = DBConnector(config['database'])

    # Initialize wearable device interface
    wearable = WearableDevice(config['wearable_device'])

    # Initialize LLM agent
    llm = LLMHandler(config['agents']['llm_handler'], db)

    # Voice interface
    voice_interface = VoiceInterface(config['voice_interface'])

    # Initialize agents
    health_agent = HealthMonitorAgent(config['agents']['health_monitor'], wearable, db)
    safety_agent = SafetyAgent(config['agents']['safety_monitor'], wearable, db)
    reminder_agent = ReminderAgent(config['agents']['reminder_agent'], voice_interface, db)

    # Start agents in background threads
    if config['agents']['health_monitor']['enabled']:
        threading.Thread(target=health_agent.start_monitoring, daemon=True).start()

    if config['agents']['safety_monitor']['enabled']:
        threading.Thread(target=safety_agent.start_monitoring, daemon=True).start()

    if config['agents']['reminder_agent']['enabled']:
        threading.Thread(target=reminder_agent.start_reminders, daemon=True).start()

    print("✅ All agents started. System is running...\n")

    # Keep the app running to listen for voice commands (optional)
    try:
        while True:
            voice_interface.listen_for_command(llm.process_command)
    except KeyboardInterrupt:
        print("🛑 Shutting down Elderly Care AI System...")

if __name__ == "__main__":
    main()
