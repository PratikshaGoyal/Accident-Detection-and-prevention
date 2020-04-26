from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    vehicle = Column(String, index=True,unique=True)
    name = Column(String, index=True)
    num = Column(String, unique=True, index=True)
    enum = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)

    loc = relationship("Location", back_populates="user")

class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(String, index=True)
    longitude = Column(String, index=True)
    vehicle = Column(String, ForeignKey("users.vehicle"), index=True)
    # user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="loc")
    sen = relationship("Sensor", back_populates="locate")

class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(Integer, primary_key=True, index=True)
    ax = Column(String, index=True)
    ay = Column(String, index=True)
    az = Column(String, index=True)
    vehicle = Column(String, ForeignKey("location.vehicle"), index=True)
    # user_id = Column(Integer, ForeignKey("users.id"))

    locate = relationship("Location", back_populates="sen")


    # items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")