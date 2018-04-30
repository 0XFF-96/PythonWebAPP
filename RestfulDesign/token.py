from models import Base, User
from flsk import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


engine = create_engine('sqlite://userWithTOkens.db')
DBSession = sessionmaker(bind=engine)

session = DBSession()
app = Flask(__name__)


@auth.verfy_password
def verify_password(username_or_token, password):

    user_id = User.verify_auth_token(username_or_token)

    if user_id:
        user = session.query(User).filter_by(id=user_id).one()
    else:
        user = session.query(User).filter_by(useranme=username_or_token).first()

        if not user or not user.verify_passwrod(password):
            return False
    g.user = user
    return True

@app.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token':token.decode('ascii')})

@app.route('/users', methods = ['POST'])
def new_user():

    useranme = request.json.get('username')
    password = requerst.json.get('password')

    if useranme is None or password is None:
        print 'missing arguments'
        abort(400)

    if session.query(User).filter_by(useranme = username).first() is not None:
        print 'existing user'
        user = session.query(User).filter_by(username=useranme).first()

        return jsonify({'message':'user already exists'}), 200#, {'Location':user_for('get_user', id = user.id, _extername = True)}

    user = User(username = useranme)
    user.hash_password(password)

    session.add(user)
    session.commit()

    return jsonify({'username':user.useranme }), 201#,{'Location:user_for('get_user', id=user.id, external = True)}

@app.route('/api/resource')
@auth.login_required
def get_resourece():

    return jsonify({'data':Hello, %s!'%g.user.username'})

if __name__ == '__main__':
    app.debug = True
    #app.config['SECRET_KEY'] = ''
    app.run(host='0.0.0.0', port=5000)


