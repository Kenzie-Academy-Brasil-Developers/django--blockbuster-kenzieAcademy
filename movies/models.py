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
    Model contendo todos os atributos necessários para a interação com filmes dentro da API.\n
    _____________________\n
    Recebe os seguintes parâmetros:\n
    `title`: String referenciando o título do filme. Tamanho máximo: 127 caracteres;\n
    `duration`: String referenciando o tempo de duração do filme. Tamanho máximo: 10 caracteres;\n
    `rating`: String referenciando a classificação indicativa do filme, contendo uma gama de escolhas definidas
    pela (class) RatingChoices (choices: G, PG, PG-13, R, NC-17), tendo como valor default
    "G" = (GENERAL_AUDIENCE) e tamanho máximo igual a 20 caracteres;\n
    `synopsis`: Campo de texto (type: str) sem tamanho máximo que faz a referência a sinopse do filme.
    """

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.GENERAL_AUDIENCE,
        null=True,
    )
    synopsis = models.TextField(default=None, null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    added_by = models.CharField(max_length=127)
    bought_by = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="buyed_movies"
    )

    def __str__(self) -> str:
        return self.title


class MovieOrder(models.Model):
    """
    Model referenciando uma tabela pivô entre `(class) Movie` e `(class) User(AbstractUser)`.

    Recebe os seguintes parâmetros:
    """
    class Meta:
        verbose_name = "Filme Comprado"
        verbose_name_plural = "Filmes Comprados"

    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    title = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="orders"
    )
    buyed_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )

    def __str__(self) -> str:
        return f"{self.title.title} - {self.buyed_by.first_name} {self.buyed_by.last_name}"
