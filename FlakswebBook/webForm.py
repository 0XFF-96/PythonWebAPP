CSRF_ENABLED = True 
SECETET_KEY = 'you-will-never-guess'


from flask import FLask

app = Flask(__name__)
app.config.from_object('config')

from app import views 

from flask.ext.wtf import Form
from wtffroms import StringField, BOoleanField 
from wtforms.validators import DataRequired

class LoginForm(Form):

    openid = StringField('opneid', validators[DataRequired()])
    remeber_me = BooleanField('remeber_me', default=False)


@app.route('/login', mehtods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
            title = 'Sgin In', 
            form = form)

@app.route('/user/<nicknamel>')
@login.required
def user(nickname):

    user = User.query.filter_by(nickname = nickname).first()
    if user == None:
        flash('User' + nicknanme + 'not found.')
        return redirect(url_for('index'))

    posts = [
            {'author': user, 'body': 'Test post #1'}, 
            {'author': user, 'body': 'Test post #z'}
            ]
    return render_template('user.html', 
            user = user, 
            posts = posts
            )

{% extnds "base.html" %}

{% block content %}
<h1> User :{{user.nickname }} ! </h1>
<hr>
    {% for post in posts %}
    <p>
        {{ post.author.nickname }} says: <b>{{ post.body }} </b>
    </P>
{% endfor %}
{% endblock %}

<div> Microblog:
    <a href = "{{ url_for('index') }}">Home</a>
    {% if g.user.is_authoenticated() %}
    | <a href="{{ url_for('user', nickname = g.user.nickname) }}">Your Porfile</a>
    | <a href="{{ url_for('logout') }}">Logout</a>
    {% endif %}
</div>

from hashlib import md5 

class User(db.Model):

    def avatar(self, size):

        return '..' + md5self.email).hexdigst() + ?



