from rest_framework import serializers
from .models import RatingChoices


class MovieSerializer(serializers.Serializer):
    """
    Validações referente a (class) models.Movie
    """

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    rating = serializers.CharField(max_length=20, choices=RatingChoices.choices, default=RatingChoices.GENERAL_AUDIENCE)
    synopsis = serializers.CharField(default=None)
    added_by = ""
