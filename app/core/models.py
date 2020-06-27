from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                            PermissionsMixin
import re


class UserManager(BaseUserManager):

    def create_user(self, emailaddress, password=None, **extra_fields):
        """ Creates and saves a new user """

        regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if not emailaddress or not re.search(regex_email, emailaddress):
            raise ValueError("Must be a valid Email ")

        user = self.model(email=self.normalize_email(emailaddress), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emailaddress, password):

        user = self.create_user(emailaddress, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
