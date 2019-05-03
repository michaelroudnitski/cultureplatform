# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import NewForumForm
from django.http import HttpResponse

def forum(request):
    return render(request, 'forum.html')


# @login_required()
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


def cultural_and_diversity(request, id):
    return HttpResponse("cultural diversity")


def philosophy_and_ethics(request, id):
    return HttpResponse("philosophy_and_ethics")


def mental_health(request, id):
    return HttpResponse("mental_health")


def miscellaneous(request, id):
    return HttpResponse("miscellaneous")
