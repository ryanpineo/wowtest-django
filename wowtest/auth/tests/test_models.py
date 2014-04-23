from django.test import TestCase

from ..models import Account


class AccountTests(TestCase):
    def test_can_create_with_username_email_password(self):
        username = 'testcreate'
        password = 'testcreate'
        email = 'testcreate@test.com'

        account = Account()
        account.username = username
        account.set_password(password)
        account.email = email
        account.save()
        self.assertGreater(account.pk, 0)

    def test_check_password_wrong_password(self):
        account = Account()
        account.set_password('test')
        self.assertFalse(account.check_password('tester'))

    def test_check_password_correct_password(self):
        account = Account()
        account.set_password('mongo')
        self.assertTrue(account.check_password('mongo'))

    def test_check_password_correct_password_different_case(self):
        account = Account()
        account.set_password('test')
        self.assertTrue(account.check_password('tesT'))
