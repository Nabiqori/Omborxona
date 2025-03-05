from django.db.models.fields import return_None


from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from datetime import datetime
class BolimlarView(View):
    def get(self, request):
        return render(request, "bo'limlar.html")

class Mahsulotlar(View):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.all()
        context ={
            'mahsulotlar':mahsulotlar,
        }
        return render(request, "mahsulotlar.html", context)
    def post(self, request):
        Mahsulot.objects.create(
            nom = request.POST.get('nom'),
            brend = request.POST.get('brend'),
            narx1 = request.POST.get('narx1'),
            narx2 =request.POST.get('narx2'),
            oxirgi_sana =request.POST.get('sana'),
            miqdor = request.POST.get('miqdor'),
            olchov = request.POST.get('olchov'),
            bolim = Bolim.objects.first()
        )
        return redirect('mahsulotlar')
class Mijozlar(View):
    def get(self,request):
        mijozlar = Mijoz.objects.all()
        context={
            "mijozlar":mijozlar,
        }
        return render(request, "mijozlar.html", context)
    def post(self, request):
        Mijoz.objects.create(
            ism = request.POST.get('ism'),
            dokon = request.POST.get('dokon'),
            manzil = request.POST.get('manzil'),
            tel =request.POST.get('tel'),
            qarz =0 if request.POST.get('qarz')=='' else request.POST.get('qarz'),
            bolim = Bolim.objects.first()
        )
        return redirect('mijozlar')
def TahrirlashMahsulot(request, pk):
    product=get_object_or_404(Mahsulot, pk=pk)
    if request.method == "POST":

            product.nom=request.POST.get("nom")
            product.brend=request.POST.get("brend")
            product.narx1=request.POST.get('narx1')
            product.narx2=request.POST.get('narx2')
            product.oxirgi_sana=request.POST.get('sana')
            product.miqdor=request.POST.get('miqdor')
            product.save()
            return redirect("mahsulotlar")
    context={
            "product":product
        }

    return render(request, 'mahsulot-tahrirlash.html', context)
def TahrirlashMijoz(request, pk):
    client=Mijoz.objects.get(pk=pk)
    if request.method == "POST":
            Mijoz.objects.filter(pk=pk).update(
                ism = request.POST.get('ism'),
                dokon = request.POST.get('dokon'),
                manzil = request.POST.get('manzil'),
                tel = request.POST.get('tel'),
                qarz=0 if request.POST.get('qarz') == '' else request.POST.get('qarz'),
            )
            return redirect("mijozlar")
    context={
            "client":client,
        }

    return render(request, 'mijoz-tahrirlash.html', context)
def logout(request):
    return redirect("mahsulotlar")
def Mahsulot_ochirish_tasdiqlash(request, pk):
    mahsulot=get_object_or_404(Mahsulot, pk=pk)
    context={
        "mahsulot":mahsulot,
    }
    return render(request, "mahsulot_delete_confirm.html", context)
def Mahsulot_ochirish(request, pk):
    mahsulot = get_object_or_404(Mahsulot, id=pk)
    mahsulot.delete()
    return redirect('mahsulotlar')
def Mijoz_ochirish_tasdiqlash(request, pk):
    mijoz=get_object_or_404(Mijoz, pk=pk)
    context={
        "mijoz":mijoz,
    }
    return render(request, "mijoz_delete_confirm.html", context)
def Mijoz_ochirish(request, pk):
    mijoz = get_object_or_404(Mijoz, pk=pk)
    mijoz.delete()
    return redirect('mijozlar')
