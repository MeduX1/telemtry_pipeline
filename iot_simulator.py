import requests
import random
import time
from collections.abc import Mapping
from collections import namedtuple

API_URL = 'http://127.0.0.1:8000/ingest-telemetry'
PATIENTS = ["PT-001", "PT-002", "PT-003", "PT-004", "PT-005"]

print("🚀 Starting Hospital IoT Sensor Simulation...")

for i in range(0,51):
    payload =  {
        'patient_id': random.choice(PATIENTS),
        'heart_rate': round(random.uniform(60,160),1),
        "systolic_bp": round(random.uniform(90.0, 190.0), 1)
    }

    try:
        response = requests.post(API_URL,json=payload)
        if response.status_code == 200:
            data = response.json().get('data', {})
            print(f"VALIDATED {data.get('id')} | Patient {data.get('patient_id')} | HR: {data.get('heart_rate')} BPM")
        else:
            print('SERVER ERROR ', response.text)
    except requests.exceptions.ConnectionError:
        print("🚨 CRITICAL: Cannot reach the API. Is your FastAPI server running?")
        break
    time.sleep(0.1)
print("🏁 Simulation Complete! Database populated.")




