from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

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
    image = ImageField(upload_to='media/', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_at']

    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



