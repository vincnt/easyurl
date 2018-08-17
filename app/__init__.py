from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/vincent/Projects/web/easyurl/urls.db'
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import routes
