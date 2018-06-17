import json 
from datetime import datetime

from flask.ext.restful import Resource, fields, marshal_with, marshal

resource_fiedls = {
        'name': fields.String, 
        'address':fields.String, 
        'date_updated':field.DateTime(dt_format='rtc822'), 
}

class UserInfo(object):
    def __init__(self, name, address, date_updated=datetime.now()):
        self.name = name
        self.address = address
        self.date_updated =  date_updated 


print json.dumps(marshal(UserInfor('magi', 'beijing'), resource_fields))

class Todo(Resource):
    @marshal_with(resource_field, envelope='resource')
    def get(self, **kwargs):
        return UserInfo('magi', 'beijing')

#Flask-OAuthlib :https.

#SSL/TLS 


