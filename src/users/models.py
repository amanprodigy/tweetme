from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    ''' Custom Base user manager to customize creation
    and handling of users '''

    use_in_migrations = True

    def _create_user(self, username, email, password, is_superuser, is_staff,
                     **extra_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        if not username:
            raise ValueError(_('Please provide a username'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_superuser=is_superuser, is_staff=is_staff,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        is_superuser = False
        is_staff = False
        return self._create_user(username, email, password,
                                 is_superuser, is_staff, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        is_superuser = True
        is_staff = True
        return self._create_user(username, email, password,
                                 is_superuser, is_staff, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User field for Tweetme. User can login with username.
    User will also be able to login using an email
    """

    username = models.CharField(_('username'), max_length=40, unique=True)
    email = models.EmailField(_('email'), unique=True)
    date_joined = models.DateField(_('date joine'), auto_now_add=True)
    first_name = models.CharField(_('first_name'), max_length=125, blank=True)
    last_name = models.CharField(_('last_name'), max_length=125, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        ''' returns full name of the user '''
        if self.first_name:
            return self.first_name + self.last_name
        return self.username

    def get_short_name(self):
        ''' returns short name of the user '''
        if self.first_name:
            return self.first_name
        return self.username

    def natural_key(self):
        ''' returns the credentials that user needs to sign in '''
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        ''' Sends email to this user '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return '{} <{}>'.format(self.username, self.email)

    def __repr__(self):
        return '{} <{}>'.format(self.username, self.email)
