from django.shortcuts import render
from django.http import HttpResponse
from api.models import *
from api.serializers import *
from rest_framework import viewsets
# Create your views here.



def home(request):
    return render(request,'home.html')


class LatestMovies_viewset(viewsets.ModelViewSet):
    queryset=LatestMovies.objects.all()
    serializer_class=LatestMovies_Serializer

class LatestTvShows_viewset(viewsets.ModelViewSet):
    queryset=LatestTvShows.objects.all()
    serializer_class=LatestTvShows_Serializer


class NetflixShows_viewset(viewsets.ModelViewSet):
    queryset=NetflixShows.objects.all()
    serializer_class=NetflixShows_Serializer

class ThrillerShows_viewset(viewsets.ModelViewSet):
    queryset=ThrillerShows.objects.all()
    serializer_class=ThrillerShows_Serializer