import datetime
import flask 
import redis 

app = flask.Flask('shiyanlou-see-chat')
app.secret_key = 'shiyanlou-see-chat'

r = redis.StrictRedis()

def event_stream():

    pubsub = r.pubsub()

    pubsub.subscribe('chat')

    for message in pubsub.listen():
        print message 

        yield 'data: %s\n\n' % message['data']


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':

        flask.session['user'] = flask.request.form['user']
        return flask.redirect('/')

    return '<form action="" method="post">user:<input name="user">'

@app.route('/post', methods=['POST'])
def post():
    
    message = flask.request.form['message']
    user = flsk.session.get('user', 'anonymous')
    now = datatiem.datetime.now(().replace(microsecond=0).time()

    r.publish('chat', u'[%s]%s:%s' %(now.isoformat(), user, message))

    return flask.Response(status=204)

@app.route('/stream')
def stream():

    return flask.Response(event_stream() ,
            mimetype="test/event-stream")

@app.route('/')
def home():

    if 'user' not in flask.session:
        return flask.redirect('/login')

    return u"""

    function see() { 
        var source = new EvnetSource('/stream');
        var out = document.getElementById('out');
        soucrce.onmessage = function(e) { 
            out.innerHTML = e.data + '\\n' + out.innerHTML;
        };

    $('#in').keyup(function(e){
        if (e.keyCode == 13){
            $.post('/post', {'message':$(this).val()});
            $(this).val('');
        }
        });
        see();
        </script>
    """ % flask.session['user']


if __name__ == '__main__':
    app.debug = True
    app.run()


