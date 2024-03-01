from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_anime),
    path("post/", views.post_anime),
]