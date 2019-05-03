# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import NewForumForm
from django.http import HttpResponse


def forum(request):
    return render(request, 'forum.html')


# @login_required(login_url='/accounts/signin/)
def create(request):
    if request.method == 'POST':
        form = NewForumForm(request.POST)
        if form.is_valid():
            print('valid form at create forum')
            new_forum = form.save()
        else:
            print('invalid form at create forum')
    else:
        form = NewForumForm()
    return render(request, 'createforum.html', {'form': form})


def cultural_and_diversity(request):
    return render(request, 'cultural_and_diversity.html')


def philosophy_and_ethics(request):
    return render(request, 'philosophy_and_ethics.html')


def mental_health(request):
    return render(request, 'mental_health.html')


def miscellaneous(request):
    return render(request, 'miscellaneous.html')
