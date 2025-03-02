
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', Mahsulotlar.as_view(), name='mahsulotlar'),
    path('<int:pk>/tahrirlash/', Tahrirlash, name='tahrirlash'),
    path('<int:pk>/ochirish/tasdiqlash', Mahsulot_ochirish_tasdiqlash, name='ochirish_tasdiqlash'),
    path("mahsulot/<int:pk>/o'chirish/", Mahsulot_ochirish, name='ochirish'),
    path('logout/', logout, name='logout'),
]
