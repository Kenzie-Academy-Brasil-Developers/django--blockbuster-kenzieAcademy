from rest_framework import permissions
from rest_framework.views import Request, View


class IsAuthEmployeeOrReadOnly(permissions.BasePermission):
    """
    Checagem para avaliar se o usuário logado está tentando acessar um método seguro e, em caso afirmativo,
    checar se o usuário é administrador. Retorna um `@bool: True` em caso afirmativo, caso contrário, retorna
    um `@bool: False`.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """
        Método responsável pela checagem da classe. Aqui é feita a checagem de usuário administrador através do
        atributo `is_staff`, o qual sempre terá o mesmo valor que o atributo `is_employee`.
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated and request.user.is_staff
