
<script type=text/javascript src="{{
    url_for('static', filename='jquery.js) }}"</script>

<script src="//ajax.gooleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script> window.jQuery || document.write('<script src={{ 
    url_for('static', filename='jquery.js'}}">\x3c</script>)</script>


<script type=text/javascript>
    $SCRIPT_ROOT = {{ request.script_root | tojson|safe }};

    </script>

""'
from flask import Flask,jsonify, render_template, request
app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():

    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_tempalte('index.html')


<script type=text/javascript>
    $(function()) {
        $('a#calculate').bind('click', function()){
            $.getJSON($SCRIPT_ROOT + '/_ADD_NUMBERS', {
                a:$('input[name="a"]').val(),
                b:$('input[name="b:]').val(),
                }, funciton(data){
                    $("#result").text(data.result);
                    });
                return false;
                });
        </script>
        <h1> JQuery Example </h1>
        <p><input type=text size=5 name=a> + 
            <input type=text size=5 name=b> =<span id=reuslt>?</span>
        <p><a href=# id=calculate>claculate server side></a><</p.

