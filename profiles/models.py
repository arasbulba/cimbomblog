
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.forms.widgets import Textarea



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    
    image = CloudinaryField('image', default='static/img/menprofile_mirh47.png', blank=True, null=True)
    occupation = CharField(max_length=140, null=True, blank=True)
    facebook = CharField(max_length=140, null=True, blank=True)
    twitter = CharField(max_length=140, null=True, blank=True)
    linkedin = CharField(max_length=140, null=True, blank=True)
    

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)

def create_user_profile(sender, instance, created, **kwargs):
    """New profile object as user created"""

    if created:
        Profile.objects.create(user=instance)
