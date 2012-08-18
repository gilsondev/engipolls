# -*- coding: utf8 -*-
import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Talk


class TalkUrlTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('home'))

    def test_get_talk_form(self):
        '''Retorna status 200 da lista de palestras'''
        self.assertEquals(self.resp.status_code, 200)

    def test_template(self):
        '''Renderiza template para enviar na resposta'''
        self.assertTemplateUsed(self.resp, 'talks/talks_list.html')


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            name=u"O que é Python?",
            resume=u"Palestra sobre Python",
            at=datetime.datetime.now(),
            talker="Guido Van Rossum"
        )

    def test_create(self):
        """Registra a palestra corretamente"""
        self.assertEquals(self.talk.pk, 1)

    def test_unicode(self):
        """É usado para retornar a representação do objeto"""
        self.assertEquals(u'Palestra: O que é Python?', unicode(self.talk))
