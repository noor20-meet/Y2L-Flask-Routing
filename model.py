from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
	__tablename__='product'
	ID=Column(Integer, primary_key=True)
	name=Column(String)
	price=Column(Float)
	picture=Column(String)
	description=Column(String)
	def __repr__(self):
		return  "ID: " + str(self.ID) +" "+ "name: " + self.name +" "+ "price: " + str(self.price) +" "+ "picture: " + self.picture +" "+ "Description: " + self.description

class Cart(Base):
	__tablename__='cart'
	ID=Column(Integer, primary_key=True)
	productID=Column(Integer)