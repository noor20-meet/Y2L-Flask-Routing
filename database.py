from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture, description): 
	product_object=Product(
			name=name,
			price=price,
			picture=picture,
			description=description)
	session.add(product_object)
	session.commit()


def delete_product(the_ID):
	session.query(Product).filter_by(ID=the_ID).delete()
	session.commit()

# delete_product(5)


def edit_description(the_ID, description):
	student_object= session.query(Product).filter_by(ID=the_ID).first()
	student_object.description = description
	session.commit()

def edit_price(the_ID, price):
	student_object= session.query(Product).filter_by(ID=the_ID).first()
	student_object.price = price
	session.commit()

def edit_picture(the_ID, picture):
	student_object= session.query(Product).filter_by(ID=the_ID).first()
	student_object.picture = picture
	session.commit()

def query_all():
	products = session.query(Product).all()
	return products

print(query_all())

def query_ID(the_ID):
	product_object=session.query(Product).filter_by(ID=the_ID)
	return product_object

def add_to_cart(productID):
	cart_object=Cart(productID=productID)
	session.add(cart_object)
	session.commit()

edit_picture(2, "https://static.maccabi-tlv.co.il/wp-content/uploads/2017/06/MTA_201706140435508f3355cc6736195b0ff234a36909905f.jpg")
