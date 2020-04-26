from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from database import SessionLocal, engine
import models, schemas
import main

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_number_by_vehicle(db: Session, vehicle: str):
    return db.query(models.User).filter(models.User.vehicle == vehicle).first()

def get_location(db: Session, vehicle: str):
    return db.query(models.Location).filter(models.Location.vehicle == vehicle).order_by(models.Location.id.desc()).first()

def location_update( db: Session, loc:schemas.Location):
    db_loc=models.Location(latitude=loc.latitude, longitude=loc.longitude, vehicle = loc.vehicle)
    # db.query(models.Location).filter(models.Location.vehicle == vehicle).update({models.Location.latitude:loc.latitude, models.Location.longitude:loc.longitude},synchronize_session = False)
    db.add(db_loc)
    db.commit()
    db.refresh(db_loc)
    return db_loc

def sensor_data_update( db: Session, data:schemas.Sensor):
    db_loc=models.Sensor(ax=data.ax, ay = data.ay, az = data.az, vehicle = data.vehicle)
    # db.query(models.Location).filter(models.Location.vehicle == vehicle).update({models.Location.latitude:loc.latitude, models.Location.longitude:loc.longitude},synchronize_session = False)
    db.add(db_loc)
    db.commit()
    db.refresh(db_loc)
    return db_loc

def get_sensor_data(db: Session, vehicle: str):
    return db.query(models.Sensor).filter(models.Sensor.vehicle == vehicle).order_by(models.Sensor.id.desc()).first()

# def location_add( vehicle: str, db: Session):
#     db_loc=models.Location(latitude=0.0, longitude=0.0, vehicle = vehicle)
#     db.add(db_loc)
#     db.commit()
#     db.refresh(db_loc)
#     return db_loc

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_loc(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

def get_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sensor).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, email=user.email, num=user.num, enum=user.enum, vehicle=user.vehicle,  password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # location_add(vehicle = user.vehicle, db = Depends(get_db))
    return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item