from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsEmployeeOrReadOnly


class MovieViews(APIView):
    """
    Tratativa de resposta referente a (class) models.Movie
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployeeOrReadOnly]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(added_by=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, _: Request) -> Response:
        movies_list = Movie.objects.all()
        serializer = MovieSerializer(movies_list, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class MovieDetailView(APIView):
    """
    Tratativa de resposta referente a (class) models.Movie
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsEmployeeOrReadOnly]

    def get(self, _: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, _: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
