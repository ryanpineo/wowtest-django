from .base_account import BaseAccount


class Account(BaseAccount):
    class Meta:
        db_table = 'account'
