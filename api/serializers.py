from api.models import *

from rest_framework import serializers



class LatestMovies_Serializer(serializers.HyperlinkedModelSerializer):
    m_id=serializers.ReadOnlyField()
    class Meta:
        model=LatestMovies
        fields="__all__"

class LatestTvShows_Serializer(serializers.HyperlinkedModelSerializer):
    m_id=serializers.ReadOnlyField()
    class Meta:
        model=LatestTvShows
        fields="__all__"


class NetflixShows_Serializer(serializers.HyperlinkedModelSerializer):
    m_id=serializers.ReadOnlyField()
    class Meta:
        model=NetflixShows
        fields="__all__"


class ThrillerShows_Serializer(serializers.HyperlinkedModelSerializer):
    m_id=serializers.ReadOnlyField()
    class Meta:
        model= ThrillerShows
        fields="__all__"