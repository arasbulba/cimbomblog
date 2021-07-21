from django.forms import ModelForm
from .models import Post
from sorl.thumbnail import ImageField



class AddPostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"