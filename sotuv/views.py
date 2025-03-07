from django.shortcuts import render, redirect, get_object_or_404
from main.views import View
from .models import *
from main.models import *

class Sotuvlar(View):
    def get(self,request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(bolim=request.user.sotuvchi.bolim)
            mijozlar = Mijoz.objects.filter(bolim=request.user.sotuvchi.bolim)
            mahsulotlar = Mahsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
            bolim = request.user.sotuvchi.bolim
            context={
                "sotuvlar":sotuvlar,
                "mahsulotlar":mahsulotlar,
                "mijozlar":mijozlar,
            }
            return render(request, "sotuv.html", context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            qarz = None if request.POST.get('qarz') == "" else float(request.POST.get('qarz'))
            mijoz = Mijoz.objects.get(id=request.POST.get('mijoz_id'))
            jami_summa = (request.POST.get('jami_summa'))
            tolandi = (request.POST.get('tolandi'))

            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot_id'))
            miqdor = float(request.POST.get('miqdor'))

            if miqdor > mahsulot.miqdor:
                return render(request, "ogohlantirish.html", {'messege':"Mahsulot yetarli emas!"})
            elif request.POST.get('jami_summa')=='' and request.POST.get('tolandi')=='':
                qarz=0
                jami_summa=miqdor*mahsulot.narx1
                tolandi=miqdor*mahsulot.narx1
            elif request.POST.get('jami_summa')=='':
                jami_summa=miqdor*mahsulot.narx1
                tolandi=jami_summa
                qarz=0
            elif request.POST.get('tolandi')=='':
                jami_summa=miqdor*mahsulot.narx1
                qarz=jami_summa-float(tolandi)
            elif qarz==None:
                qarz=float(jami_summa)-float(tolandi)
            Sotuv.objects.create(
                mahsulot=mahsulot,
                mijoz=mijoz,
                miqdor=miqdor,
                jami_summa=jami_summa,
                qarz=qarz,
                tolandi=tolandi,
                bolim=request.user.sotuvchi.bolim,
            )

            mijoz.qarz += qarz
            mijoz.save()

            mahsulot.miqdor -= miqdor
            mahsulot.save()
            return redirect('sotuvlar')
        return redirect('login')

def ogohlantirish_view(request):
    if request.user.is_authenticated:
        return render(request, "ogohlantirish.html")
    return redirect('login')
def TahrirlashSotuv(request, pk):
    sotuv = Sotuv.objects.get(pk=pk)
    if request.method == "POST":
        if request.user.is_authenticated:
            Sotuv.objects.filter(pk=pk).update(
                mahsulot_id=request.POST.get('mahsulot_id'),
                mijoz_id=request.POST.get('mijoz_id'),
                miqdor=request.POST.get('miqdor'),
                jami_summa=request.POST.get('jami_summa'),
                qarz=request.POST.get('qarz'),
                tolandi=request.POST.get('tolandi'),
                bolim=request.user.sotuvchi.bolim,
            )
            return redirect("sotuvlar")
        return redirect('login')
    mijozlar = Mijoz.objects.filter(bolim=request.user.sotuvchi.bolim)
    mahsulotlar = Mahsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
    context = {
            "sotuv": sotuv,
            "mahsulotlar": mahsulotlar,
            "mijozlar": mijozlar,
        }
    return render(request, 'sotuv-tahrirlash.html', context)

def Sotuv_ochirish_tasdiqlash(request, pk):
    if request.user.is_authenticated:
        sotuv=get_object_or_404(Sotuv, pk=pk)
        context={
            "sotuv":sotuv,
        }
        return render(request, "sotuv_delete_confirm.html", context)
    return redirect('login')

def Sotuv_ochirish(request, pk):
    if request.user.is_authenticated:
        sotuv = get_object_or_404(Sotuv, id=pk)
        sotuv.delete()
        return redirect('/sotuv/')
    return redirect('login')
