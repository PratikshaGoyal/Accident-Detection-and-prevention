from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from starlette.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/{vehicle}", response_model=schemas.UserV)
def read_number(vehicle: str, limit: int = 100, db: Session = Depends(get_db)):
    number = crud.get_number_by_vehicle(db, vehicle = vehicle)
    return number

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/location/", response_model=schemas.Location)
def add_location(loc: schemas.LocationAdd, db: Session = Depends(get_db)):
    return crud.location_update(db=db, loc=loc)    

@app.get("/location/{vehicle}", response_model=schemas.LocationV)
def read_number(vehicle: str, limit: int = 100, db: Session = Depends(get_db)):
    loc = crud.get_location(db, vehicle = vehicle)
    return loc

@app.get("/location/", response_model=List[schemas.Location])
def read_loc(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    loc = crud.get_loc(db, skip=skip, limit=limit)
    return loc

@app.post("/sensor/", response_model=schemas.Sensor)
def add_sensor_data(data: schemas.SensorData, db: Session = Depends(get_db)):
    return crud.sensor_data_update(db=db, data=data)  

@app.get("/sensor/", response_model=List[schemas.Sensor])
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_data(db, skip=skip, limit=limit)
    return data

@app.get("/sensor/{vehicle}", response_model=schemas.SensorD)
def read_number(vehicle: str, limit: int = 100, db: Session = Depends(get_db)):
    data = crud.get_sensor_data(db, vehicle = vehicle)
    return data 


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items