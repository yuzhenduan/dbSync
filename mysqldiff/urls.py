# -*- coding: utf-8 -*-
#######################
# mysqldiff.urls
#######################
from django.urls import path
from mysqldiff import views

urlpatterns = [
    path('', views.health,name="health"),
]

