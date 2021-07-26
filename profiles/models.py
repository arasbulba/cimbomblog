from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = CloudinaryField('image', default='static/img/menprofile_mirh47.png')

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)

def create_user_profile(sender, instance, created, **kwargs):
    """New profile object as user created"""

    if created:
        Profile.objects.create(user=instance)
