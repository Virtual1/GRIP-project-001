from django.db import models
from datetime import datetime
class Creator(models.Model):
    creatorname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    channelname = models.CharField(max_length=200)
    channeldescription = models.TextField(blank=True)
    channeltwitter = models.CharField(max_length=50)
    channelig = models.CharField(max_length=50)
    channelsubscribers = models.BigIntegerField()
    channelytid = models.CharField(max_length=200)
    def __str__(self):
        return self.channelname
