# -*- coding: utf-8 -*-
#######################
# dbSync.urls
#######################
from django.urls import path
from dumplocal import views

urlpatterns = [
    path('', views.health,name="health"),
]

