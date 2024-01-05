from django.contrib import admin
from django.urls import path , include
from . import views
from api.views import *
from rest_framework import routers



router=routers.DefaultRouter()
router.register(r"latestmovies" , LatestMovies_viewset)
router.register(r'latestshows' , LatestTvShows_viewset)
router.register(r'netflixshows' , NetflixShows_viewset)
router.register(r'thrillershows' , ThrillerShows_viewset)

urlpatterns = [
    path('', home , name='home' ),
    path('api/', include(router.urls)),
    
]
