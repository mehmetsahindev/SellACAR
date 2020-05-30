from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.models import CommentForm, Comment


def index(request):
    return HttpResponse("Product Page")

@login_required(login_url='/login') #check login
def addComment(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.product_id=id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarı ile gönderildi")

            return HttpResponseRedirect(url)

    messages.warning(request, "Yorumunuz kaydedilmedi, kontrol edin")
    return HttpResponseRedirect(url)
