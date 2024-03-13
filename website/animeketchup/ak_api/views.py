from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import (api_view,
                                       authentication_classes,
                                       permission_classes)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Anime
from .serializer import AnimeSerializer


@api_view(['GET'])
def json_anime_list(request):
    anime = Anime.objects.all()
    serializer = AnimeSerializer(anime, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_anime_detail(request, pk=None):
    anime = get_object_or_404(Anime, pk=pk)
    serializer = AnimeSerializer(anime)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_anime(request):
    if request.user.is_superuser:  # Only allow superusers to post anime
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(
            {
                "error": "You are not authorized to perform this action."
            }, status=status.HTTP_403_FORBIDDEN)


def landing_page(request):
    return render(request, 'landing_page.html')


def anime_list(request):
    return render(request, 'anime_list.html')
