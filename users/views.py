from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from users.permissions import IsEmployeeOrOwner

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    """
    Tratativa de resposta referente a `(class) User`
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


class UserDetailView(APIView):
    """
    Tratativa de respostas referente a filtragem de `(class) User`
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrOwner]

    def get(self, _: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
