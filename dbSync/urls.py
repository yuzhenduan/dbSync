# -*- coding: utf-8 -*-
#######################
# dbSync.urls
#######################
from django.contrib import admin
from django.urls import path,include
from dbSync.views import health

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dump/', include("mysqldump.urls")),
    path('diff/', include("mysqldiff.urls")),
    path('local/', include("local.urls")),
    path('pipeline/', include("pipeline.urls")),
    path('', health,name="health"),
]
