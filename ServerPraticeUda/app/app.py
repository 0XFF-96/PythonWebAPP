from flask import Flask
app = Flask(__name__)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    
    restaurant = session.query(Restaurant).first()
    items = sessin.query(MenuItem).filter_by(restaurant_id=restaurant.id)

    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    
    return output


@app.route('/restaurant/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):

    return "page to create a new menu item.Task 1 Complete !"
if __name__ == '__main__':

    app.debug = True
    app.run()



