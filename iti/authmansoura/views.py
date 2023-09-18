from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import *
import sys
from .models import *


# Create your views here.
def myRegister(request):
    if (request.method == 'POST'):
        Myaccount.objects.create(
            username=request.POST['Username'], password=request.POST['Password'], account=request.POST['Email'])
        return redirect('/Login')
    return render(request, 'Register.html')


def mylogin(request):
    context = {}
    if (request.method == 'POST'):
        usern = request.POST['Username']
        passw = request.POST['Password']
        try:
            obj = Myaccount.objects.filter(username=usern, password=passw)
            if (obj is not None):
                request.session['userid'] = obj[0].id
                request.session['username'] = obj[0].username
                request.session['account'] = obj[0].account
                return HttpResponseRedirect('/')
            else:
                context['msg'] = 'invalide username or password'
        except:
            context['msg'] = sys.exc_info()[1]

    return render(request, 'Login.html', context)


def mylogout(request):
    request.session.clear()
    request.session.flush()
    return redirect('/Login')


def myprofile(request):
    context = {'profile': Myaccount.objects.all()}
    return render(request, 'profile.html', context)


def Update_profile(req, ID):
    train = Myaccount.objects.get(id=ID)
    form = updateprofile(instance=train)
    if (req.method == 'POST'):
        f = updateprofile(req.POST, instance=train)
        if (f.is_valid()):
            f.save()
            return HttpResponseRedirect('/profile')
    context = {'form': form}
    return render(req, 'updateProfile.html', context)
