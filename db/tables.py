# coding: utf-8
from sqlalchemy import INTEGER, BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Integer, LargeBinary, SmallInteger, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Listings(Base):
    __tablename__ = 'listings'

    id = Column(INTEGER, primary_key=True)
    address = Column(Text)
    price = Column(INTEGER)

