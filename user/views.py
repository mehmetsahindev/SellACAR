from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile, Comment
from product.models import Category, Product
from user.forms import UserUpdateForm, ProfileUpdateForm, UserProductForm


def index(request):
    user = request.user

    current_user = UserProfile.objects.get(user_id=user.id)

    context = {
        'profile': current_user,
    }
    return render(request, 'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Porifliniz güncellendi')
            return redirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        user = request.user
        current_user = UserProfile.objects.get(user_id=user.id)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'profile': current_user,
        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz değiştirildi.')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Lütfen hatalı yerleri düzeltiniz<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        form = PasswordChangeForm(request.user)
        user = request.user
        current_user = UserProfile.objects.get(user_id=user.id)
        context = {
            'form': form,
            'profile': current_user,
        }

        return render(request, 'change_password.html', context)


@login_required(login_url='/login')
def comments(request):
    user = request.user
    current_user = UserProfile.objects.get(user_id=user.id)
    user_comments = Comment.objects.filter(user_id=user.id)
    context = {
        'profile': current_user,
        'comments': user_comments,
    }

    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Yorum silindi.')
    return HttpResponseRedirect('/user/comments')


def products(request):
    user = request.user
    current_user = UserProfile.objects.get(user_id=user.id)
    products = Product.objects.filter(user_id=user.id)
    context = {
        'profile': current_user,
        'products': products,
    }
    return render(request, 'user_products.html', context)


def products_new(request):
    if request.POST:
        form = UserProductForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            data = Product()
            data.user_id = user.id
            data.category_id = request.POST.get('category')
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.marka = form.cleaned_data['marka']
            data.model = form.cleaned_data['model']
            data.renk = form.cleaned_data['renk']
            data.year = form.cleaned_data['year']
            data.kilometre = form.cleaned_data['kilometre']
            data.vites = form.cleaned_data['vites']
            data.durum = form.cleaned_data['durum']
            data.price = form.cleaned_data['price']
            data.amount = form.cleaned_data['amount']
            data.detail = form.cleaned_data['detail']
            data.slug = form.cleaned_data['slug']
            data.status = 'Evet'
            data.save()

            messages.success(request, 'Ürününz Eklendi. <a href="/product/'+str(data.id)+'/'+str(data.slug)+'">Ürüne git >></a>')
            return HttpResponseRedirect('/user/products')
        else:
            messages.error(request, 'Lütfen hatalı alanları düzeltiniz <br>' + str(form.errors))
            return HttpResponseRedirect('/user/products/new')
    else:
        form = UserProductForm()
        user = request.user
        current_user = UserProfile.objects.get(user_id=user.id)
        context = {
            'profile': current_user,
            'form': form,
        }
        return render(request, 'user_products_new.html', context)
