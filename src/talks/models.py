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


class Poll(models.Model):
    POLL_CHOICES = (
        (u'B', u'Muito bom'),
        (u'L', u'Legal'),
        (u'R', u'Ruim'),
    )
    talk = models.ForeignKey('Talk')
    poll = models.CharField(max_length=1, choices=POLL_CHOICES)
    comments = models.TextField(blank=True)

    class Meta:
        db_table = 'polls'

    def __unicode__(self):
        return self.get_poll_display()
