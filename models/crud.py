from sqlalchemy.orm import Session

from . import models, schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.StudentID == student_id).first()


def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.Email == email).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: schemas.StudentCreate):
    # fake_hashed_password = student.password + "notreallyhashed"
    db_student = models.Student(Name=student.Name, Email=student.Email,
                                Password=student.Password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student_update: schemas.StudentUpdate):
    db_student = db.query(models.Student).filter(models.Student.StudentID == student_id).first()
    if db_student:
        for key, value in student_update.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
        return db_student
    return None


def get_event_registrations(db: Session, event_id: int):
    db_event = db.query(models.Registration).filter(models.Registration.EventID == event_id).all()
    if db_event:
        return db_event
    return None


def get_event_registration(db: Session, event_id: int, student_email: str):
    return (
        db.query(models.Student)
        .join(models.Registration, models.Registration.StudentID == models.Student.StudentID)
        .filter(models.Registration.EventID == event_id, models.Student.Email == student_email)
        .first()
    )


def get_all_registrations(db: Session):
    return (
        db.query(models.Registration)
        .all()
    )


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()


def update_event(db: Session, event_id: int, event_update: schemas.EventUpdate):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if db_event:
        for key, value in event_update.dict().items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
        return db_event
    return None


def create_registration_id(db: Session, student: schemas.StudentReg, event_id: int):
    registration = models.Registration(EventID=event_id, StudentID=student.StudentID)
    db.add(registration)
    db.commit()
    db.refresh(registration)

    return registration
