
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]
