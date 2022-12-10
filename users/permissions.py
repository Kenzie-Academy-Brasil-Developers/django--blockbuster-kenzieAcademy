from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class IsEmployeeOrOwner(permissions.BasePermission):
    """
    Responsével pela checagem de usuários, recebendo os seguintes retornos:\n
    1. `@bool: False` - Caso a requisição seja feita sem um token de acesso, ou utilizando
    um token de acesso inválido;
    2. `@bool: True` - Caso o usuário seja um superuser, staff e/ou employee e tente acessar
    os dados de qualquer usuário;
    3. `@bool: True` - Caso o usuário seja ou não um superuser, tentando acessar os dados do
    próprio perfil;
    4. `@bool: False` - Caso o usuário não seja um superuser e tente acessar a rota com o id
    de outro usuário;
    """

    def has_permission(self, request: Request, view: User) -> bool:
        user_id = view.kwargs.get("user_id")

        if not request.user and request.user.is_authenticated:
            return False
        elif not (request.user.id is user_id or request.user.is_staff):
            return False
        else:
            return True
