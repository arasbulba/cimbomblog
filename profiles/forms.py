from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.forms import ModelForm
from profiles import models

class EditUserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class EditProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['image', 'occupation', 'facebook', 'twitter', 'linkedin']

    