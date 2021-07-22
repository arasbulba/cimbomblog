from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView, CategoryView, SearchView, PlayersView


app_name = 'cimbomweb'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('add_post/', AddPostView.as_view(), name='add'),
    path('category/<int:pk>', CategoryView.as_view(), name = 'category'),
    path('search/', SearchView.as_view(), name = 'search'),
    path('players/', PlayersView.as_view(), name = 'players')
]

