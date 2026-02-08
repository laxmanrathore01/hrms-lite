from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Employee
from ..schemas import EmployeeCreate

router = APIRouter(prefix="/employees")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def add_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    if db.query(Employee).filter(
        (Employee.email == data.email) |
        (Employee.employee_id == data.employee_id)
    ).first():
        raise HTTPException(400, "Employee already exists")

    emp = Employee(**data.dict())
    db.add(emp)
    db.commit()
    return emp

@router.get("")
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).get(emp_id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}