from django.contrib import admin
from api.models import *
# Register your models here.
class LatestMoviesAdmin(admin.ModelAdmin):
    list_display=('name' ,'genre')

class LatestTvShowsAdmin(admin.ModelAdmin):
    list_display=('name' ,'genre')

class NetflixShowsAdmin(admin.ModelAdmin):
    list_display=('name' ,'genre')

class ThrillerShowsAdmin(admin.ModelAdmin):
    list_display=('name' ,'genre')


admin.site.register(LatestMovies , LatestMoviesAdmin)
admin.site.register(LatestTvShows , LatestTvShowsAdmin)
admin.site.register(NetflixShows , NetflixShowsAdmin)
admin.site.register(ThrillerShows , ThrillerShowsAdmin)