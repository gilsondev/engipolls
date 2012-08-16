# -*- coding: utf8 -*-

from django.http import HttpResponse
from django.template import loader, Context


def home(request):
    t = loader.get_template('talks/talks_list.html')
    c = Context()

    content = t.render(c)

    return HttpResponse(content)
