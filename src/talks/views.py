# -*- coding: utf8 -*-

from django.shortcuts import render

from .models import Talk


def home(request):
    talks = Talk.objects.all()

    return render(request, 'talks/talks_list.html', {
        'talks': talks,
    })
