from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from authmansoura.models import *
# Create your views here.


def home(req):
    return render(req, 'index.html')


def mybooks(request):
    data = books.objects.all()
    context = {
        'data': data
    }
    return render(request, 'books.html', context)


def viwebook(request):
    return render(request, 'index.html')


def borowbook(request):
    # ____condition to show the user how login
    account = Myaccount.objects.get(id = request.session['userid'])
    acc_id = account.id
    # ____condition to show the user books
    borrow_acc_id = borrowbook.objects.filter(account = acc_id)
    dataa = books.objects.filter(id = borrow_acc_id)
    # dsd = dataa.books.objects.all()
    # dsd = borrowbook.books.objects.all
    context = {'dataa': dataa}

    return render(request, 'borwoedbooks.html', context)
