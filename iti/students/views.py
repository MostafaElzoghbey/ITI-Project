import datetime
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
    # account = Myaccount.objects.get(id = request.session['userid'])
    # acc_id = account.id
    # ____condition to show the user books
    # borrow_acc_id = borrowbook.objects.filter(account = acc_id)
    # dataa = books.objects.filter(id = borrow_acc_id)
    # dsd = dataa.books.objects.all()
    # dsd = borrowbook.books.objects.all
    # context = {'dataa': dataa}
    return render(request, 'borwoedbooks.html')

def borrow_click(request):

    
    if(request.method=='POST'):
        
        student = Myaccount.objects.get(id = request.session['userid'])
        book = books.objects.get(id=request.POST['book_id'])

        # Check if the book is available

        # Create a new BookBorrowing object
        book_borrowing = borrowbook(
            account=student,
            borrbook=book,
        )

        book_borrowing.save()

        return render(request,'borwoedbooks.html')
    # Update the book's availability status

    # Redirect the user to a success page
    return HttpResponseRedirect('books.html')

