from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from main.utils import autoslug

User = get_user_model()


@autoslug('title')
class Genre(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    rel_date = models.DateField()
    video = models.CharField(max_length=1000)
    like = models.ManyToManyField(User, default=None, blank=True, related_name='like')
    dislike = models.ManyToManyField(User, default=None, blank=True, related_name='dislike')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    @property
    def likes(self):
        return self.like.all().count()

    @property
    def dislikes(self):
        return self.dislike.all().count()


class Comment(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.description


