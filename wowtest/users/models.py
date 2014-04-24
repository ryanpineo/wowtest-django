from django.utils.text import slugify

from .base_user import BaseUser


class User(BaseUser):
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'account'
        managed = False

    def slug(self):
        return slugify(self.username)
