from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect
from django.contrib.auth.models import User

def login( request: HttpRequest ):
    if request.method == 'GET':
        return render( request=request, template_name='login.html' )



def register( request: HttpRequest ):
    if request.method == 'GET':
        return render( request=request, template_name='register.html' )
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                username=request.POST['username'],
                password=request.POST['password1'])
            user.save()
            return redirect('')