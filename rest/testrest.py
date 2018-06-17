from flask import Flask 
from flask.ext.restful import reqparse, Api, Resource 

app = Flask(__name__)
api = Api(app)


USERS = {
        'row1' : {'name': 'jilu', 'rate':[70, 65]},
        'row2' : {'name': 'bob', 'rate': [89, 90, 68]}
        }

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('rate', type=int, help='rate is a number ', action='append')


class UserInfo(Resource):
    def get(self):
        return USERS, 200

    def post(self):
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('row')) + 1
        user_id = 'rwo%i' % user_id 
        USERS[user_id] = {'name':args['name'], 'rate': args['rate']}

        return USERS[user_id], 201

api.add_resource(UserInfo, '/')

if __name__ =='__main__':
    app.run(debug=True)


