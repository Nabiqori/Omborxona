
from django.contrib import admin
from django.urls import path, include
from setuptools.extern import names

from sotuv.views import Sotuvlar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Sotuvlar.as_view(), name="sotuvlar"),
]
