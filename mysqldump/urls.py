# -*- coding: utf-8 -*-
#######################
# mysqldump.urls
#######################
from django.urls import path
from mysqldump import views

urlpatterns = [
    path('', views.health,name="health"),
]

