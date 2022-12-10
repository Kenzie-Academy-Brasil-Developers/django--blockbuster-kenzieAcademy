from rest_framework import serializers
from .models import Movie, MovieOrder, RatingChoices


class MovieSerializer(serializers.Serializer):
    """
    Validações referente a tabela `(class) models.Movie`
    """

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, default=RatingChoices.GENERAL_AUDIENCE
    )
    synopsis = serializers.CharField(default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, instance):
        return instance.added_by.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    """
    Validações referentes a tabela pivô `(class) models.MovieOrder`
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.FloatField()
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, instance: MovieOrder) -> str:
        return instance.title.title

    def get_buyed_by(self, instance: MovieOrder) -> str:
        return instance.buyed_by.email

    def create(self, validated_data):
        print(validated_data)
        # return MovieOrder.objects.create(**validated_data)
