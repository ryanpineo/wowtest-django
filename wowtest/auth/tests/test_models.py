from django.test import TestCase

from ..models import Account


class AccountTests(TestCase):
    def test_can_create_with_username_email_password(self):
        username = 'test'
        password = 'test'
        email = 'test@test.com'

        account = Account()
        account.username = username
        account.set_password(password)
        account.email = email
        account.save()
        self.assertGreater(account.pk, 0)
