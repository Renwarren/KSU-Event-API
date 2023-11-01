from models.student import Student
from utilities.databases import *
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

@app.post('/api/login')
async def verify_login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(Student).filter(Student.Name == username, Student.Password == password).first()
    if user:
        # Authentication successful
        return {'message': 'Login successful', 'email': user.Email}
    else:
        # Authentication failed
        raise HTTPException(status_code=401, detail='Invalid credentials')