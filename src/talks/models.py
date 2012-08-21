# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class Talk(models.Model):
    TALK_CHOICES = (
        ('P', _(u'Palestra')),
        ('M', _(u'Minicurso')),
    )
    name = models.CharField(_(u'Nome da Sessão'), max_length=100)
    resume = models.TextField(_(u'Resumo'))
    at = models.DateTimeField(_(u'Data da Sessão'), auto_now_add=True)
    talker = models.CharField(_(u'Palestrante'), max_length=80)
    type_talk = models.CharField(_(u'Tipo de Sessão'), max_length=1,
                                 choices=TALK_CHOICES)

    def __unicode__(self):
        if self.type_talk == 'P':
            return "Palestra: %s" % (self.name,)
        elif self.type_talk == 'M':
            return "Minicurso: %s" % (self.name,)
