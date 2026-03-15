from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
import models 
import schemas
from schemas import TelemetryCreate
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from typing import List
from agent import agent_graph

models.Base.metadata.create_all(bind = engine)

app = FastAPI(title = 'telemetery_pipeline')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/ingest-telemetry', response_model= None)
def ingest_telemetry(data: schemas.TelemetryCreate , db: Session = Depends(get_db)):
    new_log = models.patienttelementery(
        patient_id = data.patient_id,
        heart_rate = data.heart_rate,
        systolic_bp = data.systolic_bp
    )
    db.add(new_log)

    db.commit()
    db.refresh(new_log)
    return {'status':'success', 'data': new_log}

@app.get("/patient/{'patient_id'}", response_model= List[schemas.TelemetryCreate])
def get_patient_history(patient_id: str, limit: int = 10, db: Session = Depends(get_db)):
    history = db.query( models.patienttelementery) \
    .filter(models.patienttelementery.patient_id == patient_id ) \
    .order_by(models.patienttelementery.timestamp.desc()) \
    .limit(limit)\
    .all()

    return history

@app.post("/Ask-a-Doctor", response_model= schemas.Patient_output)
def get_patient_record(data: schemas.Patient_input):
    response = agent_graph.invoke(data)

    print('[SYSTEM-LOG] Preparing the Medical Record')

    return schemas.Patient_output(
        heart_beat = response['heart_beat'] ,
        systolic_bp= response['systolic_bp'] ,
        Patient_status= response['Patient_status'],
        Medical_Recommendation = response['llm_recommendation']
    )





