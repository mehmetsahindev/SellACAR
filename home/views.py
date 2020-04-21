from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from home.models import Setting


def index(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'index.html', context)


def hakkimizda(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'hakkimizda.html', context)


def referanslarimiz(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'iletisim.html', context)
