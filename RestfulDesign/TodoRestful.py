from flask import Flask 
from flask.ext.restful import reqparse, Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

TODOS = {
        'todo1': {'task':1},
        'todo2': {'task':2},
    }

parser = reqparse.RequestParser()
parser.add_argument('task', type=int, help='Please set a int task content')

class TodoList(Resource):
    def get(self):
        return TODOS, 200, {'Etag', :'some-opaque-string'})

    def post(self):
        args = parset.aprse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id 
        TODO[todo_id] = {'task' :args['task']}

        return TODOS[todo_id], 201
api.add_resource(TodoList, '/todos', '/all_tasks')

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id 
        self.task = task

        self.status = 'active'

resource_fields = {
        'task': fields.String, 
        'uri' : fields.Url('todo_ep')
        }

class Todo(Resource):

    @marshal_with(resource_fields):
    def get(self, todo_id):
        return TodoDao(todo_id=todo_id, task='Remeber the milk'), 200

api.add_resource(Todo, '/todos/<todo_id>', endpoint='todo_ep')

if __name__ == '__main__':
    app.run(debug=True)


