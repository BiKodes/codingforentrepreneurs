from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Article

        fields = ["author","title","description","body","summary"]

        
