from django.db import models


class RatingChoices(models.TextChoices):
    """
    Opções disponíveis para @rating em (class) models.Movie
    """

    GENERAL_AUDIENCE = "G"
    PARENTAL_GUIDANCE_SUGGESTED = "PG"
    PARENTS_STRONGLY_CAUTIONED = "PG-13"
    RESTRICTED = "R"
    NO_ONE_17_AND_UNDER_ADMITTED = "NC-17"


class Movie(models.Model):
    """
    Model contendo todos os atributos necessários para a interação com filmes dentro da API.

    @title: String referenciando o título do filme. Tamanho máximo: 127 caracteres;
    @duration: String referenciando o tempo de duração do filme. Tamanho máximo: 10 caracteres;
    @rating: String referenciando a classificação indicativa do filme, contendo uma gama de escolhas definidas
    pela (class) RatingChoices (choices: G, PG, PG-13, R, NC-17), tendo como valor default
    "G" = (GENERAL_AUDIENCE) e tamanho máximo igual a 20 caracteres;
    @synopsis: Campo de texto (type: str) sem tamanho máximo que faz a referência a sinopse do filme.
    """

    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.GENERAL_AUDIENCE,
        null=True,
    )
    synopsis = models.TextField(default=None, null=True)
    added_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )
