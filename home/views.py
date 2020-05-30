import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage, Comment
from product.models import Product, Category, Images


def index(request):
    settings = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:5]
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')[:15]
    randomproducts = Product.objects.all().order_by('?')[:3]


    context = {
        'settings': settings,
        'sliderdata': sliderdata,
        'categories': categories,
        'products': products,
        'randomproducts': randomproducts,
    }
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
    if request.method == 'POST': #form post edildiyse
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız Gönderildi")
            return HttpResponseRedirect('/iletisim')

    settings = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'settings': settings, 'form': form}
    return render(request, 'iletisim.html', context)


def category_products(request,id,slug):
    categories = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'products': products,
        'categories': categories,
        'categorydata': categorydata,
    }
    return render(request, 'products.html', context)


def product_detail(request, id, slug):
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    randomproducts = Product.objects.all().order_by('?')[:3]
    categories = Category.objects.all()
    comments = Comment.objects.filter(product_id=id, status='True')

    context = {
        'product': product,
        'randomproducts': randomproducts,
        'categories': categories,
        'images': images,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            categories = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            randomproducts = Product.objects.all().order_by('?')[:3]

            context = {
                'query': query,
                'products': products,
                'categories': categories,
                'randomproducts': randomproducts,
            }
            return render(request, 'products_search.html', context)
    return HttpResponseRedirect('/')


def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Kullanıcı adı veya şifre yanlış")
            return HttpResponseRedirect('/login')

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'signup.html', context)