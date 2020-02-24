from django import forms
from posts.models import Post

class PostForm(forms.Form):
    class meta:
        model = Post
        fields = ('user','profile','title','photo')