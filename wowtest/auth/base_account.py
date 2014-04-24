from hashlib import sha1

from django.contrib.auth.models import UserManager
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class BaseAccount(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=32, unique=True, validators=[validators.RegexValidator(
            r'^[a-zA-z][a-zA-Z0-9]+',
            message=_("Your username must start with a letter and contain only "
                      "letters and numbers.")), validators.MinLengthValidator(4)]
    )
    password = models.CharField( max_length=40, db_column='sha_pass_hash')
    email = models.EmailField()

    online = models.BooleanField(default=False)

    token_key = models.CharField(max_length=100)
    sessionkey = models.CharField(max_length=80)
    v = models.CharField(max_length=64)
    s = models.CharField(max_length=64)

    reg_mail = models.EmailField()
    joindate = models.DateTimeField(default=timezone.now())

    last_ip = models.CharField(max_length=15)
    last_login = models.DateTimeField(default=timezone.now())

    failed_logins = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)
    lock_country = models.CharField(max_length=2)
    mutetime = models.BigIntegerField(default=0)
    mutereason = models.CharField(max_length=255)
    muteby = models.CharField(max_length=50)

    expansion = models.IntegerField(default=0)
    locale = models.IntegerField(default=0)
    os = models.CharField(max_length=3)
    recruiter = models.IntegerField(default=0)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        abstract = True

    def get_username(self):
        return self.username

    def __str__(self):
        return self.get_username()

    def natural_key(self):
        return (self.get_username(),)

    def is_anonymous(self):
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def _create_password_hash(self, raw_password):
        raw_password = raw_password.upper()
        username = self.username.upper()
        full_password = '{}:{}'.format(username, raw_password)
        return sha1(full_password.encode('utf-8')).hexdigest().upper()

    def set_password(self, raw_password):
        self.password = self._create_password_hash(raw_password)
        # Need to reset these so you can log ingame.
        self.v = ''
        self.s = ''
        self.sessionkey = ''

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        return self._create_password_hash(raw_password) == self.password.upper()

    def set_unusable_password(self):
        # Sets a value that will never be a valid hash
        self.password = ''

    def has_usable_password(self):
        return self.password != ''
