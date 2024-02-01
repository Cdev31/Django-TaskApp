from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def hello( request ):
    return render(request, 'sigunp.html', {
        'form': UserCreationForm
    })

def signup( request ):
    return render( request, 'home.html' )