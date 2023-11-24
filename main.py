import models.models
from models.models import Student
from models.login_credentials import LoginCredentials
from utilities.databases import *
from models.models import Event
from models import schemas, crud
from fastapi import FastAPI, HTTPException, Depends, Request, Response

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@app.post('/login')
async def verify_login(credentials: LoginCredentials, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.email == credentials.email,
                                       Student.password == credentials.password).first()
    if student:
        return {'message': 'Login successful', 'email': student.studentid}
    else:
        raise HTTPException(status_code=401, detail='Invalid credentials')


@app.post("/students/", response_model=schemas.StudentBase)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_email(db, student.Email)
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_student(db=db, student=student)


@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student


@app.get("/student_email", response_model=schemas.StudentEmail)
def read_student_email(student_email: str, db: Session = Depends(get_db)):
    db_student_email = crud.get_student_by_email(db, email=student_email)
    if db_student_email is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student_email


@app.put("/students/{student_id}", response_model=schemas.StudentUpdate)
def update_student(student_id: int, student_update: schemas.StudentUpdate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db=db, student_id=student_id, student_update=student_update)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student


@app.post("/students/{student_id}/events/", response_model=schemas.Event)
def create_event_for_student(
        student_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)
):
    return crud.create_student_event(db=db, event=event, student_id=student_id)


@app.get("/events/", response_model=list[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events


@app.get("/events/{event_id}", response_model=schemas.Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = crud.get_event(db=db, event_id=event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.put("/events/{event_id}", response_model=schemas.EventUpdate)
def update_event(event_id: int, event_update: schemas.EventUpdate, db: Session = Depends(get_db)):
    updated_event = crud.update_event(db=db, event_id=event_id, event_update=event_update)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event


@app.get("/events/{event_id}/registrations/", response_model=list[schemas.EventBase])
def get_event_registrations(event_id: int, db: Session = Depends(get_db)):
    registrations = crud.get_event_regis.trations(db=db, event_id=event_id)
    if registrations is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return registrations


@app.post("/register/", response_model=schemas.RegistrationBase)
async def register_for_event(event_id: int, student: schemas.StudentBase, db: Session = Depends(get_db)):
    # Check if the event exists
    db_event = crud.get_event(db=db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    # Check if the student already registered for the event
    existing_registration = crud.get_event_registration(db=db, event_id=event_id, student_email=student.Email)
    if existing_registration:
        raise HTTPException(status_code=400, detail="Student already registered for this event")
    # Register the student for the event
    registration_id = crud.create_registration_id(db=db, student=student, event_id=event_id)

    return registration_id
