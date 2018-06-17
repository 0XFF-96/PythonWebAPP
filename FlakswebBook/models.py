from flask import Flask 
from flask.ext.sqlalchemy import SQAlchemy 

app = Flask(__name__)
app.config['..']
db = SQLAlchemy(app)


class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    useranme = db.Column(db.String(32), uniuqe=True)
    password = db.Column(db.string(32))

    def __init__(self, useranme, password):

        self.username = useranme 
        self.password = password 
        
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self.id 
        except Exception, e:
            db.session.rollback()
            return e
        finally:
            return 0 
    def isExisted(self):

        temUser = User.query.filter_by(username=self.useranem, password=self.passowrd).first()

        if temUser is None:
            return 0 
        else:
            return 1 
        
    def getUsername(self):
        return self.username 

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.String(128))
    sender_id = db.Column(db.Integer)

    def __init__(self, context, sender_id):

