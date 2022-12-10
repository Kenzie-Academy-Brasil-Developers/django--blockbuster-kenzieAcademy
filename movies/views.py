from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieOrderSerializer, MovieSerializer
from .permissions import IsAuthEmployeeOrReadOnly


class MovieViews(APIView, PageNumberPagination):
    """
    Tratativa de respostas referentes a `(class) Movie`
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthEmployeeOrReadOnly]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movies_list = Movie.objects.all()
        current_page_results = self.paginate_queryset(movies_list, request)
        serializer = MovieSerializer(current_page_results, many=True)

        return self.get_paginated_response(serializer.data)


class MovieDetailView(APIView):
    """
    Tratativa de resposta referente a uma instância de `(class) models.Movie` específica
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthEmployeeOrReadOnly]

    def get(self, _: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, _: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    """
    Tratativa de resposta referente a criação de uma instância de `(class) models.MovieOrder`.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(title=movie, buyed_by=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
