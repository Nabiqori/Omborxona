from django.shortcuts import render, redirect
from main.views import View
from .models import *

class Sotuvlar(View):
    def get(self,request):
        sotuvlar = Sotuv.objects.all()
        context={
            "sotuvlar":sotuvlar,
        }
        return render(request, "sotuv.html", context)
    def post(self, request):
        Sotuv.objects.create(
            mahsulot=request.POST.get('mahsulot'),
            mijoz=request.POST.get('mijoz'),
            miqdor=request.POST.get('miqdor'),
            jami_summa=request.POST.get('jami_summa'),
            qarz=request.POST.get('qarz'),
            tolandi=request.POST.get('tolandi'),
            bolim=None if request.POST.get('bolim') == '' else request.POST.get('bolim'),
        )
        return redirect('sotuvlar')

def TahrirlashSotuv(request, pk):
    sotuv=Sotuv.objects.get(pk=pk)
    if request.method == "POST":
            Sotuv.objects.filter(pk=pk).update(
                mahsulot = request.POST.get('mahsulot'),
                mijoz = request.POST.get('mijoz'),
                miqdor = request.POST.get('miqdor'),
                jami_summa = request.POST.get('jami_summa'),
                qarz = request.POST.get('qarz'),
                tolandi = request.POST.get('tolandi'),
                bolim=None if request.POST.get('bolim') == '' else request.POST.get('bolim'),
            )
            return redirect("sotuvlar")
    context={
            "sotuv":sotuv,
        }

    return render(request, 'sotuv-tahrirlash.html', context)