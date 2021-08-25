from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('movies/<str:slug>/', GenreDetailView.as_view(), name='list'),
    path('watch/<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('add-movie/', MovieCreateView.as_view(), name='create'),
    path('search/', SearchResultsView.as_view(), name='search-results'),

]
