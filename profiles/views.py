from django.contrib.auth import models
from django.forms import widgets
from profiles.forms import EditProfileForm, EditUserForm
import profiles
from profiles.models import Profile
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView, FormView
from cimbomwebblog.models import Post
from django.shortcuts import render 


class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "account/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"


    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()
        return context

class ProfileEditView(UpdateView):
    template_name = "account/edit.html"
    model = Profile
    success_url = "/"
    fields = ('image', 'full_name', 'occupation', 'facebook', 'twitter', 'linkedin')

    def get_object(self):
        return self.request.user.profile
