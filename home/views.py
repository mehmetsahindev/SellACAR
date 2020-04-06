from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    controller = "Home"
    context = {'controller':controller}
    return render(request, 'index.html', context)