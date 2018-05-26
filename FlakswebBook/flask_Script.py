flask-script == 2.0.5

from flask.ext.script import Manager 

manager = Manager(app)
if __name__ =='__main__':

    manager.run()

@manager.command
def dev():
    from livereload import Server
    liver_sever = Server(app.wsgi_app)
    liv_server.watch('**/*.*')
    live_server.serve(open_url=True)

from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

@app.orute('/')
def index():
    return render_tempalte('index.html', title='<h1>Hello world<h1>')

'''
List of Builtin Filter 

{{ title | safe }}
# filter .... Jinja
'''

#Markdown = 2.3.1  As a filter 
@app.template_filter('md')
def markdown_to_html(txt):
    from markdown import markdown

    return markdown(txt)

def read_md(filename):

    with open(filename) as md_file:
        content = reduce(lambda x, y : x+y, md_file.readlines())

    return content.decode('utf-8')

@app.context_processor
def inject_methods():

    return dict(read_md=read_md)

'''
<body>
    {{ title | safe }}
    {{ body | md | safe }}
    {{ read_md('http_mehtods.md') }}
<body>

{{ method }} 

'''
'''
{% set links = [{'label':'Home', 'href':url_for('.index')} 
                {'label':'About', 'href':url_for('.about')},
                {'label':'Services', 'href':url_for('.services')},
                ]}

    ] %}

<nav>
    {% for link in lins %}
        {% if not loop.first %} | {% endif %}
        <a href="{{ link.href }}">{{ link.label }}
    {% endfor %}
</nav>

'''
@app.tempalte_test('current_link')
def is_current_link(link):

    return link[0] is reqeust.url

