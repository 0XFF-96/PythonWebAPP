{% if current_user.can(Permission.MODEATE_COMMENTS) %}
<li><a href="{{ url_for('main.moderate') }}">Moderate Comments</a></li>
{% endif %}


@mian.route('/moderate')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate():

    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.order_by(Comment.timestamp.desc)().paginate(
            page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
            error_out=Fasle)
    comments = pagination.itmes

    return render_template('moderate.html', commnets=comments, 
                            pagination=pagination, page=page)

{% extends "base.html" %}
{% import "_macros.html" as macros %}

<div class="comment-body">
    {% if comment.disabled %}
    <p></p><i> This comment has been disabled by a moderator </i></p>

    {% endif %}
    {% if moderate or not comment.disabled %}
        {% if comment.body_html %}
            {{ comment.body_html %}}
        {% else %}
            {{ comment.body }}
        {% endif %}
    {% endif %}
</div>
{% if moderate %}
    <br>
    {% if comment.disabled %}
    <a class="btn btn-default btn-xs" href="{{ url_for('.moderate_enable",          id=comment.id, page=page) }}>Enable</a>

    <a class='btn btn-danger btn-xs" href="{{ url_for('.moderate_disable', 
            id = comment.id, page=page)}}">Disable</a>
            '</a>
    {% endif %}

@main.route('/moderate/enable/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_enable(id):

    comment = Comment.query.get_or_404(id)
    comment.disabled = False
    db.session.add(comment)

    return redirect(url_for('.moderate', 
                        page=request.args.get('page', 1, type=int)))

@main.route('/moderate/disable/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_disable(id):

    comment = Comment.query.get_or_404(id)
    comment.disable = True
    db.session.add(comment)

    return redirect(url_for('.moderate', 
                        page=request.args.get('page', 1, type=int)))


