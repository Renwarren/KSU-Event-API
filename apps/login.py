from models.student import Student
from models.login_credentials import LoginCredentials
from utilities.databases import *
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

@app.post('/login')
async def verify_login(credentials: LoginCredentials, db: Session = Depends(get_db)):
    user = db.query(Student).filter(Student.Email == credentials.email, Student.Password == credentials.password).first()
    if user:
        return {'message': 'Login successful', 'email': user.StudentID}
    else:
        raise HTTPException(status_code=401, detail='Invalid credentials')