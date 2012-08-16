# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class TalkUrlTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('home'))

    def test_get_talk_form(self):
        '''Retorna status 200 da lista de palestras'''
        self.assertEquals(self.resp.status_code, 200)

    def test_template(self):
        '''Renderiza template para enviar na resposta'''
        self.assertTemplateUsed(self.resp, 'talks/talks_list.html')
