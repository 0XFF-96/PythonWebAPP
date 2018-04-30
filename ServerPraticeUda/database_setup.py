import os
import sys
from sqlalchemy import Column,ForeignKey, Integer, String
from sqlalchemy.ext.declaritive import declaratice_base
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):

    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)



class menuItem(Base):

    __tablename__ = 'nenu_item'

    name = Column(String(80), nullalbe=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)

