from django.db import models
from datetime import datetime
from channels.models import Creator

# Create your models here.
class Videos(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    video_id = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    techstack = models.TextField(blank=True)
    language = models.TextField(blank=True)
    subtitles_eng = models.BooleanField(default=False)
    def __str__(self):
        return self.title
