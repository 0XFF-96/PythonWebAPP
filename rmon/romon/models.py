# rmon.model
# picking 


from flask_sqlalchemy import SQLALchemy
from datatime imort datetime

db = SQLAlchemy()

class Server(db.Model):

    """Redis
    """

    __tablename__ = 'redis_server'

    id = db.Column(db.Integer, primary_key=True)
    #para primary_key = True means ?

    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Interger, default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.DateTime, default=datetiem.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        return '<Server(name=%s)>' %self.name

    def save(self):

        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()



