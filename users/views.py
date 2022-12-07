from rest_framework.views import APIView, Request, Response, status
from django.contrib.auth import authenticate

from .models import User
from .serializers import UserSerializer, LoginSerializer


class UserViews(APIView):
    """
    View responsável por realizar as tratativas de resposta das requisições referentes aos usuários da aplicação.
    """

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, _: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class LoginViews(APIView):
    """
    View Responsável por realizar as tratativas de espostas referentes a sessão de usuários
    """
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response({"detail": "Invalid credentials"}, status.HTTP_403_FORBIDDEN)

        return Response({"detail": f"Welcome {user.username}!"}, status.HTTP_200_OK)
