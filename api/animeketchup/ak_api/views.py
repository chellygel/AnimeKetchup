from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Anime
from .serializer import AnimeSerializer


# Create your views here.
@api_view(['GET'])
def get_anime(request):
    anime = Anime.objects.all()
    serializer = AnimeSerializer(anime, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_anime(request):
    serializer = AnimeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
