from django.utils.text import slugify

from .base_account import BaseAccount


class Account(BaseAccount):
    class Meta:
        db_table = 'account'

    def slug(self):
        return slugify(self.username)
