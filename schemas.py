from pydantic import BaseModel


class TelemetryCreate(BaseModel):
    patient_id: str
    heart_rate:float
    systolic_bp: float

    model_config = {'from_attributes': True}

class Patient_input(BaseModel):
    patient_id: str
    question: str

class Patient_output(BaseModel):
    heart_beat: float
    systolic_bp: float
    Patient_status: str
    Medical_Recommendation: str
    

