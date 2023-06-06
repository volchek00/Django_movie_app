from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    video_uri = models.URLField()
    icon_uri = models.URLField()
