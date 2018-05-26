from werkzeug.routing import BaseConverter
from werkzerug.utils import securtiy_filename

@app.route('/about')
def about():

    return 'About'

# if you access '/about' , it works
# but if you access '/about/' , it don't work.

#multi route , route rules... http method...


# route ---> request.form, cookie, args ---> redirect , make_response, render_tempalte..


#Ajax..
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uername = reqeust.form['username']
        password = request.form['password']

    return render_tempate('login.html', method='xx')

@app.route9'/upload', mehtods=['GET', 'POST'])
def upload():
    if reqeust.method == 'POST':
        f = reqeurst.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepaht, 'static/uploads')
        f.save(upload_path, f.filename)
        
'''
<form action = ""
    method=post
    enctype=multipart/form-data>
    <p><input type=file anme=file>
        <input type=submit value=Upload><p>
</form>
</body>
</html>
'''

from flask import make_response

@app.route('/')
def index():

    abort(400)
    response = make_response(render_tempalte('index.html',
                        title='Welcome'))
    response.set_cookie('username', '')

    return response
    

@app.errohanderd(404)
def page_not_found(error)
    return render_tempate('404.html'), 404




if __name__ == '__main__':
    app.run(debug=True)


