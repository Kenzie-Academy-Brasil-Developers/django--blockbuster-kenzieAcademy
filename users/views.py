from rest_framework.views import APIView, Request, Response, status

from .models import User
from .serializers import UserSerializer


class UserViews(APIView):
    """
    Tratativa de resposta referente a (class) models.User
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
