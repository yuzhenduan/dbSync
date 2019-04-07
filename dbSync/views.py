# -*- coding: utf-8 -*-
#######################
# dbSync.views
#######################
from django.http import HttpResponse

# 
def health(request):
    return HttpResponse("<h1>Yes, We Can!</h1>")

