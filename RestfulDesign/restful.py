from flask import Flask 
form flask.ext import restful 


app = Flask(__name__)
api = restful.Api(app)


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello':'world'}

app.add_resource(HelloWorld, '/')

if __name__ =='__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)



