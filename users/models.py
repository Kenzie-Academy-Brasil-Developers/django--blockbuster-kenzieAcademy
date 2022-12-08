from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    """
    Model contendo todas os atributos necessários para o cadastro de um novo usuário.

    @username(str): Nome de usuário único, máximo de 20 caracteres. Obrigatório;
    @email(str: email): Campo de email único, máximo de 127 caracteres. Obrigatório;
    @birthdate(str: datetime.date): Data de nascimento. Recebe uma string no formato de data (yyyy-MM-dd). Opcional;
    @first_name (str): Primeiro nome do usuário, máximo 50 caracteres. Obrigatório;
    @last_name (str): Sobrenome nome do usuário, máximo 50 caracteres. Obrigatório;
    @password (str): Campo de senha, máximo 127 caracteres. Obrigatório;
    @is_employee (bool): Indicação sobbre se o usuário é funcionário ou não. Caso o valor passado seja True,
    automaticamente o campo @is_superuser será definido como True;
    """
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    birthdate = models.DateField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=127)
    is_employee = models.BooleanField(default=False)
