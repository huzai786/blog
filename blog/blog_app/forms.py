from .models import Blog
from django.forms import ModelForm


class BlogCreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
