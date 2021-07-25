from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = ForeignKey(Category, on_delete=PROTECT, default=1)
    excerpt = models.CharField(max_length=200)
    body = RichTextField(blank=False, null=False)
    image = CloudinaryField('image', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_at']

    
    def __str__(self):
        return self.title



FOOT = (
    ("RIGHT","Right"),
    ("LEFT","Left")
)


class Positions(models.Model):
    position = models.CharField(max_length=60, default=None)

    def __str__(self):
        return self.position



class Players(models.Model):

    image = CloudinaryField('image', default=None)
    name = models.CharField(max_length=200, unique=True)
    pos = models.ManyToManyField(Positions, related_name="player_position")
    number = models.CharField(max_length=2, unique=True, null=True, default=None)
    country = models.CharField(max_length=60)
    salary = models.CharField(max_length=60)
    foot = models.CharField(max_length=60, choices=FOOT, default=None)
    height = models.CharField(max_length=60)
    about = models.TextField(max_length=400)


    def __str__(self):
        return self.name
    
    




