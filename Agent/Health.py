# agents/health_agent.py

from core.llm_handler import analyze_health_data
from core.db_connector import store_health_data

def process_health_data(data):
    """
    
    Processes wearable health data:
    - Sends it to an LLM for analysis
    - Stores data + analysis in a database
    - Returns the analysis
    """
    print("Received wearable data:", data)
    
    analysis = analyze_health_data(data)
    print("Health Analysis:", analysis)
    
    store_health_data(data, analysis)
    
    return analysis

if __name__ == "__main__":
    sample_data = {
        "bp": "130/85",
        "sugar": "105",
        "steps": 4300
    }
    result = process_health_data(sample_data)
    print("✅ Final Analysis:", result)
