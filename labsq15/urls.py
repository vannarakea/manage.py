
from django.contrib import admin
from django.urls import path

import labsq15.deplay
from labsq15 import deplay
urlpatterns = [
    ##path('admin/', admin.site.urls),
    path('',deplay.index,name="homepage")
]
