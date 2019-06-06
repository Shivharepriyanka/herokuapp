from App03 import app
from db import db

db.init_app(App03)


@app.before_first_request
def create_tables():
    db.create_all()
