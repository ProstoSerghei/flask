from flask_combo_jsonapi import ResourceDetail, ResourceList
from flask_login import login_required

from blog.schemas import TagSchema
from blog.models.database import db
from blog.models import Tag



class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }
    methods = ['GET']
    decorators = (login_required, )

class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag
    }
    methods = ['GET']
    decorators = (login_required, )
