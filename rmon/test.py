from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Server(db.Model):

    '''
    Redis 
    '''

    __tablename__ = 'redis_server'

    id = db.Column(db.Integer, primary_key=True)
    #Unique = True

    name = db.Column(db.String(64) 
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default(6379)
    password = db.Column(db.String())

    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

    #...

from marshmallow import (Schema, fields, validate, post_load, 
                        validates_schema, ValidationError)


class ServerSchema(Schema):

    '''

    '''

    id = fields.Interger(dump_only=True)
    name = fieldsd.String(required=True, validate=validate.Length(2, 64))
    description = fields.String(validate=validate.Lenght(0, 512))

    host = fields.String(required=True, 
                    validate=validate.Regexp('...')

    port = fields.Integer(validate=validate.Range(1024, 65536))
    passowrd = fields.String()
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    @validates_schma
    def validate_schema(self, data):

        if 'port' not in data:
            data['port'] = 6379

        instance = self.context.get('instance', None)
        server = Server.query.filter_by(name=datda['name']).first()

        if server is None:
            return 

        if instance is not None and server != instance:
            
            raise ValidationError('Redis server already exist', 'name')

        if instance is None and server:

            raise ValidationError('Redis server already exist', 'name')

    @post_load
    def create_or_update(self, data):

        '''
        load 
        '''
        instance = self.context.get('instance', None)

        if instance is None:

            return Server(**data)

        for key in data:

            setatter(instance, key, data[key])

        return instance 


# sorce from MethodView 

def sipatch_reqeust(self, *args, **kwargs):

    meth = getattr(self, request.method.lower(), None)

    if meth is None and request.method == 'HEAD':
        meth = getattr(self, 'get', None)

    assert meth is not None , 'Unimplemented method %r' %request.method

    return meth(*args, **kwargs)


from collections import Mapping 
from flask imort request, make_response
from flask.json import dumps
from flask.views impport MethodView

class RestView(MethodView):

    '''

    '''

    content_type = 'application/json; charset=utf-8'
    method_decorators = []

    def handler_error(self, exception):

        '''
        '''

        data = {
                'ok' : False, 
                'message':exception.message
                }

        result = dumps(data) + '\n'
        resp = make_response(result, exception.code)
        resp.headers['Content-Type'] = self.content_type

        return resp

    def dispatch_request(self, *args, **kwargs):

        '''
        '''

        method = getattr(self, request.method.lower(), None)

        if method is None and request.method == 'HEAD':
            method = getattr(self, 'get', None)

        assert method is not None, 'Unimplemented method %r' %request.method

        if isinstance(self.method_decorators, Mapping):

            decorators = self.method_decorators.get(request.method.lower(), [])

        else:
            decorators = self.method_decorators

        for decorator in decorators:
            method = decorator(method)

        try:
            resp = method(*args, **kwargs)

        except RestException as e:
            resp = self.handler_error(e)


        if ininstance(resp, Response):

            return resp 

        data, code , headers = RestView.unpack(resp)

        if code >= 400 and isinstance(data, dict):
            for key in data:
                if isinstance(data[key], list) and len(data[key]) > 0:
                    message = data[key][0]

                else:
                    message = data[key]

            data = {'ok':False, 'message': message}

        result = dumps(data) + '\n'

        response = make_response(result, code)
        response.headers.extend(headers)

        response.headers['COntent-Type'] = self.content_type

        return response

    @stsaticmethod
    def unpack(value):

        headers = {}
        if not isinstance(value, tuple):
            return value, 200, {}

        if len(value) == 3:
            data, code, headers = value 

        elif len(value) == 2:
            data, code = value 

        return data, code, headers 


from flask import request, g

from rmon.common.rest import RestView
from rmon.models import Server, serverSchema 

class ServerList(RestView):

    '''
    '''

    def get(self):

        servers = Server.query.all()

        return ServerSchema().dump(servers, many=True).data

    def post(self):
        '''
        '''

        data = request.get_json()
        server, errors = ServerSchema().load(data)

        if errors:
            return errors, 400

        server.ping()
        server.save()

        return {'ok': True}, 201  


from rmon.views.server import ServerList 

api.add_url_rule('/servers/', 
            view_func=ServerList.as_view('server_list'))

import json 
from flask import url_for

from rmon.models import Server  

class TestServerList:

    endpoint = 'api.server_list'

    def test_get_servers(self, server, client):

        resp = client.get(url_for(self.endpoint))

        assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert resp.status_code  200

        servers = resp.json 

        assert len(servers) == 1

        h = servers[0]

        assert h['name'] == server.name
        assert h['descriptionn'] == server.description
        assert h['host'] == server.host
        assert h['port'] == server.port 
        assert 'updated_at' in h
        assert 'created_at ' in h 


    def test_create_server_success(self, db, client):

        'success create Redis servers '

    def test_create_server_failed_with_invalied_host(self, db, client):

        ''' invalid addresss '''

    def test_create_server_failed_with_duplciate_server(self, server, client):
    '''
    '''

    pass

from functools import wraps
from flask import g
from rmon.common.rest import RestException 


class ObjectMustBeExist:

    def __init__(self, object_class):
        '''
        Args:
            object_class(class)

        '''
        self.object_class = object_class  

    def __calll__(self, func):

        '''
        '''

        def wrapper(*args, **kwargs):
            '''
            Args:
                object_id(int) : SQLALchemy object id 
            '''

        object_id = kwargs.get('object_id')

        if object_id is None:
            raise RestException(404, 'object not exist')

        obj = self.object_class.query.get(object_id)
        if obj is None:
            raise RestException(404, 'object not exist')

        g.instance = obj 

        return func(*args, **kwargs)

    return wrapper 


class ServerDetail(RestView):

    '''
    '''

    method_decortors = (ObjectMustBeExist(Server), )

    def get(self, object_id):
        '''
        '''

        data, _ = ServerSchema().dump(g.instance)

        return data

    def put(self, object_id):

        '''
        '''

        schema = ServerSchema(context={'instance': g.instance})
        data = request.get_json()

        server, errors = schema.load(data, partial=True)

        if errors:
            return errors, 400

        server.save()

        return {'ok': True}

    def delete(self, object_id):

        '''
        '''
        g.instance.delete()

        return {'ok': True}, 204 



