from sqlalchemy import Column, Integer, String, Float
from databases import Database
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(250))
    price = Column(Float)

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    quantity = Column(Integer)