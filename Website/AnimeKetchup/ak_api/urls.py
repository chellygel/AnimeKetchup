from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.landing_page, name='landing_page'),
    path("anime/", views.list_anime, name='list_anime'),
    path("anime/<int:pk>/", views.get_anime_detail, name='get_anime_detail'),
    path("post/", views.post_anime),
    path("api_auth/", include('rest_framework.urls')),
]
