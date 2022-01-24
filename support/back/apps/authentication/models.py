from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from back.core.models import AbsModel


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The field 'email' cannot be emtpy")
        if not password:
            raise ValueError("The field password cannot be empty")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if not password:
            raise ValueError("The field password cannot be empty")
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, AbsModel):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    phone_number = models.CharField(max_length=13, unique=True, validators=[RegexValidator(
        regex=r'+[^0-9]',
        message="The format field 'phone_number' should be like this +123456789012",
        code='Invalid phone number',
        inverse_match=True,
    )])
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return f"{self.email} {self.phone_number}"
