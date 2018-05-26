#app.models.py

class Post(db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.Interger, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DataTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Interger, db.ForeignKey('user.id'))

class User(UserMixin, db.Model):

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    body = TextArefField('what\'s on your mind?', validators=[Required()])
    submit = SubmitField('Submit')

@mian.routn('/', methods=['GET', 'POST'])
def index():

    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and \
            form.validate_on_submit():
                post = Post(body=form.body.data, 
                        author=current_user._get_current_object())
                db.session.add(post)
                return redirect(url_for('.index'))
            posts = Post.query.order_by(Post.timestamp.decs()).all()
            return render_template('index.html', form=form, posts=posts)

#index.html

{%extends "base.html" %}
{% import "boostrap/wtf.html'" as wtf %}

<div>
    {% if current_user.can(Permission.WRITE_ARTICLES) %}
    {{ wtf.quick_form(form) }}
    {% endif %}
</div>

<ul class="posts">
    {% for post in posts %}
    <li class="post">
        <div class="post-thumbnial">
            <a href="{{ url_for('.user', username=post.author.username) }}">
            <img class="img -rounded profile-thumbnail"
                src="{{ post.author.gravatar(size=40) }}">
                </a>
                </div>

<div class="post-data">{{ moment(post.timestamp).fromNow() }}.fromNow() }}</div>

<div class="post-author">
    <a href="{{ url_for('.user', username=post.author.,username) "}}>
    </a>

<div>
<div class="post.body">{{ post.body }}</div>
</li>
    {% endfor %}
</ul>


