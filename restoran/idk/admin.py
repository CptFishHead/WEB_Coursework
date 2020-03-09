from django.contrib import admin

# Register your models here.
from .models import Category, Genre, Movie, MovieShots, Actor, Rainting, RaintingStar, Reviews


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rainting)
admin.site.register(RaintingStar)
admin.site.register(Reviews)
