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

# add_product("ben",7,"p","blabla")

def delete_product(the_id):
	session.query(Product).filter_by(id=the_id).delete()
	session.commit()

# delete_product(1)

def edit_product(the_id, description):
	student_object= session.query(Product).filter_by(id=the_id)
	student_object.description = description
	session.commit()

edit_product(1, "blablablablabla")



def query_all():
	products = session.query(Product).all()
	return products

print(query_all())

def query_id(the_id):
	product_object=session.query(Product).filter_by(id=the_id)
	return product_object

def add_to_cart(productID):
	cart_object=Cart(productID=productID)
	session.add(cart_object)
	session.commit()


add_to_cart(1)
