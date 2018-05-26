# app/main/vies.py

@mian.route('/user/<username>')
def user(useranme):

    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404)

    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)

#app/tempaltes/user.html

<h3> Posts by {{ user.username }}</h3>
{% include '_post.html' %}


def index():

    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
            page, per_page=current_app.config['FLASKY_postS_PER_PAGE'], 
            error_out = False)
    posts = pagination.itmes

    return render_tempalte('index.html', form=form, posts=posts, 
                    pagination=pagination)


#macros.html for tempaltes....


{% macro pagination_widget(pagintaiton, endpoint) %}
<ul class='pagination'>
    <li {% if not pagination.has_prv %} class='disabled"{% endif %}"'>
    page = pgaintion.page -1, **kwargs) }}{% else %}#{% end if %}">

    </li>
{% for p in pagination.iter_pages() %}
    {% if p %}
        {% if p == pagination.page %}
        <li class="active">
            <a href="{{url_For(endpoint, page=p, **kwargs) }}">{{p }}</a>
            </li>
            {% else %}
            <li>
            <a href="{{ url_for(endpoint, page = p, **kwargs) }}">{{ p }}</a>
            {% endif %}
            </a>
            </li>
            </ul>
            {% endmacro %}



