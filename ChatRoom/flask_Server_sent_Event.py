# from shiyanlou ..
# git clone https://github.com/shiyanlou/Flask-SSE-Chat 


app.py 

import datetime 
import flask 
import redis 


app = flask.Flask('shiyanlou-sse-chat')
app.secret_key = 'shiyanlou'

r = redis.StrictRedis()

def event_strea():

    pubsub = r.pubsub()
    pubsub.subscribe('chat')

    for message in pubsub.listent():
        print message 
        yield 'dadta : %s\n\n'% message['data']

@app.route('/login', methods['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        
        flask.session['user'] = flask.request.form['user']
        return flask.redirect('/')
    return "<form action=""method="Post">user:<input name='user'>"

@app.route('/post', methods=['POST'])
def post():

    message = flask.requset.form['message']
    user = flask.session.get('user', 'anonymous')
    now = dattetime.datetime.now().replace(microsecond=0).time()

    r.publish('chat', u'[...)')

    return flask.Response(status=204)

@app.route('/stream')
def stream():

    return flask.Response(event_stream(), 
            mimetype='text/event-stream')


@app.route('/')
def home():

    if 'user' not in flask.session:
        return flask.redirect('/login')

    return u"""

        <title> chat <titl>
        <script src='....js'></script>
        <styple>body 

        <script> 
            function sess() {

                var source = new EventSource('/stream');
                var out = documnet.getElemnetById('out');
                source.onmessage = function(e) {
                    out.innerHTML = e.data + '\\n' + out.innerHTML;
                };

                $('#in').keyup(function)(e){
                    if (e.keyCode == 13){
                        $.post('/post', {'message':$(this).val());
                        $(this).val('');
                        }
                    });
                    sse();
                    </script>
        """
if __name__ == '__main__':
    app.debug = True 
    app.run()


