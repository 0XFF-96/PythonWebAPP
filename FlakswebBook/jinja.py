{% extends 'base.html' %}
{% block content %}
{% block title%}{{ title}} {% endblock %}
<head>
    {% block head %}
        <meta charset="UTF-8">
        <title>{% block title %}{% endblock %}</title>
    {% %}
<nav>
    {% for label, href, in links %}
        {% if not loop.first %} | {% endif %}
            <a href="{% if href is current }"}
            {% else %}
            {{ href }}
            {% endif %}>
                {{ label }}</a>
            {% endfor %}
</nav>
<h1>{{ slef.title() }} </h1>

{% block footer %}
    <hr>
    {{ supper() }}
{% endblock %}

{% for item in itmes %}
    <li>{% block loop_itme %}{{ item }} {% endblock %}</li>
    {% endfor %}


{% macro input(name, value='', type='text', size=20) %}
    <input type="{{ type }}"
            name="{{ name }}"
            value="{{ name }}"
            size="{{ size }}"
            />
{% endmacro %}

    {{ input('username')}}
    {{ input('password', type='password')}}

{% endblock content %}


{{%% import 'marcos.html' as ui %}}

flask-Boostrap=3.3.5.6

from flask_boostrap import Bootstrap
Bootstrap(app)

{{% bll
