# -*- coding: utf8 -*-

from django.shortcuts import render

from .models import Talk
from .forms import PollForm


def home(request):
    talks = Talk.objects.all()

    return render(request, 'talks/talks_list.html', {
        'talks': talks,
    })


def poll_form(request):
    return render(request, 'talks/polls_form.html', {
        'form': PollForm(),
    })
