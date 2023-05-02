import os

from flask import Flask, render_template
from flask_migrate import Migrate
import psycopg2


from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app



app = Flask(__name__)
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(articles_app, url_prefix='/articles')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@192.168.1.9:5432/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config['SECRET_KEY'] = 'abcdefg123456'
app.register_blueprint(auth_app, url_prefix='/auth')

login_manager.init_app(app)


# cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
app.config.from_object(f"blog.configs.{cfg_name}")



@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('done!')


@app.cli.command('create-user')
def create_user():
    from blog.models import User

    admin = User(username='admin', is_staff=True)
    james = User(username='James')

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print('done! created users:', admin, james, end='\n')
