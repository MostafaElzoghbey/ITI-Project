"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authmansoura.views import *
from students.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('Register', myRegister, name='myRegister'),
    path('Login', mylogin, name='mylogin'),
    path('Logout', mylogout, name='mylogout'),
    path('profile', myprofile, name='myprofile'),
    path('books', mybooks, name='mybooks'),
    path('Update_profile/<int:ID>', Update_profile, name='Update_profile'),
    path('bookdetail', viwebook, name='bookdetail'),
    path('borowbook', borowbook, name='borowbook'),

]
