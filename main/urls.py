
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', Mahsulotlar.as_view(), name='mahsulotlar'),
    path('mijozlar/', Mijozlar.as_view(), name='mijozlar'),
    path('mahsulot/<int:pk>/tahrirlash/', TahrirlashMahsulot, name='tahrirlash_mahsulot'),
    path('mijoz/<int:pk>/tahrirlash/', TahrirlashMijoz, name='tahrirlash_mijoz'),
    path('mahsulot/<int:pk>/ochirish/tasdiqlash', Mahsulot_ochirish_tasdiqlash, name='mahsulot_ochirish_tasdiqlash'),
    path("mahsulot/<int:pk>/o'chirish/", Mahsulot_ochirish, name='mahsulot_ochirish'),
    path('mijoz/<int:pk>/ochirish/tasdiqlash', Mijoz_ochirish_tasdiqlash, name='mijoz_ochirish_tasdiqlash'),
    path("mijoz/<int:pk>/ochirish/", Mijoz_ochirish, name='mijoz_ochirish'),
    path('logout/', logout, name='logout'),
]
