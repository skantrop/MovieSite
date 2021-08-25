import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters import FilterSet

from main.forms import CreateMovieForm, CommentForm
from main.models import *

from django.template import RequestContext



class IndexPageView(View):
    def get(self, request):
        genres = Genre.objects.all()
        movies = Movie.objects.all()
        return render(request, 'movie/index.html', locals())


class MovieFilterSet(FilterSet):
    author = django_filters.CharFilter('author__email', lookup_expr='iecxact')
    created_at = django_filters.DateFilter('created_at', lookup_expr='gt')

    class Meta:
        model = Movie
        fields = ['genre', ]


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'
    form = CommentForm
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = Comment.objects.filter(movie=kwargs.get("object"))
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            user = self.request.user
            movie = self.get_object()
            form.save(description, user, movie)
        else:
            form = CommentForm()
        return redirect(self.request.get_full_path())


class MovieCreateView(LoginRequiredMixin, CreateView):
    queryset = Movie.objects.all()
    template_name = 'movie/add_movie.html'
    form_class = CreateMovieForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('detail', args=(self.object.id, ))


class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_authenticated and \
               self.request.user == post.author


# class EditPostView(IsAuthorMixin, UpdateView):
#     queryset = Movie.objects.all()
#     template_name = 'main/edit_post.html'
#     form_class = UpdatePostForm

    # def get_success_url(self):
    #     return reverse('post-details', args=(self.object.id, ))


class DeleteMovieView(IsAuthorMixin, DeleteView):
    queryset = Movie.objects.all()
    template_name = 'movie/delete_movie.html'

    def get_success_url(self):
        return reverse('home')


class SearchResultsView(View):
    def get(self, request):
        q = request.GET.get('q', '')
        if q:
            movies = Movie.objects.filter(Q(title__icontains=q)|
                                       Q(description__icontains=q))
        else:
            movies = Movie.objects.none()
        return render(request, 'movie/index.html', {'movies': movies})


# class AddToWishList(LoginRequiredMixin, View):
#     def get(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         WishList.objects.create(post=post, user=request.user)
#         return redirect('main/index.html')


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'movie/movie_list.html'
    context_object_name = 'genre'

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.id = kwargs.get('id', None)
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = self.get_object()
        context['movies'] = Movie.objects.filter(genre_id=genre.id).select_related('genre')
        return context


class CommentView(DetailView):
    model = Comment
    template_name = 'movie/movie_detail.html'
    form_class = CommentForm
