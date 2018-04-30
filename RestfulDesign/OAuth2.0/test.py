# GET https://github.com/login/oauth/authorize 

#https://redirect:url?code=your authorized&state=CSRF..?

# POST https://github.com/login/oauth/access_token


# acces_token=e72e16e42f292c...=.

wget http://labfile.oss.aliyuncs.com/courses/644/material.zip
unzip material.zip
rm -rf material.zip ___MACOSX

sudo pip install virtualenv 
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

from flask import Flask, request, session, redirect, url_for, render_template
from flask_pymongo import PyMongo
from reqeusts_oauthlib import OAuth2Session
import datetime, time
import os



app = Flask(__name__)
mongo = PyMongo(app)
app.config['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_BDNAME'] = 'github_cafe'

client_id = 'what is your application id'
client_secret = ' ....secret'
authorization_base_url = 'htpps://github.com/login/oauth/authorize'
toten_url = 'https://github.com/login/oauth/access_token'

@app.route('/', methos=['GET', 'POST'])
@app.route('page/<int:page>', methods=['GET', 'POST'])
def index(page = 1):
    if request.method == 'POST':
        session['geek_wisdom'] = reqeust.form['geek_wisdom']
        try:
            githuber_say()
        except:
            github = OAuth2Session(client_id)
            authorization_url, state = github.authorization_url(authorization_base_url)
            session['oauth_state'] = state

            return redirect(authorization_url)

    wisdom_list = get_githuber_wisdowm(page=page)

    return render_template('index.html', wisdom_list=wisdom_list, page=page)


def callback():
    github = OAuth2Session(client_id, state)

    token = github.ofetch_token(token_url, client_secret=client_secret, 
                    authorization_response=request.url)
    session['oauth_token'] = token
    github_say()

    return redirect(url_for('index'))


def github_say():
    
    github = OAuth2Session(client_id, token=session['oauth_token']) 
    profile = github.get('https://api.github.com/user').json()

    wisdom_dict = {
            'username': profile['name'],
            'avatar_url':profile['avatar_url'],
            'html_url' : profile['html_url'],
            'geek_wisdom'session['geek_wisdom'],
            'datetime':datetime.datetime.today().strftime('%Y%-m'),
            'timestamp':time.time()
            }
    del session['geek_wisdom']
    mongo.db.wisdom.insert(wisdom_dict)

def get_githuber_wisdom(count1-, page=1):

    return mongo.db.wisdomfind({}).sort([('timestamp', -1)]) - skip(count * (page - 1)).limit(count)


def get_page_count(count=10):

    return mongo.db.wisdom.find({}).count() / count + 1

if __name__ =='__main__':

    app.secret_key = os.urandom(24)
    app.run(debug=True, ssl_context('ssl.crt', 'ssl.key'), threaded=True)

'''

APP = Flask(__name__)
mongo =PyMongo(app)
app.conffig['MONGO_HOST'] = '127.0.0.1'
app.config['MONGO_PORT'] = 27017 
app.confgi['MONGO_DBNAME'] = 'github_cafe'

client_id = 'replace your severce id ' 
client_secret = ' ..... secret'

authorization_base_url = 'https://github.com/login/oauth/authorize'

token_url = 'https://github.ocm/login/oauth/access_token'



