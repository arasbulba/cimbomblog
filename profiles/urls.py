from django.urls import path
from . import views

app_name = "profiles"


urlpatterns = [
    path('<str:username>/', views.ProfileDetailView.as_view(), name='details'),
    path('<str:username>/edit', views.ProfileEditView.as_view(), name='profiledit'),
]



