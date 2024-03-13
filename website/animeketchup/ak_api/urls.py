from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.landing_page, name='landing_page'),
    path("api/anime/", views.json_anime_list, name='json_anime_list'),
    path("anime/<int:pk>/", views.get_anime_detail, name='get_anime_detail'),
    path("anime/", views.anime_list, name='anime_list'),
    path("post/", views.post_anime),
    path("api_auth/", include('rest_framework.urls')),
]
