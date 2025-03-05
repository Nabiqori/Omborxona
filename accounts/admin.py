from django.contrib import admin

from main.models import Mahsulot, Bolim, Mijoz
from sotuv.models import *

admin.site.register([Mahsulot, Bolim, Mijoz, Sotuv])
