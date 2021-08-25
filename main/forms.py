from datetime import datetime

from django import forms

from account.tasks import send_new_addition_mail
from .models import Movie, Comment


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('author', 'id', 'like', 'dislike')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateMovieForm, self).__init__(*args, **kwargs)

    def save(self):
        data = self.cleaned_data
        data['author'] = self.request.user
        genre = data.pop('genre')
        movie = Movie.objects.create(**data)
        movie.genre.add(*genre)
        # send_new_addition_mail.delay(self.user.email, movie.title )
        return movie


class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('author', 'id', 'like', 'dislike')


class CommentForm(forms.ModelForm):
    pub_date = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)

    class Meta:
        model = Comment
        fields = ('description',)

    def save(self, d, u, m):
        return Comment.objects.create(user=u, description=d, movie=m)

