# -*- coding: utf8 -*-

from django.test import TestCase


class TalkUrlTest(TestCase):
    def test_get_talk_form(self):
        '''Retorna status 200 da lista de palestras'''
        response = self.client.get('/palestras/')
        self.assertEquals(response.status_code, 200)
