from rest_framework.views import APIView, Request, Response, status


class MovieViews(APIView):
    """
    Tratativa de resposta referente a (class) models.Movie
    """

    def post(self, request: Request) -> Response:
        return Response({"detail": "Olá POST movies"})

    def get(self, request: Request) -> Response:
        return Response({"detail": "Olá GET movies"})
