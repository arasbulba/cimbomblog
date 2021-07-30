from django.forms import ModelForm
from .models import Players, Post



class AddPostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'category', 'excerpt', 'body', 'image', 'status')


class AddPlayerForm(ModelForm):

  model = Players
  fields = "__all__"