import os 
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))


class User(db.Model):

    id = db.Column(db.Inter, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    emial = db.Column(db.String(64), index=True, uniuqe=True)
    post = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True
    @property
    def is_cative(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id) # python3 
        except NameError:
            return str(self.id) #python3

    def __repr__(self):

        return '<USer %r>'%(self.nickname)


