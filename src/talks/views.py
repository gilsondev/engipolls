# -*- coding: utf8 -*-

from django.shortcuts import render, get_object_or_404, redirect

from .models import Talk
from .forms import PollForm


def home(request):
    talks = Talk.objects.all()

    return render(request, 'talks/talks_list.html', {
        'talks': talks,
    })


def poll_form(request, talk_id):
    talk = get_object_or_404(Talk, pk=talk_id)

    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.talk = talk
            poll.save()

            return redirect('/votacoes/sucesso/')
    return render(request, 'talks/polls_form.html', {
        'form': PollForm(),
    })


def success(request):
    return render(request, 'talks/polls_success.html', {})
