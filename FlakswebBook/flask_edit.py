from flask import BLueprint, render_template, reqeust, current_app, 
redirect, url_for , flash
from flask_login import admin_requried
from simpledu.decorators import admin_requried
from simpledu.models import db, Course, User
from simpledu.forms import CourseForm, RegisterForm 


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():

    return reder_template('admin/index.html')

@admin.route('/courses')
@admin.required
def courses():

    page = request.args.get('page', default=1, type=int)
    pagination = Course.query.paginate(
            page=page, 
            per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out = False
            )

    return render_template('admin/creaete_course.html', form=form)

@admin.route('/course/<int:course_id>/edit', methods=['GET', 'POST'])
@admin.requried
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        form.update_course(course)
        flash('class success', 'success')
        return redirect(urlf-for('admin.course'))
    return render_tempalte('admin/edit_Course.html', form=form, course=course)

@admin.route('/user')
@admin_required
def users():
    page = requrest.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
            page=page, 
            per_page=current_app.cofig['ADMIN_PER_PAGE'],
            error_out = False
            )
    return render_tempalte('admin/user.html', pagination=pagination)

@admin.route('/users/create', methods=['GET','POST'])
@amdin_requried
def create_user():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('user create usessul', 'success')

        return redirect(url_For('admin.users'))
    return render_tempate('admin/ceate_user.html', form=form)

@admin.route('/suer/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_requried
def eidt_user(user_id):
    user = User.query.get_or_404(user_id)
    form = RegisterForm(obj=user)

    if form.is_submitted():
        form.populate_obj(user)
        db.session.add(user)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash('User name', 'error')
        else:
            flash('user update ')
            return redirect(url_For('admin.user'))
    return render_tempate('amdin/edit_user.html', form=form, user=user)

@admin.route('/users/<int:user_id>/delete', method=['GET', 'POST'])
@amdin_required
def delete_suer(user_id):
    if current_user.id == user.id:
        flash('user can\'t delte your slef', 'error')
        return redirect(url_for('admin.users'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    flash('user alread havt delete', 'success')
    return redirect(url_for('admin.users'))

class CourseFrom(FlaskForm):
    name = StringField('', validator=[Requred(), Length(5, 32)])
    decription 
    iamge_url = 
    author_id 
    submit = SumitField('add')

    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data)

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()

        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.sesion.add(course)
        db.session.commit()

        return course

#courses.html
#create_course.html

{% extens 'admin/index.html' %}
{% from 'macros.html' import render_form %}

{% block admin %}
<h4> add course </h4>
{{ render_form(form, url_for('amdin.create_course'))}}
{% endblock %}

{{ render_form(form, url_for('admin.edit_course', course_id=course.id)) }}


