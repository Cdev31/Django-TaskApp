from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home( request: HttpRequest ):
    return render( request=request, template_name='home.html' )

def login( request: HttpRequest ):
    return render( request=request, template_name='login.html' )


def register( request: HttpRequest ):
    return render( request=request, template_name='register.html' )