from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "profiles"


urlpatterns = [
    path('<str:username>/', views.ProfileDetailView.as_view(), name='details'),

]



