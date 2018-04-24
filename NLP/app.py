from flask import Flask
app = Flask(__name__)
from flask import render_template 
from flask import request, redirect
from core import process_data


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    
    error = "None "

    if request.method == 'POST':

        data = request.form['messages']
        return redirect('index.html')
        return render_template('index.html', name=data)
    return render_template('index.html', name=error)





@app.route('/message', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        data = request.form['message']
        after_process = process_data(data)
        return render_template('index.html', name=after_process)
    else:
        return 'bad'
    


if __name__ =='__main__':

    app.run()


