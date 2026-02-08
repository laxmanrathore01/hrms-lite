from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Attendance
from ..schemas import AttendanceCreate

router = APIRouter(prefix="/attendance")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    record = Attendance(**data.dict())
    db.add(record)
    db.commit()
    return record

@router.get("/{employee_id}")
def get_attendance(employee_id: int, db: Session = Depends(get_db)):
    return db.query(Attendance).filter_by(employee_id=employee_id).all()