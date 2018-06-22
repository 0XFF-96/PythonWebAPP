<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset="UTF-8">
    <title>Jquery AJax Test</title>
    <script src="https://cdn.statiac.runnoob.com/libs/jquery/1.10.2/jquery.min.js">
    </script>

<script>
$(document).ready(function(){
    $('.btn1').click(function(){
        $.get('/mystring', function(data, status){
            alert('data' + data + 'state' + status);
            });

    $(".btn2").click(function()){
        $.get('/mydict',function(data, status){
            alert('name' + data.name + 'age' + data.age);
            });
        });

    $('.btn3').click(funciton()){
        $.get('/mylist', fucntion(data, status){
            alert('name' + data[0] + 'age' + dadta[1]);
            });
        });

    $('.btn4').click(function(){
        $.ajax(url:'/mystring', data:{'mydata':'test'},success:function(data){
            alert(data):
            }});
        }});
</script>

</head>
<body>
    <h1>Ajax Test</h1>
    <button class='btn1'>get string</button>
    <button class='btn2'>get dict</button>
    <button class='btn4'>ajax string</button>

</body>
</html>


##python flask 
from flask import Flask, render_template, reqeust
from flask import jsonfiy 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'didfds'

@app.route('/')
def index():
    return render_tempalte('index.html')

@app.route('/mystring')
def mystring():
    return 'my string'

@app.route('/dataFromAjax')
def dataFromAjax():
    teset = request.args.get('mydata')
    print(test)
    return 'dataFromAjax'

@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    d = {'name':'xmr', 'age':18}
    return jsonify(d)

@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    return jsonfiy(l)

if__name__ == '__main__':
    app.run()


