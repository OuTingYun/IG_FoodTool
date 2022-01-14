from django.db import models

# Create your models here.
# Create your models here.
class Store(models.Model):
    AccountName = models.CharField(max_length= 32)

class total(models.Model):
    PostID = models.CharField(max_length= 32,primary_key=True)
    AccountName = models.CharField(max_length= 32)
    PlaceID = models.PositiveIntegerField()
    Content = models.TextField(blank=True)
    Place = models.CharField(max_length= 32,null=True)
    PictureUrl = models.CharField(max_length= 5000,null=True)

class posts(models.Model):
    PostID = models.CharField(max_length= 32,primary_key=True)
    AccountName = models.CharField(max_length= 32)
    PlaceID = models.PositiveIntegerField()
    Content = models.TextField(blank=True)
    Place = models.CharField(max_length= 32,null=True)
    PictureUrl = models.CharField(max_length= 5000,null=True)