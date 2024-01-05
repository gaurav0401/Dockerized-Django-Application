from django.db import models

# Create your models here.
#user-gaurav21
#pass-Ab22558800


class LatestMovies(models.Model):
    m_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    genre=models.CharField( max_length=50 ,choices=(
                                                   ('Sci-Fi' , 'Sci-Fi') , 
                                                   ('Thriller' ,'Thriller') , 
                                                   ('Action' ,"Action"),
                                                   ('Horror' ,'Horror') , 
                                                   ('Mystery' ,'Mystery') , 
                                                  
                                                   ))
    director=models.CharField( max_length=50)
    ratings=models.FloatField()
    year=models.IntegerField()


class LatestTvShows(models.Model):
    m_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    director=models.CharField( max_length=50)
    genre=models.CharField( max_length=50 , choices=(
                                                   ('Sci-Fi' , 'Sci-Fi') , 
                                                   ('Thriller' ,'Thriller') , 
                                                   ('Action' ,"Action"),
                                                   ('Horror' ,'Horror') , 
                                                   ('Mystery' ,'Mystery') , 
                                                  
                                                   ))
    ratings=models.FloatField()
    year=models.IntegerField()


class NetflixShows(models.Model):
    m_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    director=models.CharField( max_length=50)
    genre=models.CharField( max_length=50, choices=(
                                                   ('Sci-Fi' , 'Sci-Fi') , 
                                                   ('Thriller' ,'Thriller') , 
                                                   ('Action' ,"Action"),
                                                   ('Horror' ,'Horror') , 
                                                   ('Mystery' ,'Mystery') , 
                                                  
                                                   ))
    ratings=models.FloatField()
    year=models.IntegerField()

class ThrillerShows(models.Model):
    m_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    director=models.CharField( max_length=50)
    genre=models.CharField( max_length=50 ,choices=(
                                                   ('Sci-Fi' , 'Sci-Fi') , 
                                                   ('Thriller' ,'Thriller') , 
                                                   ('Action' ,"Action"),
                                                   ('Horror' ,'Horror') , 
                                                   ('Mystery' ,'Mystery') , 
                                                  
                                                   ))
    ratings=models.FloatField()
    year=models.IntegerField()





