from django.contrib import admin
from .models import Players, Post, Category

class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'created_at', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

class PlayersAdmin(admin.ModelAdmin):
   list_display = ('name', 'foot', 'height', 'country')

admin.site.register(Players, PlayersAdmin)

