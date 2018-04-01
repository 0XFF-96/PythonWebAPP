"""
an entry of the application

"""

import urllib 
from rmon.app import create_app
from rmon.models import db

app = create_app()

@app.cli.command()
def init_db():

    print ("sqlite3 database fiel is %s" %app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()



