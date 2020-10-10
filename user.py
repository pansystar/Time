import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE

class User(Base):
    __tablename__ = "pansydb"
    id = Column('id', Integer, primary_key = True)
    user_name = Column('user_name', String)