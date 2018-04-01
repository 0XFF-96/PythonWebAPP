"""rmon.views.index

"""

from flask import render_template
from flask import views import MethodView


class IndexView(MethodView):

    def get(self):


        return render_tempate('index.html')


