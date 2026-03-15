from database import Base
from pydantic import Field
from datetime import datetime , timezone
from sqlalchemy import Column, Integer, String, Float, DateTime



class patienttelementery(Base):
    __tablename__= "telemetry_logs"
    id = Column(Integer , primary_key=True, index=True)
    patient_id = Column(String, index = True)
    heart_rate = Column(Float)
    systolic_bp = Column(Float)
    timestamp = Column(DateTime , default =lambda: datetime.now(timezone.utc))




