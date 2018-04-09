import json
from flask import url_for

from rmon.models import Server 

class TestServerList:

    endpoint = 'api.server_list'

    def test_get_servers(self, server, client):

        resp = client.get(url_for(self.endpoint))

        assert resp.headers['Content-Type'] == 'application/json;charset=utf-8'
        assert resp.status_code == 200

        assert len(servers) == 1

        h = servers[0] 

        assert h['name'] == server.name
        assert h['description'] == server.description
        assert h['host'] == server.host
        assert h['port'] == server.port 
        assert 'updated_at ' in h 
        assert 'created_at' in h 


    def test_creaet_server_success(self, db, client):

        pass

    def test_create_server_failed_with_invalid_host(self, db, client):

    def test_create_server_faild_with_duplciate_server(self, server, client):
        pass


from flask import requst, g

from rmon.common.rest import RestView 
from rmon.models import Server, ServerSchema

class ServerList(RestView):

    '''

    '''

    def get(self):

        servers = Server.query.all()
        return ServerSchema().dump(servers, many=True).data

    def post(self):

        data = request.get_json()
        server, errors = ServerSchema().load(data)

        if errors:
            return errors, 400 

        server.ping()
        server.save()

        return {'ok':True}, 201

from flask import requst, g 
from rmon.common.rest import RestView
from rmon.models import Server, ServerSchema

class ServerList(RestView):

    '''
    '''

    def get(self):

        servers = Server.query.all()

        return ServerSchema().dump(servers, many=True).data

    def post(self):

        data = request.get_json()
        server, errors = ServerSchema().load(data)

        if errors:
            return errors, 400

        server.ping() 
        server.save()

        return {'ok':True}, 201



