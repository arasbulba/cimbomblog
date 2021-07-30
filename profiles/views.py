from profiles.forms import EditProfileForm
from profiles.models import Profile
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from cimbomwebblog.models import Post
from django.urls import reverse


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
        context['all_posts'] = Post.objects.filter(author=user)[0:9]
        return context


class ProfileEditView(UpdateView):
    template_name = "account/edit.html"
    model = Profile
    form_class = EditProfileForm
  

    def get_object(self):
        return self.request.user.profile
    
    def get_success_url(self):
        return reverse('profiles:details', args=[self.request.user.username])

 
