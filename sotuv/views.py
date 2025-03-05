from django.shortcuts import render, redirect, get_object_or_404
from main.views import View
from .models import *
from main.models import *

class Sotuvlar(View):
    def get(self,request):
        sotuvlar = Sotuv.objects.all()
        mijozlar = Mijoz.objects.all()
        mahsulotlar = Mahsulot.objects.all()
        bolimlar = Bolim.objects.all()
        context={
            "sotuvlar":sotuvlar,
            "mahsulotlar":mahsulotlar,
            "mijozlar":mijozlar,
            "bolimlar":bolimlar,
        }
        return render(request, "sotuv.html", context)

    def post(self, request):
        Sotuv.objects.create(
            mahsulot_id=request.POST.get('mahsulot_id'),
            mijoz_id=request.POST.get('mijoz_id'),
            miqdor=request.POST.get('miqdor'),
            jami_summa=request.POST.get('jami_summa'),
            qarz=request.POST.get('qarz'),
            tolandi=request.POST.get('tolandi'),
            bolim_id=None if request.POST.get('bolim_id') == '' else request.POST.get('bolim_id'),
        )
        return redirect('sotuvlar')

def TahrirlashSotuv(request, pk):
    sotuv = Sotuv.objects.get(pk=pk)
    if request.method == "POST":
        Sotuv.objects.filter(pk=pk).update(
            mahsulot_id=request.POST.get('mahsulot_id'),
            mijoz_id=request.POST.get('mijoz_id'),
            miqdor=request.POST.get('miqdor'),
            jami_summa=request.POST.get('jami_summa'),
            qarz=request.POST.get('qarz'),
            tolandi=request.POST.get('tolandi'),
            bolim_id=None if request.POST.get('bolim_id') == '' else request.POST.get('bolim_id'),
        )
        return redirect("sotuvlar")
    mijozlar = Mijoz.objects.all()
    mahsulotlar = Mahsulot.objects.all()
    bolimlar = Bolim.objects.all()
    context = {
        "sotuv": sotuv,
        "mahsulotlar": mahsulotlar,
        "mijozlar": mijozlar,
        "bolimlar": bolimlar,
    }

    return render(request, 'sotuv-tahrirlash.html', context)

def Sotuv_ochirish_tasdiqlash(request, pk):
    sotuv=get_object_or_404(Sotuv, pk=pk)
    context={
        "sotuv":sotuv,
    }
    return render(request, "sotuv_delete_confirm.html", context)
def Sotuv_ochirish(request, pk):
    sotuv = get_object_or_404(Sotuv, id=pk)
    sotuv.delete()
    return redirect('/sotuv/')