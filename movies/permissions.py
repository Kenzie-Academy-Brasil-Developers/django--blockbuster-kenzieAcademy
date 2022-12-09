from rest_framework import permissions
from rest_framework.views import Request, View


class IsEmployeeOrReadOnly(permissions.BasePermission):
    """
    Checagem para avaliar se o usuário logado está tentando acessar um método seguro e, em caso afirmativo,
    checar se o usuário é administrador. Retorna um `@bool: True` em caso afirmativo, caso contrário, retorna
    um `@bool: False`.
    """
    def has_permission(self, request: Request, view: View) -> bool:
        is_safe_method = request.method in permissions.SAFE_METHODS
        is_employee = request.user and request.user.is_staff

        return bool(is_safe_method or is_employee)
