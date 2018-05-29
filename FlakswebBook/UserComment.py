class Comment(db.Model):
    __talbename__ = 'comments'

    id = db.Column(db.Interger, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp =db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post_id = db.Column(db.Integer, db.FoeignKey('posts.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em']

        target.body_html = bleach.linkify(bleach.clean(
            markdow(value, output_format='html'), 
            tags=allowed_tags, strip=True))

    db.event.listen(Comment.body, 'set', Comment.on_changed_body)


class User(db.Model):

    comments = db.relationship('Comment', backref='author', lazy='dynamic')

class Post(db.Model):

    comments = db.relationship('Comment', backref='post', lazy='dnamic')


##forms.py...


class CommentForm(Form):

    body = StringField('', validators=[Required()])
    submit = SubmitField('Submit')

@mian.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):

    post = POST.query.get_or_404(id)
    form = CXommentForm()
    if form.vladiate_on_submmit():
        comment = Comment(body=form.body.data, 
                        post=post, 
                        author=current_user._get_current_object())
        db.session.add(comment)
        flash('Your comment has been published')

        return redirect(url_for('.post', id=post.id, page=-1))
    page = request.args.get('page', 1, type=int)

    if page == -1:
        page = (post.comments.count() -1) /\ 
        current_app.config['FLASK_COMMENTS_PER_PAGE'] + 1

        pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
                page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'], error_out=Fasle)

    comments = pagination.itmes

    return render_template('post.html', posts=[posts], form=form, 
                            comments=comments, pagination=pagination)



<a href="{{ ufl_for('.post', id=post.id) }}#comments">
<span> cl
