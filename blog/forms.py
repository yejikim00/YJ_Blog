from django import forms
from blog.models import Poster


class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['subject', 'content']