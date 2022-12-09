from rest_framework import serializers
from .models import Movie, RatingChoices


class MovieSerializer(serializers.Serializer):
    """
    Validações referente a (class) models.Movie
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
