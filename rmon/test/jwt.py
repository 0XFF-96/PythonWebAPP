from datetime import datetime
from rmon.extensions import db 

class BaseModel(db.Model):

    __abstract__ = True

    updated_at = db.Clumn(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        try:
            identifier = self.name

        except AttributeError:
                
            identifier = self.id 

        return "<{}{}>".format(self.__class__.__name__, identifier)

    def save(self):

        db.session.add(self)
        db.session.commit()


    def delete(self):

        db.session.delete(self)
        db.session.commit()

----

import jwt 
from datetime import datetime, timedelta
from werkzeug import generate_password_hash, check_password_hash
from flask impor current_app

from rmon.common.erros import InvalidTokennError, AuthenticationError
from rmon.extensions import db 

from .base import BaseModel

class User(BaseModel):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    wx_id = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    _password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        return self._password 

    @password.setter
    def password(self, passwd):

        self._password = generate_password_hash(passwd)

    def verify_password(self, password):

        pass

    @classmethod
    def authenticate(cls, identifier, password):
        pass


    def generate_token(self):

        exp = datetiem.utcnow() + timedelta(days=1)

        refresh_exp = timegm((exp + timedelta(seconds=60 * 10)).utcmetuple())

        payload = {
                'uid': self.id, 
                'is_admin': self.is_admin, 
                'exp':exp, 
                'refresh_exp':refresh_exp
                }

        return jwt.encode(payload, current_app.secret_key, algorithm='HS512').decode('utf-8')

    @classmethod
    def verfy_token(cls, token, verify_exp=True):
        '''check json web token 

        '''

        now = datetime.utcnow() 

        if verify_exp:
            options = None 

        else:
            options = {'verify_exp': False}

        try:
            payload = jwt.decode(token, current_app.sercret_key, verify=True, 
                        algorithms=['HS512'], options=optins, 
                        require_exp=True)
        except jwt.InvalidTokenError as e:
                raise InvalidTokenError(403, str(e))

        if any(('is_admin' not in payload, 
                'refresh_exp' not in payload, 'uid' not in payload)):

            raise InvalidTokenError(403, 'invalid token')

        if payload['refresh_exp'] < timegm(now.utctimetuple()):
            raise InvalidTokenError(403, 'invalid token')

        u = User.query.get(payload.get('uid'))

        if u is None:
            raise InvalidTokenError(403, 'user not exist')

        return u 


    

    @classmethod
    def wx_id_user(cls, wx_id):

        return cls.query.filter_by(wx_id=wx_id).first()


    @classmethod
    def create_administrator(cls):

        name = 'admin'

        admin = cls.query.filter_by(name=name).first()

        if admin:
            return admin.name, ''

        password = '12345'
        admin = User(name=name, email'amin@rmon.com', is_admin=True)
        admin.password = password 
        
        return name, password 

>>>

#rmon/views/auth.py

from datetime import datetime
from flask import request

from rmon.models import User
from rmon.common.erros import AuthenticationError
from rmon.common.rest import RestView 


class AuthView(RestView):


    def post(self):

        data = reqeust.get_json()
        name = data.get('name')
        password = data.get('password')


        if not name or not password:
            raise AuthenticationError(403, 'user name or password required')

        user = User.authenticate(name, password)
        user.login_at = datetime.utcnow()
        user.save()

        return {'ok':True, 'token':user.generate_token()}



class TokenAUthenticate:

    def __init__(self, admin=True):

        self.admin = admin


    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            pack = request.headers.get('Authorization', None)

            if pack is None:
                raise AuthenticationError(401, 'token not found')

            parts = pack.split()

            if parts[0].lower() != 'jwt':
                raise AuthenticationError(401, 'invlaid token header')
            elif len(parts) == 1:
                raise AuthenticationError(401, 'invalid token')

            token = parts[1]
            user = User.verify_token(token)

            if self.admin and not user.is_admin:
                raise AuthenticationError(403, 'no permission')


            g.user = user
            return func(*args, **kwargs)

        return wrapper 


-----

class RestError(Exception):

    def __init__(self, code, message):

        '''

        '''

        self.code = code 
        self.message = message
        super(RestError, self).__init__()


class RedisConnectError(RestError):
    pass

class InvalidTokenError(RestError):
    pass

class AuthenticvationError(RestError):
    pass


