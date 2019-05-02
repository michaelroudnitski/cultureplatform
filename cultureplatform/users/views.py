# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World, you are viewing the user index page")

def login(request):
    return HttpResponse("Hello, world. You're at the users index.")