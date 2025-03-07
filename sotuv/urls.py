from django.contrib import admin
from django.urls import path, include


from sotuv.views import Sotuvlar, TahrirlashSotuv, Sotuv_ochirish, Sotuv_ochirish_tasdiqlash, ogohlantirish_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Sotuvlar.as_view(), name="sotuvlar"),
    path('ogohlantirish/', ogohlantirish_view, name="ogohlantirish"),
    path('<int:pk>/tahrirlash/', TahrirlashSotuv, name='tahrirlash_sotuv'),
    path('<int:pk>/ochirish/tasdiqlash', Sotuv_ochirish_tasdiqlash, name='sotuv_ochirish_tasdiqlash'),
    path("<int:pk>/ochirish/", Sotuv_ochirish, name='sotuv_ochirish'),
]
