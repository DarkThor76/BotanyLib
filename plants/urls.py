# -*- coding: utf-8 -*-
"""Created on Fri Oct 11 14:53:27 2024.

@author: jreed
"""


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="plants-home"),
]
