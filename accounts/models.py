from django.db import models
# from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user_obj.set_password(password)  # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class Account(AbstractBaseUser):
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, blank=True, null=True)
#     is_active = models.BooleanField(default=True)  # can login
#     staff = models.BooleanField(default=False)  # staff user non superuser
#     admin = models.BooleanField(default=False)  # superuser
#     timestamp = models.DateTimeField(auto_now_add=True)
#     # confirm     = models.BooleanField(default=False)
#     # confirmed_date     = models.DateTimeField(default=False)

#     USERNAME_FIELD = 'email'  # username
#     # USERNAME_FIELD and password are required by default
#     # ['username'] #python manage.py createsuperuser
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         return self.email

#     def get_username(self):
#         if self.username:
#             return self.username
#         return self.email

#     def get_short_name(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         if self.is_admin:
#             return True
#         return self.staff

#     @property
#     def is_admin(self):
#         return self.admin

    # @property
    # def is_active(self):
    #     return self.active


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     id_user = models.IntegerField()
#     bio = models.TextField(blank=True)
#     location = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.user.username
