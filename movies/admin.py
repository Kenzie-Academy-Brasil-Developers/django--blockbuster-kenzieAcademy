from django.contrib import admin
from .models import Movie, MovieOrder

admin.site.register([Movie, MovieOrder])
