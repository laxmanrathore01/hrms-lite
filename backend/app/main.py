from fastapi import FastAPI
from app.routes import employee, attendance

app = FastAPI()

@app.get("/")
def root():
    return {"message": "HRMS Lite Backend Running 🚀"}

app.include_router(employee.router, prefix="/employees", tags=["Employees"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])