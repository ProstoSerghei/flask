from flask import Blueprint, render_template
from flask_login import login_required

from werkzeug.exceptions import NotFound


articles_app = Blueprint('articles_app', __name__)

ARTICLES = {
        'Flask': 'Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.', 
        'Django': 'Django is a free and open-source, Python-based web framework that follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.', 
        'JSON:API': 'A web API is an application programming interface (API) for either a web server or a web browser. As a web development concept, it can be related to a web application\'s client side (including any web frameworks being used). A server-side web API consists of one or more publicly exposed endpoints to a defined request–response message system, typically expressed in JSON or XML by means of an HTTP-based web server. A server API (SAPI) is not considered a server-side web API, unless it is publicly accessible by a remote web application.'
    }


@articles_app.route('/', endpoint='list')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@articles_app.route('/<article_name>/', endpoint='details')
@login_required
def article_details(article_name):
    try:
        article_text = ARTICLES[article_name]
    except KeyError:
        raise NotFound(f'User #{article_name} doesn\'t exist!')
    return render_template('articles/details.html', article_name=article_name, article_text=article_text)


