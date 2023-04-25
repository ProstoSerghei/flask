from flask import Flask, render_template

from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(articles_app, url_prefix='/articles')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config['SECRET_KEY'] = 'abcdefg123456'
app.register_blueprint(auth_app, url_prefix='/auth')

login_manager.init_app(app)

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
