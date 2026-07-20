from django.contrib.auth.models import AbstractUser, PermissionsMixin


class Usuario(AbstractUser, PermissionsMixin):
    pass