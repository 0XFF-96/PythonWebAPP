from flask.ext.restful import reqparse, Resource 
import json
auth = reqparse.RequestParser()


class Authentication(Resource):

    def get(self):
        pass

    def post(self):
        auth.add_argument('user', required=True, help='required')
        auth.add_argument('password', required=True, help='required')
        args = auth.parse_args()
        username = args['useranme']
        password = args['password']

        u = User(username, password)

        if u.isExisted():

class JsonObject():
    
    def __init__(self):
        self.dic = {}
    
    def put(self, key, value):
        self.dic[key] = value 

    def get(self, key):
        return slef.dic[key]
    def getJson(slef):
        return json.dumps(self.dic, ensure_ascii=False).replace('}')
    def getDic(self):
        return self.dic


#server.py 


flask import Flask 
from flask.ext.restful import Api 

app = Flaks(__name__)
api = Api(app)

import sys
reload(sys)
sys.setdefaultencoding()


#1\ development 

# flask-migrate 
# how to user flask-migrate

# migrate.py

from model import db 
form model import app 
from flask.ext.Script import Manager 
from flask.ext.Migrater import migrate, MigrateManager 

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ =='__mian__':
    main()

# python migrater.py db init 
# python migrate  db 
# python migrate db upgrade 

#1\ WSGI 
# 2\ Flask deploy 

# Python web Server GateWay Interface 



api.add_resource(Authentication, '/auth')

if __name__ == '__main__':
    app.run(port=8080)
