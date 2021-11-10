from flask import Flask

from flask import render_template, request, session
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf.csrf import CsrfProtect


from flask_wtf.csrf import CSRFProtect

# Kết nối đến CSDL trong PostgresSQL
database_url = 'postgresql+psycopg2://postgres:thanhnho@localhost/phunhuan'
#database_url = ('postgresql://user:password@server/db')
#DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost:5432/books'
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            pass

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = ()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token    
