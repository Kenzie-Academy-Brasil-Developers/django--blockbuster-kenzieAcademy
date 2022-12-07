from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model contendo todas os atributos necessários para o cadastro de um novo usuário.
    """
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    birthdate = models.DateField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=127)
    is_employee = models.BooleanField(default=False)
