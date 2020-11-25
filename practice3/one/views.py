from django.shortcuts import render
from one.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'one/home.html',{})



def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('one:user_info'))
            else:
                return HttpResponse("Account inactive")
        else:
            print('Login tried and failed')
            print('Username={} Password={}'.format(username,password))
            return HttpResponse("Invalid Login details")
    else:
        return render(request,'one/login.html',{})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('one:home'))


def user_register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=UserForm()

    return render(request,'one/register.html',{'user_form':user_form,
                                                'registered':registered})

def user_info(request):
    return render(request,'one/info.html')
