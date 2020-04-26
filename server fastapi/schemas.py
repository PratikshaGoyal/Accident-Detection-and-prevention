from typing import List

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserBase1(BaseModel):
    enum: str  

class LocationBase(BaseModel):
    latitude: str
    longitude: str

class SensorBase(BaseModel):
    ax: str
    ay: str
    az: str

class UserCreate(UserBase):
    name: str
    num: str
    enum: str
    vehicle: str
    password: str

class User(UserBase):
    id: int
    name: str
    num: str
    enum: str
    vehicle: str
    
    class Config:
        orm_mode = True

class UserV(UserBase1):

    class Config:
        orm_mode = True

class LocationAdd(LocationBase):
    latitude: str
    longitude: str
    vehicle: str

class Location(LocationBase):
    id: int
    vehicle: str
    latitude: str
    longitude: str

    class Config:
        orm_mode = True

class LocationV(LocationBase):

    class Config:
        orm_mode = True


class SensorData(SensorBase):
    ax: str
    ay: str
    az: str
    vehicle: str

class Sensor(SensorBase):
    id: int
    vehicle: str
    ax: str
    ay: str
    az: str

    class Config:
        orm_mode = True

class SensorD(SensorBase):

    class Config:
        orm_mode = True
# class ItemBase(BaseModel):
#     title: str
#     description: str = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     # owner_id: int

#     class Config:
#         orm_mode = True
