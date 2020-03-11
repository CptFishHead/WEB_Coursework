from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
from django.views.generic.base import View

from .models import Movie




# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})

class MoviesView(GenreYear, ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
=======

# Create your views here.
>>>>>>> parent of 1ea4aa8... Error
=======

# Create your views here.
>>>>>>> parent of 1ea4aa8... Error
