@admin.route('/user/create', methods=['GET', 'POST'])
@admin_required
def create_user():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('user craeted', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_suer.html', form=form)


from flask_wtf import FlaskFrom 
from wtfforms import StringField, PasswrodField, SubmitField, BooleanField, ValidationError, TextAreaFeidl, IntergerFiel
from simpledu.models import db, User, Course

class LoginForm(FlaskForm):
    email = StringField('email', validators=[Required(), Email()])
    password = Password('pass', validators=



class CourseForm(FlaskForm):

    name = StringField('name', validators=[Required(), Length(5, 32)])
    description = TextAreField('course', validators=[Required(), Length(20, 256)])
    image_url = StringField('image address', validadtions=[Requried(), URL()])
    author_id = IntegerField('author_id', validators=[Required(), NumberRange(min=1, message='invalid user ID')])

    submit = SubmitFild('submit')

    def validate_author_id(slef, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('user doent' exist)

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()

        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()

        return course


