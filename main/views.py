from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CreateMovieForm
from .models import *


class IndexPageView(ListView):
    model = Movie
    template_name = 'movie/index.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'


class MovieCreateView(CreateView):
    queryset = Movie.objects.all()
    template_name = 'movie/add_movie.html'
    form_class = CreateMovieForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class MovieUpdateView(UpdateView):
#     queryset = Movie.objects.get(id=id)







