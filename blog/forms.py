from django import forms
from django.db import models
from .models import Post

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"