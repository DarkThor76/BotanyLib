# -*- coding: utf-8 -*-
"""Created on Fri Oct 11 14:53:27 2024.

@author: jreed
"""

# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    Call at / (root) path. Returns a 'Hello World' response.

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.

    Returns
    -------
    django.http.HttpResponse
        DESCRIPTION.


    """
    return HttpResponse("<h1>Hello, world. You're at the plants index.</h1>")
