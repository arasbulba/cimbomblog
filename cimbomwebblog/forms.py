from django.forms import ModelForm
from .models import Players, Post



class AddPostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"


class AddPlayerForm(ModelForm):

  model = Players
  fields = "__all__"