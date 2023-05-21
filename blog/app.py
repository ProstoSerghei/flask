import os

from flask import Flask, render_template
from flask_migrate import Migrate
import psycopg2

from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.authors import authors_app
from blog.views.auth import login_manager, auth_app
from blog.models.database import db
from blog.security import flask_bcrypt


app = Flask(__name__)
migrate = Migrate(app, db, compare_type=True)

app.config.from_object('blog.configs.DevConfig')

app.register_blueprint(users_app, url_prefix='/users')

app.register_blueprint(articles_app, url_prefix='/articles')

app.register_blueprint(authors_app, url_prefix='/authors')

app.register_blueprint(auth_app, url_prefix='/auth')

db.init_app(app)

login_manager.init_app(app)

flask_bcrypt.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command('create-admin')
def create_admin():
    from blog.models import User

    admin = User(username='admin', is_staff=True)
    admin.password = 'password'

    db.session.add(admin)
    db.session.commit()

    print('done! created users:', admin, end='\n')
