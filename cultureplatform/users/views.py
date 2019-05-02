# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse("loginin")


def signup(request):
    return HttpResponse("signup")
