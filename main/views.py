from django.db.models.fields import return_None
\

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
def Tahrirlash(request, pk):
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
