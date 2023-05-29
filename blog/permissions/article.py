from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForPatch,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user
from sqlalchemy.orm import joinedload

from blog.models.article import Article
from blog.models.database import db




class ArticlePermission(PermissionMixin):
    PATCH_AVAILABLE_FIELDS = [
        "title",
        "text",
    ]

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch
    
    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        """
        Предобрат данных в соответствие с ограничениями перед обновлением объекта
        :param args:
        :param Dict data: входные данные, прошедшие валидацию (через схему в marshmallow)
        :param obj: обновляемый объект из БД
        :param PermissionUser user_permission: объект, на инстанс с пермишеннами данного пользователя в данном запросе
        :param kwargs:
        :return: возвращает очищенные данные в соответствие с пермишенами данного пользователя
        """
        if current_user.is_staff:
            return data
        article_id = int(data['id'])
        article = Article.query.get(article_id)

        if not article.author.user.username == current_user.username:
            raise AccessDenied('no acces')
        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)
        new_data = {i_key: i_val for (i_key, i_val) in data.items() if i_key in permission_for_patch.columns}
        return new_data

        