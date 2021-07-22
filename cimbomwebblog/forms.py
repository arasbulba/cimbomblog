from django.forms import ModelForm
from .models import Players, Post
from sorl.thumbnail import ImageField



class AddPostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"


class AddPlayerForm(ModelForm):

  model = Players
  fields = "__all__"