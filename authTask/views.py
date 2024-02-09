from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import login, logout, authenticate

def user_login( request: HttpRequest ):
    if request.method == 'GET':
        return render( request=request, template_name='login.html' )
    elif request.method == 'POST':
        user = authenticate( request,
                username=request.POST['email'],
                password=request.POST['password']
                )
        print(user)
        if user is None:
            return render( request=request, template_name='login.html' , context={
                'error': 'user not valid'
            })    
        login( request, user )
        return redirect('/')


def signup( request: HttpRequest ):
    logout( request )
    return redirect('/')

def register( request: HttpRequest ):
    try:
        if request.method == 'GET':
            return render( request=request, template_name='register.html' )
        elif request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                user = User(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password1'])
                user.save()
                login( request , user )
                return redirect('/')
            return render( request=request, template_name='register.html', context={
                'error': 'password invalid'
            })
    except IntegrityError as e:
        return render( request=request, template_name='register.html', context={
                'error': 'usuario ya existe'
            })
