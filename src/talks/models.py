# -*- coding: utf8 -*-

from django.db import models


class Talk(models.Model):
    name = models.CharField(max_length=100)
    resume = models.TextField()
    at = models.DateTimeField(auto_now_add=True)
    talker = models.CharField(max_length=80)
