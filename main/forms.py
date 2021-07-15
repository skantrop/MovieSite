from datetime import datetime

from django import forms

from .models import Movie


class CreateMovieForm(forms.ModelForm):
    pub_date = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d '), required=False)

    class Meta:
        model = Movie
        exclude = ('author', 'id',)
