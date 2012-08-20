# -*- coding: utf8 -*-

from django.db import models


class Talk(models.Model):
    TALK_CHOICES = (
        ('P', u'Palestra'),
        ('M', u'Minicurso'),
    )
    name = models.CharField(max_length=100)
    resume = models.TextField()
    at = models.DateTimeField(auto_now_add=True)
    talker = models.CharField(max_length=80)
    type_talk = models.CharField(max_length=1, choices=TALK_CHOICES)

    def __unicode__(self):
        if self.type_talk == 'P':
            return "Palestra: %s" % (self.name,)
        elif self.type_talk == 'M':
            return "Minicurso: %s" % (self.name,)
