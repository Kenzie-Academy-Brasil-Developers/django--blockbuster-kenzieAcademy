from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model contendo todas os atributos necessários para o cadastro de um novo usuário.

    `@str username`: Nome de usuário único, máximo de 20 caracteres. Obrigatório;
    `@str email`: Campo de email único, máximo de 127 caracteres. Obrigatório;
    `@str birthdate (datetime.date)`: Data de nascimento. Recebe uma string no formato de data (yyyy-MM-dd). Opcional;
    `@str first_name` : Primeiro nome do usuário, máximo 50 caracteres. Obrigatório;
    `@str last_name` : Sobrenome nome do usuário, máximo 50 caracteres. Obrigatório;
    `@str password`: Campo de senha, máximo 127 caracteres. Obrigatório;
    `@bool is_employee`: Indicação sobbre se o usuário é funcionário ou não. Caso o valor passado seja True,
    automaticamente {1} o campo `@is_superuser` será definido como True;
    """

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    birthdate = models.DateField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=127)
    is_employee = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
