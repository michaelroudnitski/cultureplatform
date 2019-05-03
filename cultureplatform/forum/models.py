# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Forum(models.Model):
    title = models.CharField(max_length=30)
    date_posted = models.DateField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Video(models.Model):
    videoID = models.CharField(max_length=300)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)