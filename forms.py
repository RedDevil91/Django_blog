from django.forms import ModelForm
from .models import BlogPost


class PostFrom(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'body')
