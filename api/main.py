from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas

app = FastAPI(title="PRM Webhook API")

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/persons")
def add_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return {"message": "Person added", "id": db_person.id}

@app.post("/touches")
def add_touch(touch: schemas.TouchCreate, db: Session = Depends(get_db)):
    db_touch = models.Touch(**touch.dict())
    db.add(db_touch)
    db.commit()
    db.refresh(db_touch)
    return {"message": "Touch added", "id": db_touch.id}
