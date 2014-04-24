from django.test import TestCase

from ..models import User


class UserTests(TestCase):
    def test_can_create_with_username_email_password(self):
        username = 'testcreate'
        password = 'testcreate'
        email = 'testcreate@test.com'

        user = User()
        user.username = username
        user.set_password(password)
        user.email = email
        user.save()
        self.assertGreater(user.pk, 0)

    def test_check_password_wrong_password(self):
        user = User()
        user.set_password('test')
        self.assertFalse(user.check_password('tester'))

    def test_check_password_correct_password(self):
        user = User()
        user.set_password('mongo')
        self.assertTrue(user.check_password('mongo'))

    def test_check_password_correct_password_different_case(self):
        user = User()
        user.set_password('test')
        self.assertTrue(user.check_password('tesT'))
